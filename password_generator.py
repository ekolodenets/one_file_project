import random
import string

symbols = list(string.ascii_letters + string.digits + "!@#$%^&*()_")


def generate_password():
    password_length = 10
    random.shuffle(symbols)
    password = []

    for _ in range(password_length):
        password.append(random.choice(symbols))

    print(''.join(password))


generate_password()
