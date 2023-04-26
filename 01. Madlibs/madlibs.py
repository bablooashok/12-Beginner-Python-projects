#String concatenation
#if we want to create a string that says "Hi, I am _____"
name = input("Name: ")
age = input("Age: ")
location = input("Location: ")

#few ways to this is
print("Hi, I am " + name)
print("Hi, I am {}".format(name))
print(f"Hi, I am {name}")


madlib = f"Hi, I am {name}. my age is {age}.\
 I live in {location}."

print(madlib)