
def translate(phrase):
    transaltion = ""
    for letter in phrase:
        if letter in "AIOUEaioeu":
            transaltion = transaltion + "k"
        else:
            transaltion = transaltion + letter
    return transaltion

print(translate(input("enter a phrase: ")))