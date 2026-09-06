
prices = {"apple":12, "banana":7, "cherry":25}
print(prices)

key = input("which fruit? ")

try:
    print(prices[key])
except KeyError:
    print(f"{key} not exist!")

