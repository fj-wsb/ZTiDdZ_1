import secrets, string

def gen_pass():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_chars = string.punctuation
    digits = string.digits
    alphabet = lowercase + uppercase + special_chars + digits
    pwd_length = 12

    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (sum(char in special_chars for char in pwd)>=2 and any(char in lowercase for char in pwd) and any(char in uppercase for char in pwd)and sum(char in digits for char in pwd)>=2):
            break
    return pwd

print(gen_pass())