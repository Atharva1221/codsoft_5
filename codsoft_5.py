#Contact Book
#TASK-5
contact={}
print("-----------Contact Book-----------")
def show_contact():
    print("Name\t\tContact Number\t\tEmail")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    print("Enter choice please:")
    choice=int(input(" 1.Add Contact \n 2.Search Contact\n 3.View Contact List\n 4.Update Contact\n 5. Delete Contact \n 6.Exit \n"))
    if choice==1:
        name=input("Enter contact name: ")
        phone=input("Enter mobile number: ")
       
        contact[name]=phone
    elif choice==2:
        search_name=input("enter contact name")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("Name is not found in contact book")
    
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            show_contact()
    
    elif choice==4:
        edit_contact=input("enter contact name to be edited: ")
        if edit_contact in contact:
            phone=input("enter mobile number: ")
            contact[edit_contact]=phone
            print("contact updated")
            show_contact()
        else:
            print("name is not found in contact book")
            
    elif choice==5:
        del_contact=input("enter contact name to be deleted")
        if del_contact in contact:
            confirm= input("do you want to delete this contact Y/N ?")
            if confirm=='Y' or confirm=='y':
                contact.pop(del_contact)
            show_contact()
        else:    
            print("name is not found in contact book")
    else:
        print("Thankyou")
        break