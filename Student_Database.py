"""
Create a student management system using List with following options...
"""
list_1, Len = [], int(input("Length of Student List :"))
for i in range(0, Len):
    list_1 = list_1 + [[input("Name of Student :"), int(input("Age of Student :")), input("City of Student :"),
                        int(input("Roll no of Student :"))]]
print(f"Input List :{list_1}")
count, no_of_times = 1, int(input("Total Iterations :"))
while (count <= no_of_times):
    print(".............................Program Starts :")
    user_option = input("Option entered by User :")
    if user_option == "Add_Student":
        list_1.append([input("Name of Student :"), int(input("Age of Student :")), input("City of Student :"),
                       int(input("Roll no of Student :"))])
    elif user_option == "View_All_Student":
        for i in list_1[::]:
            print(i)
    elif user_option == "Search_By_Name":
        name = input("Student name to be searched :")
        for i in list_1:
            for j in i[0]:
                if name == j:
                    print(f"Student found in given List :{name}")
                else:
                    print("Student not found in given List")
    elif user_option == "Search_By_Roll_No":
        roll_no = int(input("Roll no to be searched :"))
        for i in list_1[::]:
            for j in i[len(i) - 1]:
                if roll_no == j:
                    print(f"Student found in given List :{roll_no}")
                else:
                    print("Student not found in given List")
    elif user_option == "Update_Student":
        pos = int(input("Given Index :"))
        for k in range(0, len(list_1)):
            if list_1.index(list_1[k]) == pos:
                for l in range(0, len(list_1[k])):
                    if list_1[k].index(list_1[k][l]) == 0:
                        list_1[k][l] = input("Update the Name of Student :")
                    elif list_1[k].index(list_1[k][l]) == 1:
                        list_1[k][l] = int(input("Update the Age of Student :"))
                    elif list_1[k].index(list_1[k][l]) == 2:
                        list_1[k][l] = input("Update the City of Student :")
                    else:
                        list_1[k][l] = int(input("Update the Roll_No of Student :"))
    elif user_option == "Delete_Student":
        pos = int(input("Given Index :"))
        list_1.pop(pos)
    elif user_option == "EXIT":
        print("EXIT FROM STUDENT MANAGEMENT SYSTEM")
    else:
        pass
    count += 1
else:
    print("..........................................Program Ends")
