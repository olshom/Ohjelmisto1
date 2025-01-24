import random
code_of_3=[]
for i in range(3):
    code_of_3.append(random.randint(1, 9))
code_of_4=[]
for i in range(4):
    code_of_4.append(random.randint(1, 6))
print("3-digit code with numbers between 0 and 9: ", end="")
for e in code_of_3:
    print(e, end="")
print("")
print("4-digit code with numbers between 0 and 6: ", end="")
for e in code_of_4:
    print(e, end="")

