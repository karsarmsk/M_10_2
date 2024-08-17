from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.den = 0
        self.kolvo_vragov = 100

   def run(self):
        print(f'{self.name}, на нас напали!')
        while self.kolvo_vragov > 0:
            print(f'{self.name}, сражается {self.den} день(дня), осталось {self.kolvo_vragov} воинов.')
            self.kolvo_vragov -= self.power
            self.den += 1
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.den} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')