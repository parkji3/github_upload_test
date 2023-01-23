num_integers = int(input("How many integers would you like to enter?\n"))
print("Please enter", num_integers, "integers.")

# take the first integer as initial value for min and max
min_num = int(input())
max_num = min_num

# loop through the rest of the integers
for i in range(1,num_integers):
    integer = int(input())
    # compare the integer with min and max, and update if needed
    if integer > max_num:
        max_num = integer
    if integer < min_num:
        min_num = integer

print("min:", min_num)
print("max:", max_num)