print("Sequencia de fibonacci")

n = int(input("Quantos termos voce quer mostrar: "))
t1 = 0
t2 = 1
print((t1, t2))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1

print("FIM")
