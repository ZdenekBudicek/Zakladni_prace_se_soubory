with open("Input/general_letter.txt") as letter:
    letter_content = letter.read()

with open("Input/names.txt") as names:
    list_of_names = names.readlines()
    for one_name in list_of_names:
        one_name = one_name.strip()
        letter_text = letter_content.replace("[name]", one_name)
        with open(f"Output/letter_{one_name}.txt", mode="w") as final_letter:
            final_letter.write(letter_text)
