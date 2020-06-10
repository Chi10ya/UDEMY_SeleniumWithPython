# 19 - Working with strings

a = "This is a simple string"
b = "Using single Quotes"
c = "Chaitanya's family"
d = 'Chaitanya family "Ambica", "Yashvir", "Dhiyanshi"'
e = 'Chaitanya\'s family "Ambica", "Yashvir", "Dhiyanshi"'
f = """ Hi this is Chaitanya
my family memebers are 
Ambica
Yashvir
Dhiyanshi
"""

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 20 - String methods - Part 1
# Accessing characters in a string ==> len(), lower(), upper(), str()

first = "nyc"
second = "abc"[0]
print(first)
print(second)
print(len(first))
print(first[1])
print(first.upper())
print(str(second))
print(first[1] + second)
print(first +' '+ second)

# 21: Sting methods - Part 2

a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABCD'))

b = "1abc2abc3abc4abc"
print(b.replace('abc', 'ABCD', 1))
print(b[1:4]) # Starting index is inclusive and Ending Index is exclusive.
print(b[:3])
print(b[1:])
print('*'*20)
print(b[1:6:3]) # Stepping


# 22: More String slicing and Indexing.

print('-'*20)
print(b[:])
print(b[4:])
print(b[-3])
print(b[:-2])
print(b[::2])
print(b[::-1])

# 23: String Formating

city = 'Ireland'
event = 'Lecture Show'

print("Welcome to "+city+" and enjoy the "+ event)
print("Welcome to %s" %city)
# print("Welcome to %s" %city% "and enjoy the %s" %event) # You cannot give like this
print("Welcome to %s and enjoy the %s" %(city, event))
print(f"Welcome to {city} and enjoy the {event}")

