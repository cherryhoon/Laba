A = {1: "Яблочко", 2: "Груша"}
B = {a: b for b, a in A.items()}
print('Изначально:',A)
print('Обратный:',B)