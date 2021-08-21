''' Exercise #8. Python for Engineers.'''

class Animals:
    def __init__(self,speed):
        self.speed=speed
        if speed<0:
            raise ValueError("speed is negative num")

    def get_name(self):
        return self.__class__.__name__

class Predator(Animals):
    def __init__(self,speed,force):
        Animals.__init__(self, speed)
        self.force = force

    def get_velocity(self):
        return int(self.speed)

    def get_power(self):
        return int(self.force)

    def fight(self , other):
        if other.get_name() == "Lion" or other.get_name() == "Alligator":
            return self.get_power() > other.get_power()
        if other.get_name() == "Rabbit":
            return True
        if other.get_name() == "Zebra":
            return True
        return ValueError("Predators eat meat")

    def __repr__(self):
        return str(self.get_name()) + " v " + str(self.speed) + " p " + str(self.force)

class Lion(Predator):
    def __init__(self,speed,force):
       Predator.__init__(self, speed , force)

class Alligator(Predator):
    def __init__(self,speed,force):
       Predator.__init__(self, speed , force)

class Vegiterian(Animals):
    def __init__(self,speed, age):
        Animals.__init__(self,speed)
        self.age = age

    def get_velocity(self):
        return int(self.speed)

    def get_age(self):
        return self.age

    def fight(self, other):
        if other.get_name() == "Lion":
            return False
        if other.get_name() == "Alligator":
            return False
        if other.get_name() == "Rabbit":
            return self.get_age() > other.get_age()
        if other.get_name() == "Zebra":
            return self.get_age() > other.get_age()
        if other.get_name() == "Grass":
            return True
        if other.get_name() == "Mango":
            return True

    def __repr__(self):
        return str(self.get_name())+ " v " + str(self.speed) + " a " + str(self.age)

class Rabbit(Vegiterian):
    def __init__(self, speed, age):
        Vegiterian.__init__(self, speed , age)

class Zebra(Vegiterian):
    def __init__(self,speed, age):
        Vegiterian.__init__(self, speed , age)

class Plants:
    def __init__(self):
        pass

    def get_name(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self.get_name())

class Grass(Plants):
    def __init__(self):
        Plants.__init__(self)

class Mango(Plants):
    def __init__(self):
        Plants.__init__(self)

class Jungle:
    def __init__(self , list_of_items):
        self.list_of_items = list_of_items

    def __getitem__(self, item):
        j = str(item).strip("[")
        f = j.strip("]")
        return self.list_of_items[int(f)]

    def get_organisms(self):
        return str(self.list_of_items)

    def get_mean_velocity(self):
        count_speed = 0
        count_animals = 0
        for i in range(len(self.list_of_items)):
            a = self.list_of_items[i].get_name()
            if a == "Lion" or a== "Alligator" or a== "Zebra" or a== "Rabbit":
                count_speed = count_speed + self.list_of_items[i].get_velocity()
                count_animals = count_animals + 1
        if count_animals == 0:
            return 0.0

        return float(count_speed)/float(count_animals)

    def get_predators(self):
        predators = []
        for i in range(len(self.list_of_items)):
            if self.list_of_items[i].get_name() == "Lion":
                predators.append(self.list_of_items[i])
            if self.list_of_items[i].get_name() == "Alligator":
                predators.append(self.list_of_items[i])

        predators.sort(key=Predator.get_power , reverse=True)
        return predators

    def run_fight(self, first , second):
        if self.__getitem__(first).get_name() == "Mango" or self.__getitem__(first).get_name() == "Grass":
                if self.__getitem__(second).get_name() == "Mango" or self.__getitem__(second).get_name() == "Grass":
                   return None
        if self.__getitem__(first).get_name() == "Mango" or self.__getitem__(first).get_name() == "Grass" or self.__getitem__(second).get_name() == "Mango" or self.__getitem__(second).get_name() == "Grass":
            if self.__getitem__(first).get_name() == "Lion" or self.__getitem__(first).get_name() =="Alligator" or self.__getitem__(second).get_name() == "Lion" or self.__getitem__(second).get_name() == "Alligator":
                return None
        if self.__getitem__(first).fight(self.__getitem__(second)) is True:
            self.list_of_items.remove(self.__getitem__(second))
        else:
            self.list_of_items.remove(self.__getitem__(first))

        return self.list_of_items

    def getitem_operator(self , i):
        j= str(i).strip("[")
        f = j.strip("]")
        return self.list_of_items[int(f)]


leo1=Lion(35 , 50)
print leo1
print leo1.get_name()
leo2=Lion(20,60)
print leo2
print leo2.get_velocity()
print leo1.fight(leo2)
zebra=Zebra(11,5)
print zebra
print zebra.get_name()
print zebra.get_velocity()
print zebra.get_age()
print leo1.fight(zebra)
mango = Mango()
print leo1.fight(mango)
print mango
print zebra.fight(mango)
grass = Grass()
print grass
jungle = Jungle([leo1,leo2,zebra,mango,grass])
print jungle.get_organisms()
print jungle.get_mean_velocity()
print jungle.get_predators()
print jungle.run_fight(3,4)
print jungle[2]