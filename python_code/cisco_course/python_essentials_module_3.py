import math
'''
# 3.1.1.12 common/leap year
year = int(input("Enter a year: "))

if(year % 4 != 0):
    type = "common"
elif(year % 100 != 0):
    type = "leap"
elif(year % 400 != 0):
    type = "common"
else:
    type = "leap"
print(type)

# 3.2.1.3 Stuck in magicians loop
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_input = int(input("Enter an integer number"))
while True:
    if(secret_number == user_input):
        print(secret_number)
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Haha you're stuck in my loop!")
        input("Enter an integer number")

"3.2.1.6"
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for i in range(1, 5):
    print(i, " Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

# Write a print function with the final message.

"Lab 3.2.1.9"
codeword = "chupacabra"
while True:
    guess = input("Geben Sie ein Wort ein: ")
    if guess == codeword:
        print("You've successfully left the loop")
        break


'Lab 3.2.1.10'
user_word = input("Enter a word: ")
user_word = user_word.upper()
shortened_word = ""
for letter in user_word:
    # Complete the body of the for loop.
    for letter in user_word:
        print(letter)
        if letter not in ["A", "E", "I", "O", "U"]:
            shortened_word + letter

print(shortened_word)
'''

# 3.2.1.14 Pyramide 1
bricks = int(input("Geben Sie die Anzahl an Steinen an: "))
counter = 0
while True:
    counter += 1
    if counter > bricks:
        break
    bricks -= counter

print(counter-1)

# Pyramide 2
bricks = int(input("Geben Sie die Anzahl an Steinen an: "))
hoehe = math.floor(-0.5 + math.sqrt(0.25+2*bricks))
print(hoehe)

# 3.2.1.15 Collatz Hypothesis
c0 = int(input("Geben Sie einen positiven Integer an: "))

counter = 0
while True:
    counter += 1
    if(c0 % 2 == 0):
        c0 = c0/2
    else:
        c0 = 3*c0 + 1
    print(c0)
    if(c0 == 1):
        break
print(counter)