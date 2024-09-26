from random import randint
from json import load
from string import ascii_letters


def choose_number(dico: list) -> str:

    i = randint(0,len(dico)-1)
    return dico[i]

def hide_letters(found_letters: list, word: str) -> str:

    word = list(word)

    for i in range(len(word)):
        if word[i] not in found_letters:
            word[i] = "_"
        word[i] += " "
    
    return "".join(word).strip()

with open("words.json") as file:
    words = load(file)

choosen = choose_number(words)
found_letters = ["-"]
proposed_letters = []

letters_auth = ascii_letters + "àâäéèêëîïôöùûüÿçÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇ"
fails_auth = 9

print(letters_auth)

print("Mot généré !\n")

while True:

    print("="*50+"\n")

    print("Mot :",hide_letters(found_letters, choosen))
    print("Erreur(s) autorisée(s) :",fails_auth)

    while True:

        letter = input("Entrez une lettre: ")

        if len(letter) != 1 or letter not in letters_auth:
            continue

        if letter in proposed_letters:
            print("Vous avez déjà entré cette lettre.")
            continue

        proposed_letters += letter
        break

    if letter in choosen:
        found_letters.append(letter)

    else:
        fails_auth -= 1
        print("Non !")

    if hide_letters(found_letters, choosen) == choosen or not fails_auth:
        break

    print("")

if fails_auth:
    print("Vous avez gagné !")
else:
    print("Vous avez perdu...\nLe mot était", choosen)
