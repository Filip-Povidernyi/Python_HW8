from pathlib import Path
import pickle
from handler import command_parser, add_contact, change_contact, show_phone, show_all


def main():

    print("Welcome to the assistant bot!")

    path = Path('contacts.pkl')

    if path.exists() and path.is_file():

        with open('contacts.pkl', 'rb') as file:
            contacts = pickle.load(file)

    else:
        contacts = {}

    while True:

        command = input("Enter a command: ").strip().lower()
        cmd, args = command_parser(command)

        match cmd:

            case "hello":
                print("How can I help you?")

            case "add":
                answer = add_contact(args, contacts)
                if isinstance(answer, str):
                    print(answer)
                else:
                    contacts = answer
                    print("New contact added")

            case "change":
                answer = change_contact(args, contacts)
                if isinstance(answer, str):
                    print(answer)
                else:
                    contacts = answer
                    print("Contact updated.")

            case "phone":
                number = show_phone(args, contacts)
                print(f"{number}")

            case "all":
                show_all(contacts)

            case "exit":
                with open('contacts.pkl', 'wb') as file:
                    pickle.dump(contacts, file)
                print("Good bye!")
                break

            case "close":
                with open('contacts.pkl', 'wb') as file:
                    pickle.dump(contacts, file)
                print("Good bye!")
                break

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
