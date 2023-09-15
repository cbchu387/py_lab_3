# conrad chu
# python class cspc 233P
# 9/14/23
# run the python file for the dictionary examples
# which organizes and accepts new dictionary entries
from newfile import*


while True:
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program")
    choice = input("Enter menu choice: ");

    if int(choice) == 1:
        Print_list(contact_list)
    elif int(choice) == 2:
        add_contact(contact_list)
    elif int(choice) == 3:
        modify_contact(contact_list)
    elif int(choice) == 4:
        delete_contact(contact_list)
    elif int(choice) ==5:
        sort_contacts(contact_list,column = 0)
    elif int(choice) ==6:
        sort_contacts(contact_list,column = 1)
    elif int(choice) == 7:
            break
    else:
            print("not valid choice")