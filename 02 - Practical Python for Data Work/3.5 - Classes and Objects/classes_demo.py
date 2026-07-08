# ===== 1. Class Circle =====
import matplotlib.pyplot as plt


class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method: menambah radius
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    # Method: menggambar lingkaran, simpan ke file (bukan plt.show())
    def draw_circle(self, filename="circle.png"):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.savefig(filename)
        plt.close()
        print(f"Circle saved to {filename}")


# ===== 2. Membuat instance/object dari class Circle =====
RedCircle = Circle(10, 'red')

print(dir(RedCircle))   # semua method yang bisa dipakai objek ini

print("Radius:", RedCircle.radius)
print("Color:", RedCircle.color)

RedCircle.radius = 1    # ubah atribut langsung
print("Radius after change:", RedCircle.radius)

RedCircle.draw_circle("red_circle.png")

print('Radius of object:', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius after add_radius(2):', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius after add_radius(5):', RedCircle.radius)

# Object baru dengan default color (blue)
BlueCircle = Circle(radius=100)
print("BlueCircle radius:", BlueCircle.radius)
print("BlueCircle color:", BlueCircle.color)
BlueCircle.draw_circle("blue_circle.png")

# ===== 3. Class Rectangle =====
class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method: menggambar persegi panjang, simpan ke file
    def draw_rectangle(self, filename="rectangle.png"):
        plt.gca().add_patch(
            plt.Rectangle((0, 0), self.width, self.height, fc=self.color)
        )
        plt.axis('scaled')
        plt.savefig(filename)
        plt.close()
        print(f"Rectangle saved to {filename}")


# ===== 4. Membuat instance Rectangle =====
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
print("Height:", SkinnyBlueRectangle.height)
print("Width:", SkinnyBlueRectangle.width)
print("Color:", SkinnyBlueRectangle.color)
SkinnyBlueRectangle.draw_rectangle("skinny_blue_rectangle.png")

FatYellowRectangle = Rectangle(20, 5, 'yellow')
print("Height:", FatYellowRectangle.height)
print("Width:", FatYellowRectangle.width)
print("Color:", FatYellowRectangle.color)
FatYellowRectangle.draw_rectangle("fat_yellow_rectangle.png")

# ===== 5. Scenario: Car Dealership Inventory System =====

class Vehicle:
    color = "white"   # class attribute -> sama untuk SEMUA object, kecuali di-override

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed          # instance attribute -> beda tiap object
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)


# Membuat 2 object Vehicle
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

print()  # pemisah biar rapi

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()

# ===== 6. Reading: Real-World Example - Car Class =====

class Car:
    # Class attribute (sama untuk semua object)
    max_speed = 120  # km/h

    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        # kecepatan tidak boleh melebihi max_speed
        if self.speed + acceleration <= self.max_speed:
            self.speed += acceleration
        else:
            self.speed = self.max_speed

    def get_speed(self):
        return self.speed


# Membuat 2 object Car
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

car1.accelerate(30)
car2.accelerate(20)

print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

# Bukti class attribute bisa diakses lewat nama class langsung (bukan cuma lewat object)
print("Max speed (class attribute):", Car.max_speed)