

"""This program writes a greeting and a recipient of your choice."""
"""Then you can set the number of times greeting repeats itself."""

print("Enter a greeting")
greeting = input()
print("Enter a recipient")
recipient = input()
print("How many times to repeat")
number = int(input())
sum = (greeting + " " + recipient + "! ")
print(sum * number)
