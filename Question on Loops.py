"""Show the concept of break keyword"""
"""chances=1"""
print("..................Program Starts")
list_1,Len=list(),int(input("Length of Given List :"))
for i in range(0,Len):
    list_1=list_1+[int(input("Enter any element :"))]
print(f"Input List :{list_1}")
while(True):
    search_element = int(input("Element to be Searched :"))
    """
    for num in list_1[:len(list_1):1]:
        if num==search_element:
            print(f"Search Completed :{num}")
    """
    if search_element in list_1[:len(list_1):1]:
        print(f"Search Completed and number is {search_element}")
        break
    else:
        print("Loop Continues...")
        continue
    """
    while(start<=end):
        if start==num:
            print("Hello World")
            break
        start+=1
    else:
        print("Inner Loop Terminated...")
    chances+=1
    """
print(".......................Program Ends")
