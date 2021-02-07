import random
import string
import pyperclip

a = string.ascii_letters+string.digits
key = []


def get_key():
    key = random.sample(a, 10)
    keys = "".join(key)
    return keys


pyperclip.copy(get_key())
spam = pyperclip.paste()
