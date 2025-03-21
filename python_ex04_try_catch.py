# -*- coding: utf-8 -*-
"""python_ex04_try-catch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zs3y3SLjdz72bQNF2M3AvX5TPZFsInvx

https://www.w3schools.com/python/python_try_except.asp

**Ex 1. *try* - *catch***
"""

def sum_digits(s: str) -> int:
  d_sum = 0
  for ch in s:
    try:
      d_sum += int(ch)
    except:
      print(f'{ch} is not a digit')
  return d_sum

print(f'Result equals {sum_digits(input())}')

"""**Ex 2. *try* - *catch* - *else***"""

def reminder(a: int, b: int) -> int:
    try:
        result = a % b
    except ZeroDivisionError:
        print("Division by zero ")
    else:
        print(f'Reminder equals {result}')

reminder(5, 2)
reminder(10, 0)

"""**Ex 3. *except***"""

try:
  a = int(input("Enter 1st number: "))
  b = int(input("Enter 2nd number: "))
  print(f'Result of a/b = {a/b}')
except ZeroDivisionError:
  print("Error. Zero division")
except ValueError:
  print("Error. At least one of the arguments is not a number")
except:
  print("Unknown error")

try:
  a = int(input("Enter 1st number: "))
  b = int(input("Enter 2nd number: "))
  print(f'Result of a/b = {a/b}')
except Exception as e:
  print(f'Error: {e}')

def sum_digits(s):
  d_sum = 0
  for ch in s:
    try:
      d_sum += int(ch)
    except:
     raise ValueError(f'{ch} is not a digit')
  return d_sum

print(f'Result equals {sum_digits(input())}')

"""**Ex 4. *try* - *except* - *finally***"""

try:
  raise ValueError("Incorrect value")
except ValueError:
  print("Handling ValueError")
finally:
  print("Finally is executed")

try:
  raise ValueError("Incorrect value")
except ValueError:
  print("Handling ValueError")
  raise Exception("This is the end")

print("Finally is executed")

try:
  raise ValueError("Incorrect value")
except ValueError:
  print("Handling ValueError")
  raise Exception("This is the end")
finally:
  print("Finally is executed")

try:
  raise ValueError("Incorrect value")
except ValueError:
  print("Handling ValueError")
  exit()
finally:
  print("Finally is executed")

"""**Ex 5. *finally* inside a function**"""

def add_one(val: int) -> int:
  try:
    val += 1
    return val
  except ValueError:
    print("Input is not an integer")
    return "Not an int"
  finally:
    return 0

print(add_one(5))

"""**Ex 6. *assert***"""

def sum_digits(s: str) ->int:
  assert len(s) != 0, "No input data"
  d_sum = 0
  for ch in s:
    try:
      d_sum += int(ch)
    except:
      print(f'{ch} is not a digit')
  return d_sum

print(f'Result equals {sum_digits(input())}')

def save_bigger(list_1, list_2):
  assert len(list_1) != 0 and len(list_2) != 0, "At least one of the lists is empty"
  assert len(list_1) == len(list_2), "Lists have different sizes"
  for i in range(len(list_1)):
   try:
    if list_1[i] < list_2[i]:
      list_1[i] = list_2[i]
   except:
    raise ValueError("Co najmniej 1 z elementów nie jest liczbą")

list_1 = [5,10]
list_2 = [4,0,1]
save_bigger(list_1,list_2)
print(list_1)