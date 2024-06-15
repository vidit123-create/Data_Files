"""
Concept of File Handling...
"""
f=open('FirstFile.txt','x')
f.close()
while(True):
    def add_values(list_1):
        sum=0
        for i in list_1[::]:
            sum=sum+i
        return sum
    Len=input("Total Length :")
    if Len.isnumeric()==True:
        list_2=list()
        for i in range(0,int(Len)):
            list_2.append(int(input("Element to be Inserted :")))
        print(f"Sum of all the values in a given list :{add_values(list_1=list_2)}")
    else:
        break
f=open('FirstFile.txt','a')
#f=open('FirstFile.txt','r')