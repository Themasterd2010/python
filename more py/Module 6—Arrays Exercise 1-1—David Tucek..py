#Design the logic for a program that allows a user to enter 20 numbers,
#then displays them in the reverse order of entry.

count = 0
numbers = []
while count < 20:
    number = input("Enter a number: ")
    numbers.append(number)
    count += 1


for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])