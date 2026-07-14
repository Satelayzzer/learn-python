num = 10

# ==, !=, >, <, >=, <=
if num > 0 and num < 100:
    print("The number is positive.")
    if num == 100:
        print("The number is 100.")
elif num == 40:
    print("The number is 40.")
elif num == 20:
    print("The number is 20.")
elif num < 4:
    print("The number is less than 4.")
else:
    print("The number is not positive.")

#bool

isTrue = True 
if not isTrue:
    print("This statement is true.")