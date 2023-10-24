Not = input("Lütfen notunuzu giriniz= ")

NotAsInteger = int(Not)


if NotAsInteger > 80 :
    print("Geçerli not")
    if NotAsInteger > 90:
        print("Bravo")

elif NotAsInteger >50 :
    print("Koşullu geçiş")
    

else:
    print("Geçemediniz")


print("************************")

print(type(Not))
print(type(NotAsInteger))