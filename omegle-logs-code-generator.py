from bs4 import BeautifulSoup
import requests
import random
import time
import sys

def generate() -> str:
    """Generates a random 16-characters code"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    res = ""
    for i in range(16): # logs.omegle.com requires a 16-characters code
        res += random.choice(letters + numbers)
    return res

def is404(code: str) -> tuple:
    """Returns a tuple with a boolean value and the time it took"""
    start = time.time()
    try:
        res = requests.get("https://logs.omegle.com/" + code)
        return True, time.time() - start
    except: # If the script cannot reach the page...
        return True, time.time() - start

def find(n: int=10) -> None:
    """Generates n codes and tries to reach logs.omegle.com using them"""
    for i in range(n):
        code = generate()
        codes = []
        res = is404(code)
        if not res[0]:
            print("Found: " + code)
            print("Time:", res[1])
            codes.append(code)
        else:
            print(f"Attempt {i+1}: Failed")
            print("Time:", res[1], end="\n"+"-"*10+"\n")
    if not codes: # If no code was found...
        print("\nWe did not find any code :(")
    else:
        print("\nWe found some codes! Codes:\n" + "\n".join(codes))

if __name__ == '__main__':
    attempts = int(sys.argv[1]) # The program should be run in command-line
    find(attempts)
