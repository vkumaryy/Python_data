#Zoo Entity

class Animal:
    def __init__(self,name, species,age):
        self.name = name
        self.species = species
        self.age = age
        self.info =[name, species, age]
    
class Zoo:
    def __init__(self):
        self.animals =[""]

    def add_animal(self,name,species,age):
        self.animals.append(Animal(name, species, age))

z = Zoo()
z.add_animal('dog','viller','19')
print(z.animals[1].info)