# Contestant Number: 00051589

class Octane:
    def __init__(self, name) -> None:
        self.name = name
        self.price = 0
    
    def discount(self, discountAmmout):
        self.price -= self.price * discountAmmout
        self.price = round(self.price, 2)
        return self.price
    
    def no_discount(self):
        return False
    
    def __str__(self):
        return self.name + " price: $" + str(self.price)
    
def get_octanes():
    octanes = [Octane("Premium 93"), Octane("Midgrade 89"), Octane("Regular 87")]
    
    octanes[0].price = 4.68
    octanes[1].price = 4.55
    octanes[2].price = 4.42
    
    return octanes

def get_octane(octanes):
    def get_user_input(min_num:int, max_num:int, num = "", values = None):
        
        # make the list holding the right values this is in a if statment so we dont have to recreate the list ever recursive call
        if values == None:
            values = []
            for i in range(min_num, max_num):
                values.append(str(i))
        
        # get the number from the user and make sure its actually a number
        num = input("Please input a number from " + str(min_num) + " to " + str(max_num-1) + " \n: ")
        while num not in values:
            num = input("Please input a number from " + str(min_num) + " to " + str(max_num-1) + " \n: ")
        
        # make sure its the right number
        for i in range(min_num, max_num):
            if int(num) == i:
                return i
        
        return get_user_input(min_num, max_num, num, values)
    
    print("Octane Number\tOctane Name\tPrice (Before Discount)")
    
    for i in range(len(octanes)):
        print(str(i) + "\t\t" + octanes[i].name + "\t" + str(octanes[i].price))

    print("Which octane would you like to use?")
    return octanes[get_user_input(0, len(octanes))]

def round(num_to_round:float, places_to_round_to = 0) -> float:
    """ this rounds a given number. doesn't round 5 up and the number of places to round to means the number of decmile places you want"""
    return float(format(num_to_round,".{}f".format(places_to_round_to)))