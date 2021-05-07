import hashlib
import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if hash(guess) == hash(real):
                print("Brute force algo cracked password :", guess, '(in', attempts, 'attempts)')
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
 
def readwordlist():
    try:
        wordlistfile = open('dictionary.txt','r').read()
    except Exception as e:
        print("There was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile
 
 
def hash(wordlistpassword):
    #returns hash value of a string
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()
 
 
def dictionary_attack(guesspasswordlist, actual_password_hash):
    found = False
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            found = True
            print("Your password is present in dictionary :", guess_password)
            # If the password is found then it will break here
            break
    if not found:
        print("Password not present in dictionary")

actual_password = 'abcd'
actual_password_hash = hash(actual_password)
 
wordlist = readwordlist()
guesspasswordlist = wordlist.split('\n')

# Running dictionary attack
dictionary_attack(guesspasswordlist, actual_password_hash)

# Running the Brute Force attack
guess_password(actual_password)

