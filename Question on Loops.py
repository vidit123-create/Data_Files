"""Show the concept of break keyword"""
chances=1
while(chances<=3):
    start, end = int(input("Starting Value :")), int(input("Ending Value :"))
    num = int(input("Enter any value :"))
    while(start<=end):
        if start==num:
            print("Hello World")
            break
        start+=1
    else:
        print("Inner Loop Terminated...")
    chances+=1
