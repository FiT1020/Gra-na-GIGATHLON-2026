import turtle
import random

KROKI_ZROBIONE=0

for i in range(60):
    print("-", end="")
print()
print("          WITAMY W GRZE KURIER W PYTHONLANDZIE!        ")
for i in range(60):
    print("-", end="")
print()
print("Twoim dzisiejszym zadaniem jest zbieranie utraconych przez naszego")
print("kuriera fajtłapę paczek. Niestety zadanie nie jest proste albowiem masz")
print("ograniczoną liczbę kroków i paliwo w odrzutowym zółwiu, które sam ustalasz.")
print("Poza tym, aby nie było tak łatwo na swojej drodze znajdziesz także przeszkody")
print("i wspomagacze. Uderzenie lub przejście przez czerwoną oponę zabiera ci")
print("10 jednostek paliwa i 4 kroki. Natomiast przejście przez niebieski trójkąt daje ci")
print("dodatkowe 40 jednostek paliwa i 13 kroków. Paczki są przedstawione jako pomarańczowe")
print("kwadraty i dają one +20 do wyniku. Jeśli wyjdziesz za białą granicę, to zostaniesz ")
print("cofnięty do środka pola z obiektami. Z zasad to tyle. POWODZENIA!")
for i in range(60):
    print("-", end="")
print()
print("Początkowe pytanka:")
NAZWA=input("Jak się nazywasz :")
print(f"Witaj, kurier {NAZWA}, teraz ustalimy początkowe wartości:")
PALIWO=int(input("Podaj początkową ilość paliwa od 400 do 900 : "))
if PALIWO < 400:
    PALIWO = 400
if PALIWO > 900:
    PALIWO = 900
KROKI=int(input("Podaj początkową ilość kroków od 150 do 350 : "))
if KROKI < 150:
    KROKI = 150
if KROKI > 350:
    KROKI = 350
l_paczek=int(input("Podaj początkową ilość paczek od 1 do 5 : "))
if l_paczek < 1:
    l_paczek = 1
if l_paczek > 5:
    l_paczek = 5
opon=int(input("Podaj początkową ilość opon od 1 do 10 : "))
if opon < 1:
    opon = 1
if opon > 10:
    opon = 10
wspomagacz=int(input("Podaj początkową ilość wspomagaczy od 1 do 5 : "))
if wspomagacz < 1:
    wspomagacz = 1
if wspomagacz > 5:
    wspomagacz = 5
xpocz=int(input("Podaj współrzędną x od -240 do 240: "))
if xpocz < -240:
    xpocz = -240
if xpocz > 240:
    xpocz = 240
ypocz=int(input("Podaj współrzędną y od -240 do 240: "))
if ypocz < -240:
    ypocz = -240
if ypocz > 240:
    ypocz = 240
kierunek=int(input("Podaj kierunek początkowy od 0 do 360: "))
if kierunek < 0:
    kierunek = 0
if kierunek > 360:
    kierunek = 360
cel=int(input("Jaki procent paczek chcesz zebrać od 0 do 100:"))
if cel < 0:
    cel = 0
if cel > 100:
    cel = 100
poczpal=PALIWO
poczkrok=KROKI
zboje=0
drogowe=0

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Kurier w Pythonlandzie")
wn.tracer()

score=0

postac=turtle.Turtle()
postac.speed(0)
postac.shape("turtle")
postac.color("green")
postac.penup()
postac.goto(xpocz, ypocz)
postac.setheading(kierunek)
postac.pendown()

#postac do linii:
linia=turtle.Turtle()
linia.speed(0)
linia.penup()
linia.hideturtle()
linia.color("white")
linia.goto(-250, 250)
linia.pendown()
linia.goto(250, 250)
linia.goto(250, -250)
linia.goto(-250, -250)
linia.goto(-250, 250)
linia.penup()

#postac do pisania:
pisak=turtle.Turtle()
pisak.speed(0)
pisak.penup()
pisak.color("white")
pisak.hideturtle()
pisak.goto(-15, 270)
pisak.clear()
pisak.write(f"Wynik: {score}, Kroki: {KROKI}, Paliwo: {PALIWO}, X: {postac.xcor()} , Y: {postac.ycor()}", align="center", font=("Arial", 28, "normal"))
pisak.penup()

#paczki:
pacz1=turtle.Turtle()
pacz1.speed(0)
pacz1.penup()
pacz1.color("orange")
pacz1.shape("square")
pacz1.shapesize()
pacz1.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if l_paczek>1:
    pacz2=turtle.Turtle()
    pacz2.speed(0)
    pacz2.penup()
    pacz2.color("orange")
    pacz2.shape("square")
    pacz2.shapesize()
    pacz2.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if l_paczek>2:
    pacz3=turtle.Turtle()
    pacz3.speed(0)
    pacz3.penup()
    pacz3.color("orange")
    pacz3.shape("square")
    pacz3.shapesize()
    pacz3.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if l_paczek>3:
    pacz4=turtle.Turtle()
    pacz4.speed(0)
    pacz4.penup()
    pacz4.color("orange")
    pacz4.shape("square")
    pacz4.shapesize()
    pacz4.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if l_paczek>4:
    pacz5=turtle.Turtle()
    pacz5.speed(0)
    pacz5.penup()
    pacz5.color("orange")
    pacz5.shape("square")
    pacz5.shapesize()
    pacz5.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

#opony:
op1=turtle.Turtle()
op1.speed(0)
op1.penup()
op1.color("red")
op1.shape("circle")
op1.shapesize()
op1.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if opon>1:
    op2 = turtle.Turtle()
    op2.speed(0)
    op2.penup()
    op2.color("red")
    op2.shape("circle")
    op2.shapesize()
    op2.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>2:
    op3 = turtle.Turtle()
    op3.speed(0)
    op3.penup()
    op3.color("red")
    op3.shape("circle")
    op3.shapesize()
    op3.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>3:
    op4 = turtle.Turtle()
    op4.speed(0)
    op4.penup()
    op4.color("red")
    op4.shape("circle")
    op4.shapesize()
    op4.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>4:
    op5 = turtle.Turtle()
    op5.speed(0)
    op5.penup()
    op5.color("red")
    op5.shape("circle")
    op5.shapesize()
    op5.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>5:
    op6 = turtle.Turtle()
    op6.speed(0)
    op6.penup()
    op6.color("red")
    op6.shape("circle")
    op6.shapesize()
    op6.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>6:
    op7 = turtle.Turtle()
    op7.speed(0)
    op7.penup()
    op7.color("red")
    op7.shape("circle")
    op7.shapesize()
    op7.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>7:
    op8 = turtle.Turtle()
    op8.speed(0)
    op8.penup()
    op8.color("red")
    op8.shape("circle")
    op8.shapesize()
    op8.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>8:
    op9 = turtle.Turtle()
    op9.speed(0)
    op9.penup()
    op9.color("red")
    op9.shape("circle")
    op9.shapesize()
    op9.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if opon>9:
    op10 = turtle.Turtle()
    op10.speed(0)
    op10.penup()
    op10.color("red")
    op10.shape("circle")
    op10.shapesize()
    op10.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

#wspomagacze:
wsp1=turtle.Turtle()
wsp1.speed(0)
wsp1.penup()
wsp1.color("blue")
wsp1.shape("triangle")
wsp1.shapesize()
wsp1.goto(random.randint(-48,48)*5, random.randint(-48,48)*5)

if wspomagacz>1:
    wsp2 = turtle.Turtle()
    wsp2.speed(0)
    wsp2.penup()
    wsp2.color("blue")
    wsp2.shape("triangle")
    wsp2.shapesize()
    wsp2.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if wspomagacz>2:
    wsp3 = turtle.Turtle()
    wsp3.speed(0)
    wsp3.penup()
    wsp3.color("blue")
    wsp3.shape("triangle")
    wsp3.shapesize()
    wsp3.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if wspomagacz>3:
    wsp4 = turtle.Turtle()
    wsp4.speed(0)
    wsp4.penup()
    wsp4.color("blue")
    wsp4.shape("triangle")
    wsp4.shapesize()
    wsp4.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

if wspomagacz>4:
    wsp5 = turtle.Turtle()
    wsp5.speed(0)
    wsp5.penup()
    wsp5.color("blue")
    wsp5.shape("triangle")
    wsp5.shapesize()
    wsp5.goto(random.randint(-48, 48) * 5, random.randint(-48, 48) * 5)

dotkop=0
zebrwsp=0

def aktualizacja_wypisu():
    global score, KROKI, PALIWO

    pisak.clear()
    pisak.write(f"Wynik: {score}, Kroki: {KROKI}, Paliwo: {PALIWO}, X: {postac.xcor()} , Y: {postac.ycor()}", align="center", font=("Arial", 28, "normal"))
    pisak.penup()


def wgore():
    global PALIWO, KROKI, score, KROKI_ZROBIONE, dotkop, zebrwsp, zboje, drogowe
    postac.setheading(90)
    KROKI_ZROBIONE+=1
    print(f"Krok: {KROKI_ZROBIONE}, \nWspółrzędna x przed ruchem: {postac.xcor()} \nWspółrzędna y przed ruchem: {postac.ycor()} \nIlość paliwa przed krokiem: {PALIWO} \nPozostała ilość kroków przed ruchem: {KROKI} \nWynik przed krokiem: {score} \nZrobiono krok w górę")
    postac.goto(postac.xcor(), postac.ycor()+5)
    if postac.xcor()>240 or postac.xcor()<-240 or postac.ycor()>240 or postac.ycor()<-240:
        postac.goto(0,0)
    print(f"Współrzędna x po kroku: {postac.xcor()} \nWspółrzędna y po kroku: {postac.ycor()}")
    if postac.distance(pacz1) < 10:
        score += 20
        pacz1.hideturtle()
        pacz1.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 1 and postac.distance(pacz2) < 10:
        score += 20
        pacz2.hideturtle()
        pacz2.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 2 and postac.distance(pacz3) < 10:
        score += 20
        pacz3.hideturtle()
        pacz3.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 3 and postac.distance(pacz4) < 10:
        score += 20
        pacz4.hideturtle()
        pacz4.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 4 and postac.distance(pacz5) < 10:
        score += 20
        pacz5.hideturtle()
        pacz5.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if postac.distance(op1) < 10:
        op1.hideturtle()
        op1.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop+=1
    if opon > 1 and postac.distance(op2) < 10:
        op2.hideturtle()
        op2.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 2 and postac.distance(op3) < 10:
        op3.hideturtle()
        op3.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 3 and postac.distance(op4) < 10:
        op4.hideturtle()
        op4.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 4 and postac.distance(op5) < 10:
        op5.hideturtle()
        op5.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 5 and postac.distance(op6) < 10:
        op6.hideturtle()
        op6.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 6 and postac.distance(op7) < 10:
        op7.hideturtle()
        op7.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 7 and postac.distance(op8) < 10:
        op8.hideturtle()
        op8.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 8 and postac.distance(op9) < 10:
        op9.hideturtle()
        op9.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 9 and postac.distance(op10) < 10:
        op10.hideturtle()
        op10.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if postac.distance(wsp1) < 10:
        wsp1.hideturtle()
        wsp1.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 1 and postac.distance(wsp2) < 10:
        wsp2.hideturtle()
        wsp2.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 2 and postac.distance(wsp3) < 10:
        wsp3.hideturtle()
        wsp3.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 3 and postac.distance(wsp4) < 10:
        wsp4.hideturtle()
        wsp4.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 4 and postac.distance(wsp5) < 10:
        wsp5.hideturtle()
        wsp5.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    PALIWO -= 3
    KROKI -= 1
    if random.randint(1,100)==1:
        PALIWO -=25
        print("NAGŁE ZDARZENIE: napadli na ciebie zbóje drogowi i zabrali Ci paliwo - 25 paliwa")
        zboje+=1
    if random.randint(1,120)==1:
        KROKI -=5
        print("NAGŁE ZDARZENIE: prace drogowe, trzeba wybrać objazdówkę -5 kroków")
        drogowe+=1
    print(f"Ilość paliwa po kroku: {PALIWO} \nPozostała ilość kroków po kroku: {KROKI} \nWynik po kroku: {score}")
    print()
    aktualizacja_wypisu()

def wdol():
    global PALIWO, KROKI, score, KROKI_ZROBIONE, zebrwsp, dotkop, zboje, drogowe
    postac.setheading(270)
    KROKI_ZROBIONE += 1
    print(f"Krok: {KROKI_ZROBIONE}, \nWspółrzędna x przed ruchem: {postac.xcor()} \nWspółrzędna y przed ruchem: {postac.ycor()} \nIlość paliwa przed krokiem: {PALIWO} \nPozostała ilość kroków przed ruchem: {KROKI} \nWynik przed krokiem: {score} \nZrobiono krok w dół")
    postac.goto(postac.xcor(), postac.ycor() - 5)
    if postac.xcor() > 240 or postac.xcor() < -240 or postac.ycor() > 240 or postac.ycor() < -240:
        postac.goto(0, 0)
    print(f"Współrzędna x po kroku: {postac.xcor()} \nWspółrzędna y po kroku: {postac.ycor()}")
    if postac.distance(pacz1) < 10:
        score += 20
        pacz1.hideturtle()
        pacz1.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 1 and postac.distance(pacz2) < 10:
        score += 20
        pacz2.hideturtle()
        pacz2.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 2 and postac.distance(pacz3) < 10:
        score += 20
        pacz3.hideturtle()
        pacz3.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 3 and postac.distance(pacz4) < 10:
        score += 20
        pacz4.hideturtle()
        pacz4.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 4 and postac.distance(pacz5) < 10:
        score += 20
        pacz5.hideturtle()
        pacz5.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if postac.distance(op1) < 10:
        op1.hideturtle()
        op1.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 1 and postac.distance(op2) < 10:
        op2.hideturtle()
        op2.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 2 and postac.distance(op3) < 10:
        op3.hideturtle()
        op3.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 3 and postac.distance(op4) < 10:
        op4.hideturtle()
        op4.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 4 and postac.distance(op5) < 10:
        op5.hideturtle()
        op5.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 5 and postac.distance(op6) < 10:
        op6.hideturtle()
        op6.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 6 and postac.distance(op7) < 10:
        op7.hideturtle()
        op7.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 7 and postac.distance(op8) < 10:
        op8.hideturtle()
        op8.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 8 and postac.distance(op9) < 10:
        op9.hideturtle()
        op9.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 9 and postac.distance(op10) < 10:
        op10.hideturtle()
        op10.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if postac.distance(wsp1) < 10:
        wsp1.hideturtle()
        wsp1.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 1 and postac.distance(wsp2) < 10:
        wsp2.hideturtle()
        wsp2.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 2 and postac.distance(wsp3) < 10:
        wsp3.hideturtle()
        wsp3.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 3 and postac.distance(wsp4) < 10:
        wsp4.hideturtle()
        wsp4.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 4 and postac.distance(wsp5) < 10:
        wsp5.hideturtle()
        wsp5.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    PALIWO -= 3
    KROKI -= 1
    if random.randint(1,100)==1:
        PALIWO -=25
        print("NAGŁE ZDARZENIE: napadli na ciebie zbóje drogowi i zabrali Ci paliwo - 25 paliwa")
        zboje+=1
    if random.randint(1,120)==1:
        KROKI -=5
        print("NAGŁE ZDARZENIE: prace drogowe, trzeba wybrać objazdówkę -5 kroków")
        drogowe+=1
    print(f"Ilość paliwa po kroku: {PALIWO} \nPozostała ilość kroków po kroku: {KROKI} \nWynik po kroku: {score}")
    print()
    aktualizacja_wypisu()

def wprawo():
    global PALIWO, KROKI, score, KROKI_ZROBIONE, zebrwsp, dotkop, zboje, drogowe
    postac.setheading(0)
    KROKI_ZROBIONE += 1
    print(f"Krok: {KROKI_ZROBIONE}, \nWspółrzędna x przed ruchem: {postac.xcor()} \nWspółrzędna y przed ruchem: {postac.ycor()} \nIlość paliwa przed krokiem: {PALIWO} \nPozostała ilość kroków przed ruchem: {KROKI} \nWynik przed krokiem: {score} \nZrobiono krok w prawo")
    postac.goto(postac.xcor() + 5, postac.ycor())
    if postac.xcor() > 240 or postac.xcor() < -240 or postac.ycor() > 240 or postac.ycor() < -240:
        postac.goto(0, 0)
    print(f"Współrzędna x po kroku: {postac.xcor()} \nWspółrzędna y po kroku: {postac.ycor()}")
    if postac.distance(pacz1) < 10:
        score += 20
        pacz1.hideturtle()
        pacz1.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 1 and postac.distance(pacz2) < 10:
        score += 20
        pacz2.hideturtle()
        pacz2.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 2 and postac.distance(pacz3) < 10:
        score += 20
        pacz3.hideturtle()
        pacz3.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 3 and postac.distance(pacz4) < 10:
        score += 20
        pacz4.hideturtle()
        pacz4.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 4 and postac.distance(pacz5) < 10:
        score += 20
        pacz5.hideturtle()
        pacz5.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if postac.distance(op1) < 10:
        op1.hideturtle()
        op1.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 1 and postac.distance(op2) < 10:
        op2.hideturtle()
        op2.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 2 and postac.distance(op3) < 10:
        op3.hideturtle()
        op3.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 3 and postac.distance(op4) < 10:
        op4.hideturtle()
        op4.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 4 and postac.distance(op5) < 10:
        op5.hideturtle()
        op5.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 5 and postac.distance(op6) < 10:
        op6.hideturtle()
        op6.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 6 and postac.distance(op7) < 10:
        op7.hideturtle()
        op7.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 7 and postac.distance(op8) < 10:
        op8.hideturtle()
        op8.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 8 and postac.distance(op9) < 10:
        op9.hideturtle()
        op9.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 9 and postac.distance(op10) < 10:
        op10.hideturtle()
        op10.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if postac.distance(wsp1) < 10:
        wsp1.hideturtle()
        wsp1.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 1 and postac.distance(wsp2) < 10:
        wsp2.hideturtle()
        wsp2.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 2 and postac.distance(wsp3) < 10:
        wsp3.hideturtle()
        wsp3.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 3 and postac.distance(wsp4) < 10:
        wsp4.hideturtle()
        wsp4.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 4 and postac.distance(wsp5) < 10:
        wsp5.hideturtle()
        wsp5.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    PALIWO -= 3
    KROKI -= 1
    if random.randint(1,100)==1:
        PALIWO -=25
        print("NAGŁE ZDARZENIE: napadli na ciebie zbóje drogowi i zabrali Ci paliwo - 25 paliwa")
        zboje+=1
    if random.randint(1,120)==1:
        KROKI -=5
        print("NAGŁE ZDARZENIE: prace drogowe, trzeba wybrać objazdówkę -5 kroków")
        drogowe+=1
    print(f"Ilość paliwa po kroku: {PALIWO} \nPozostała ilość kroków po kroku: {KROKI} \nWynik po kroku: {score}")
    print()
    aktualizacja_wypisu()

def wlewo():
    global PALIWO, KROKI, score, KROKI_ZROBIONE, zebrwsp, dotkop, zboje, drogowe
    postac.setheading(180)
    KROKI_ZROBIONE += 1
    print(f"Krok: {KROKI_ZROBIONE}, \nWspółrzędna x przed ruchem: {postac.xcor()} \nWspółrzędna y przed ruchem: {postac.ycor()} \nIlość paliwa przed krokiem: {PALIWO} \nPozostała ilość kroków przed ruchem: {KROKI} \nWynik przed krokiem: {score} \nZrobiono krok w lewo")
    postac.goto(postac.xcor() - 5, postac.ycor())
    if postac.xcor() > 240 or postac.xcor() < -240 or postac.ycor() > 240 or postac.ycor() < -240:
        postac.goto(0, 0)
    print(f"Współrzędna x po kroku: {postac.xcor()} \nWspółrzędna y po kroku: {postac.ycor()}")
    if postac.distance(pacz1) < 10:
        score += 20
        pacz1.hideturtle()
        pacz1.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 1 and postac.distance(pacz2) < 10:
        score += 20
        pacz2.hideturtle()
        pacz2.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 2 and postac.distance(pacz3) < 10:
        score += 20
        pacz3.hideturtle()
        pacz3.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 3 and postac.distance(pacz4) < 10:
        score += 20
        pacz4.hideturtle()
        pacz4.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if l_paczek > 4 and postac.distance(pacz5) < 10:
        score += 20
        pacz5.hideturtle()
        pacz5.goto(500, 500)
        print("PRZYCZYNA ZMIANY WYNIKU: zebrano paczkę")
    if postac.distance(op1) < 10:
        op1.hideturtle()
        op1.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 1 and postac.distance(op2) < 10:
        op2.hideturtle()
        op2.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 2 and postac.distance(op3) < 10:
        op3.hideturtle()
        op3.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 3 and postac.distance(op4) < 10:
        op4.hideturtle()
        op4.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 4 and postac.distance(op5) < 10:
        op5.hideturtle()
        op5.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 5 and postac.distance(op6) < 10:
        op6.hideturtle()
        op6.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 6 and postac.distance(op7) < 10:
        op7.hideturtle()
        op7.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 7 and postac.distance(op8) < 10:
        op8.hideturtle()
        op8.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 8 and postac.distance(op9) < 10:
        op9.hideturtle()
        op9.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if opon > 9 and postac.distance(op10) < 10:
        op10.hideturtle()
        op10.goto(500, 500)
        PALIWO -= 10
        KROKI -= 4
        print("PRZYCZYNA ZMIANY ZASOBÓW: uderzono w oponę")
        dotkop += 1
    if postac.distance(wsp1) < 10:
        wsp1.hideturtle()
        wsp1.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 1 and postac.distance(wsp2) < 10:
        wsp2.hideturtle()
        wsp2.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 2 and postac.distance(wsp3) < 10:
        wsp3.hideturtle()
        wsp3.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 3 and postac.distance(wsp4) < 10:
        wsp4.hideturtle()
        wsp4.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    if wspomagacz > 4 and postac.distance(wsp5) < 10:
        wsp5.hideturtle()
        wsp5.goto(500, 500)
        PALIWO += 40
        KROKI += 13
        print("PRZYCZYNA ZMIANY ZASOBÓW: zebrano wspomagacz")
        zebrwsp += 1
    PALIWO -= 3
    KROKI -= 1
    if random.randint(1,100)==1:
        PALIWO -=25
        print("NAGŁE ZDARZENIE: napadli na ciebie zbóje drogowi i zabrali Ci paliwo - 25 paliwa")
        zboje+=1
    if random.randint(1,120)==1:
        KROKI -=5
        print("NAGŁE ZDARZENIE: prace drogowe, trzeba wybrać objazdówkę -5 kroków")
        drogowe+=1
    print(f"Ilość paliwa po kroku: {PALIWO} \nPozostała ilość kroków po kroku: {KROKI} \nWynik po kroku: {score}")
    print()
    aktualizacja_wypisu()

wn.listen()
wn.onkeypress(wgore,"w")
wn.onkeypress(wgore,"Up")
wn.onkeypress(wdol,"s")
wn.onkeypress(wdol,"Down")
wn.onkeypress(wprawo,"d")
wn.onkeypress(wprawo,"Right")
wn.onkeypress(wlewo,"a")
wn.onkeypress(wlewo,"Left")

while True:
    wn.update()
    if score==l_paczek*20 or PALIWO<=0 or KROKI<=0:
        print("KONIEC GRY")
        if score==l_paczek*20:
            print("Powód zakończenia wyprawy: zebrano wszytskie paczki! Gratulacje!")
        elif PALIWO<=0:
            print("Powód zakończenia wyprawy: skończyło Ci się paliwo. Spróbuj ponownie, nie poddawaj się!")
        else:
            print("Powód zakończenia wyprawy: skończył ci się limit kroków. Każdemu może się zdarzyć, trudno.")
        for i in range(50):
            print("-", end="")
        print()
        print("          PODSUMOWANIE TWOJEJ WYPRAWY:        ")
        for i in range(50):
            print("-", end="")
        print()
        if PALIWO<0:
            PALIWO=0
        if KROKI<0:
            KROKI=0
        print(f"NAZWA BOHATERA: {NAZWA}")
        print(f"POCZĄTKOWE PARAMETRY: kroki: {poczkrok}, paliwo:{poczpal}")
        print(f"ŁĄCZNIE NA MAPIE BYŁO {l_paczek+wspomagacz+opon} OBIEKTÓW, W TYM: (PACZEK: {l_paczek}, OPON: {opon}, WSPOMAGACZY: {wspomagacz})")
        print(f"POCZĄTKOWA POZYCJA: (x: {xpocz}, y: {ypocz})")
        print(f"KOŃCOWA POZYCJA: (x: {postac.xcor()}, y: {postac.ycor()})")
        print(f"LICZBA WYKONANYCH KROKÓW: {KROKI_ZROBIONE}")
        print(f"POZOSTAŁA ILOŚĆ PALIWA: {PALIWO}")
        print(f"POZOSTAŁA ILOŚĆ KROKÓW: {KROKI}")
        print(f"NAJWAŻNIEJSZE ZDARZENIA:")
        print(f" - ZEBRANE PACZKI: {score//20}")
        print(f" - ZDERZENIA Z OPONAMI: {dotkop}")
        print(f" - ZEBRANE WSPOMAGACZE: {zebrwsp}")
        print(f" - NAPADY: {zboje}")
        print(f" - OBJAZDY: {drogowe}")
        print(f"KOŃCOWY WYNIK: {score}")
        if score*5//l_paczek>=cel:
            print("Wykonałeś swój cel. Gratulacje!")
        else:
            print("Nie udało Ci się wykonać swego celu, ale nie poddawaj się i próbuj dalej!")
        print("DZIĘKUJĘ ZA GRĘ!!!")
        turtle.bye()
        break
