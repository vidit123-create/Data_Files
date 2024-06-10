"""
Inserting the elements in list using Function Concept...
"""
def create_list(list_1):
    Len=int(input("Total Length :"))
    for i in range(0,Len):
        list_1=list_1+[int(input("Enter any element :"))]
    return list_1
list_2=list_3=list()
for j in create_list(list_2):
    list_3=list_3+[j]
print(f"Output List :{list_3}")
"""
Use of Default Parameter and keyword argument...
"""
def create_list(list_1=list()):
    Len=int(input("Total Length :"))
    for i in range(0,Len):
        list_1=list_1+[int(input("Enter any element :"))]
    return list_1
#keyword Argument -
# list_2=list()
# for j in create_list(list_1=[]):
#     list_2=list_2+[j]
# print(f"Elements in the list :{list_2}")
#Default parameter -
list_2=list()
for j in create_list():
    list_2=list_2+[j]
print(f"Elements in the list :{list_2}")
"""
Concept of ASCII Code
"""
# chr() - It take ascii value of a particular character and return us the corresponding character...
num_1=98
print(chr(num_1))
# ord() - It take one particular character and return us the corresponding ascii value...
st_1='a'
print(ord(st_1))
# """
# Python Program to take a string as an input which contains both lower and upper case
# characters and return a list which contains only lower case chars but we should not use list()...
# NOTE : Use Function Concept
# """
while(True):
    def list_convert(st_1):
        list_1=list()
        for i in range(0,len(st_1)):
            if (st_1[i].isupper()==True) and (st_1[i].isalpha()==True):
                list_1=list_1+[chr(ord(st_1[i])+32)]
            else:
                list_1.append(st_1[i])
        return list_1
    st_2,list_2=input("Enter any String of Your Choice :"),list()
    if (st_2.isalpha()==True) and (st_2.isnumeric()!=True):
        for j in list_convert(st_2):
            list_2=list_2+[j]
        print(f"List with all lower chars :{list_2}")
    else:
        print("Wrong Input")
        break
""" Function Assignment """
"""
Create a Function which take your name and greet you.(Using Function)
"""
def add_name(st_1):
    return st_1
st_2=input("Person Name :")
print(f"My Name is {add_name(st_2)}")

"""
Take two values from user and print the sum.(Using Function)
"""
def add(x,y):
    sum=x+y
    return sum
a,b=int(input("First Number :")),int(input("Second Number :"))
print(f"Sum of two given values are :{add(a,b)}")

"""
Print the Multiplication table using function
"""
def mul_table(num_1):
    list_1,Len=list(),int(input("Total Length of Given Table :"))
    for i in range(1,Len):
        list_1=list_1+[num_1 * i]
    return list_1
num_2,list_2=int(input("Enter any number :")),list()
for j in mul_table(num_2):
    list_2=list_2+[j]
print(f"Multiplication Table of given number {num_2} :{list_2}")

"""
Calculate area of square using function
"""
def area_of_square(side):
    return side**2
num_1=int(input("Side of a Square :"))
print(f"Area of Square :{area_of_square(num_1)}")

"""
Calculate area of rectangle using function
"""
def area_of_rectangle(x,y):
    return x*y
a,b=int(input("Length of Rectangle :")),int(input("Breadth of Rectangle :"))
print(f"Area of Rectangle :{area_of_rectangle(x=a,y=b)}")

"""
Take three integers and print sum and product both using function
"""
def cal_sum_prod(x,y,z):
    add,mul=x+y+z, x*y*z
    return add, mul
a,b,c=int(input("First Number :")),int(input("Second Number :")),int(input("Third Number :"))
print(f"Addition and Multiplication of three numbers are :{cal_sum_prod(x=a,y=b,z=c)}")

"""
Check given number is odd or even using function.
"""
while(True):
    def even_odd_num(num_1):
        if int(num_1)%2==0:
            return "Even Number"
        else:
            return "Odd Number"
    num_2=input("Enter any number :")
    if num_2.isnumeric()==True:
        print(f"{int(num_2)} is an {even_odd_num(num_1=num_2)}")
    else:
        break
"""
Python Program to print sum of all even numbers between a given range using function...
"""
def sum_even(start,end):
    sum=0
    for value in range(start,end):
        if value%2==0:
            sum=sum+value
    return sum
first,last=int(input("Starting Range :")),int(input("Ending Range :"))
print(f"Sum of all even numbers :{sum_even(start=first,end=last)}")

st_1,st_2="Vidit-is-a-good-boy",str()
list_1=st_1.split('-')
for i in list_1[:len(list_1)-1]:
    st_2=st_2+i+'-'
st_2=st_2+list_1[len(list_1)-1]
print(f"Output String :{st_2}")

"""
Python Program to check whether a given sentence is a Pangram or not using function
"""
while(True):
    def ispangram(st_1):
        count=0
        for i in st_1[::]:
            if ((('a'<=i<='z') or ('A'<=i<='Z')) and i!=' '):
                count+=1
            else:
                pass
        if count>=26:
            return "Pangram"
        else:
            return "Not a Pangram"
    st_2=input("Given Sentence :")
    if st_2.replace(' ','').isalpha()==True:
        print(f"Given Sentence is {ispangram(st_1=st_2)}")
    else:
        break

"""
Python Program to Reverse a Given String...
"""
def reverse_string(st_1):
    return st_1[-1:-len(st_1)-1:-1]
st_2=input("Given String :")
print(f"Reverse of a String :{reverse_string(st_2)}")

"""
Python Program which takes '-' separated sequence as a value and convert
it into '-' separated sequence again but in a sorted format...
"""
while(True):
    def convert(st_1):
        list_1,st_3=st_1.split('-'),str()
        for i in range(0,len(list_1)-1):
            for j in range(i+1,len(list_1)):
                if list_1[i]>list_1[j]:
                    temp=list_1[i]
                    list_1[i]=list_1[j]
                    list_1[j]=temp
        for k in list_1[:len(list_1)-1]:
            st_3=st_3+k+'-'
        st_3=st_3+list_1[len(list_1)-1]
        return st_3
    st_2=input("Given Sentence :")
    if st_2.replace('-','').isalpha()==True:
        print(f" - Separated Sentence in sorted format :{convert(st_1=st_2)}")
    else:
        break

list_1,t_1=[],tuple()
for i in range(0,5):
    t_1=t_1+(int(input("Enter any number :")),)
list_1=list_1+[t_1]
print(f"Input List :{list_1}")

"""
Python Program to return a list containing the given form (x, x^2, x^3,.......)
in the form of a tuple using function within a range of (1,20) including them...
"""
while(True):
    def list_inside_tuple(num_1):
        list_1,t_1,Len=[],(),int(input("Total Length :"))
        for i in range(1,Len):
            t_1=t_1+(int(num_1)*i ,)
        list_1=list_1+[t_1]
        return list_1
    num_2=input("Enter any number :")
    if num_2.isnumeric()==True:
        print(f"Tuple Inside List :{list_inside_tuple(num_1=num_2)}")
    else:
        break

"""
Python Program to check whether a given sentence is palindrome or not.
"""
while(True):
    def ispalindrome(st_1):
        st_1=st_1.lower()
        if st_1==st_1[-1:-len(st_1)-1:-1]:
            return "Palindrome"
        else:
            return "Not a Palindrome"
    st_2=input("Given Sentence/Word :")
    if st_2.replace(' ','').isalpha()==True:
        print(f"Given sentence is a {ispalindrome(st_1=st_2.replace(' ',''))}")
    else:
        break

st_1="deed"
print(st_1[-1:-len(st_1)-1:-1])

"""
Python Program to create a function frequency() which will computes the frequency of words
present in the string passed to it and return the frequencies in a sorted order by words in
the given string.
"""
while(True):
    def frequency(st_1):
        list_1,list_2=st_1.split(' '),list()
        for i in list_1:
            count=0
            for j in i:
                count+=1
            list_2.append(count)
        #print(list_2) - Debugging Point
        for k in range(0,len(list_2)-1):
            for l in range(k+1,len(list_2)):
                if list_2[k]>list_2[l]:
                    temp=list_2[k]
                    list_2[k]=list_2[l]
                    list_2[l]=temp
        #print(list_2) - Debugging Point
        dict_1=dict()
        for m in list_2:
            for n in list_1:
                if len(n)==m:
                    dict_1[n]=m
        return dict_1
    st_2=input("Given String :")
    if st_2.replace(' ','').isalpha()==True:
        print(f"Given Words in Sorted format along with there frequency :{frequency(st_2)}")
    else:
        break

"""
Python Program to find the factorial of a number given through user input.
"""
while(True):
    def factorial(num_1):
        fact=1
        while(num_1>0):
            fact=fact*num_1
            num_1-=1
        return fact
    num_2=input("Given Number :")
    if num_2.isnumeric()==True:
        print(f"Factorial of Given Number {num_2} is:{factorial(num_1=int(num_2))}")
    else:
        break

"""
Python Program to accepts a string and calculate the no of alphabets and digits...
It should return these values as a dictionary using function.
"""
def count_alpha_digit(st_1):
    count_1=count_2=0
    dict_1=dict()
    for i in st_1:
        if ('a'<=i<='z' or 'A'<=i<='Z'):
            count_1+=1
        elif '0'<=i<='9':
            count_2+=1
        else:
            pass
    #print(count_1,count_2)
    for i in range(0,2):
        key=input("Key provided by user :")
        if key=="No_of_alphabets":
            dict_1[key]=count_1
        else:
            dict_1[key]=count_2
    return dict_1
st_2=input("Given String :")
print(f"Dictionary :{count_alpha_digit(st_2)}")

"""
Python Program to count the number of vowels in the given string...
"""
while(True):
    def isvowel(st_1):
        count=0
        for i in st_1:
            if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u') or (i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
               count+=1
        return count
    st_2=input("Given String :")
    if st_2.isalpha()==True:
        print(f"Total no of vowels in the given string :{isvowel(st_1=st_2)}")
    else:
        break

"""
Python Program to find the sum of digits of a given number...
"""
while(True):
    def isnumber(num_1):
        sum=0
        for i in num_1:
            sum=sum+int(i)
        return sum
    num_2=input("Any Number :")
    if num_2.isnumeric()==True:
        print(f"Sum of all digits in a given number :{isnumber(num_2)}")
    else:
        break

"""
Python Program to take multiple no of variable but arguments are not same as the no of
variables and calculate the sum of those numbers.
Constraint : All the arguments passed should be your numbers.
"""
while(True):
    def isarguments(a,b,c=12,d=16): # Default Parameter
        sum=int(a)+int(b)+c+d
        return sum
    x,y=input("First Number :"), input("Second Number :")
    if (x.isnumeric()==True and y.isnumeric()==True):
        print(f"Sum of all numbers :{isarguments(a=x,b=y)}") # Keyword Argument
    else:
        break

"""
Python Program that takes list of numbers as input and outputs the range of the list...
Range of List is the difference between largest and smallest number...
"""
while(True):
    def isrange(list_1):
        t_1=tuple()
        t_1=t_1+(list_1.index(list_1[0]),)
        t_1=t_1+(len(list_1),)
        return t_1
    Len=input("Total Length :")
    if Len.isnumeric()==True:
        list_2=list()
        for i in range(0,int(Len)):
            list_2=list_2+[int(input("Element to be inserted :"))]
        print(f"Range of Given List :{isrange(list_1=list_2)}")
    else:
        break

"""
Python Program that takes list as an input and returns a new list containing only the
even numbers from the input list...
"""
while(True):
    def iseven(list_1):
        list_2=list()
        for i in list_1[::]:
            if i%2==0:
                list_2=list_2+[i]
        return list_2
    Len=input("Total Length :")
    if Len.isnumeric()==True:
        list_3=list()
        for i in range(0,int(Len)):
            list_3=list_3+[int(input("Element to be Inserted :"))]
        print(f"Even no's in the list :{iseven(list_1=list_3)}")
    else:
        break

"""
Python Program which takes input as a list and return a new list which contains
only those string which are starting with 'A'...
"""
while(True):
    def isnewlist_A(list_1):
        list_2=list()
        for i in list_1[::]:
            if i[0]=='A':
                list_2=list_2+[i]
        return list_2
    Len = input("Total Length :")
    if Len.isnumeric() == True:
        list_3 = list()
        for i in range(0, int(Len)):
            list_3 = list_3 + [input("Element to be Inserted :")]
        print(f"Output List with only string which startswith 'A' :{isnewlist_A(list_1=list_3)}")
    else:
        break

"""
Python Program to take list as an input and return the average of given list...
"""
while(True):
    def average_num(list_1):
        sum=0
        for i in list_1:
            sum=sum+i
        avg=sum/len(list_1)
        return avg
    Len = input("Total Length :")
    if Len.isnumeric() == True:
        list_3 = list()
        for i in range(0, int(Len)):
            list_3 = list_3 + [int(input("Element to be Inserted :"))]
        print(f"Average of all numbers in the given List :{average_num(list_1=list_3)}")
    else:
        break






