# Point outliers / Contextual Outliers / Collective Outliers

"## Extreme value analysis using univariate methods"
 
 import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
 %matplotlib inline
rcParams['figure.figsize'] = 5,4
 
df = pd.read_csv( filepath_or_buffer='C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch05/05_01/iris.data.csv'
     header=None,  sep=',')
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
X = df.ix[:,0:4].values
 y = df.ix[:,4].values

df[:5]
 
 "### Identifying outliers from Tukey boxplots"
df.boxplot(return_type='dict')
plt.plot()
 
Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width > 4)
df[iris_outliers]
 
 Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width < 2.05)
 df[iris_outliers]
 
"### Applying Tukey outlier labeling
 pd.options.display.float_format = '{:.1f}'.format
X_df = pd.DataFrame(X)
print X_df.describe()


"## Segment 2 - Multivariate analysis for outlier detection
 import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

 %matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
 
 "### Visually inspecting boxplots"
df = pd.read_csv(
     filepath_or_buffer='C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch05/05_02/iris.data.csv',
     header=None, sep=',')
 
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
data = df.ix[:,0:4].values
target = df.ix[:,4].values
df[:5]

sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')

### Looking at the scatterplot matrix
 sb.pairplot(df, hue='Species', palette='hls')


## Segment 3 - DBSCan clustering to identify outliers - less than 5% of outliers
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams\n",
import seaborn as sb

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter
 
%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
 
### DBSCan clustering to identify outliers
#### Train your model and identify outliers
df = pd.read_csv
filepath_or_buffer='C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch05/05_03/iris.data.csv'
       header=None, sep=',')
  
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
data = df.ix[:,0:4].values
target = df.ix[:,4].values
df[:5]
 
model = DBSCAN(eps=0.8, min_samples=19).fit(data)
print(model)
 
#### Visualize your results"
 outliers_df = pd.DataFrame(data)

print Counter(model.labels_)

print outliers_df[model.labels_ == -1]

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

colors = model.labels_

ax.scatter(data[:,2], data[:,1], c=colors, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBScan for Outlier Detection')
