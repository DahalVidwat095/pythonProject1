'''N students take K apples and distribute them among each other evenly .The remaining (the undivisible)
part remains in the basket.How many apples will each single student get?How many apples will remain in the basket?
The program reads the numbers N and K.It should print the two answers for the questions above.'''
N=int(input("enter the  number of students:"))
K=int(input("enter the number of apples:"))
get=K//N
remain=K%N
print(f"The number of apples each student gets is {get}.")
print(f"The number of remaining apples is {remain}.")