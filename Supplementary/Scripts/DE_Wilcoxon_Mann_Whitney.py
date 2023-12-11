import numpy as np
from scipy.stats import wilcoxon, mannwhitneyu
import pandas as pd
import statsmodels.api as sm

skip_header = 0
genes = []
pvals = []
with open("GSE_integrated.tsv") as fileobject:
    for line in fileobject:
        if skip_header == 0:
            skip_header += 1
            print('Skipped header')
            continue
        l = line.split()
        genes.append(l[0])
        l = [eval(i) for i in l[1:]]
        cases = np.array(l[:38599])
        controls = np.array(l[38599:])
        _, pv = mannwhitneyu(cases, controls)
        pvals.append(pv)
        print(skip_header)
        skip_header += 1

reject, p_values_corrected, _, _ = sm.stats.multipletests(pvals, alpha=0.05, method='fdr_bh')

df = pd.DataFrame({'gene':genes, 'pvalues':pvals, 'pvaluesC':p_values_corrected})

df.to_csv("test.tsv", sep='\t', index=False)
