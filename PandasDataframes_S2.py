#In Pandas Series is one dimentional data structures
#Data frames are two dimentional data structures defined in pandas which consists of rows and columns.
#We can analyze data in pandas with: Series and DataFrames
    
import pandas as pd 

# Create series with Data, and Index 
a = pd.Series(Data, index = Index) 
'''
Data can be:

A Scalar value which can be integerValue, string
A Python Dictionary which can be Key, Value pair
A Ndarray
Note: Index by default is from 0, 1, 2, …(n-1) where n is length of data.
'''
Data =[1, 3, 4, 5, 6, 2, 9]   
# Creating series with default index values 
s = pd.Series(Data)     
print(s) 
#############################################
# predefined index values 
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g']  
  
# Creating series with predefined index values 
si = pd.Series(Data, Index)  
print(si) 
#############################################
dictionary ={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}  
  
# Creating series of Dictionary type 
sd = pd.Series(dictionary)  
print(sd) 
############################################
# Defining 2darray 
Data =[[2, 3, 4], [5, 6, 7]]   
  
# Creating series of 2darray 
snd = pd.Series(Data)   
print(snd)  
##########################################
a = pd.DataFrame(Data)  
print(a)   
##########################################
# Define Dictionary 1 
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}    
  
# Define Dictionary 2      
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9}  
  
# Define Data with dict1 and dict2 
Data = {'first':dict1, 'second':dict2}  
  
# Create DataFrame  
df = pd.DataFrame(Data)   
print(df) 
##########################################
# Program to create Dataframe of three series  
# Define series 1 
s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])    
  
# Define series 2        
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  
  
# Define series 3 
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])      
  
# Define Data 
Data ={'first':s1, 'second':s2, 'third':s3}  
  
# Create DataFrame 
dfseries = pd.DataFrame(Data)
print(dfseries)    
##########################################
# Define 2d array 1 
d1 =[[2, 3, 4], [5, 6, 7]]  
  
# Define 2d array 2 
d2 =[[2, 4, 8], [1, 3, 9]]  
  
# Define Data 
Data ={'first': d1, 'second': d2}   
  
# Create DataFrame 
df2d = pd.DataFrame(Data)  
print(df2d) 
#######################################
df = pd.read_csv("E:\Office\Python\Rk\PYTHON_master\Pandas\data\IND.csv") 
# Prints all the columns headers when header=0
df = pd.read_csv("E:\Office\Python\Rk\PYTHON_master\Pandas\data\IND.csv", header=0) 
# Prints without columns headers when header=1
df = pd.read_csv("E:\Office\Python\Rk\PYTHON_master\Pandas\data\IND.csv", header=1)   
print(df)

# Prints the first 5 rows of a DataFrame as default 
df.head()   
# Prints no. of rows and columns of a DataFrame 
df.shape 

###########################################
#The iloc method allows to retrieve as  many as rows and columns by position.
# prints first 5 rows and every column which replicates df.head() 
df.iloc[0:5,:] 
# prints entire rows and columns 
df.iloc[:,:] 
# prints from 5th rows and first 5 columns 
df.iloc[5:,:5] 
#############################################
'''
Indexing can be worked with labels using the pandas.DataFrame.loc method, 
which allows to index using labels instead of positions.
'''
# prints first five rows including 5th index and every columns of df 
df.loc[0:5,:] 
# prints from 5th rows onwards and entire columns 
df = df.loc[5:,:] 
#############################################
# Prints the first 5 rows of Time period 
# value  
df.loc[:5,"Time period"] 
############################################
# computes various summary statistics, excluding NaN values 
df.describe() 
# for computing correlations 
df.corr() 
# computes numerical data ranks 
df.rank() 

###########Storing DataFrame in CSV Format###########################
#to.csv('filename', index = "False|True")
# assigning three series to s1, s2, s3 
s1 = pd.Series([0, 4, 8]) 
s2 = pd.Series([1, 5, 9]) 
s3 = pd.Series([2, 6, 10]) 
  
# taking index and column values 
dframe = pd.DataFrame([s1, s2, s3]) 
  
# assign column name 
dframe.columns =['Chakra1', 'Chakra2', 'Chakra3'] 
  
# write data to csv file 
dframe.to_csv('E:\Office\Python\Rk\PYTHON_master\Pandas\data\Chakra.csv', index = False)   
dframe.to_csv('E:\Office\Python\Rk\PYTHON_master\Pandas\data\Chakra1.csv', index = True) 

##################Handling Missing Data#############################
# Create a DataFrame 
dframe = pd.DataFrame({'Chakra1': [23, 24, 22],  
                       'Chakra2': [10, 12, np.nan], 
                       'Chakra3': [0, np.nan, np.nan]}, 
                       columns =['Chakra1', 'Chakra2', 'Chakra3']) 
  
# This will remove all the rows with NAN values 
  
# If axis is not defined then it is along rows i.e. axis = 0 
dframe.dropna(inplace = True) 
print(dframe) 
  
# if axis is equal to 1 
dframe.dropna(axis = 1, inplace = True)  
print(dframe) 
###################################################
# import the required module  
import matplotlib.pyplot as plt 
# plot a histogram  
df['Observation Value'].hist(bins=10) 
  
# shows presence of a lot of outliers/extreme values 
df.boxplot(column='Observation Value', by = 'Time period') 
  
# plotting points as a scatter plot 
x = df["Observation Value"] 
y = df["Time period"] 
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 
# x-axis label 
plt.xlabel('Observation Value') 
# frequency label 
plt.ylabel('Time period') 
# function to show the plot 
plt.show() 
################Fill the missing values############################
import numpy as np 
import pandas as pd 
# Create a DataFrame 
dframe = pd.DataFrame({'Chakra1': [23, 24, 22],  
                        'Chakra2': [10, 12, np.nan], 
                        'Chakra3': [0, np.nan, np.nan]}, 
                        columns = ['Chakra1', 'Chakra2', 'Chakra3']) 
  
# Use fillna of complete Dataframe  
  
# value function will be applied on every column 
dframe.fillna(value = dframe.mean(), inplace = True) 
print(dframe) 
  
# filling value of one column 
dframe['Chakra2'].fillna(value = dframe['Chakra2'].mean(), inplace = True) 
print(dframe) 
##################Groupby Method (Aggregation) #####################
dframe = pd.DataFrame({'Chakra1': [23, 24, 22, 22, 23, 24],  
                        'Chakra2': [10, 12, 13, 14, 15, 16], 
                        'Chakra3': [122, 142, 112, 122, 114, 112]}, 
                        columns = ['Chakra1', 'Chakra2', 'Chakra3'])  
  
# Apply groupby and aggregate function 
# max to find max value of column  
  
# &quot;For&quot; and column &quot;chakra&quot; for every 
# different value of column &quot;Chakra&quot;. 
  
print(dframe.groupby(['Chakra1']).max()) 
################################################