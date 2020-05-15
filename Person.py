from p5 import *
from random import randrange



class Person:
    def __init__(self, width, height, degre_liberte):
        probability_infected = randrange(100)
        if probability_infected <= 4:
            self.state = "I"
        else:
            self.state = "S"

        probability_liberte = randrange(100)
        if probability_liberte <= degre_liberte:
            self.dirX = 2 * randrange(-1, 1) + 1
            self.dirY = 2 * randrange(-1, 1) + 1
        else:
            self.dirX = 0
            self.dirY = 0

        self.nbr_days_infected = 0
        self.dead = False
        self.radius = 15
        self.pos = Vector(randrange(self.radius, width - self.radius), randrange(self.radius, height - self.radius))
        self.nbr_contact = 0

    def __add__(self, other):
        if self.touched(other):
            self.nbr_contact += 1
            other.state = "I"
            other.nbr_contact += 1

    def touched(self, other):
        return self.pos.x - self.radius < other.pos.x < self.pos.x + self.radius and self.pos.y - self.radius < other.pos.y < self.pos.y + self.radius

    def draw(self):
        if self.state == "I":
            fill(226, 0, 0)
        if self.state == "S":
            fill(255)
        if self.state == "G":
            fill(0, 246, 0)
        if self.state == "D":
            fill(51)

        circle((self.pos.x, self.pos.y), self.radius)


    def move(self, width, height):
        if self.state != "D":
            if self.pos.x - self.radius < 0 or self.pos.x + self.radius > width:
                self.dirX *= -1
            if self.pos.y - self.radius < 0 or self.pos.y + self.radius > height:
                self.dirY *= -1

            self.pos.x += 5 * self.dirX
            self.pos.y += 5 * self.dirY

    def grow(self):
        if self.state == "I":
            self.nbr_days_infected += 1
            if self.nbr_days_infected == 14:
                probability_dying = randrange(100)
                if probability_dying <= 6:
                    self.nbr_days_infected = 0
                    self.state = "D"
                else:
                    self.nbr_days_infected = 0
                    self.state = "G"
