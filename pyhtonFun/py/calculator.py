print("__  Menüye Hoşgeldin__")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

secenek = input("Hangi İşlemi Yapmak İstiyorsun ?")
sayi1 = int(input("İlk sayiyi giriniz ?"))
sayi2 = int(input("İkinci sayiyi giriniz ?"))

def topla(sayi1, sayi2):
        return sayi1 + sayi2
def cikar(sayi1, sayi2):
        return sayi1 - sayi2
def carp(sayi1, sayi2):
        return sayi1 * sayi2
def bol(sayi1, sayi2):
        return sayi1 / sayi2

 
if secenek == '1':
    print("Toplam : " + str(topla(sayi1, sayi2)))
elif secenek == '2':
    print("Çıkarma : " + str(cikar(sayi1, sayi2)))
elif secenek == '3':
    print("Çarpım : " + str(carp(sayi1, sayi2)))
elif secenek == '4':
    print("Bölme : " + str(bol(sayi1, sayi2)))
else:
    print("geçersiz!!")