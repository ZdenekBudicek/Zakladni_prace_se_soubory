# r = read - číst
# w = write - zapisovat
# r+ = read + write - číst - zapisovat
# a = append - vložit na konec
with open("test.txt", mode="a") as my_file:
    my_file.write("\nZdravím\n vkládání je v pořádku.")
