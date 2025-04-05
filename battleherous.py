import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        increase_health = random.randint(5, 15)
        increase_attack = random.randint(1, 5)
        self.health += increase_health
        self.attack_power += increase_attack
        print(
            f"{self.name} поднял уровень! Здоровье увеличено на {increase_health}, сила удара увеличена на {increase_attack}.")


class Game:
    def __init__(self):
        self.player = Hero(input("Введите имя вашего героя: "))
        self.computer = Hero("Компьютер")
        self.level = self.choose_level()

    def choose_level(self):
        print("Выберите уровень сложности:")
        print("1. Легкий")
        print("2. Средний")
        print("3. Сложный")
        level = input("Введите номер уровня (1-3): ")

        if level == '1':
            self.computer.attack_power = 10
        elif level == '2':
            self.computer.attack_power = 20
        elif level == '3':
            self.computer.attack_power = 30
        else:
            print("Неверный выбор, уровень установлен на средний.")
            self.computer.attack_power = 20

        print(f"\nВы выбрали уровень {level}. Сила удара компьютера: {self.computer.attack_power}")
        return level

    def start(self):
        print(
            f"\nВ бой вступают: {self.player.name} (здоровье: {self.player.health}) против {self.computer.name} (здоровье: {self.computer.health})")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"{self.computer.name} осталось здоровья: {self.computer.health}\n")

            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                self.player.level_up()  # Увеличить уровень игрока после победы
                break

                # Ход компьютера
            self.computer.attack(self.player)
            print(f"{self.player.name} осталось здоровья: {self.player.health}\n")

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    game = Game()
    game.start()