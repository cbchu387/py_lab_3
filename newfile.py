contact_list = {3282738293: ['conrad', 'chu']}

def print_list(contact_dictionary,/):
    print(contact_dictionary)

def add_contact(contact_dictionary,/,*, id_input, first_name, last_name):
    """Adds contact to the contact list"""
    if id_input in contact_dictionary:
        print("error")
        return
    else:
        contact_dictionary[id_input] = [first_name,last_name] 
    return first_name, last_name

def modify_contact(contact_dictionary,/,*,id_input, first_name, last_name):
    """modifies contact to the contact list based on id number indicated"""
    if id_input not in contact_dictionary:
        print("error")
    else:    
        contact_dictionary[id_input] = [first_name,last_name] 
    return id_input, first_name, last_name

def delete_contact(contact_dictionary,/,*,id_input):
    """deletes contact based on ID indicated """
    if id_input not in contact_dictionary:
        print("error")
    else:
        del contact_dictionary[id_input]
    return id_input, first_name, last_name

def sort_contacts(contact_dictionary,/):
    """Sorts contact in ascending order"""
    contact_dictionary = sorted(contact_dictionary, key = lambda x:x[1])
    contact_dictionary = sorted(contact_dictionary, key = lambda x:x[0])

def find_contact(contact_dictionary,/,*, find):
    """Adds a contacts found based on ID number in the main dictionary"""
    if find.isdigit() and  (find in contact_dictionary):
        empty_dictionary[find] = contact_dictionary[find]
    
