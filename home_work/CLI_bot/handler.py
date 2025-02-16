from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError:
            if func.__name__ == 'add_contact':
                return 'For add contact, please, enter <add name phone>'
            elif func.__name__ == 'change_contact':
                return 'For change contact, please, enter <change name new_phone>'

        except IndexError:
            if func.__name__ == 'show_phone':
                return 'For get phone number, please, enter <phone name>'

        except KeyError as error:
            if func.__name__ == 'add_contact':
                return str(error)
            elif func.__name__ == 'change_contact':
                return str(error)
            elif func.__name__ == 'show_phone':
                return str(error)

    return inner


def command_parser(command):

    cmd, *args = command.split(' ')
    cmd = cmd.strip().lower()

    return cmd, args


@input_error
def add_contact(args: list, contacts: dict):

    name, phone = args

    if name in contacts.keys():

        raise KeyError(
            f"This name {name.title()} is busy. Please, try enother one")

    else:
        contacts[name] = phone

    return contacts


@input_error
def change_contact(args: list, contacts: dict):

    name, phone = args

    if name in contacts.keys():
        contacts[name] = phone

    else:
        raise KeyError(f'This name: {name.title()} is absent')

    return contacts


@input_error
def show_phone(args: list, contacts: dict):

    name = args[0]

    if name in contacts.keys():
        return contacts[name]

    else:
        raise KeyError(f'No contact with name {name.title()}.')


def show_all(contacts: dict):

    if not contacts:
        return "No contacts in your phonebook"
    else:
        for name, number in contacts.items():
            print(f"{name.title()}.....{number}")
