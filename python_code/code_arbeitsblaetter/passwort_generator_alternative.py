# Variante über eine Scheife über den kompletten text
def create_new_password(sentence):
    word = ""
    for i in range(len(sentence)):
        if i == 0:
            word += sentence[i]
        if sentence[i] == " ":
            word += sentence[i + 1]
        word.lower()

    password = ""
    for i in range(len(word)):
        if i % 2 == 0:
            password += word[i].upper()
        else:
            password += word[i].lower()
    return password


text = input("Geben Sie einen Satz ein: ")
print(create_new_password(text))
