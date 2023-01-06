from faker import Faker
import string

faker = Faker()

def validate_pass(password: str) -> bool:
    '''length must be > 8 and the symbols from the groups below must be present'''
    # necessary groups of symbols
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    ]
    return all(
                any(x in group for x in password) 
                for group in groups
                ) and len(password) > 8



def create_user(name: str = None, password: str = None) -> None:
    if not name:
        name = faker.name()
    print(name)
    if not validate_pass(password):
        print('Password is not strong, user is not created')
        return
    print(f'New user name is {name}, new password is {password}')
    return name, password
# dir(faker)
