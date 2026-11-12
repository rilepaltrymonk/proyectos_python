personas = [
    {'nombre': 'Emilio', 'edad': 32},
    {'nombre': 'Norma', 'edad': 32},
    {'nombre': 'Sharon', 'edad': 35}
]

personas.append({'nombre': 'Santiago', 'edad': 10})

for persona in personas: 
    print(persona)

for persona in personas: 
    print(persona['nombre'], persona['edad'])

for i, persona in enumerate(personas, start=1):
    print(i, persona['nombre'])