import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from scipy.stats import ttest_ind

# For Statistical Description of Variables
def bs_median_stats(df, m=10000, n=0, p1=2.5, p2=97.5):
    if n==0:
        n = df.shape[0]
    numeric_cols = [ind for ind, val in df.dtypes.items() if val == 'float64']

    stats_df = pd.DataFrame()
    for col in numeric_cols:
        temp_df = bs_median_by_stage(df, col, m=m, n=n, p1=p1, p2=p2)
        stats_df = pd.concat([stats_df, temp_df], axis=1)

    return stats_df

def bs_median_by_stage(df, col, m=10000, n=100, p1=2.5, p2=97.5):
    medians = np.empty([m, 3])
    for i in range(m):
        samples = df[[col, 'Stage']].sample(n, replace=True)
        medians[i] = samples.groupby('Stage').median().values.flatten()

    med, p = (np.median(medians, axis=0), np.percentile(medians, [p1, p2], axis=0).T.reshape(3,2))

    pval1 = ttest_ind(medians[:,0], medians[:,1])[1]
    pval2 = ttest_ind(medians[:,0], medians[:,2])[1]
    pval3 = ttest_ind(medians[:,1], medians[:,2])[1]

    data = np.array([[med[i], p[i]] for i in range(3)], dtype='object').flatten()
    data = np.append(data, [pval1, pval2, pval3])

    index = list(itertools.product(['F1/F2', 'F3', 'F4'], ['median', str(p2-p1)+'% CI']))
    index.extend([('p-value', 'F1/F2 vs F3'), ('p-value', 'F1/F2 vs F4'), ('p-value', 'F3 vs F4')])
    index = pd.MultiIndex.from_tuples(index)

    return pd.DataFrame(data, columns=[col], index=index)

def add_apri_fib4_albi(df):
    df['APRI'] = df['SGOT']/40/df['Platelets']*100
    df['FIB-4'] = (df['Age']/365.25)*df['SGOT']/(df['Platelets']*np.sqrt(df['Alk_Phos']))
    df['ALBI'] = 0.66*np.log(df['Bilirubin']*100000/584.66 - 0.085*df['Albumin']*100)
    
    return df

# For Permutation Bootstrap ALBI, APRI, FIB-4
def perm_bs_pval(female_df, male_df, m=10000):
    '''
    Main function that calculates the p-values for observed difference in means between the two dataframes.
    '''
    obs_diff = female_df.groupby('Stage').mean() - male_df.groupby('Stage').mean()
    a, b = obs_diff.shape
    diff_vals = np.abs(obs_diff.values)
    cols = obs_diff.columns
    index = obs_diff.index

    bs_means = np.abs(perm_bs_means(female_df, male_df, m=m))
    m = bs_means.shape[0]

    pvals = np.empty([a,b])
    for i in range(a):
        for j in range(b):
            pvals[i,j] = np.sum(bs_means[:,i,j] > diff_vals[i,j])/m

    return pd.DataFrame(pvals, columns=cols, index=index)

def perm_bs_means(female_df, male_df, m=10000):
    stage_counts = dict(male_df.Stage.value_counts())

    bs_means = np.empty([m,3,3])
    for i in range(m):
        sample_f_df = sample_df(female_df, stage_counts)
        sample_m_df = sample_df(male_df, stage_counts)

        sample_mf = concat_permute(sample_f_df, sample_m_df)
        bs_means[i] = diff_mean_by_stage(sample_mf).values

    return bs_means

def sample_df(df, sample_counts):
    '''
    intended to take in trunc_female/trunc_male and return samples of ALBI, APRI, FIB-4 with the same stage counts as trunc_male
    '''
    samples = pd.DataFrame()
    for key, val in sample_counts.items():
        temp_df = df[df['Stage'] == key].sample(val, replace=True)
        samples = pd.concat([samples, temp_df], axis=0)
    return samples

def concat_permute(df1, df2):
    len1, len2 = (df1.shape[0], df2.shape[0])
    
    df = pd.concat([df1, df2], axis=0)
    df = df.sample(frac=1)
    df['Sex'] = ['F']*len1 + ['M']*len2
    
    return df

def diff_mean_by_stage(df):
    f_mean = df[df['Sex'] == 'F'][df.columns.drop('Sex')].groupby('Stage').mean()
    m_mean = df[df['Sex'] == 'M'][df.columns.drop('Sex')].groupby('Stage').mean()
    
    return f_mean - m_mean