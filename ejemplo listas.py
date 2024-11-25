print("holiii")

deportes=["futbol","voleibol","natacion","basquetbol"]

print(deportes)

print(deportes[1])

#posicion de natacion
pos=deportes.index("natacion")
print("la posicion de natacion es:",pos)
print(deportes.index("natacion"))

#agregar otro deporte
deportes.append("hanball")

print(deportes)

#agregar otro deporte en una posicion espesifica
deportes.insert(5,"tenis")
print(deportes)

cantidad_saludos=int(input("cunatos saludos quieres?"))
for i in range(cantidad_saludos):
    print("hola")

num_deportes=int(input("cuantos deportes quieres agregar?"))
for i in (range(num_deportes)):
    dep=input("ingresa deporte ")
    deportes.append(dep)
    