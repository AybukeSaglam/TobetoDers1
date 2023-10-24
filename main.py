print("Merhaba Tobeto Test Ekibi")

print("**************************************")

#degiskenler

#metinsel => String

text= "Merhaba"

print(text)
print(text)
print(text)
print(text)
print(text)

text = "Merhaba Tobeto"

print(text)
print(text)
print(text)
print(text)
print(text)


#numerik => Int, Integer, Tam Sayı

studentCount = 45

print(studentCount)

#double, decimal, float => Ondalıklı Sayı

studentCount1 = 50.6
print(studentCount1)


#boolean => True, False (0,1)

isVerified = True
print(isVerified)

print(text, studentCount, studentCount1, isVerified)



print("**************************************")

#type => Değişkenlerin türünü gösterir

#print(type(text, studentCount, studentCount1, isVerified))


print("**************************************")

#operatörler
#matematiksel işlemler + - * / %

number = 10
number1 = 20

print(number + number)

print (number1 - number)

print (number * number1)

print(number1/2)

print(number1 % 2)


print("**************************************")

#mantıksal operatörler (karşılaştırma)

print(number == 10)  #true
print(number1 == 10) #false

print(number != 10) #false
print(number1 != 10) #true

print(number < 10) #false
print(number <= 10) #true



print("**************************************")

#string interpolation => metin birleştirme

hello = "merhaba"
userName = "Aybüke"

totalText = hello + userName

totalText1 = hello + " " + userName

print(totalText)
print(totalText1)

totalText2 = "{message} Sayın {name}".format(message ="Selam", name=userName)
print(totalText2)

#f-string

totalText3 = f"Hoşgeldiniz {userName}"
print(totalText3)

print("**************************************")







