sayilar = [100,200,300,400,"Aybüke", "Merhaba"]

print(sayilar)
print(sayilar[0])
print(sayilar[1])
print(sayilar[2])
print(sayilar[3])
print(sayilar[4])
print(sayilar[5])

print("**************************************")

#append => listenin sonuna ekleme yapar 
sayilar.append(500)
print(sayilar)

#pop => verilen index'e göre eleman siler. index vermezsen en sondaki elemanı siler

sayilar.pop
sayilar.pop(2)

print(sayilar)


#remove => index' göre değil değere göre silme yapar. Eğer birden fazla aynı eleman varsa ilk gördüğünü siler
sayilar.remove(100)
print(sayilar)

#extend => toplu şekilde veri ekler

sayilar.extend([10,20,30])
print(sayilar)


#clear => herşeyi siler
sayilar.clear()
print(sayilar)


