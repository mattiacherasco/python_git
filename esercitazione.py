import turtle
import random
import time

def nord(alice):
    alice.setheading(90)
    return alice.forward(10)

def sud(alice):
    alice.setheading(270)
    return alice.forward(10)

def est(alice):
    alice.setheading(0)
    return alice.forward(10)

def ovest(alice):
    alice.setheading(180)
    return alice.forward(10)

def main():
    finestra = turtle.Screen()
    alice = turtle.Turtle()

    dizionario = {"S" : sud, "N" : nord, "E" : est, "O" : ovest}
    possibiliCaratteri = ['S', 'N', 'E', 'O']
    listaCordinate = []
    listaCordinateDoppie = []

    durataCiclo = 60
    alice.goto(0,0)
    for k in range(durataCiclo):
        cordinate = alice.pos()
        direzione = random.choice(possibiliCaratteri)
        dizionario[direzione](alice)
        time.sleep(1)

        if cordinate in listaCordinate:
            if not cordinate in listaCordinateDoppie: 
                listaCordinateDoppie.append(cordinate)
        
        listaCordinate.append(cordinate)

    with open("esercitazione.txt", "a") as file:
        file.write(str(listaCordinate))

    print(str(listaCordinate))
    print("Cordinate doppie: ")
    print(str(listaCordinateDoppie))
    
if __name__ == "__main__":
    main()