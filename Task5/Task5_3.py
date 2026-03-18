import json
import string
import random

# создание случайного пароля
def password(lenght  = 12):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(lenght))

def email(name):
    name = name.lower().replace(' ', '.')
    number = random.randint(1, 500)
    domain = ['gmail.com','mail.ru', 'yandex.com']
    return f"{name}{number}@{random.choice(domain)}"

name = random.choice(["John", "Michael", "Emma", "Sarah"])

data = {
    "name": name,
    "age": random.randint(10, 80),
    "email": email(name),
    "password": password()
}

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

with open('data.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

print(json.dumps(data, ensure_ascii=False, indent=4))