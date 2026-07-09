# Cheat Sheet: Python Programming Fundamentals

Referensi cepat sintaks conditions, loops, functions, exception handling, dan classes. Pelengkap dari lab [3.1](../3.1%20-%20Conditions%20and%20Branching/README.md), [3.2](../3.2%20-%20Loops/README.md), [3.3](../3.3%20-%20Functions/README.md), [3.4](../3.4%20-%20Exception%20Handling/README.md), dan [3.5](../3.5%20-%20Classes%20and%20Objects/README.md).

## Comparison Operators

| Operator | Fungsi | Contoh |
|---|---|---|
| `==` | Sama dengan | `5 == 5` → `True` |
| `!=` | Tidak sama dengan | `a != b` |
| `>` | Lebih besar dari | `9 > 6` → `True` |
| `>=` | Lebih besar atau sama dengan | `quantity >= minimum` |
| `<` | Lebih kecil dari | `4 < 6` → `True` |
| `<=` | Lebih kecil atau sama dengan | `size <= max_size` |

## Logical Operators

**AND** — True hanya kalau kedua kondisi True.
```python
if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
```

**OR** — True kalau salah satu kondisi True.
```python
if grade == 11 or grade == 12:
    print("Farewell Party Invitation")
```

**NOT** — membalik nilai boolean.
```python
isLocked = False
print(not isLocked)   # True
```

## Branching

**If Statement**
```python
if temperature > 30:
    print("It's a hot day!")
```

**If-Else**
```python
if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")
```

**If-Elif-Else**
```python
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")
```

## Loops

**range()**
```python
range(5)          # 0 sampai 4
range(2, 10)       # 2 sampai 9
range(1, 11, 2)    # ganjil, 1 sampai 9
```

**For Loop**
```python
for num in range(1, 10):
    print(num)

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

**While Loop**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**break dan continue**
```python
for num in range(1, 6):
    if num == 3:
        break        # keluar loop total
    print(num)

for num in range(1, 6):
    if num == 3:
        continue     # skip iterasi ini, lanjut ke berikutnya
    print(num)
```

## Functions

**Definisi & Pemanggilan**
```python
def greet(name):
    print("Hello,", name)

greet("Alice")   # function call
```

**Return Statement**
```python
def add(a, b):
    return a + b

result = add(3, 5)
```

## Exception Handling

**Try-Except**
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
```

**Try-Except-Else** — `else` jalan kalau TIDAK ada exception.
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number")
else:
    print("You entered:", num)
```

**Try-Except-Finally** — `finally` SELALU jalan, untuk cleanup resource.
```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
```

## Classes & Objects

**Definisi Class**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**Membuat Object (Instantiation)**
```python
person1 = Person("Alice", 25)
```