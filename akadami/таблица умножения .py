# таблица умножения
n = int(input())
for i in range(1, n + 1): #перебираем первый множитель i от 1 до n
    for j in range(1, n + 1): # перебираем второй множитель j от 1 до n
        print(f"{i}x{j}={(i * j):2} ", end="")
    print() #чтоб выод был в столбик