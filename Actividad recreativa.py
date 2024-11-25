print("Hola bienvenido al programa ")
opcion=1
while opcion!=0:

    print("Ingresar 1. Area triangulo")
    print("Ingresar 2. Area rectangulo ")
    print("Ingresar 3. Area circulo ")
    print("Ingresar 4. Convertir temperatura °F a °C ")
    print("Ingresar 5. Convertir temperatura °C a °F ")
    print("Ingresar 0. Salir del programa ")
    op=int(input("¿Que actividad quieres realizar?"))
    if (op==1):
     num1=int(input("Ingresa la base del triangulo "))
     num2=int(input("Ingresa la altura del triangulo "))
     res=num1*num2/2
     print("El area del triangulo es :", res )
    elif(op==2):
        num1=int(input("Ingresar la base del rectangulo "))
        num2=int(input("Ingresar la altura del rectangulo "))
        res=num1*num2
        print("El area del rectangulo es :", res)
    elif(op==3):
        num1=int(input("Ingresar el radio del circulo "))
        res=num1*num1*3.1416
        print("El area del circulo es :", res)
    elif(op==4):
       num1=int(input("¿Que grados fahrenheit quieres convertir?"))
       gradosf=(num1-32)*5/9
       print("tus grados fahremheit son:", gradosf, "en celsius")
    elif(op==5):
       num1=int(input("¿Que grados celsius quieres convertir?"))
       gradosc=(num1*9/5)+32
       print("tus grados celsius son:", gradosc, "en fahremheit")