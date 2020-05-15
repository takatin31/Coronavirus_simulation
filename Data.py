from p5 import *
from DailyData import DailyData


class Data:

    def __init__(self, size_population):
        self.sizePopulation = size_population
        self.nbr_days = 0
        self.population = []
        self.populationI = []
        self.populationG = []
        self.populationS = []
        self.populationD = []
        self.counter = 0
        self.all_data = []
        self.stats_showed = False

    def draw_nbr_day(self):
        fill(0)
        text("Day : " + str(self.nbr_days), (0, 0))

    def next_day(self):
        self.counter += 1
        if self.counter == 5:
            self.counter = 0
            self.nbr_days += 1
            self.add_today_data()
            return True
        return False

    def get_population_infected(self):
        return self.populationI

    def get_population_recovered(self):
        return self.populationG

    def get_population_dead(self):
        return self.populationD

    def get_population_sain(self):
        return self.populationS

    def get_all_population(self):
        return self.population

    def get_population_size(self):
        return self.sizePopulation

    def get_infected_population_size(self):
        return len(self.populationI)

    def get_sain_population_size(self):
        return len(self.populationS)

    def get_dead_population_size(self):
        return len(self.populationD)

    def get_recovered_population_size(self):
        return len(self.populationG)

    def sain_to_infected(self, person):
        self.populationS.remove(person)
        self.populationI.append(person)

    def infected_to_recovered(self, person):
        self.populationI.remove(person)
        self.populationG.append(person)

    def infected_to_dead(self, person):
        self.populationI.remove(person)
        self.populationD.append(person)

    def add_to_population(self, person):
        self.population.append(person)

    def add_to_infected(self, person):
        self.populationI.append(person)

    def add_to_sain(self, person):
        self.populationS.append(person)

    def add_today_data(self):
        sain_pop_size = self.get_sain_population_size()
        infected_pop_size = self.get_infected_population_size()
        dead_pop_size = self.get_dead_population_size()
        recovered_pop_size = self.get_recovered_population_size()
        self.all_data.append(
            DailyData(self.nbr_days, sain_pop_size, infected_pop_size, recovered_pop_size, dead_pop_size))

    def show_stats(self):
        import matplotlib.pyplot as plt
        days = []
        infected_data = []
        recovered_data = []
        deaths_data = []
        sain_data = []
        for daily_data in self.all_data:
            days.append(daily_data.day)
            infected_data.append(daily_data.nbr_i)
            recovered_data.append(daily_data.nbr_g)
            deaths_data.append(daily_data.nbr_d)
            sain_data.append(daily_data.nbr_s)

        plt.plot(days, infected_data)
        plt.ylabel('nombre de cas infectés')
        plt.show()

        plt.plot(days, sain_data)
        plt.ylabel('nombre de cas sain')
        plt.show()

        plt.plot(days, deaths_data)
        plt.ylabel('nombre de cas décédés')
        plt.show()

        plt.plot(days, recovered_data)
        plt.ylabel('nombre de cas guéris')
        plt.show()

    def set_stats_shown(self):
        self.stats_showed = True