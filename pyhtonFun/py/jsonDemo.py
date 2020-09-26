import json
with open("users.json") as users:
    data = json.load(users)
    #print(data) # tüm bilgileri getir
    print("----")
    print(data[5]["username"]) # 5. id nin username
    print("----")
    print(data[5]["email"])
    print("----")
    print(data[5]["address"])
    print("----")
    print(data[5]["address"]["zipcode"])
    print("----")
    print(data[5]["address"]["geo"]["lng"])

print("##########################################")

for i  in range (5): # ilk 4 değerin bilgileri
    print(data[i]["username"])
    print(data[i]["email"])
    print(data[i]["address"]["street"])
    print(data[i]["address"]["geo"]["lat"])