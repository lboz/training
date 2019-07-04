### Basic Math and Statistics
## Using NumPy to perform arithmetic operations on data

import numpy as np
from numpy.random import randn
 
np.set_printoptions(precision=2)
 
## Creating arrays
"### Creating arrays using a list

a = np.array([1,2,3,4,5,6])
b = np.array([[10,20,30], [40,50,60]])
 
"### Creating arrays via assignment
 np.random.seed(25)
 c = 36*np.random.randn(6)
c
d = np.arange(1, 35)
  
 "## Performing arthimetic on arrays
a * 10
c + a
c - a
c * a
c / a
 
### Multiplying matrices and basic linear algebra
aa = np.array([[2.,4.,6.], [1.,3.,5.], [10.,20.,30.]])
aa
bb = np.array([[0.,1.,2.], [3.,4.,5.], [6.,7.,8.]])
bb
aa * bb

np.dot(aa, bb)

"## Segment 2 - Generating summary statistics using pandas and scipy

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats
 
 address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars.head()
 
 "### Looking at summary statistics that describe a variable's numeric values
 cars.sum()
 # ???
cars.sum(axis=1)

cars.median()
cars.mean()
cars.max()
 
mpg=cars.mpg
# identify the row with the max value
mpg.idxmax()
 
 ### Looking at summary statistics that describe variable distribution
cars.std()
cars.var()
 
gear=cars.gear
# unique values
gear.value_counts()

cars.describe()

"## Segment 3 - Summarizing categorical data using pandas
 
import numpy as np
import pandas as pd

"### The basics"
 
 address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
cars.head(15)
  
"# object_name.value_counts()

 "# The .value_counts() method makes a count of all unique values in an array or Series object. \n"
 carb = cars.carb
carb.value_counts()

# object_name.groupby('column_index')
 "# To group a DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass\n",
"# in the index value of the column Series you want the DataFrame to be grouped by.\n",
cars_cat = cars[['cyl','vs','am','gear','carb']]
cars_cat.head()
 
gears_group = cars_cat.groupby('gear')
gears_group.describe()

"### Transforming variables to categorical data type
 pd.Series(x_variable, dtype)
 
"# To create a Series of categorical data type, call the pd.Series() function on the array or Series that holds the data you\n",
"# want the new Series object to contain. When you pass in the dtype=\"category\" argument, this tells Python to assign the new\n",
"# Series a data type of \"category\". Here we create a new categorical Series from the gear variable, and then assign it to a\n",
"# new column in the cars DataFrame, called 'group'.
cars['group'] = pd.Series(cars.gear, dtype=\"category\")
cars['group'].dtypes
cars['group'].value_counts()

"### Describing categorical data with crosstabs
pd.crosstab(y_variable, x_variable)
 
 "# To create a cross-tab, just call the pd.crosstab() function on the variables you want included in \n",
"# the output table.
pd.crosstab(cars['am'], cars['gear'])
 
"## Segment 4 - Starting with parametric methods in pandas and scipy
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr
 
%matplotlib inline
rcParams['figure.figsize'] = 8, 4
plt.style.use('seaborn-whitegrid')
 
 "### The Pearson Correlation"
 # Assumptions: normally distributed, linearly related, continuous, numeric variables
address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch03/03_04/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
sb.pairplot(cars)
# keep just variables we want
X = cars[['mpg', 'hp', 'qsec','wt']]
sb.pairplot(X)

"### Using scipy to calculate the Pearson correlation coefficient"
mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']
 
 pearsonr_coefficient, p_value = pearsonr(mpg, hp)
 print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)

"### Using pandas to calculate the Pearson correlation coefficient
 corr=X.corr()
 corr
 
"### Using Seaborn to visualize the Pearson correlation coefficient"
 sb.heatmap(corr,xticklabels=corr.columns.values, yticklabels=corr.columns.values)
 
"## Delving into non-parametric methods using pandas and scipy
import numpy as np
 import pandas as pd
 
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr

 %matplotlib inline
rcParams['figure.figsize'] = 14, 7
plt.style.use('seaborn-whitegrid')

 "### The Spearman Rank Correlation - ordinal data types

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch03/03_05/mtcars.csv'
cars = pd.read_csv(address)
 cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
 cars.head()

 sb.pairplot(cars)
 
X = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(X)

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']
spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
 
 spearmanr_coefficient, p_value = spearmanr(cyl, am)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)

spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
 
 "### Chi-square test for independence
table = pd.crosstab(cyl, am)
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)

table=pd.crosstab(cars['cyl'], cars['vs'])    
chi2, p, dof, expected=chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
  
table=pd.crosstab(cars['cyl'], cars['gear'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)

"## Transforming dataset distributions
import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

 %matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
 
"### Normalizing and transforming features with MinMaxScalar() and fit_transform()
 address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch03/03_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']"
 
 mpg = cars.mpg
 plt.plot(mpg)

cars[['mpg']].describe()

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
 
  "### Using scale() to scale your features
 standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standardized_mpg)

standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)