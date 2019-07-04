# Types of ML Algorithms
""" - Deep Learning         - Ensemble                - Rule System
     - Neural Network       - Decision Trees         - Regularization
     - Regression               - Bayesian                  - Dimension Reduction
     - Instance Based         - Clustering
 """

### Factor Analysis
""" features are metrics // features are continuous or ordinal // r > 0.3 correlation //
     100+ observations and 5+ observations per feature // sample is homogenous
"""
# Dimensionality Reduction

 "## Segment 2 - Explanatory factor analysis"
import pandas as pd
import numpy as np
 
import sklearn
from sklearn.decomposition import FactorAnalysis

from sklearn import datasets"

"### Factor analysis on iris dataset
 
iris =  datasets.load_iris()
X = iris.data
variable_names = iris.feature_names
X[0:10,]

factor = FactorAnalysis().fit(X)
pd.DataFrame(factor.components_, columns=variable_names)

 ### SVD - Singular Value Decomposition
 
"## Segment 3 - Principal component analysis (PCA)
 import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

%matplotlib inline
 rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
 
 "### PCA on the iris dataset
 X = iris.data
variable_names = iris.feature_names
 X[0:10,]
 
 pca = decomposition.PCA()
iris_pca = pca.fit_transform(X)

pca.explained_variance_ratio_
pca.explained_variance_ratio_.sum()

comps = pd.DataFrame(pca.components_, columns=variable_names)
comps

sb.heatmap(comps) 