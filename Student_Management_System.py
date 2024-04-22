"""Student Management System"""
names=age=city=course=roll_no=list() #List_Constructor
Len_1=Len_2=Len_3=Len_4=Len_5=int(input("Length of All List :"))
print("......................................Initialization of Data in Student Management System...")
for i,j,k,l,m in zip(range(0,Len_1),range(0,Len_2),range(0,Len_3),range(0,Len_4),
                     range(0,Len_5)): # Zip()
    names,age,city,course,roll_no=names+[input("Enter Student name :")],age+[int(input("Enter Student age :"))],\
                     city+[input("Enter Student City :")],course+[input("Enter Course to be enrolled :")],\
                        roll_no+[int(input("Enter Student Roll_No :"))]
    print("...................................")
while(True):
    opr=int(input("1.Add_Student"+'\n'+"2.Search_By_Name"+'\n'+
                  "3.Update_Student"+'\n'+"4.Delete_Student"+'\n'+
                  "5.Sort_Student"+'\n'+"6.View_All_Student"+'\n'+
                  "7.Quit_Student"+'\n'+
                  "..........................................Choose :"))
    if opr==1:
        print("""Add Student Details on the basis of Roll_No"""+'\n'+"................................")
        while(True):
            std_roll_no=int(input("Roll_No to be Searched for which Student Details to be Added :"))
            if std_roll_no in roll_no:
                print(f"Roll_No :{std_roll_no} already exists...Add Student Not Required...")
            else:
                std_name=input("Add_Student_Name :")
                std_age=int(input("Add_Student_Age :"))
                std_city=input("Add_Student_City :")
                course_enrolled=input("Course_Opt_By_Student :")
                names.append(std_name),roll_no.append(std_roll_no),age.append(std_age)
                city.append(std_city),course.append(course_enrolled)
                for name_1,age_1,city_1,course_1,roll_no_s in zip(names[len(names)-1:],age[len(age)-1:],city[len(city)-1:],
                                                                  course[len(course)-1:],roll_no[len(roll_no)-1:]):
                    print(f"Name :{name_1}"+'|'+f"Age :{age_1}"+'|'+f"City :{city_1}"+'|'+
                          f"Course_Enrolled :{course_1}"+'|'+f"Roll_No :{roll_no_s}")
                break
    elif opr==2:
        print(".................................." + '\n' +
              """Student Info to be Search based on Name""" + '\n' + "..................................")
        while(True):
            name=input("Name to be Searched :")
            if name in names:
                index=names.index(name)
                for std_name,std_roll_no,std_age,std_city,std_course_enroll in zip(names[index:index+1],
                                                                                   roll_no[index:index+1],age[index:index+1],
                                                                city[index:index+1],course[index:index+1]):
                    print(f"Name :{std_name}"+'|'+f"Roll_No :{std_roll_no}"+'|'+f"Age :{std_age}"+'|'+
                              f"City :{std_city}"+'|'+f"Course_Enrolled :{std_course_enroll}")
                break
            else:
                print(f"Given Student :{name} information not present")
    elif opr==3:
        print("..................................."+'\n'+"""Update Course Detail on the basis of Student Name..."""+
              '\n'+".................................")
        while(True):
            std_name=input("Name to be Searched :")
            if std_name in names:
                print(".................................Previous Course Enrolled By Given Student...")
                # print(f"Name :{std_name}"+'|'+
                #       f"Previous_Course :{course[names.index(std_name)]}")
                # Method I - List Item Assignment...
                pos_1=names.index(std_name)
                for j in zip(names[pos_1:pos_1+1],course[pos_1:pos_1+1]):
                    print(f"Name | Previous_Course :{list(j)}")
                #course_change = input("New Course Enrolled by Given Student :")
                # course[pos_1]=course_change
                # Method II - List Methods...
                course_change=input("New Course Enrolled by Given Student :")
                course.pop(pos_1),course.insert(pos_1,course_change)
                print("..............................New Course Opt By Given Student...")
                for k in zip(names[pos_1:pos_1+1],course[pos_1:pos_1+1]):
                    print(f"Name | New_Course :{list(k)}")
                break
            else:
                print(f"Student Name :{std_name} not found in given list... ")
    elif opr==4:
        print("......................................"+'\n'+
              """Delete a Given Student Record on the basis of Roll_No and View the Updated List..."""+'\n'+
              "......................................")
        while(True):
            std_roll_no=int(input("Roll_No to be Deleted from List :"))
            if std_roll_no in roll_no:
                print("Deletion Process Started....")
                pos_1=roll_no.index(std_roll_no)
                # Method I - POP()
                roll_no.pop(pos_1),names.pop(pos_1),age.pop(pos_1)
                city.pop(pos_1),course.pop(pos_1)
                print("After Deletion Process Completed....Below is the Updated List....")
                for std_roll_no_s,std_name,std_age,std_city,std_course in zip(roll_no,names,age,city,course):
                    print(f"Name :{std_name}"+'|'+f"Roll_No :{std_roll_no_s}"+'|'+f"Age :{std_age}"+'|'+
                          f"City :{std_city}"+'|'+f"Course_Enrolled :{std_course}")
                break
            else:
                print(f"Given Roll_No :{std_roll_no} not found to remove the student info....")
    elif opr==5:
        print("..................................."+'\n'+
              """Sort the Student Names on the basis of Roll_No and Print the Index_Value of the Roll_No and Name of the Student"""+
              '\n'+".................................")
        roll_no_name=list()
        for index_no,std_roll_no in enumerate(roll_no):
            roll_no_name=roll_no_name+[{std_roll_no:names[index_no]}]
        for index_no_1 in range(0,len(roll_no)-1):
            for index_no_2 in range(index_no_1+1,len(roll_no)):
                if roll_no[index_no_1]>roll_no[index_no_2]:
                    temp=roll_no[index_no_1]
                    roll_no[index_no_1]=roll_no[index_no_2]
                    roll_no[index_no_2]=temp
        for index_s in roll_no_name:
            for roll_no_s in index_s:
                print(f"Index_No :{roll_no.index(roll_no_s)}"+'|'+f"Name :{index_s[roll_no_s]}")
    elif opr==6:
         print(".................................."+'\n'+
              """View All Student Info"""+'\n'+"......................................")
         for std_name, std_roll_no, std_age, std_city, std_course_enroll in zip(names,roll_no,age,city,course):
            print(f"Name :{std_name}" + '|' + f"Roll_No :{std_roll_no}" + '|' + f"Age :{std_age}" + '|' +
                  f"City :{std_city}" + '|' + f"Course_Enrolled :{std_course_enroll}")
    elif opr==7:
        print("""Quit the Student_Management_System""")
        break
    else:
        print("""Invalid Option""")

