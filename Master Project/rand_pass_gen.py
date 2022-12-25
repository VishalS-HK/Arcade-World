import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
numbers=["0","1","2","3","4","5","6","7","8","9"]

def generate_random_password():
	length=10
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	return "".join(password)

def generate_2FA_code():
        length=6
        random.shuffle(numbers)
        twofa=[]
        for i in range(length):
                twofa.append(random.choice(numbers))
        random.shuffle(twofa)
        return "".join(twofa)

