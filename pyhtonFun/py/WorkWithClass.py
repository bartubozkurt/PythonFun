class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    
    matematik =  Matematik(2,78)
    matematik2 = Matematik(11,11)
    matematik3 = Matematik(82,30)
    matematik4 = Matematik(100,4)
    print("Toplam = "  + str(matematik.topla())) 
    print("Çarp = " + str(matematik2.carp()))
    print("Çıkar = " + str(matematik3.cikar()))
    print("Böl = " + str(matematik4.bol()))   
    