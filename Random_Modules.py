import random as rnm
Len,list_1=int(input("Length :")),[]
for i in range(0,Len):
    list_1=list_1+[input("Enter any String :")]
random_password=rnm.choice(list_1)
validity_checker=1
chances=int(input("No of Chances :"))
while(validity_checker<=chances):
    print(f"Chance :{validity_checker}")
    user_pwd,count=input("Given Password :"),0
    count_1=count_2=count_3=count_4=0
    if 6<=len(user_pwd)<=16:
        while(count<len(user_pwd)):
            if 'a'<=user_pwd[count]<='z':
                count_1+=1
            elif 'A'<=user_pwd[count]<='Z':
                count_2+=1
            elif '1'<=user_pwd[count]<='9':
                count_3+=1
            else:
                count_4+=1
            count+=1
        if count_1>=1 and count_2>=1 and count_3>=1 and count_4>=1:
            print(f"Valid Password")
            if user_pwd==random_password:
                print(f"User Guesses the computer generated password in {validity_checker} chance"+'\n'+f"Chances left was :{chances-validity_checker}")
                break
            else:
                pass
        else:
            print("Invalid Password...")
    else:
        print("Invalid Password...")
    validity_checker+=1
else:
    print("Chances End but user was unable to guess the computer generated password....")