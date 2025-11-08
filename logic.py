from random import randint
import requests
import random
import datetime
import time
from datetime import datetime, timedelta
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.stats = self.get_stats()
        self.move = self.get_move()
        self.hp = randint(50,100)
        self.power = randint(50,100)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self

      

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"  

    def get_move(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['moves'][0]['move']['name'])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"    



    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name},Хп: {self.hp}, Сила: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time + delta_time}"


    #def show_stats(self):
    #   return f'Хп: {self.stats}, Сила: {self.power}' 
    
    def show_move(self):
        return f'Движение: {self.move}'


    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "

    def info(self):
        return 'У вас покемон-боец\n' + super().info()
    
    def feed(self):
        return super().feed(feed_interval=5)


class Wizard(Pokemon):
    def info(self):
        return 'У вас покемон-волшебник\n' + super().info()

    def feed(self):
        return super().feed(hp_increase=20)

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")
    print(wizard.info())
    time.sleep(21)
    print(wizard.feed())
    print(wizard.info())
    print()
    print(fighter.info())
    time.sleep(11)
    print(fighter.feed())
    print(fighter.info())
