file = open("customer.txt")
# "r" : Read  "a" Append "w" Write "x" Createw
print(file.read())  #  DOSYAYI OKU !
# print(file.read(10)) İLK 10 KARAKTERİ OKU !
print("***************")

for line in file:  # DOSYAYI SONUNA KADAR OKU !
    print(line)

file.close()

fileToAppend = open("worker.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Salih")
fileToAppend.write("\n")
fileToAppend.write("Ali")   
fileToAppend.close()


import os
os.remove("worker.txt") 

os.rmdir("empty.txt") # KLASÖR  SİLMEK İÇİN !
