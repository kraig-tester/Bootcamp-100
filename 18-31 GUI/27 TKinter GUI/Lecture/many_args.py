# *args - Multiple positional arguments
# args is a tuple
def add(*numbers):
    # print(sum(numbers))

    num_sum = 0
    for num in numbers:
        num_sum += num

    print(num_sum)

# **kwargs - Multiple keyword arguments
# kwargs is a dictionary
def calculate(n, **kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

add(4,5,2,1)
calculate(2, add=3, multiply=5)

# Creating constructor using kwargs
class Car:


    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

    
    def showroom(self):
        print(f"{self.make} - {self.model}")


my_car_1 = Car(make="KIA", model="Sportage")
my_car_2 = Car(make="Lamborghini")
my_car_1.showroom()
my_car_2.showroom()