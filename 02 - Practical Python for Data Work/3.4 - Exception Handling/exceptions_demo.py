# ===== 1. Contoh Exception (dibungkus try/except supaya program tidak berhenti) =====

# ZeroDivisionError: dibagi dengan nol
try:
    1 / 0
except Exception as e:
    print(f"Error 1: {type(e).__name__} - {e}")

# NameError: pakai variabel yang belum didefinisikan
try:
    y = a + 5
except Exception as e:
    print(f"Error 2: {type(e).__name__} - {e}")

# IndexError: akses index yang tidak ada di list
try:
    a = [1, 2, 3]
    a[10]
except Exception as e:
    print(f"Error 3: {type(e).__name__} - {e}")

# ===== 2. Try-Except Generik =====
def divide_generic(b):
    a = 1
    try:
        result = a / b
        print("Success a=", result)
    except:
        print("There was an error")

divide_generic(5)   # normal
divide_generic(0)   # ZeroDivisionError

# ===== 3. Try-Except Spesifik (beda pesan per jenis error) =====
def divide_specific(b_input):
    a = 1
    try:
        b = int(b_input)
        result = a / b
        print("Success a=", result)
    except ZeroDivisionError:
        print("The number you provided can't divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")

divide_specific("5")       # sukses
divide_specific("0")       # ZeroDivisionError
divide_specific("abc")     # ValueError, "abc" bukan angka

# ===== 4. Try-Except-Else-Finally =====
def divide_full(b_input):
    a = 1
    try:
        b = int(b_input)
        a = a / b
    except ZeroDivisionError:
        print("The number you provided can't divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")
    else:
        print("success a=", a)     # cuma jalan kalau TIDAK ada exception
    finally:
        print("Processing Complete")   # SELALU jalan, error atau tidak

divide_full("5")     # sukses -> else + finally
divide_full("0")     # ZeroDivisionError -> except + finally
divide_full("abc")   # ValueError -> except + finally

import math

# ===== 5. Exercise 1: safe_divide =====
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None, dengan pesan error

# ===== 6. Exercise 2: perform_calculation (square root) =====
def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")

perform_calculation(16)     # 4.0
perform_calculation(-4)     # ValueError, akar negatif tidak valid

# ===== 7. Exercise 3: complex_calculation =====
def complex_calculation(num):
    try:
        result = num / (num - 5)
        print(f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")

complex_calculation(10)     # normal
complex_calculation(5)      # ZeroDivisionError (5-5=0), tertangkap generik
