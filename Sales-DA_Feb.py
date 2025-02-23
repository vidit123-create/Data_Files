# Import libraries :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset :
df = pd.read_excel('Sales_By_Months_1.xlsx')

# Get the top and bottom five values from the dataset :
print(f"Top five values from dataset : \n {df.head()}"+'\n'+
      f"Bottom five values from dataset : \n {df.tail()}")

# Extract all the headers from dataset :
print(f"All the headers : {list(df.columns)}")

# Check the overall summary :
print(df.info())

# Let us focus on the Order Date column :
df = df.rename(columns={'Order Date': 'Date_Time'})
print(df.columns)

print(len(df))
# df = df.dropna(subset='Date_Time', how='any')
# print(len(df))

df.to_csv('Filtered_Sales.csv', index=False)

df1 = pd.read_excel('Filtered_Sales_1.xlsx')

# Calculated columns from a given column :
print(df1['Date_Time'].head(20))
S1 = df1['Date_Time'].str.split(' ')
list_1, list_2 = list(S1), []
for i in list_1:
    list_2.append(i[0])
# print(list_2[0:21])
for j in range(0, len(list_2)):
    df1.loc[j, 'Date'] = list_2[j]
# print(df1['Date'].head(20))
list_3, list_4 = list(df1['Date']), []
# print(list_3[0:5])
for i in list_3:
    st_1 = str()
    for j in range(0,1):
        st_1 = st_1 + i[0:5] + '/2019'
    list_4.append(st_1)
# print(list_4[0:20])
for k in range(0, len(list_4)):
    df1.loc[k, 'Date'] = list_4[k]
print(df1['Date'].head(20))
df1['Date'] = pd.to_datetime(df1['Date'],format='%m/%d/%Y')
print(df1['Date'].dtypes)

# Get the top and bottom five values from the above dataset :
print(f"Top five values : \n {df1.head()}"+'\n'+
      f"Bottom five values : \n {df1.tail()}")

# Data Cleansing : Check the missing values

list_1 = list(df1.columns)
# print(list_1)
for i in list_1:
    print(f"Missing value in column {i} : {df1[i].isnull().sum()}")

"""
There is no missing values in the given dataset.
"""
# Method II - Data Validation based on Date Time column :
print(df1['Date_Time'].head(20))
# Check the data type of datetime column :
print(df1['Date_Time'].dtypes)

S1 = df1['Date_Time'].str.split(' ')
# print(S1.head(20))
for i in range(0, len(S1)):
    df1.loc[i, 'Date'] = S1[i][0]
print(df1[['Date_Time', 'Date']].head(20))

# Remove the Junk data out of the specific Date column : /19 is the Junk value not a valid year
for j in range(0, len(df1['Date'])):
    st_1 = ''
    for k in range(0, 1):
        st_1 = st_1 + df1.iloc[j,4][0:5] + '/2019'
    df1.loc[j, 'Date'] = st_1
print(df1[['Date_Time', 'Date']].head(20))

# Conversion of given Date column into a proper DateTime column :
df1['Date'] = pd.to_datetime(df1['Date'], format='%m/%d/%Y')
print(df1['Date'].dtypes)

# Statistical Analysis : Column - Price Each
df1 = df1.rename(columns={'Price Each': 'Retail_Price'})
print(df1.columns)

# Data Distribution : Histogram using Matplotlib
plt.figure(figsize=(20,5))
plt.hist(df1['Retail_Price'], color='green',
         label='Range v/s Frequency')
plt.xlabel('Price_Range')
plt.ylabel('Frequency')
plt.grid()
plt.title('Price_Range v/s Frequency')
plt.legend()
plt.show()

"""
By seeing the distribution of given graph it is right-skewed data which means data points are
more at the left side comparatively to right side which means skewness is there are data is 
not normally distributed - Median < Mean
"""

# Variability - Measure of center v/s Measure of spread
print(f"Mean of Retail_Price : {round(df1['Retail_Price'].mean(), 2)}")
print(f"Median of Retail_Price : {round(df1['Retail_Price'].median(), 2)}")

print("...........................")

print(f"Range in Retail_Price column : {df1['Retail_Price'].max() - df1['Retail_Price'].min()}")
print(f"STD in Retail_Price column : {round(df1['Retail_Price'].std(), 2)}")

# Average deviation : Data_Points - Mean
avg = round(df1['Retail_Price'].mean())
for i in range(0, len(df1['Retail_Price'])):
    df1.loc[i, 'Average_Deviation'] = abs(df1.loc[i, 'Retail_Price'] - avg)
print(df1['Average_Deviation'].head(20))

# Percentage deviation : (Average_deviation/Mean) * 100
for j in range(0, len(df1['Retail_Price'])):
    df1.loc[j, 'Percentage_Deviation'] = round((df1.loc[j, 'Average_Deviation']/avg) * 100, 2)
print(df1[['Average_Deviation', 'Percentage_Deviation']].head(20))

# Overall % deviation in Retail_Price column :
overall_percentage_deviation = (df1['Percentage_Deviation'].sum())/len(df1)
print(overall_percentage_deviation)

"""
We can conclude that more than 99.7% of the data points are deviated from the mean with 
a standard deviation of 3. This means we have higher deviation and this also says we have 
outliers in the Retail_Price column.
"""

""" Outlier detection in Retail Price Column """

list_1 = list(df1.columns)
Actual_Data = len(df1['Retail_Price'])
print(f"Total No of Data Points in {list_1[3]} column before Outlier Detection : {Actual_Data}")

# Extract the given column as the part of Series :
S1 = df1['Retail_Price']

# Get the Q1, Q2, Q3 out in terms of quartiles and percentiles :
Q1, Q2, Q3 = np.percentile(S1, [25, 50, 75])
print(f"25 % : {round(Q1, 2)}"+'\n'+
      f"50 % : {round(Q2, 2)}"+'\n'+
      f"75 % : {round(Q3, 2)}")

# Calculate the Inter-Quartile Range (IQR) - Q3 - Q1
IQR = Q3 - Q1
print(f"Inter-Quartile Range : {IQR}")

# Calculate the Lower and Upper Extreme value -
Lx, Ux = (Q1-1.5*IQR), (Q3+1.5*IQR)
print(f"Lower Extreme Value : {round(Lx, 2)}"+'\n'+
      f"Upper Extreme Value : {round(Ux, 2)}")

# Filter the Outliers based on Lx and Ux concept :
Filtered_Data = df1.loc[(df1['Retail_Price'] > Lx)
                        & (df1['Retail_Price'] < Ux)]
Count_Filtered_Data = len(Filtered_Data)
print(f"Total no of data points in {list_1[3]} column after Outlier Detection : {Count_Filtered_Data}")

# Points detected as an Outlier :
Data_With_Outlier = Actual_Data - Count_Filtered_Data
print(f"Points detected with Outliers : {Data_With_Outlier}")

# Get the points which non-outliers -
Filtered_Data = Filtered_Data.reset_index(drop=True)
print(f"Data Points with non outlier :\n {Filtered_Data}")
list_1 = list(df1.columns)
print(f"New set of headers : {list_1}")
Filtered_Data = Filtered_Data.drop(columns=['Average_Deviation', 'Percentage_Deviation'])
print(Filtered_Data)

# Re-Validation of Retail Price column after Outlier Detection :
# Plot a histogram to check the data distribution -
plt.figure(figsize=(20,5))
plt.hist(Filtered_Data['Retail_Price'], color='red',
         label='Range v/s Frequency')
plt.xlabel('Price_Range')
plt.ylabel('Frequency')
plt.title('Price_Range v/s Frequency')
plt.grid()
plt.legend()
plt.show()

# Re-checking of the variability between Data Points and Mean :
# Measure of Center :
print(f"Overall mean of the {list_1[3]} column : {Filtered_Data.loc[:,'Retail_Price'].mean()}")
Filtered_Data = Filtered_Data.sort_values(by='Retail_Price', ascending=True)
print(f"Overall median of the {list_1[3]} column : {Filtered_Data.loc[:,'Retail_Price'].median()}")
# Measure of Spread :
# Standard deviation :
print(f"STD of the {list_1[3]} column : {round(Filtered_Data.loc[:,'Retail_Price'].std(), 2)}")

# Average deviation :
avg = Filtered_Data.loc[:,'Retail_Price'].mean()
for i in range(0, len(Filtered_Data.loc[:,'Retail_Price'])):
    Filtered_Data.loc[i, 'Average_Deviation'] =  round(abs(Filtered_Data.loc[i ,'Retail_Price'] - avg), 2)
print(Filtered_Data[['Retail_Price', 'Average_Deviation']].head(20))

# Percentage deviation :
for i in range(0, len(Filtered_Data.loc[:,'Retail_Price'])):
    Filtered_Data.loc[i, 'Percentage_Deviation'] = round((Filtered_Data.loc[i, 'Average_Deviation']/avg) * 100, 2)
print(Filtered_Data[['Retail_Price', 'Average_Deviation', 'Percentage_Deviation']].head(20))

# Overall Percentage deviation :
overall_percentage_deviation = round(Filtered_Data['Percentage_Deviation'].sum()/len(Filtered_Data), 2)
print(f"Overall Percentage deviation in {list_1[3]} column : {round(overall_percentage_deviation, 2)}")
"""
After correlating both the graphs we can see that now some of the data points are in the mid 
means the overall percentage deviation is less as compared to previous because 1341 data points 
has been removed as the part of Outliers but we got to know one more thing -

1. Even after the Outlier Detection done we have filtered approx 20% of the data points and it 
results to approx 4% of the reduction in the overall percentage deviation which is still not 
quite good so this states that there are most of the data points which lies outside the 25 - 75 % 
range but falls under Lx to 25% and Ux to 75% which are not termed as an Outlier.

2. If scenario - 1 kind of case occurs then we need to check with the client if we can remove 
some of the more bad samples to make data points looks more symmetric.
"""

# Exporting the data to a new file :
Filtered_Data = Filtered_Data.drop(columns=['Average_Deviation', 'Percentage_Deviation'])
Filtered_Data.to_csv('Sales_BY_Months.csv', index=False)

""" Importing the Consistent Data """
ndf = pd.read_csv('Sales_BY_Months.csv')
list_1 = list(ndf.columns)
print(ndf['Date_Time'].head())

""" Perform Data Cleansing in Date_Time column """
# Check the datatype in the Date_Time column -
print(ndf['Date_Time'].dtypes)

# Check for the no of missing values in the given column - Date_Time
Missing_values_DT = ndf['Date_Time'].isnull().sum()
print(f"Missing values in column {list_1[4]} : {Missing_values_DT}")

print(ndf.dtypes)

# Check for the no of missing values in rest of the categorical columns - Product, Purchase Address
list_2 = list_1[1:len(list_1):4]
for k in list_2:
    print(f"Missing values in column {k} : {ndf[k].isnull().sum()}")

"""
In my dataset I am seeing no missing values in the categorical data 
"""

# Missing values in Continuous columns -
list_3 = []
list_3.extend([list_1[0], list_1[2], list_1[3]])
print(f"New list : {list_3}")

for i in list_3:
    print(f"Missing values in column {i} : {ndf[i].isnull().sum()}")

"""
There is no missing values in continuous columns as well.
"""

""" Data Validation on Purchase Address column """
print(ndf['Purchase Address'].head())
S1 = ndf['Purchase Address'].str.split(',')
print(S1.head())
for i in range(0, len(S1)):
    ndf.loc[i, 'Street_Lane'] = S1.loc[i][0]
print(ndf['Street_Lane'].head())
S2 = ndf['Street_Lane'].str.split(' ', n=1)
print(S2.head())
for i in range(0, len(S2)):
    ndf.loc[i, 'Street_No'] = S2[i][0]
print(ndf[['Purchase Address','Street_Lane','Street_No']].head())

# Extract the City out of Purchase Address column :
for i in range(0, len(S1)):
    ndf.loc[i, 'City_Name'] = S1[i][1]
print(ndf[['Purchase Address', 'City_Name']].head())

# Extract the country and pin code out of Purchase Address column :
S2 = ndf['Purchase Address'].str.split(',')
print(S2.head())
for j in range(0, len(S2)):
    ndf.loc[j, 'Country_Pin_Code'] = S2[j][2]
print(ndf['Country_Pin_Code'].head())
S3 = ndf['Country_Pin_Code'].str.replace(' ', '', n = 1).str.rsplit(' ', n = 1)
print(S3.head())
for j in range(0, len(S3)):
    ndf.loc[j, 'CountryCode'] = S3[j][0]
    ndf.loc[j, 'Pincode'] = S3[j][1]
print(ndf['Pincode'].head())
ndf['Pincode'] = ndf['Pincode'].str.replace(' ', '')
print(ndf[['CountryCode', 'Pincode']].head())

# Get the total no of columns(headers) :
list_2 = list(ndf.columns)
print(f"No of headers present in dataset after doing data validation on purchase address column : \n {list_2}")
print(len(list_2))

# Get the top five rows :
print(ndf.head())

# Data Validation on Product column:
print(ndf['Product'].head())
S1 = ndf['Product'].str.split(' ', n = 1)
print(S1.head())
for i in range(0, len(S1)):
    ndf.loc[i, 'Product_Names'] = S1[i][1]
print(ndf[['Product', 'Product_Names']].head(20))

# Read the top five values from the dataset :
list_1 = list(ndf.columns)
print(f"Total no of columns : {list_1}")

def ischange(value):
    if value == 'Batteries (4-pack)':
        return '(4-pack) Batteries'
    return value
ndf['Product_Names'] = ndf['Product_Names'].apply(ischange)
print(f"Unique values in column {list_1[12]} : {ndf['Product_Names'].unique()}" + '\n' +
      f" DataType of given column : {type(ndf['Product_Names'].unique())}")

# Perform Data Mining more in the Product Names and create another column :

def checkinputs(value):
    my_list = ['Headphones', 'Batteries', 'Cable', 'Monitor', 'TV']
    if value not in my_list:
        return value.split(' ')[1]
    return value
ndf['Product_Names'] = ndf['Product_Names'].apply(checkinputs)
print(ndf['Product_Names'].tail())
ndf = ndf.drop(columns='Country_Pin_Code')
ndf.to_csv('Sales_BY_Months.csv', index = False)

""" Data Analysis based on question derivation """
# Import the pre-processed dataset :
ndf1 = pd.read_csv('Sales_BY_Months.csv')
print(ndf1.head())

# Get the total no of columns out -
list_1 = list(ndf1.columns)
print(f"Total no of columns : \n {list_1}")

""" Show the discrepancy between the total Sales of different products - """
ndf1['Total_Price_Per_Quantity'] = ndf1['Quantity Ordered'] * ndf1['Retail_Price']
print(ndf1['Total_Price_Per_Quantity'][50:81])

# Price in Indian Rupees -
ndf1['Price_In_Indian_Rupees'] = round(ndf1['Total_Price_Per_Quantity'] * 85.83, 2)
print(ndf1['Price_In_Indian_Rupees'][50:81])

df = ndf1.groupby('Product_Names').agg(
    TotalPriceInIndianRupees=('Price_In_Indian_Rupees', 'sum')
).reset_index().sort_values(by='TotalPriceInIndianRupees', ascending = False).reset_index(drop=True)
print(df)

df['TotalPriceInUSDollars'] = round(df['TotalPriceInIndianRupees'] / 85.83, 2)
print(df)

""" From the above analysis we got to know that Headphones are the highest selling product with 
a wiping amount of 1,44,099.69 USD where as Batteries are the lowest selling product with 7,344.25 USD
"""

# Identify the costlier product among the given set of products :
print(list_1)
df1 = ndf1.groupby('Product_Names').agg(
    TotalQuantityPurchased=('Quantity Ordered', 'sum')
).reset_index().sort_values(by='TotalQuantityPurchased', ascending=False).reset_index(drop=True)
print(df1)
""" Perform Merging based on dataframes DF and DF1 """
df2 = df.merge(df1, on='Product_Names', how='inner')
print(df2)
print(list(df2.columns))
df2['Retail_Price_Per_Quantity'] = df2['TotalPriceInUSDollars']/df2['TotalQuantityPurchased']
print(df2[['Product_Names','Retail_Price_Per_Quantity']])

"""
From the above analysis we came to know that TV is the costlier product with 300 USD purchase 
for a single quantity ordered.
"""

""" Date Time Analytics """
# Figure out the date on which the maximum sales happened with the highest selling product :
print(list(ndf1.columns))
df2 = ndf1.groupby(['Date', 'Product_Names']).agg(
    TotalRetailSales=('Total_Price_Per_Quantity', 'sum')
).reset_index().sort_values(by='TotalRetailSales', ascending=False).reset_index(drop=True)
# print(df2)
df2 = df2.rename(columns={'Date': 'DATE', 'Product_Names': 'PRODUCT_NAMES', 'TotalRetailSales': 'OVERALLSALES'})
print(df2)
df2.to_csv('SalesByDate.csv', index=False)
""" 
From the above analysis we got to know that 18-02-2019 is the date on which the maximum sales i.e. 11,591.26 INR
happened through Headphones. 
"""

# Identify the most selling product on Monday -
print(list(ndf1.columns))
print(ndf1[['Date_Time','Date']].dtypes)
ndf1['Date'] = pd.to_datetime(ndf1['Date'], format = '%Y-%m-%d')
print(ndf1['Date'].dtypes)
ndf1['DayName'] = ndf1['Date'].dt.day_name()
print(ndf1[['Date', 'DayName']].head(50))
df1 = ndf1.set_index('DayName')
df1 = df1.loc['Monday']
print(df1.tail())
df1 = df1.reset_index()
print(list(df1.columns))
print(df1.head())
df1 = df1.groupby(['DayName', 'Product_Names']).agg(
    TotalSalesOnMonday=('Price_In_Indian_Rupees', 'sum')
).reset_index().sort_values(by='TotalSalesOnMonday', ascending=False).reset_index(drop=True)
print(df1[['DayName', 'Product_Names', 'TotalSalesOnMonday']])
df1['SalesOnMonday(Dollars)'] = round(df1['TotalSalesOnMonday']/85.83, 2)
print(df1[['DayName', 'Product_Names', 'SalesOnMonday(Dollars)']].head())

"""
From the above analysis, we got to know that Headphones are the most selling product with overall sales
as 20,044.57 USD on Monday(First Opening Day).
"""

# Create a given column as DayName in the existing dataset :
print(ndf1[['Date', 'DayName']].head())
ndf1.to_csv('Sales_BY_Months.csv', index=False)

# Extract the highest selling products based on Weekends - Sat/Sun :
df2 = pd.read_csv('Sales_BY_Months.csv')
df2 = df2.rename(columns={'DayName': 'DAY_NAME', 'Product_Names': 'PRODUCT_NAME'})
list_1 = ['Saturday', 'Sunday']
df2 = df2.loc[df2['DAY_NAME'].isin(list_1)]
df2 = df2.groupby(['PRODUCT_NAME', 'DAY_NAME']).agg(
    TotalSalesWeekend=('Price_In_Indian_Rupees', 'sum')
).reset_index().sort_values(by='TotalSalesWeekend', ascending=False).reset_index(drop=True)
# print(df2)
df2['Price_In_USD'] = round(df2['TotalSalesWeekend']/85.83, 2)
print(df2)

"""
From the above analysis we got to know that Headphones are the one which is 
the highest selling product with 16598.51 USD for Saturday and 17920.40 USD for Sunday.
"""

# Extract those Street Lane along with the city names where the highest amount of quantity ordered -
print(list(df2.columns))
print(list(ndf1.columns))
ndf1['Price_In_USD'] = round(ndf1['Price_In_Indian_Rupees']/87.13, 2)
print(ndf1[['Price_In_Indian_Rupees', 'Price_In_USD']])
df2 = ndf1.groupby(['City_Name', 'Street_Lane']).agg(
    OverallQuantityPurchased=('Quantity Ordered', 'sum'),
    OverallPriceInUSD=('Price_In_USD', 'sum')
).reset_index().sort_values(by='OverallPriceInUSD', ascending=False).\
    reset_index(drop=True)
print(df2)
df2.to_csv('SalesByCityLane.csv', index=False)

"""
From the above analysis, we got to know that if customer is purchasing more from that specific street lane 
for any of city it does not mean company is having the highest purchase rate for that specific street lane
and city.
Below are two findings :
-  Los Angeles	    168 14thSt	6	314.43	27396.29
-  New York City	320 LakeSt	2	591.05	51498.19
Here for Los Angeles for 168 14th St we have total 6 quantity purchased but overall sales is 314.43 USD
where as for New York City for 320 Lake St we have only 2 quantity purchased but overall sales is 591.USD
"""

# Dip in the Weekly Sales for each City :
print(ndf1['Date'].dtypes)
ndf1['DayName'] = ndf1['Date'].dt.day_name()
print(ndf1[['Date', 'DayName']].head())
arr_1 = ndf1['DayName'].unique()
list_2 = list(arr_1)
df2 = ndf1.loc[ndf1['DayName'].isin(list_2)]
print(df2[['City_Name', 'Date', 'DayName']].head())
df2 = ndf1.groupby(['City_Name', 'DayName']).agg(
    OverallWeeklySales=('Price_In_USD', 'sum')
).reset_index().sort_values(by=['City_Name', 'DayName'], ascending=[True, True]).reset_index(drop=True)
print(df2)
# list_1, df3 = ['New York', 'San Franscisco'], pd.DataFrame()
# for i in range(0, len(list_1)):
#     df3.loc[i, 'City_Name'] = list_1[i]
#     df3.loc[i, 'Difference_In_Weekly_Sales'] = df1.loc[i, '']
ndf = df2.loc[df2['DayName'] == 'Monday'].reset_index(drop=True)
print(ndf)
ndf2 = df2.loc[df2['DayName'] == 'Sunday'].reset_index(drop=True)
print(ndf2)
# arr_1 = df2['City_Name'].unique()
# list_1, list_2 = list(arr_1), []
# for i in list_1:
#     list_2.append(i.replace(' ', ''))
# print(list_2)
# list_1 = []
# for i in range(0, len(list_2)):
#     list_3 = []
#     for j in range(1):
#         list_3.append(list_2[i])
#         list_3.append(ndf.loc[i, 'OverallWeeklySales'] - ndf2.loc[i, 'OverallWeeklySales'])
#     list_1.append(list_3)
# print(f"Appended List : \n {list_1}")
# list_3, list_4 = [], []
# S1, S2 = ndf['OverallWeeklySales'], ndf2['OverallWeeklySales']
# for i in S1:
#     list_3.append(i)
# for j in S2:
#     list_4.append(j)
# list_1 = []
# for i, j in zip(list_3, list_4):
#     list_1.append(round(i-j, 2))
# print(list_1)
# list_5 = []
# for i in zip(list_2, list_1):
#     list_5.append(i)
# print(f"Final List : {list_5}")
# ndf4 = pd.DataFrame(list_5, columns=['City_Name', 'Dip_In_WeeklySales'])
# print(f"Dip in Weekly Sales : \n {ndf4}")

"""
From the above conclusion we can see that for cities like Atlanta, Boston, Dallas, NewYorkCity,
Portland, Seattle the overall weekly sales have an increase from Monday to Sunday where as 
cities like Austin, LosAngeles, SanFrancisco are having dip in weekly sales from Monday to Sunday.
"""

# Get that specific city out which is having the highest increase in the weekly sales from Monday to Sunday.
# list_1 = ['Atlanta', 'Boston', 'Dallas', 'NewYorkCity', 'Portland', 'Seattle']
# ndf4 = ndf2.loc[ndf2['City_Name'].isin(list_1)]
print(f"No of columns : \n {list(ndf.columns)}")
print(ndf)
list_1, S1 = list(), ndf['OverallWeeklySales']
for i in S1:
    list_1.append(round(i, 2))
list_2, S2 = list(), ndf2['OverallWeeklySales']
for j in S2:
    list_2.append(round(j, 2))
list_3, list_4, list_5 = [], [], []
for i, j in zip(list_2, list_1):
    list_3.append(round(i-j, 2))
print(list_1, list_2)
S3 = ndf['City_Name']
for k in S3:
    list_4.append(k.replace(' ', ''))
for l in zip(list_4, list_3):
    list_5.append(l)
print(list_5)
df3 = pd.DataFrame(list_5, columns=['City_Name', 'Increase_In_Weekly_Sales'])
df3 = df3.sort_values(by='Increase_In_Weekly_Sales', ascending = False).reset_index(drop=True)
print(f"DataFrame with Increase_In_Weekly_Sales : \n {df3.head(1)}")

"""
Dallas is the city which is having the highest increase in weekly sales from Monday to Sunday 
with a total of 1686.68 USD.
"""

# Get the top five rows out :
print(ndf1.head())
# Get all the columns:
print(f"Total headers in the given dataset : {ndf1.columns}")
# Create specific month column out using date column :
ndf1['Specific_Month'] = ndf1['Date'].dt.month_name()
print(ndf1[['Date', 'Specific_Month']].head())

# Highest Earning Product for each city for a specific month February :
arr_1 = ndf1['City_Name'].unique()
list_1, list_2 = list(arr_1), []
for i in list_1:
    list_2.append(i.replace(' ', ''))
print(f"Total Unique values in City column : {list_2}")
ndf1['City_Name'] = ndf1['City_Name'].str.replace(' ', '')
# print(ndf1['City_Name'].head())
# print(list(ndf1['City_Name'].unique()))
list_5 = []
for i in list_2:
    ndf2 = ndf1.loc[(ndf1['City_Name'] == i) & (ndf1['Specific_Month'] == 'February')]
    # print(ndf2)
    ndf3 = ndf2.groupby(['City_Name', 'Product_Names']).agg(
        HighestEarningProduct=('Price_In_USD', 'sum')
    ).reset_index().sort_values(by='HighestEarningProduct', ascending=False).reset_index(drop=True).head(1)
    print(f"Highest Earning Product for {i} City : \n {ndf3}"+'\n'+
          "..........................................................")
    ndf3 = ndf3.rename(columns={'HighestEarningProduct': 'Highest_Earning_Product'})
    ndf3['Highest_Earning_Product'] = round(ndf3['Highest_Earning_Product'], 2)
    print(ndf3['Highest_Earning_Product'])
    list_1, list_3 = list(ndf3.columns), []
    for j in range(0, len(list_1)):
        S1 = ndf3.loc[0, list_1[j]]
        list_3.append(S1)
    list_5.append(list_3)
print(f"List with the highest earning products : {list_5[0:3]}")
df8 = pd.DataFrame(list_5, columns = ['City_Name', 'Highest_Earning_Product_Name', 'Total_Earning'])
df8 = df8.sort_values(by='Total_Earning', ascending = False).reset_index(drop=True)
print(f"DataFrame which shows total earning for each product and city : \n {df8}")
df8.to_csv('HighestEarningProductByCity.csv', index = False)

"""
From the above analysis, we can conclude that for each city "Headphones" are the highest selling product 
where San Francisco is the city with top earning as 34886.37 USD and Austin with least earning as 7753.95 USD
for month of february.
"""

# SanFrancisco   Headphones      34886.37
# Austin         Headphones      7753.95

"""
Get those products out for each city which shows a dip in overall sales from starting to ending of the month.
"""
# Create a DataFrame with City_Name, Product_Name, OverallSales for 13th date(starting of the month) :
ndf1['Specific_DATE'] = ndf1['Date'].dt.day
print(ndf1[['Date', 'Specific_DATE']].head(20))
ndf1 = ndf1.sort_values(by='Specific_DATE', ascending = True).reset_index(drop=True)
ndf1.to_csv('DatabyDate.csv', index = False)
list_3, arr_1, list_2 = list(ndf1.columns), ndf1['Specific_DATE'].unique(), []
print(list_3)
for i in arr_1:
    list_2.append(i)
print(f"Total Unique Elements in Specific Date column : {list_2[0:]}")
arr_2 = ndf1['City_Name'].unique()
list_3, list_5 = list(arr_2), []
# print(list_3)
for i in list_3:
    ndf9 = ndf1.loc[(ndf1['City_Name'] == i) & (ndf1['Specific_DATE'] == 13)]
    ndf10 = ndf9.groupby(['City_Name', 'Product_Names']).agg(
        OverallSales=('Price_In_USD', 'sum')
    ).reset_index()
    # print(ndf10)
    list_4 = list(ndf10.columns)
    # print(list_4)
    for i in range(0, len(ndf10)):
        list_6 = []
        for j in range(0, len(list_4)):
            S1 = ndf10.loc[i, list_4[j]]
            list_6.append(S1)
        list_5.append(list_6)
# print(list_5)
ndf10 = pd.DataFrame(list_5, columns = ['City_Name', 'Product_Name', 'TotalOverallSales'])
print(f"DataFrame with overall sales for the starting of the month : \n {ndf10}"+'\n'+
      "................................................................."+'\n'+
      ".................................................................")

# Create a DataFrame with City_Name, Product_Name, OverallSales for 28th date(ending of the month) :
list_5 = []
for i in list_3:
    ndf8 = ndf1.loc[(ndf1['City_Name'] == i) & (ndf1['Specific_DATE'] == 28)]
    ndf11 = ndf8.groupby(['City_Name', 'Product_Names']).agg(
        OverallSales=('Price_In_USD', 'sum')
    ).reset_index()
    # print(ndf10)
    list_4 = list(ndf11.columns)
    # print(list_4)
    for i in range(0, len(ndf11)):
        list_6 = []
        for j in range(0, len(list_4)):
            S1 = ndf11.loc[i, list_4[j]]
            list_6.append(S1)
        list_5.append(list_6)
# print(list_5)
ndf11 = pd.DataFrame(list_5, columns = ['City_Name', 'Product_Name', 'TotalOverallSales'])
print(f"DataFrame with overall sales for the ending of the month : \n {ndf11}")

# Merge both the dataframes :
df12 = ndf10.merge(ndf11, on=['City_Name', 'Product_Name'], how='inner')
df12 = df12.rename(columns={'TotalOverallSales_x': 'TotalSalesByStartDate', 'TotalOverallSales_y': 'TotalSalesByEndDate'})
# print(f"Merged DataFrame : \n {df12}")
df12['Dip_In_Overall_Sales'] = df12['TotalSalesByEndDate'] - df12['TotalSalesByStartDate']
print(df12)
list_5, list_3 = [], list(df12['City_Name'].unique())
for i in list_3:
    df13 = df12.loc[df12['City_Name'] == i].sort_values(by='Dip_In_Overall_Sales', ascending = True)\
        .reset_index(drop=True).head(1)
    list_6, list_7 = [], list(df13.columns)
    for j in range(0, len(list_7)):
        S1 = df13.loc[0, list_7[j]]
        list_6.append(S1)
    list_5.append(list_6)
# print(list_5)
df13 = pd.DataFrame(list_5, columns=['City_Name', 'Product_Name', 'TotalSalesByStartDate', 'TotalSalesByEndDate', 'Dip_In_Overall_Sales'])
df13 = df13.drop(columns=['TotalSalesByStartDate', 'TotalSalesByEndDate'])
df13['Dip_In_Overall_Sales'] = abs(df13['Dip_In_Overall_Sales'])
df13 = df13.sort_values(by='Product_Name', ascending = True).reset_index(drop=True)
print(f"DataFrame with Dip In Overall Sales for each city with product name : \n {df13}")

# Extract the specific date on which the maximum and minimum sales has been done for each city along with their product name -
list_1 = list(ndf1.columns)
print(list_1)
ndf12 = ndf1.groupby(['City_Name', 'Product_Names', 'Date']).agg(
    TotalOverallSales=('Price_In_USD', 'sum')
).reset_index()
print(f"DataFrame after calculating total overall sales : \n {ndf12}")
ndf12.to_csv('OverallSalesByCityProduct.csv', index = False)
list_5, list_7, list_2 = list(), list(), list(ndf12['City_Name'].unique())
for i in list_2:
    ndf13 = ndf12.loc[ndf12['City_Name'] == i].sort_values(by='TotalOverallSales', ascending = False).reset_index(drop=True).head(1)
    ndf14 = ndf12.loc[ndf12['City_Name'] == i].sort_values(by='TotalOverallSales', ascending = True).reset_index(drop=True).head(1)
    list_3, list_6, list_4 = [],[], list(ndf13.columns)
    for j in range(0, len(list_4)):
        S1, S2 = ndf13.loc[0, list_4[j]], ndf14.loc[0, list_4[j]]
        list_3.append(S1), list_6.append(S2)
    list_5.append(list_3), list_7.append(list_6)
# print(list_5[0:3])
ndf13 = pd.DataFrame(list_5, columns = ['City', 'Product', 'Date_Max_Sales', 'MaximumOverallSales'])
ndf14 = pd.DataFrame(list_7, columns = ['City', 'Product', 'Date_Min_Sales', 'MinimumOverallSales'])
# print(ndf13)
# print(ndf14)

# Merge the two dataframes (ndf13, ndf14) :
df15 = ndf13.merge(ndf14, on = ['City'], how = 'inner')
df15 = df15.rename(columns={'Product_x': 'Product_Name_Max_Sales', 'Product_y': 'Product_Name_Min_Sales'})
print(f"DataFrame with maximum overall sales for each city with a specific product : \n {df15}")
df15.to_csv('Max_Min_OverallSalesByCityByProduct.csv', index = False)

# Extract the specific day and the product name for each city when they have the maximum sales.
print(list(ndf1.columns))
my_list, list_5 = [], list(ndf1['City_Name'].unique())
print(f"No of unique values in the city name column : \n {list_5}")
for i in list_5:
    ndf2 = ndf1.loc[ndf1['City_Name'] == i]
    ndf2 = ndf2.groupby(['City_Name', 'Product_Names', 'DayName']).agg(
        TotalOverallSales=('Price_In_USD', 'sum')
    ).reset_index().sort_values(by='TotalOverallSales', ascending = False).reset_index(drop=True).head(1)
    list_3, list_2 = [], list(ndf2.columns)
    for j in range(0, len(list_2)):
        S1 = ndf2.loc[0, list_2[j]]
        list_3.append(S1)
    my_list.append(list_3)
print(f"Nested List with important columns : \n {my_list}")
headers = ['City', 'Product', 'DayName', 'MaximumOverallSales']
df17 = pd.DataFrame(my_list, columns = headers)
print(f"DataFrame with maximum overall sales on a specific day for each city by product : \n {df17}")
df17.to_excel('MaximumSalesByDayName.xlsx', index = False)

