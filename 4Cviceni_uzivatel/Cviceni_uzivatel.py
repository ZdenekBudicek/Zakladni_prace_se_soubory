result = "ano"
while result == "ano":
    user = input("Zadejte název souboru: ")
    with open(f"Output/{user}.txt", mode="w") as text:
        text.write("")
    result = input("Chcete pokračovat? (Ano/Ne)\n").lower()
