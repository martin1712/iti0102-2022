

"""A programm that counts how many coins are included in the number you enter."""

amount = int(input("Enter a sum: "))
fifty = (amount // 50)
a = amount - 50 * fifty
twenty = (a // 20)
b = a - 20 * twenty
ten = (b // 10)
c = b - 10 * ten
five = (c // 5)
d = c - 5 * five
one = (d // 1)
e = d - 1 * one
coins = fifty + twenty + ten + five + one
print(f"Amount of coins needed: {coins}")
