n = int(input("Enter N: "))

a = 0                  
b = 1                  
forward_text = ""      
reversed_text = ""   
even_sum = 0

for i in range(n):
    if forward_text == "":
        forward_text = str(a)
    else:
        forward_text = forward_text + ", " + str(a)


    if reversed_text == "":
        reversed_text = str(a)
    else:
        reversed_text = str(a) + ", " + reversed_text


    if a % 2 == 0:
        even_sum += a


    next_number = a + b
    a = b
    b = next_number

print("Sequence:", forward_text)
print("Even Sum:", even_sum)
print("Reversed:", reversed_text)
