import pandas as pd
import os

gene_list = []
ff = open("Gene_names.txt", 'r')
for line in ff.readlines():
    if '\n' in line:
        gene_list.append(line.split(sep='\n')[0])
    else:
        gene_list.append(line)
print(gene_list)

def check_files_for_string(folder_path, target_string):
    # Traverse the directory and check each file
    l = 'null'
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if target_string in file_name:
               l = file_name
    return l


starting_folder = 'hs.FANTOM.annotated'
for gene_name in gene_list:
    # select isoform 1
    target = f'p1@{gene_name}.csv'
    matching_file = check_files_for_string(starting_folder, target)
    if matching_file == 'null':
        print(f'MATCH NOT FOUND for {gene_name}')
        continue
    print(f'MATCHING {gene_name}')
    test_set = pd.read_csv(f'/hs.FANTOM.annotated/{matching_file}', sep=',', skiprows=1)
    # print(test_set.head())
    # f_rel = input("insert relative frequency: ")
    f_rel = 0.95

# put inside gene:name
    saved_genes = [gene_name]
    for i, row in test_set.iterrows():
        if row['Frel'] >= f_rel and row['transcript'].split('@')[1] not in saved_genes:
            saved_genes.append(row['transcript'].split('@')[1])
        if row['Frel'] < f_rel:
            break

# filename gene:name
    f = open(f"{gene_name}_edges.txt", 'w')
    for el in saved_genes[1:]:
        f.write(f'{saved_genes[0]} {el}\n')

    f.close()

