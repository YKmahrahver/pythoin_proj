#Dictionary
capitals = {"USA" : "washington", "India": "new delhi"}

print(capitals.get("USA"))
#insert or update new element
capitals.update({"japan": "tokyo"})
print(capitals)
#remove is pop, popitem for latest element
#keys() for get key