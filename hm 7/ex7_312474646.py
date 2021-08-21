""" Exercise #7. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

class Food:
    def __init__(self, name, price, calories, ingredients):
        self.name = name
        self.price = price
        if price <= 0:
            raise ValueError("price cannot be 0!")
        self.calories = calories
        if calories <= 0:
            raise ValueError("calories cannot be 0!")
        self.ingredients = ingredients

    def __repr__(self):
        return self.name + " cost " + str(self.price) + " NIS and contain: " + \
               str(self.ingredients) + " only " + str(self.calories) + " calories"

    def __lt__(self, other):
        if self.price < other.price:
            return True
        if self.price == other.price:
            if len(self.ingredients) > len(other.ingredients):
                return True
        return False

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def add_ingredient(self, ingredient, calories):
        self.ingredients.append(ingredient)
        self.calories = self.calories + int(calories)

    def remove_ingredient(self, ingredient, calories):
        self.ingredients.remove(ingredient)
        self.calories = self.calories - int(calories)


burger = Food('burger', 50, 200, ['bun', 'meat', 'ketchup', 'fries'])
burger.add_ingredient('musterd', 30)
burger.remove_ingredient('bun', 40)
crepe = Food('crepe', 20, 300, ['nutela', 'dou', 'oil'])
print burger
print crepe


#########################################
# Question 2 - do not delete this comment
#########################################


class Beverage:
    def __init__(self, name, price, is_diet):
        self.name = name
        self.price = price
        if price <= 0:
            raise ValueError("price cannot be 0!")
        self.is_diet = is_diet

    def __repr__(self):
        if self.is_diet == True:
            return str(self.name) + " costs " + str(self.price) + " NIS (is diet)"
        if self.is_diet == False:
            return str(self.name) + " costs " + str(self.price) + " NIS "

    def get_price(self, size):
        if str(size) == 'normal':
            return self.price
        if str(size) is None:
            return self.price
        if str(size) == 'big':
            return self.price * 1.2
        if str(size) == 'small':
            return self.price * 0.8
        raise ValueError("size not as needed")


coke = Beverage('coke', 10, True)
print coke.is_diet
print coke
print coke.get_price('big')


#########################################
# Question 3 - do not delete this comment
#########################################


class Meal:
    def __init__(self, name, beverage, food):
        self.name = name
        self.beverage = beverage
        self.food = food

    def __repr__(self):
        if self.is_healthy():
            return str(self.name) + " meal costs " + str(self.get_price()) + " NIS (healthy!) "
        else:
            return str(self.name) + " meal costs " + str(self.get_price()) + " NIS "

    def get_price(self):
        count = 0
        mini = self.food[0].price
        for i in range(len(self.food)):
            count = count + self.food[i].price
            if self.food[i].price < mini:
                mini = self.food[i].price

        return (count + self.beverage.get_price("small")) - mini

    def get_price1(self):
        count = 0
        for i in range(len(self.food)):
            count = count + self.food[i].price

        return count + self.beverage.get_price('normal')

    def __contains__(self, ingredient):
        for i in range(len(self.food)):
            if ingredient in self.food[i].ingredients:
                return True
        return False

    def is_healthy(self):
        count = 0
        for i in range(len(self.food)):
            count = count + self.food[i].calories
        return count < 800 and self.beverage.is_diet


italian = Meal('italian', coke, [burger, crepe])
print italian
print italian.__contains__('nutela')


#########################################
# Question 4 - do not delete this comment
#########################################

def check_if_float(num):
    try:
         x= float(num)
         return True
    except:
        return False

def load_meal(file_name):
    f = open(file_name, "r")
    i = 0
    foods = []
    try:
     for line in f:
        temp = line.split(",")
        i = i + 1
        if temp[0] != "food":
            if temp[0] != "beverage":
               print "row " + str(i) + " is not vaild"
               continue
        if temp[2] < 0:
            print "row " + str(i) + " is not vaild"
            continue
        if check_if_float(temp[2]) == False:
            print "row " + str(i) + " is not vaild"
            continue
        if temp[0] == "food" and temp[3] < 0:
            print "row " + str(i) + " is not vaild"
            continue
        if temp[0] == "food" and check_if_float(temp[3]) == False:
            print "row " + str(i) + " is not vaild"
            continue
        if temp[0] == "beverage":
                if temp[3] != "t" :
                 if temp[3] != "f":
                  print "row " + str(i) + " is not vaild"
                  continue
        if temp[0] == "beverage":
            if temp[3] == 't':
                x1 = Beverage(temp[1], int(temp[2]), True)
            else:
                x1 = Beverage(temp[1], int(temp[2]), False)
        if temp[0] == "food":
            b = Food(temp[1], int(temp[2]), int(temp[3]), temp[4].split(";"))
            foods.append(b)
    except:
        IOError(" annot load menu due to IOError")
    meal = Meal(str(file_name), x1 , foods)
    print "meal costs " + str(meal.get_price1()) + " load successfully "
    f.close()
    return meal


print load_meal("C:\\Users\\yonle\\hm5\\italian.csv")


