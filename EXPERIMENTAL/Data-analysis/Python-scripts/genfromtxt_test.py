import numpy as np



rootpath_file = 'C:\\MASTER-THESIS\\EXPERIMENTAL\\Data\\SEM-images\\2024-02-21_Cu-Li_SEM-03_110_test.sem' # remember to write '\\' for every '\'

generated_file = np.genfromtxt(rootpath_file, skip_header=89, dtype='int16')
print(len(generated_file))















