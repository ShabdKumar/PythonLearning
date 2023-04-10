# Numbers: (int & float)

print(type(2 + 4))  # <class 'int'>     6
print(type(2 - 4))  # <class 'int'>     -2
print(type(2 * 4))  # <class 'int'>     8
print(type(2 / 4))  # <class 'float'>   0.5

print(type(0.0001)) # <class 'float'>
print(type(0))      # <class 'int'>
print(type(20 + 1.1))   # <class 'float'>   21.1
print(type(9.9 + 1.1))  # <class 'float'>   11.0

print(2 ** 3)   # 8 (Power)
print(2 // 4)   # 0
print(6 // 4)   # 1 (Quotient)
print(6 / 4)    # 1.5
print(6 % 4)    # 2 (Remainder)

#------------------------------------------------
# Math Function: (https://www.programiz.com/python-programming/modules/math)

print(round(3.9))   # 4 (Rounding Any Number)
print(abs(-20))     # 20 (Absolute Value)

#---------------------------------------------
# Operator Precedence:

# ()
# **
# * /
# + -

print(20 - 3  * 4)      # 8
print((20 - 3) + 2 ** 2)    # 21

#----------------------------------
# bin(), int() functions & Complex Numbers (complex): (https://www.geeksforgeeks.org/python-int-function/)

print(bin(5))       # 0b101 (Binary Representation)
print(oct(37))      # 0o45  (Octal Represenatation)
print(hex(69))      # 0x45  (Hexa Decimal Representation)
print(int('0b101', 2))      # 5
print(int('0o45', 8))       # 37
print(int('0x45', 16))      # 69
print(3+4j)     # (3+4j)

#-------------------------------
# Variables:

iq = 190
user_iq = 200
print(iq)       # 190
print(user_iq)  # 200

iq = 400
user_iq = iq // 4
a = user_iq / 2
print(iq)       # 400
print(user_iq)  # 100
print(a)        # 50.0

PI = 3.14       # (Constants = We can change the value but it will be better not to change it)

a,b,c = 1,2,3
print(a,b,c)    # 1 2 3

#-----------------------
# Augmented Assigment Operator

number = 10
number += 5     # (number = number + 5)
print(number)       # 15

#--------------------------------------
# Strings (str):

short_string = 'supercool'
long_string = "Hi! How are you?"
multi_line_string = '''WOW
0 0
---'''
print(short_string)     # supercool
print(long_string)      # Hi! How are you?
print(multi_line_string)    # WOW
                            # 0 0
                            # ---

#-----------------------------------------
# String Concatenation:

first_name = 'Shabd'
last_name = 'Kumar'
full_name = first_name + ' ' + last_name
print(full_name)        # Shabd Kumar

#----------------------------------------
# Type Conversion:

a = 100
b = str(a)
c = int(b)
print(type(a))      # <class 'int'>
print(type(b))      # <class 'str'>
print(type(c))      # <class 'int'>

#------------------------------------
# Escape Sequence:

weather = "It\'s a \"kind of\" sunny"
print(weather)      # It's a "kind of" sunny

greetings = "Hey!\tIt\'s a \"kind of\" sunny \n hope you have a good day."
print(greetings)        # Hey!    It's a "kind of" sunny
                        # hope you have a good day

#-------------------------------------------------------------------------
# Formatted Strings:

name = 'Shabd Kumar'
age = 28

print("Hi! " + name + ". You are " + str(age) + " years old.")                      # Hi! Shabd Kumar. You are 28 years old.
print(f"Hi! {name}. You are {age} years old.")                                      # Hi! Shabd Kumar. You are 28 years old. (Python-3)
print("Hi! {}. You are {} years old.".format('Kumar Akash', '25'))                  # Hi! Kumar Akash. You are 25 years old. (Python-2)
print("Hi! {}. You are {} years old.".format(name, age))                            # Hi! Shabd Kumar. You are 28 years old.
print("Hi! {1}. You are {2} years old.".format(name, age, "bye"))                   # Hi! 28. You are bye years old.
print("Hi! {name}. You are {age} years old.".format(name='Ganpat Gandhi', age=38))  # Hi! Ganpat Gandhi. You are 38 years old.
print("Hi! {0}. You are {age} years old.".format(name, age=30))                     # Hi! Shabd Kumar. You are 30 years old.