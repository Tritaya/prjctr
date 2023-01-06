from hello import hello
from try_faker import create_user


if __name__ == '__main__':
    print(__name__)
    name_pass = create_user('', '')
    # name_pass = create_user('Jo', '123-aA789')
    if name_pass:
        hello(name_pass[0])