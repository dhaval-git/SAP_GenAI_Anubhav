from datetime import datetime


#Scalar variable - store single value

#Integer variable - store whole number
#Converting to integer using int() function, as input() function returns a string by default
age = int(input("Enter your age: "))

#string variable - store text
name = "Dhaval Patel"

#float variable - store decimal number
height = 5.9

#boolean variable - store True or False
is_adult = True

# #Display the values of the variables
# print("Name:", name, " is of type:", type(name))
# print("Age:", age, " is of type:", type(age))
# print("Height:", height, " is of type:", type(height))
# print("Is Adult:", is_adult, " is of type:", type(is_adult))

# #Type conversion
# age_str = "35"  # Convert integer to string
# print("Age as string:", age_str, " is of type:", type(age_str))

# age_int = int(age_str)  # Convert string to integer
# print("Age as integer:", age_int, " is of type:", type(age_int))


# #Convert Float to String
# height_str = str(height)
# print("Height as string:", height_str, " is of type:", type(height_str))

# #Convert String to Float
# height_float = float(height_str)
# print("Height as float:", height_float, " is of type:", type(height_float))


# #Convert Integer to Float
# age_float = float(age)
# print("Age as float:", age_float, " is of type:", type(age_float))


# #Convert Float to Integer
# height_int = int(height_float)
# print("Height as integer:", height_int, " is of type:", type(height_int))


# #Convert Boolean to String
# is_adult_str = str(is_adult)
# print("Is Adult as string:", is_adult_str, " is of type:", type(is_adult_str))

# #Convert String to Boolean
# is_adult_bool = bool(is_adult_str)
# print("Is Adult as boolean:", is_adult_bool, " is of type:", type(is_adult_bool))


#Simple if condition to check if the person is an adult
if age > 18:
    # print(name, "is an adult.")
    #Way to print using f-string, it makes easier to format the string and include variables    
    print(f"{name} with height {height} is an adult as of {datetime.now()} ")
elif age == 18:
    print(name, "has just made to an adult.")
else:
    print(name, "is not an adult.")




