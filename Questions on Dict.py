"""
Create a dict name Fruit dict and display it...
"""
Fruit_dict={'apple':1,
            'mango':2,
            'banana':3,
            'pineapple':4}
for i in Fruit_dict:
    print(f"Fruit_Name :{i}"+'|'+f"Total_Purchase :{Fruit_dict[i]}")

"""
Create a dictionary and use dict.items() to display key-value pair separately...
"""
dict_1={'name':'Vidit',
        'age':26,
        'city':"Ranchi"}
print(".................")
for item_value in dict_1.items():
    #print(f"Key_Value :{item_value}")
    list_2=list()
    list_2=list_2+list(item_value)
    for key in range(0,len(list_2),2):
        print(f"Key :{list_2[key]}")
    for value in range(len(list_2)-1,len(list_2)):
        print(f"Value :{list_2[value]}"+'\n'+".................")
""" Another Method """
for key,value in dict_1.items():
    print(f"Key :{key}"+'|'+f"Value :{value}")

"""
Display the three countries with maximum no of covid cases...
"""
cases_dict={"USA":6500000,
            "India":8300000,"Brazil":1800000,"Russia":7600000,
            "France":4800000,"UK":7000000,"Italy":910000,"Spain":550000,
            "Germany":8400000}
list_values=list(cases_dict.values())
#print(list_values)
for i in range(0,len(list_values)-1):
    for j in range(i+1,len(list_values)):
        if list_values[i]<list_values[j]:
            temp=list_values[i]
            list_values[i]=list_values[j]
            list_values[j]=temp
#print(f"Sorted List :{list_values}") #Debugging Point
print("Countries with maximum no of covid cases....")
for keys in cases_dict:
    if (cases_dict[keys]==list_values[0]) or (cases_dict[keys]==list_values[1]) or \
        (cases_dict[keys]==list_values[2]):
        print(f"Country_Name :{keys}"+'|'+f"No_of_covid_cases :{cases_dict[keys]}")

"""
Create a dictionary called Fruit Dict
"""
Fruit_Dict={"apple":1,"banana":2,"orange":3}
print(f"Fruit Dictionary :{Fruit_Dict}")
"""Add one key-value pair in the existing Fruit Dict"""
Fruit_Dict["mango"]=4
for fruits in Fruit_Dict:
    print(f"Name of Fruits are :{fruits}")
"""Print the Fruit Dict in an Ordered Way"""
for fruits in Fruit_Dict:
    print(f"{fruits}:{Fruit_Dict[fruits]}")
"""Create a Dictionary where key-value pair should be taken from user as an input"""
fruit_dict,Len={},int(input("Total Length :"))
for i in range(0,Len):
    fruit_name,fruit_price=input("Fruit Name :"),float(input("Fruit Price :"))
    fruit_dict[fruit_name]=fruit_price
print(f"Fruit_Dict :{fruit_dict}")
"""Count the frequency of each word in a given sentence"""
#First Method
st_1="the quick brown fox jumps over the lazy dog"
list_1=st_1.split(' ')
for i in list_1[0:len(list_1)]:
    count=0
    for j in list_1[::]:
        if i==j:
            count+=1
    print(f"Given Word :{i} and Total Count :{count}")
#Another Method
st_1="the quick brown fox jumps over the lazy dog"
list_1=st_1.split(' ')
tuple_1=tuple(list_1)
for i in tuple_1:
    print(f"Given Word :{i} and Count :{tuple_1.count(i)}")

"""
Create a dict called my_dict and perform certain operations
"""
my_dict={"name":"John","age":30,"city":"New York"}
# Search whether key : name exist in my_dict
keys=list(my_dict.keys())
search_key=input("Key to be search in my_dict :")
if search_key in keys:
    print(f"Search Key Found :{search_key}")
else:
    print("Search Key Not Found")
# Search whether value : chicago exist in my_dict
values=list(my_dict.values())
search_value=input("Value to be search in my_dict :")
if search_value in values:
    print(f"Given Value Found :{search_value}")
else:
    print("Given Value Not Found")
# Length of my_dict
print(len(my_dict))
#Clear all the elements in my_dict
my_dict.clear()
print(my_dict)

"""
Create a new dict by intersection(common key-value pairs) of two dict....
"""
dict_1,dict_2={"a":1,"b":2,"c":3},{"c":4,"d":5,"e":6}
list_1,list_2=list(dict_1.keys()),list(dict_2.keys())
dict_3=dict()
for i in range(0,len(list_1)):
    count=0
    for j in range(0,len(list_2)):
        if list_1[i]==list_2[j]:
            count+=1
            break
    if count==1:
        dict_3[list_1[i]]=[dict_1[list_1[i]],dict_2[list_2[j]]]
print(f"New Dict :{dict_3}")
"""Merge two dictionaries dict_1 and dict_2"""
for i in dict_2:
    dict_1[i]=dict_2[i]
print(f"Merging dict_2 into dict_1 :{dict_1}")
"""Remove a key-value pair from dict_1"""
key_1=input("Key-Value Pair to be Removed :")
dict_1.pop(key_1)
print(f"After removal of particular key-value pair :{dict_1}")
"""Sort the given dictionary in ascending order..."""
d={"oil":230,"clip":150,"stud":175,"nut":35}
list_1=list(d.values())
for i in range(0,len(list_1)-1):
    for j in range(i+1,len(list_1)):
        if list_1[i]>list_1[j]:
            temp=list_1[i]
            list_1[i]=list_1[j]
            list_1[j]=temp
d_1=dict()
for k in list_1:
    for l in d:
        if d[l]==k:
            d_1[l]=k
d=d_1
print(f"Sorted the dictionary in ascending order :{d}")
"""Dict inside Dict Concept..."""
dict_1={"John":{"salary":5000,"department":"Sales"},
        "Mike":{"salary":6000,"department":"Marketing"},
        "Sara":{"salary":7000,"department":"Operations"}}
list_1=list()
for i in dict_1:
    for j in dict_1[i]:
        list_1=list_1+[dict_1[i][j]]
print(list_1)
for i in dict_1:
    list_1=list_1+[dict_1[i]["salary"]]
print(list_1)

"""
Create a dictionary employee_dict and find the employee getting highest salary...
"""
emp_dict={"John":{"salary":5000,"department":"Sales"},
          "Mike":{"salary":6000,"department":"Marketing"},
          "Sara":{"salary":7000,"department":"Operations"}}
list_1=list()
for values in emp_dict:
    list_1=list_1+[emp_dict[values]["salary"]]
max=list_1[0]
for i in list_1[1:len(list_1)]:
    if max<i:
        max=i
for emp_name in emp_dict:
    if emp_dict[emp_name]["salary"]==max:
        print(f"Employee with highest Salary :{emp_name}")
        break
"""Python Program to get the Average Salary in dict called emp_dict..."""
sum=0
for values in list_1[::]:
    sum=sum+values
print(f"Average Salary :{sum/len(list_1)}")
"""Python Program to add a new employee in emp_dict..."""
emp_dict["Simran"]={"salary":8000,"department":"Finance"}
print(f"After adding new emp in emp_dict :{emp_dict}")
"""Python Program to remove an employee from emp_dict..."""
emp_name=input("Employee to be Removed :")
emp_dict.pop(emp_name)
print(f"After removing particular employee from emp_dict :{emp_dict}")

"""
Create a dictionary called sales_dict and perform the following operations...
"""
Len,sales_dict=int(input("Total Length :")),dict()
for i in range(0,Len):
    month=input("Month to be entered :")
    sales=int(input("Total sales per month to be entered :"))
    sales_dict[month]=sales
print(f"Sales Dictionary :{sales_dict}")
# Print the sales in Jan
print(f"Sales in January :{sales_dict['Jan']}")
# Total Sales of First Quarter (Jan to Mar)
values=list(sales_dict.values())
sum=0
for sales in values[:len(values)-2]:
    sum=sum+sales
print(f"Total Sales of First Quarter :{sum}")
# Print the months in which sales where greater than 6000.
month_list=list()
for month in sales_dict:
    if sales_dict[month]>6000:
        month_list=month_list+[month]
print(f"Months with sales greater than 6k :{month_list}")
# Add the sales data for June as 8k in sales_dict
month=input("Month to be entered :")
sales=int(input("Total sales per month to be entered :"))
sales_dict[month]=sales
for month in sales_dict:
    print(f"Month :{month}"+"|"+
          f"Sales :{sales_dict[month]}")
# Remove the sales data for Apr from sales_dict
print("...........................")
sales_dict.pop("Apr")
print(f"Sales Dict after removal of Apr Month Sales..."+'\n'+
      "...........................")
for month in sales_dict:
    print(f"Month :{month}"+"|"+
          f"Sales :{sales_dict[month]}")

"""
Create a dictionary called covid_cases and get the top three countries
with highest no of covid cases...
"""
covid_cases={"Russia":1200000,"Italy":600000,"Spain":550000,
             "France":800000,"UK":700000,"Germany":500000,
             "USA":3500000,"India":2300000,"Turkey":650000,
             "Brazil":1800000}
covid_counts=list(covid_cases.values())
for i in range(0,len(covid_counts)-1):
    for j in range(i+1,len(covid_counts)):
        if covid_counts[i]<covid_counts[j]:
            temp=covid_counts[i]
            covid_counts[i]=covid_counts[j]
            covid_counts[j]=temp
countries_list=list()
for values in covid_counts[::]:
    for keys in covid_cases:
        if covid_cases[keys]==values:
            countries_list=countries_list+[keys]
print(f"Top-3 countries with highest no of covid cases :{countries_list[0:3]}")

"""
Create a dictionary called sales_data which contains sales for the given 
product in the form key-value pair and perform the following operations...
"""
print("...................................Company Name :Nike")
Len,sales_data=int(input("Total Length :")),dict()
for i in range(0,Len):
    product_name=input("Product Name :")
    sales_per_product=int(input("Per Year Sales for the Given Product :"))
    sales_data[product_name]=sales_per_product
print("..........................")
for index in sales_data:
    print(f"{index}"+'-'+f"{sales_data[index]}")
# Total Sales for the company for year 2k23 after selling all these products...
print("..........................."+'\n'+
      "Total Sales for Year 2k23"+'\n'+"..........................")
sum,sales=0,list(sales_data.values())
for counts in sales[::]:
    sum=sum+counts
print(f"Sales :{sum}")
# Calculate Average Sales per product for year 2k23...
print("..........................."+'\n'+
      "Average Sales per product for Year 2k23"+'\n'+"...........................")
for keys in sales_data:
    avg=sales_data[keys]/12
    print(f"Product_Name :{keys}"+'|'+f"Average Sales :{round(avg,2)}")
# Find the best-selling product for year 2k23...
print("............................"+'\n'+
      "Best-Selling Product for Year 2k23"+'\n'+"..............................")
max=sales[0]
for value in sales[1:len(sales)]:
    if max<value:
        max=value
for key_index in sales_data:
    if sales_data[key_index]==max:
        print(f"Product_Name :{key_index}")
        break












