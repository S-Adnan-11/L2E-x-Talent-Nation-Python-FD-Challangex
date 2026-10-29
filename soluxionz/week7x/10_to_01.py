number = int(input("Enter a positive integer: "))

if number < 0:
    print("we said, enter a postive integer!")

if number == 0:
    binary = "0"
else:
    binary = ""
    while number > 0:
        remainder = number % 2        
        binary = str(remainder) + binary     
        number = number // 2                 

print(binary)
