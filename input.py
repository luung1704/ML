import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
names = ['id','class','clump_thickness','uniform_cell_size','uniform_cell_shape','marginal_adhesion','single_epi_cell_size','bare_nuclei','bland_chromation','normal_nucleoli','mitoses']
df = pd.read_csv('data.csv',names=names)
# replace missing values
#df= df.replace('?',-1)
#df= df.replace(-1,np.nan)
#df = df.dropna(how='any')
df.drop(['id'], 1, inplace=True)
X_test = np.array(df.drop(['class'], 1))
y_test= np.array(df['class'])
print(X_test)
