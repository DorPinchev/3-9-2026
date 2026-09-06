

fruits = ["apple", "banana"]

try:
    fruits.remove("orange")
except ValueError as e:
    print(f"orange is not on the list, {e}")


print(fruits)