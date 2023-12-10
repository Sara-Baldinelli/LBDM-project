import numpy as np
from scipy.stats import wilcoxon, mannwhitneyu
import pandas as pd
import statsmodels.api as sm

skip_header = 0
genes = []
pvals = []

# INTERVALS
# GP4 = []
# GP3 = []
# SHH = []
# WNT = []
# Cntrl = []
#
# DF = pd.read_csv("label_integrated.tsv", sep='\t')
# for index, row in DF.iterrows():
#     if row['subtype'] == 'GP4':
#         GP4.append(index)
#     elif row['subtype'] == 'GP3':
#         GP3.append(index)
#     elif row['subtype'] == 'SHH':
#         SHH.append(index)
#     elif row['subtype'] == 'WNT':
#         WNT.append(index)
#     else:
#         Cntrl.append(index)
#
# def convert_to_intervals(index_list):
#     intervals = []
#     if not index_list:
#         return intervals
#
#     current_start = index_list[0]
#     current_end = index_list[0]
#
#     for index in index_list[1:]:
#         if index == current_end + 1:
#             current_end = index
#         else:
#             intervals.append((current_start, current_end))
#             current_start = current_end = index
#
#     intervals.append((current_start, current_end))
#     return intervals
#
#
#
# intervals1 = convert_to_intervals(GP4)
# intervals2 = convert_to_intervals(GP3)
# intervals3 = convert_to_intervals(SHH)
# intervals4 = convert_to_intervals(WNT)
# intervals5 = convert_to_intervals(Cntrl)
#
# print("Intervals:", intervals1)
# print(intervals2)
# print(intervals3)
# print(intervals4)
# print(intervals5)

with open("GSE_integrated.tsv") as fileobject:
    for line in fileobject:
        if skip_header == 0:
            skip_header += 1
            print('Skipped header')
            continue
        l = line.split()
        genes.append(l[0])
        l = [eval(i) for i in l[1:]]
        # cases = np.concatenate((np.array(l[:1121]), np.array(l[4605:7144]),
        #                         np.array(l[9144:10827]), np.array(l[12244:18215]),
        #                         np.array(l[21700:22158]), np.array(l[25231:27124]),
        #                         np.array(l[28879:30493]), np.array(l[38467:39946])))
        #
        cases = np.array(l[18215:19047])
        controls = np.array(l[39946:])
        _, pv = mannwhitneyu(cases, controls)
        pvals.append(pv)
        print(skip_header)
        skip_header += 1

reject, p_values_corrected, _, _ = sm.stats.multipletests(pvals, alpha=0.05, method='fdr_bh')

df = pd.DataFrame({'gene':genes, 'pvalues':pvals, 'pvaluesC':p_values_corrected})

df.to_csv("WNT_DE_pvalues.tsv", sep='\t', index=False)

