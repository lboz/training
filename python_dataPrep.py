
# Segment 1 - Filtering and selecting data"

# import library

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

 # Selecting and retrieving data"
series_obj = Series(np.arange(8), index=[
                    'row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])
series_obj

 # When you write square brackets with a label-index inside them, this tells Python to select and
# retrieve all records with that label-index.
series_obj['row 7']
series_obj[[0, 7]]

np.random.seed(25)

DF_obj = DataFrame(np.random.rand(36).reshape((6, 6)),  index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                                  columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
DF_obj

DF_obj.ix[['row 2', 'row 5'], ['column 5', 'column 2']]


 # Data slicing
 """Data slicing allows you to select and retrieve all records from the starting label-index, to the \n",
     ending label-index, and every record in between.
 """
series_obj['row 3':'row 7']

# Comparing with scalars"
"""You can use comparison operators (like greater than or less than) to return True / False values for
     all records, to indicate how each element compares to a scalar value.
"""
DF_obj < .2

 # Filtering with scalars
 """ You can also use comparison operators and scalar values for indexing, to return only the records \n",
       that satisfy the comparison expression you write.
 """
series_obj[series_obj > 6]

# Setting values with scalars
""" Setting is where you select all records associated with the specified label-indexes and set those \n",
     values equal to a scalar
"""
series_obj['row 1', 'row 5', 'row 8'] = 8
series_obj


#######################################
 # Treating missing values
#######################################

 import numpy as np
 import pandas as pd
from pandas import Series, DataFrame

# Figuring out what data is missing"
 missing = np.nan
series_obj = Series(['row 1', 'row 2', missing, 'row 4',
                    'row 5', 'row 6', missing, 'row 8'])
series_obj

# isnull method
# The .isnull() method returns a Boolean value that describes (True or False) whether an element in a \n",
# Pandas object is a null value
 series_obj.isnull()

 # Filling in for missing values
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6, 6))
DF_obj

DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
DF_obj

# object_name.fillna(numeric value)
# The .fillna method() finds each missing value from within a Pandas object and fills it with the \n",
# numeric value that you've passed in.\
filled_DF = DF_obj.fillna(0)
filled_DF

# object_name.fillna(dict)
 # You can pass a dictionary into the .fillna() method. The method will then fill in missing values \n",
# from each column Series (as designated by the dictionary key) with its own unique value \n",
# (as specified in the corresponding dictionary value).\n",
filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
filled_DF

# You can also pass in the method='ffill' arguement, and the .fillna() method will fill-forward any \n",
# missing values with values from the last non-null element in the column Series.\n",
fill_DF = DF_obj.fillna(method='ffill')
 fill_DF"


 # Counting missing values         ]
 np.random.seed(25)
 DF_obj = DataFrame(np.random.randn(36).reshape(6, 6))
 DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
DF_obj


 # object_name.isnull().sum()\n",
# To generate a count of how many missing values a DataFrame has per column, just call the .isnull() \n",
# method off of the object, and then call the .sum() method off of the matrix of Boolean values it \n",
# returns.
DF_obj.isnull().sum()

 # Filtering out missing values

 # object_name.dropna()
 # To identify and drop all rows from a DataFrame that contain ANY missing values, simply call the \n",
 # .dropna() method off of the DataFrame object. NOTE: If you wanted to drop columns that contain \n",
# any missing values, you'd just pass in the axis=1 argument to select and search the DataFrame \n",
# by columns, instead of by row.\n",
DF_no_NaN = DF_obj.dropna(axis=1)
 DF_no_NaN

 # object_name.dropna(how='all')\n",
 # To identify and drop only the rows from a DataFrame that contain ALL missing values, simply \n",
# call the .dropna() method off of the DataFrame object, and pass in the how='all' argument.\n",
DF_obj.dropna(how='all')


#######################################
# Removing duplicates
#######################################
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
 
### Removing duplicates
DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                    'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                     'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
DF_obj

# object_name.duplicated()
# The .duplicated() method searches each row in the DataFrame, and returns a True or False value to \n",
 #indicate whether it is a duplicate of another row found earlier in the DataFrame.\n",
 DF_obj.duplicated()
 
# object_name.drop_duplicates()
# To drop all duplicate rows, just call the drop_duplicates() method off of the DataFrame.\n",
 DF_obj.drop_duplicates()
  
 # drop duplicates - column name
 # To drop the rows that have duplicates in only one column Series, just call the drop_duplicates() \n",
 # method off of the DataFrame, and pass in the label-index of the column you want the de-duplication \n",
# to be based on. This method will drops all rows that have duplicates in the column you specify.\n",

 DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                     'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                     'column 3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']})
DF_obj
DF_obj.drop_duplicates(['column 3'])
  
##################################################################
## Concatenating and transforming data
##################################################################
  
import numpy as np
 import pandas as pd
 from pandas import Series, DataFrame
 
 DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
 DF_obj"
  
DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
 DF_obj_2
 
 ### Concatenating data
 
#  pd.concat([left_object, right_object], axis=1)
 # The concat() method joins data from seperate sources into one combined data table. If you want to \n",
 # join objects based on their row index values, just call the pd.concat() method on the objects you \n",
# want joined, and then pass in the axis=1 argument. The axis=1 argument tells Python to concatenate \n",
 # the DataFrames by adding columns (in other words, joining on the row index values).\n",
 pd.concat([DF_obj, DF_obj_2], axis =1)
 
 # no axis - the second data frame is added to the buttom (union)
 pd.concat([DF_obj, DF_obj_2])
 
 ### Transforming data
 #### Dropping data
# object_name.drop([row indexes])
 
 # You can easily drop rows from a DataFrame by calling the .drop() method and passing in the index \n",
 # values for the rows you want dropped.
# drop rows
DF_obj.drop([0,2])
 
 # drop columns
 DF_obj.drop([0,2], axis=1)
 
 ### Adding data
 series_obj = Series(np.arange(6))
series_obj.name = \"added_variable\"
 series_obj
 
# DataFrame.join(left_object, right_object)
# You can use .join() method two join two data sources into one. The .join() method works by joining \n",
# the two sources on their row index values.\n",
 variable_added = DataFrame.join(DF_obj, series_obj)
variable_added

added_datatable = variable_added.append(variable_added, ignore_index=False)
 added_datatable
 # variables added and reindexed
 added_datatable = variable_added.append(variable_added, ignore_index=True)
 added_datatable
  
  
 # sorting data 
 # object_name.sort_values(by=[index value], ascending=[False])
 # To sort rows in a DataFrame, either in ascending or descending order, call the .sort_values() \n",
 # method off of the DataFrame, and pass in the by argument to specify the column index upon which \n",
 # the DataFrame should be sorted.\n",
 DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
 DF_sorted
 

 ## Grouping and data aggregation
 
import  numpy as np
 import pandas as pd
 from pandas import Series, DataFrame"
 
### Grouping data by column index"
 
# import the file
address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
 cars.head()
 
# object_name.groupby('Series_name')
# To group a  DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass\n",
# in the column Series you want the DataFrame to be grouped by.\n",
cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()

