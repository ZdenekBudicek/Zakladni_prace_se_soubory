names = open("names.txt")
print(names.read())
names.seek(0)

for _ in range(10):
    print(names.readline())

names.seek(0)
vypis = names.readlines()
for one_student in vypis:
    print(one_student)

names.close()
