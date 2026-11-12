frutas = ['Mango', 'Fresas', 'Uvas']

print(frutas)

frutas.append('Platano')

print(frutas)
print(frutas[-1])

frutas.remove('Platano')
print(frutas)

frutas.pop(0)
print(frutas)

print(len(frutas))

for fruta in frutas:
    print(fruta)