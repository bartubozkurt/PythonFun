import json
data  = '{"firstName" : "Bartu", "lastName" : "BOZKURT"}'

ex = json.loads(data)

type(ex)

print(ex["firstName"], ex["lastName"])

customer = {
         "firstName" : "bartu",
         "email" : "bartubozkurt35@gmailcom"
        }

customerJson = json.dumps(customer)
print(customer)