
import random

baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
signos = ["\u2660", "\u2764", "\u2663", "\u2666"]

def repartir():
    acum = 0
    acum1 = 0
    suma11 = 0
    suma12 = 0
    suma13 = 0
    suma14 = 0
    suma3 = 0
    suma4 = 0
    continua = True
    while continua:
        letra = "I"
        while letra == "I":
            p1=random.randint(0,48) 
            p2=random.randint(0,48)
            p1c=random.randint(0,3) 
            p2c=random.randint(0,3)
            v1 = baraja[p1]
            v2 = baraja[p2]
            vs1 = signos[p1c]
            vs2 = signos[p2c]
            if ((v1 == "J" or v1 == "Q" or v1 == "K" or v1 == "A") and (v2 == "J" or v2 == "Q" or v2 == "K" or v2 == "A")): #Declara valores
                valor2 = 11
                valor1 = 11
                combina1 = str(v1) + str(vs1)
                combina2 = str(v2) + str(vs2)
                suma11 = valor1 + valor2
                print(combina1,combina2,"Puntuación: %i "% suma11)
                letra=str(input("¿Desea tomar más cartas? S/N: "))
            elif v1 == "J" or v1 == "Q" or v1 == "K" or v1 == "A":
                valor12 = 11
                combina1 = str(v1) + str(vs1)
                combina2 = str(v2) + str(vs2)
                suma12 = v2 + valor12
                print(combina1,combina2,"Puntuación: %i "% suma12)
                letra=str(input("¿Desea tomar más cartas? S/N: "))
            elif v2 == "J" or v2 == "Q" or v2 == "K" or v2 == "A":
                valor2_1 = 11
                combina1 = str(v1) + str(vs1)
                combina2 =str(v2) + str(vs2)
                suma13 = v1 + valor2_1
                print(combina1,combina2,"Puntuación: %i "% suma13)
                letra=str(input("¿Desea tomar más cartas? S/N: "))
            elif v1 <= 10 and v2 <= 10:
                combina1 = str(v1) + str(vs1)
                combina2 = str(v2) + str(vs2)
                suma14 = v1 + v2
                print(combina1,combina2,"Puntuación: %i "% suma14)
                letra=str(input("¿Desea tomar más cartas? S/N: "))
            if letra == "N" or letra == "n": 
                suma = suma11 + suma12 + suma13 + suma14
                continua = False
                print("Aquí están sus cartas: ", (combina1,combina2)) 
                print("Puntuación: %i" % suma)
                print()
                if suma == 21:
                    print("Has ganado. Sacaste 21.")
                    main()
                elif suma < 21:
                    print("No has llegado a 21, pero obtuviste buen puntaje.")
                    main()
                elif suma > 21:
                    print("Has perdido.")
                    main()
                else:
                    print("Introduzca S/N")
                    main()
            while letra == "S" or letra == "s": 
                p3=random.randint(0,48)
                p3c=random.randint(0,3)
                v3 = baraja [p3]
                vs3 = signos[p3c]
                if v3 == "J" or v3 == "Q" or v3 == "K" or v3 == "A":
                    valor3 = 11
                    vs3 = signos[p3c]
                    combina3 = str(v3) + str(vs3)
                    acum1 = acum1 + valor3
                    suma3 = suma11 + suma12 + suma13 + suma14 + acum1
                    print(combina3,"Puntuación: ", suma3)
                    letra=str(input("¿Desea tomar otra carta? S/N: "))
                elif v3 <= 10:
                    combina3 = str(v3) + str(vs3)
                    acum = acum + v3
                    suma4 = acum + suma11 + suma12 + suma13 + suma14
                    print(combina3,"Puntuación: ", suma4)
                    letra=str(input("¿Desea tomar otra carta? S/N: "))
            if letra == "N" or letra == "n": 
                suma5 = suma3 + suma4
                continua = False
                print("Aquí están sus cartas: ", (combina1,combina2,combina3))
                print("Puntuación: ", suma5)
                print()
                if suma5 == 21:
                    print("Has ganado. Llegaste a 21.")
                elif suma5 < 21:
                    print("No llegaste a 21. Obtuviste un buen puntaje")
                    letra = str(input("¿Desea jugar otra vez? S/N: "))
                elif suma5 > 21:
                    print("Has perdido.")
                    letra = str(input("¿Desea jugar otra vez? S/N: "))
                else:
                    print("Introduce S/N: ")


def menu():
    print("1. Jugar Blackjack")
    print("2. Salir")

def main():
    continua = True
    while continua:
        menu()
        opcion = int(input("Introduzca la opción que desee: "))
        if opcion == 1:
            print()
            repartir() 
            #Se llama a toda la función
        elif opcion == 2:
            print("Hasta pronto.")
            continua = False
        else:
            print("Introduzca una opción válida: ")
main()







