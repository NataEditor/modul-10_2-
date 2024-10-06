from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name=str, power=int):
        super().__init__()
        self.name=name
        self.power=power
        
        

    def run(self):
        enemy=100
        n_days=0
        for i in range(enemy):
            if enemy > 0:
                
                print(f' {self.name}, на нас напали!')
                enemy-=self.power
                sleep(1)
                n_days+=1
             
                print(f' {self.name} сражается {n_days} день(дней), осталось {enemy} воинов')
                if enemy<= 1:
                    print(f'{self.name} одержал победу спустя {n_days} дней(дня)')
            
            
            
            
            
            


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
