numbers = [1,2,3,4,5, 6, 7, 8, 9]
animals = ["cat", "dog", "horse", "mouse"]




# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return multiply_list(l[0:len(l)-1]) * l[len(l)-1]

print multiply_list(numbers)

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        return count_list(l[0:len(l)-1]) + 1

print count_list(numbers)

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return sum_list(l[0:len(l)-1]) + l[len(l)-1]

print sum_list(numbers)

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:
        last = l.pop()
        return [last] + reverse(l)

print reverse(numbers)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print fibonacci(2)
print fibonacci(7)



# Finds the item i in the list l.... RECURSIVELY     BETTER
def find(l, i):
    if len(l) == 0:
        return False
    if l[-1] == i:
        return len(l) - 1
    else:
        l.pop()
        return find(l,i)

print find(animals,"dog")
    
# Determines if a string is a palindrome
def palindrome(some_string):
    some_string = list(some_string)
    if len(some_string) == 1:
        return True
    elif len(some_string) == 0:
        return True
    else:
        if some_string.pop(0) == some_string.pop():
            return palindrome(some_string)
        else:
            return False

print palindrome("abba")

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final
# dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    else:
        if width > height:
            width = width/2
        else:
            height = height/2
        folds -= 1
        return fold_paper(width,height,folds)

print fold_paper(10,6,3)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if target <= 0:
        return target
    else:
        count = target
        print count_up(target - n, n)
        return count


print count_up(20, 4)
