# r druhý error
try:
    with open("chyba.txt", mode="w") as my_file:
        print(my_file.read())
except FileNotFoundError as not_found_error:
    print("Soubor nenalezen, musíš to udělat jinak.")
    # Už se většinou nepoužívá ale pro ukázku
    # print(not_found_error)
    # raise not_found_error
except IOError as in_out_error:
    print("Máš něco špatně, pravděpodobně nemáš pravomoce!")
