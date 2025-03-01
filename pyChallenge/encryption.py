import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars) #rewrite chars as list
print(chars)
key = chars.copy()
