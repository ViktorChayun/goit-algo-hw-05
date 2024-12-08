"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951593/homework
    
    додайте обробку помилок за допомоги декораторів.
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error
"""
import sys
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid command"
        except ValueError:
            return "Invalid command"
        except IndexError:
            return "Invalid command"
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner_func

@input_error
def parse_input(user_input:str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#add [ім'я] [номер телефону]
@input_error
def add_contact(args, contacts)->str:
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

#change [ім'я] [новий номер телефону]
@input_error
def change_contact(args, contacts):
        key, val = args
        contacts[key.lower()] = val
        return "Contact updated."

#phone [ім'я]
@input_error
def show_phone(args, contacts) -> str:
    [key] = args
    return contacts[key.lower()]

#all
@input_error
def show_all(args, contacts):
    all_contacts = ""
    for key, val in contacts.items():
        all_contacts = all_contacts + key + ": " + val + "\n"
    return all_contacts

def main():
    contacts ={}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                sys.exit(0)
            case "hello":
                print("How can I help you?")
            case "all":
                print(show_all(args, contacts))
            #add [ім'я] [номер телефону]    
            case "add":
                print(add_contact(args, contacts))
            #change [ім'я] [новий номер телефону]
            case "change":
                print(change_contact(args, contacts))
            #phone [ім'я]
            case "phone":
                print(show_phone(args, contacts))
            case _:
                print("Invalid command.")
            
if __name__ =="__main__":
    main()