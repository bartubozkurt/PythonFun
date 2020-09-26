import module

module.topla(2,3)
module.carp(11,11)

print(module.customer["firstName"],module.customer["lastName"],module.customer["age"])
#------------------------------
from  module import customer

print(customer["firstName"])


"""
import module as m 
m.topla(1,2)
m.carp(2,2)
"""
#------------------------------
"""
from module import topla
topla(2,2)
"""