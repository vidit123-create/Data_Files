"""
Mini Python Program to Guess the Word by user which is generated
randomly by computer...
"""
print(".............................Program Starts")
import random as rm
Len,list_1=int(input("Total Length :")),[]
for i in range(0,Len):
    list_1=list_1+[input("Word to be Entered :")]
chance,total_chance=1,int(input("Total Chances to guess the computer generated word by user :"))
score=0
user_inputted=input("Word to be Entered by User :")
while(chance<=total_chance):
    computer_generated = rm.choice(list_1)
    print(f"Computer Generated Word :{computer_generated}"+'\n'+
          f"....................................Chance :{chance}")
    if (user_inputted==computer_generated) and (chance==1):
        score=score+100
        remaining_chance=total_chance-chance
        print(f"User guess the word correct with a total score of {score} and no of chances left was {remaining_chance}")
        break
    elif (user_inputted==computer_generated) and (chance==2):
        score=score+70
        remaining_chance=total_chance-chance
        print(f"User guess the word correct with a total score of {score} and no of chances left was {remaining_chance}")
        break
    elif (user_inputted==computer_generated) and (chance==3):
        score=score+50
        remaining_chance=total_chance-chance
        print(f"User guess the word correct with a total score of {score} and no of chances left was {remaining_chance}")
        break
    elif (user_inputted==computer_generated) and (chance==4):
        score=score+30
        remaining_chance=total_chance-chance
        print(f"User guess the word correct with a total score of {score} and no of chances left was {remaining_chance}")
        break
    elif (user_inputted==computer_generated) and (chance==5):
        score =score+10
        remaining_chance =total_chance - chance
        print(f"User guess the word correct with a total score of {score} and no of chances left was {remaining_chance}")
        break
    else:
        print("Wrong Guess....Try Again")
    chance+=1
else:
    print(f"User unable to guess the given word and went out of chances :{chance}")
print("..............................Program Ends")

