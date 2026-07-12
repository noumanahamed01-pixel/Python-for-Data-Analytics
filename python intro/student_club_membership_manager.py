Team_A=set()
Team_B=set()
while True:
    print("---------Student Club Membership Manager--------")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Display Member")
    print("4. Find Common Member")
    print("5. Exit")
    choice=int(input("Enter Your Choice:\n"))
    if choice==1:
        print("1.=== TEAM_A ===")
        print("2.=== TEAM_B ===")
        Tchoice=int(input("Enter Your Team Choice:\n"))
        member=input("Enter member name:\n")
        if Tchoice==1:
           Team_A.add(member) 
           print(f"{member} Added Successfully to the Team_A club.")
        elif Tchoice==2:
            Team_B.add(member)
            print(f"{member} Added Successfully to the Team_B club.")
        else:
            print("Invalid Team.")
    elif choice==2:
        r=input("Enter a member to remove from the club")
        if r in Team_A and r in Team_B:
            print("1. Remove From both Team.")
            print("2. Only Remove from Team_A")
            print("3. Only Remove from Team_B")
            Rchoice=int(input("Enter the Rchoice to remove:\n"))
            if Rchoice==1:
                Team_A.remove(r)
                Team_B.remove(r)
                print(f"{r} removed Successfully from Team_A and Team_B.")
            elif Rchoice==2:
                Team_A.remove(r)
                print(f"{r} removed successfully from Team_A.")
            elif Rchoice==3:
                Team_B.remove(r)
                print(f"{r} removed successfully from Team_B")
            else:
                print("Invalid Rchoice")
        elif r in Team_A:
            Team_A.remove(r)
            print(f"{r} removed successfully from Team_A.")
        elif r in Team_B:
            Team_B.remove(r)
            print(f"{r} removed Successfully From Team_B.")
        else:
            print(f"{r} is not in the club.")
    elif choice==3:
        print("Student Club Members are:\n")
        print("Team_A:",Team_A)
        print("Team_B:",Team_B)
    elif choice==4:
        print("Common Members From Team_A and Team_B:\n")
        print(Team_A.intersection(Team_B))
    elif choice==5:
        print("Exit")
        print("Thanking for using Student Club Membership Manager.")
        break
    else:
        print("!Choice is Invalid")
