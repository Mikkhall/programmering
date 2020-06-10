import pygame as p
from random import randint
from enum import Enum

class Directions (Enum):                    # Her lager jeg en klasse for å kunne hente retningene enklere senere
    RIGHT = (20, 0)                         # En av retningene
    LEFT = (-20, 0)                         #
    UP = (0, -20)                           #
    DOWN = (0, 20)                          #
    def __init__(self, x, y):               #
        self.x = x                          #
        self.y = y                          #
    @property                               #
    def getX(self):                         #
        return self.x                       #
    @property                               # Tobias hjalp meg med det
    def getY(self):                         # 
        return self.y                       #


screen = p.display.set_mode((700, 500))     # Skjermen
clock = p.time.Clock()
length = 0                                  # Bare en variabel til senere
theFood = 0                                 #
direction = Directions.DOWN                 # Starter med å bevege seg nedover
snakeLength = 1
snake = [ [0, 0] ]                          # Må ha to brackets for at når jeg legger på andre arrays forblir de separerte


def removeTail () :                         # Funksjon  Fjerner halen på slangen om den er for lang
    while snakeLength < len( snake ) :      # Mens slangen er større enn den skal, kunne tatt en if setning, men da tar den ikke alle stegene som er for lange
        a = snake[0][0]
        b = snake[0][1]
        draw(a, b, 0, 0, 0)                 # Aktiverer en funksjon som tegner en sort firkant over halen
        snake.pop(0)                        # Sletter første elementet i arrayet Slangen


def move ():                                # Funksjon  Beveger slangen
    global snakeLength                      # Noen variabler jeg må endre på, og derfor må gjøre dem globale
    global theFood

    if not theFood:                         # Om det ikke er mat på skjermen,
        food()                              # lager den en med mat-funksjonen

    length = len(snake) - 1
    a = snake[length][0] + direction.getX   # Beveger hodet
    b = snake[length][1] + direction.getY
    try:
        snake.index([a, b])                 # Sjekker om hodet den skal plasere allerede finnes, om blir det en feilmelding
    except:                                 # gjør den except
        snake.append([a, b])                # Flytter hodet
        a = snake[length + 1][0]            
        b = snake[length + 1][1]
        draw(a, b, 0, 255, 0)               # Tegner hodet
        if snake[length + 1] == theFood:    # Sjekker om hodet har samme posisjon som en matbit
            snakeLength += 1                # om det legger øker makslengden på slangen 
            theFood = 0                     # og fjerner maten
    else:                                   
        raise SystemExit                    # Om hodet finnes alerede lukker den programmet og man har tapt
    

def getEvent () :                           # Funksjon  Finner tastetrykk for å finne retingen å bevege seg i
    global direction                        # Noen flere variabler jeg skal endre på

    for event in p.event.get():                                     # Finner events
        if event.type == p.KEYDOWN and event.key == p.K_q:          # Ser om det er et tastetrykk og det er q som er trykket
            raise SystemExit                                        # Om q er trykket lukkes programmet
        if event.type == p.KEYDOWN and event.key == p.K_w:
            if direction != Directions.DOWN or len(snake) == 1:
                direction = Directions.UP
        if event.type == p.KEYDOWN and event.key == p.K_d:          # Om det er d (høyre) som er trykket, 
            if direction != Directions.LEFT or len(snake) == 1:     # og slangen ikke beveger seg til venstre eller har lengde på en, 
                direction = Directions.RIGHT                        # settes retningen til høyre
        if event.type == p.KEYDOWN and event.key == p.K_s:          # --- om slangen er en lang krasjer den ikke med seg selv om den snur, 
            if direction != Directions.UP or len(snake) == 1:       # --- men ellers vil det vært et tap om man kunne snudd 180 grader
                direction = Directions.DOWN
        if event.type == p.KEYDOWN and event.key == p.K_a:
            if direction != Directions.RIGHT or len(snake) == 1:
                direction = Directions.LEFT


def draw (a, b, colour1, colour2, colour3):                                 # Funksjon  Tegner slangen og maten
    p.draw.rect(screen, (colour1, colour2, colour3), p.Rect(a, b, 18, 18))  # Tegner


def food ():                            # Funksjon Lager maten
    global theFood                      

    while True:
        a = randint(0, 34) * 20         # Lager et tilfeldig tall
        b = randint(0, 24) * 20
        try:
            snake.index([a, b])         # sjekker om det er en av slangens brikker, samme måte som for å sjekke kolisjoner på slangen
        except:
            draw(a, b, 255, 0, 0)       # Om maten ikke koliderer med slangen kaller den på å tegne maten
            theFood = [a, b]            # Setter theFood til kordinatene til maten
            break                       # Og slutter while True loopen


def death ():                                           # Funksjon  Sjekker om man har gått ut av skjermen
    length = len(snake) - 1
    if snake[length][0] > 700 or snake[length][0] < 0:  # Om hodet er utenfor på x aksen
        raise SystemExit                                # Om det, lukker programmet
    if snake[length][1] > 500 or snake[length][1] < 0:  # y aksen
        raise SystemExit

while True:                                                     # Loopen spillet skjører på, det er den som kaller på funksjonene
    p.time.wait(100)                                            # Venter 100 millisekunder
    getEvent()                                                  # Henter alle hendelsene
    move()                                                      # Beveger slangen og alle operasjonene knyttet til det
    removeTail()                                                # Fjerner halen
    death()                                                     # Sjekker om man har gått ut av skjermen
    
    p.display.flip()                                            # Snur skjermen (Vet ikke hvorfor man må snu skjermen, men fungerer ikke uten)
    p.display.set_caption("Score: " + str(snakeLength - 1))     # I headeren skriver den hvor mange poeng man har, hvor mange mat man har samlet