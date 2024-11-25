equipo=["angy", "MARIO", "CARLOS"]
integrantes=int(input("¿cuantos integrantes mas va a ingresar?"))
for i in (range(integrantes)):
    integrantes=input("ingresa nombres: ")
    equipo.append(integrantes)
    print(equipo)