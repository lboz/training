## Segment 1 - Linear Regression"
import numpy as np\n"
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.linear_model import LinearRegression
 from sklearn.preprocessing import scale
from collections import Counter

%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch08/08_01/enrollment_forecast.csv'
enroll = pd.read_csv(address)
enroll.columns = ['year','roll','unem', 'hgrad', 'inc']
enroll.head()"

sb.pairplot(enroll)

print enroll.corr()"
enroll_data = enroll.ix[:,(2,3)].values
enroll_target = enroll.ix[:, 1].values

enroll_data_names = ['unem', 'hgrad']

# scales variables
X, y = scale(enroll_data), enroll_target

"### Checking for missing values"
missing_values = X==np.NAN
X[missing_values == True]

LinReg = LinearRegression(normalize=True)

LinReg.fit(X,y)

print LinReg.score(X, y)


"## Segment 2 - Logistic Regression
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy.stats import spearmanr

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.preprocessing import scale 
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing"

%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')"

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch08/08_02/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

cars_data = cars.ix[:,(5,11)].values
cars_data_names = ['drat', 'carb']

# isolates the target variable
y = cars.ix[:,9].values"

#### Checking for independence between features"
sb.regplot(x='drat', y='carb', data=cars, scatter=True)"

drat = cars['drat']
carb = cars['carb']

spearmanr_coefficient, p_value =  spearmanr(drat, carb)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)"

#### Checking for missing values"
cars.isnull().sum()"

#### Checking that your target is binary or ordinal"
sb.countplot(x='am', data=cars, palette='hls')"

#### Checking that your dataset size is sufficient - 50+ per value
cars.info()

#### Deploying and evaluating your model"
X = scale(cars_data)"
LogReg = LogisticRegression()

LogReg.fit(X,y)
print LogReg.score(X,y)"

y_pred = LogReg.predict(X)
# gives precision - recall - f1 score - support information
from sklearn.metrics import classification_report
print(classification_report(y, y_pred))


"##  Naive Bayes Classifiers"
 
import numpy as np
import pandas as pd

import urllib

import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score"
 
## Naive Bayes
" 3 types: multinomial, Bernoulli, Gaussian"

### Using Naive Bayes to predict spam"
 """ Assumptions: predictors are independent to each other
      Past conditions still hold true
      All regression models maintain an a priori assumption as well
"""
url = \"https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data\"
# opens the url
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=\",\")
print dataset[0]
 
X = dataset[:,0:48]
y = dataset[:, -1]
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)"
 
 # Bernoulli method
BernNB = BernoulliNB(binarize=True)
BernNB.fit(X_train, y_train)
print(BernNB)

y_expect = y_test
y_pred = BernNB.predict(X_test)
print accuracy_score(y_expect, y_pred)
 
 # multinominal
MultiNB = MultinomialNB()

MultiNB.fit(X_train, y_train)
print(MultiNB)

y_pred = MultiNB.predict(X_test)
print accuracy_score(y_expect, y_pred)
 
# Gaussian method
GausNB = GaussianNB()
GausNB.fit(X_train, y_train)
print(GausNB)

y_pred = GausNB.predict(X_test)
print accuracy_score(y_expect, y_pred)

# Bernoulli method ???? 
BernNB = BernoulliNB(binarize=0.1)
BernNB.fit(X_train, y_train)
print(BernNB)

y_expect = y_test
y_pred = BernNB.predict(X_test)
print accuracy_score(y_expect, y_pred)