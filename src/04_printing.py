"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("%d"%(x))
print("%.2f"%(y))
print("%s"%(z))

# Use the 'format' string method to print the same thing
print(format(x, 'd'))
print(format(y, '.2f'))
print(format(z,'s'))

# Finally, print the same thing using an f-string
print(f"{x:d}")
print(f"{y:.2f}")
print(f"{z:s}")