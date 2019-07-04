# k-means
""" scale your variables
     estimate the number of centroids
"""

"### Setting up for clustering analysis"
 import numpy as np
 import pandas as pd

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm   # to evaluate the model
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
 
%matplotlib inline
plt.figure(figsize=(7, 4))

iris = datasets.load_iris()

X = scale(iris.data)
y = pd.DataFrame(iris.target)
variable_names = iris.feature_names
X[0:10,]
 
 "## Building and running your model
 
clustering = KMeans(n_clusters=3, random_state=5)   # state - initializes the centroids before clustering
clustering.fit(X)
 
 "## Plotting your model outputs
iris_df = pd.DataFrame(iris.data)
iris_df.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y.columns = ['Targets']

color_theme = np.array(['darkgray', 'lightsalmon', 'powderblue'])

plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[clustering.labels_], s=50)
plt.title('K-Means Classification')

relabel = np.choose(clustering.labels_, [2, 0, 1]).astype(np.int64)
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1, 2, 2)
# relabel the clusters
relabel = np.choose(clustering.labels_, [2, 0, 1]).astype(np.int64)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[relabel], s=50)
plt.title('K-Means Classification')

"## Evaluate your clustering results
print(classification_report(y, relabel))

""" precision - measure of the model's relevancy
     recall - measure of the model's completeness
"""

### Hierarchical Clustering
"#### Setting up for clustering analysis"
""" Distance Metrics: Euclidian, Manhattan, Cosine
     Linkage Parameters: Ward, Complete, Average
     Parameter selection method - trial and error
"""
 import numpy as np
import pandas as pd

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm
 
 np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10, 3))
%matplotlib inline
plt.style.use('seaborn-whitegrid')
 
 address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch06/06_02/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X = cars.ix[:,(1,3,4,6)].values

y = cars.ix[:,(9)].values

 "### Using scipy to generate dendrograms
 
 Z = linkage(X, 'ward')"
 dendrogram(Z, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=15., show_contracted=True)

plt.title('Truncated Hierarchical Clustering Dendrogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.axhline(y=500)
plt.axhline(y=150)
plt.show()"
 
 "### Generating hierarchical clusters"
 
 k=2
 
 Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
Hclustering.fit(X)
 
sm.accuracy_score(y, Hclustering.labels_)"

# different combinations of parameters -> chose best results
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='complete')
Hclustering.fit(X)

sm.accuracy_score(y, Hclustering.labels_)"
 
 Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='average')
Hclustering.fit(X)
,
sm.accuracy_score(y, Hclustering.labels_)"

Hclustering = AgglomerativeClustering(n_clusters=k, affinity='manhattan', linkage='average')
"Hclustering.fit(X)

sm.accuracy_score(y, Hclustering.labels_)"
 

"## Segment 3 - Instance-based learning w/ k-Nearest Neighbor
"#### Setting up for classification analysis"
 import numpy as np
import pandas as pd
import scipy
,
import matplotlib.pyplot as plt
from pylab import rcParams
 
import urllib

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import metrics
 
 np.set_printoptions(precision=4, suppress=True) 
%matplotlib inline
rcParams['figure.figsize'] = 7, 4
plt.style.use('seaborn-whitegrid')
 
"## Splitting your data into test and training datasets"
address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch06/06_03/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X_prime = cars.ix[:,(1,3,4,6)].values
 y = cars.ix[:,9].values
 
 # scale variables
 X = preprocessing.scale(X_prime)"
# random_state - to be able to reproduce results
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)"
 
 "## Building and training your model with training data"
 
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)
 
 "## Evaluating your model's predictions against the test dataset"
 
y_expect = y_test
y_pred = clf.predict(X_test)
print(metrics.classification_report(y_expect, y_pred))"
 