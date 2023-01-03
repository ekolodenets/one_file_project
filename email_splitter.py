with open('emails_list.txt', 'r') as f:
    lines = f.read().splitlines()

for mail in lines:
    login, rdomain = mail.split('@')
    domain = rdomain.split('.')[0]
    print(f'{login=}, {domain=}')