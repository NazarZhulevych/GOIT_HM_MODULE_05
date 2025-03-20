import re
from typing import Callable

# Decorator to handle input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Invalid input format."
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Missing arguments."
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, args = parts[0].strip().lower(), parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if not phone.isdigit():
        return "Error: Phone number must be numeric."
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_number(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if not phone.isdigit():
        return "Error: Phone number must be numeric."
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Number for {name} updated."

@input_error
def find_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts.get(name, "Error: User not found.")

def all_phones(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                print("Error: Please enter a command.")
                continue

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Goodbye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "all":
                print(all_phones(contacts))
            elif command == "change":
                print(change_number(args, contacts))
            elif command == "phone":
                print(find_phone(args, contacts))
            else:
                print("Error: Invalid command.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


