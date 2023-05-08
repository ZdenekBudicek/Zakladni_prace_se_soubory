# File  I / 0 = input / output = vstup / výstup

my_file = open("test.txt")
print(my_file.read())

# Číslo určuje pozici kurzoru seek
my_file.seek(3)
print(my_file.read())

my_file.seek(0)
# Čte jen řádek
print(my_file.readline())

# Tady to čte ten enter, takže prázdnej řádek
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)

# Funguje jako list
text = my_file.readlines()
print(text)
print(text[0])
print(text[1])
print(text[2])

# Je dobré soubor také zavírat
my_file.close()
