student=[]
while True:
    print("=======students list manager========")
    print("1. ADD student")
    print("2. Remove student")
    print("3. Display student")
    print("4. Search Student")
    print("5. Count student")
    print("6. Exit")
    choice=int(input("Enter your Choice:\n"))
    if choice==1:
        name=(input("Enter a student:\n"))
        student.append(name)
        print(name,"added to the list")
    elif choice==2:
        give=input("Enter a student to be remove from the LIST:\n")
        if give in student:
            student.remove(give)
            print(give,"has been Removed Successfully:")
        else:
            print(give,"Is not found in the list.")
    elif choice == 3:
        for i in student:
            print(i)
    elif choice == 4:
        num=input("Enter a student to be search:\n")
        if num in student:
            print(student.index(num))
            print("Search successfull:")
        else:
            print("Student not Found:")
    elif choice == 5:
        value=input("Enter a value which need to be count:\n")
        if value in student:
           print(student.count(value))
        else:
            print("Not Found")
    elif choice==6:
        print("EXIT")
        break
    else:
        print("invalid choice")
