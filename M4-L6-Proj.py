import random
def generate_password(length=10):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    all_chars = lowercase + uppercase + numbers
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]
    for _ in range(length - 3):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)
print("Generated Password:", generate_password())
