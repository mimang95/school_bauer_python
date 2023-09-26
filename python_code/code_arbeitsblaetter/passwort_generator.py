# Passwort Generator
'''
# Variante über Split
def create_password(sentence):
    words = sentence.split()

    password = ""

    for word in words:
        if word:
            password += word[0]

    alternating_password = ""
    to_upper = True

    for char in password:
        if to_upper:
            alternating_password += char.upper()
        else:
            alternating_password += char.lower()

        to_upper = not to_upper

    return alternating_password

sentence = input("Geben Sie einen Satz ein: ")

password = create_password(sentence)
print("Das generierte Passwort ist:", password)
'''