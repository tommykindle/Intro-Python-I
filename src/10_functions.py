# Write a function is_even that will return true if the passed-in number is even.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num):
    print('Even!')
else:
    print('Odd')
