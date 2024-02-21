import secrets
import string

# This is example of a function that generates a random string of letters, numbers, and punctuation for
# use as a password.

print(string.ascii_letters + string.digits + string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(20)))

