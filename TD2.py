from p5 import *
from Data import Data

from Person import Person

population_size = 200
degre_liberte = 10
data = Data(population_size)



def setup():
    size(1080, 720)
    no_stroke()
    background(204)
    init_population()
    f = create_font("arial.ttf", 30)
    text_font(f, 30)


def draw():
    if data.get_infected_population_size() != 0:
        background(204)
        data.draw_nbr_day()
        next_day = data.next_day()
        for sickPerson in data.get_population_infected():
            if next_day:
                sickPerson.grow()
            if sickPerson.state == "G":
                data.infected_to_recovered(sickPerson)
            elif sickPerson.state == "D":
                data.infected_to_dead(sickPerson)
            else:
                for sainPerson in data.get_population_sain():
                    sickPerson.__add__(sainPerson)
                    if sainPerson.state == "I":
                        data.sain_to_infected(sainPerson)

        for person in data.get_all_population():
            person.draw()
            person.move(1080, 720)
    else:
        if not data.stats_showed:
            data.set_stats_shown()
            f = create_font("arial.ttf", 50)
            text_font(f, 50)
            fill(0)
            text("L'épidémie est finie", (300, 300))
            data.show_stats()

def init_population():
    for i in range(population_size):
        person = Person(1080, 720, degre_liberte)
        data.add_to_population(person)

        if person.state == "I":
            data.add_to_infected(person)
        else:
            data.add_to_sain(person)


run()
