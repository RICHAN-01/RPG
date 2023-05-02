import time
from time import sleep
import random


class Hero:
    def __init__(self, name, hp, hp_1, damage, mana, speed):
        self.lvl = 1
        self.xp = 0
        self.name = name
        self.hp = hp
        self.hp_1 = hp_1
        self.damage = damage
        self.mana = mana
        self.speed = speed

    def create_hero(name, race):
        name = name
        hp = 0
        damage = 0
        mana = 0
        speed = 0
        if race == race_list[0]:
            hp += 100
            damage += 10
            mana += 10
            speed += 100
        elif race == race_list[1]:
            hp += 130
            damage += 12.5
            mana += 1
            speed += 70
        else:
            print('This race of character does not exist.')
            quit()
        hp_1 = hp
        return Hero(name, hp, hp_1, damage, mana, speed)

    def lvl_up(self, max_xp):
        self.xp -= max_xp
        self.lvl += 1
        self.hp = self.hp + (self.hp * 0.05)
        self.hp_1 = self.hp
        self.damage += 1
        self.mana += 5
        print(f"{hero.name}, congratulations, your lvl is: {self.lvl} ")

    def weapon(self):
        wpn_type = weapon_type_list[random.randint(0, 2)]
        wpn_rare = random.choice(list(weapon_rare.keys()))
        if wpn_type == weapon_type_list[0]:
            self.damage += 4 * wpn_rare
        elif wpn_type == weapon_type_list[1]:
            self.damage += 5 * wpn_rare
        elif wpn_type == weapon_type_list[2]:
            self.damage += 6 * wpn_rare
        return wpn_type, weapon_rare[wpn_rare]

    def armor(self):
        arm_type = armor_type_list[random.randint(0, 2)]
        arm_rare = random.choice(list(armor_rare.keys()))
        if arm_type == armor_type_list[0]:
            self.hp_1 += 4 * arm_rare
        elif arm_type == armor_type_list[1]:
            self.hp_1 += 5 * arm_rare
        elif arm_type == armor_type_list[2]:
            self.hp_1 += 6 * arm_rare
        return arm_type, armor_rare[arm_rare]

    def attack(self, victim):
        rnd_num = random.randint(1, 3)
        if rnd_num == 1:
            victim.hp -= self.damage * 1.5
            print('Your damage was boosted')
        elif rnd_num == 2:
            victim.hp -= self.damage
        else:
            print('You missed')
        max_xp = self.lvl * 100
        if victim.hp <= 0:
            print('Enemy eliminated')
            thing = random.randint(0, 3)
            if thing == 1:
                wpn = self.weapon()
                print(f'You got {wpn[0]} {wpn[1]}')
            elif thing == 2:
                arm = self.armor()
                print(f'You got {arm[0]} {arm[1]}')
            else:
                print('You did not get any items')
            self.xp += 20
            if self.xp >= max_xp:
                self.lvl_up(max_xp)
            return False
        else:
            print(f"{victim.name}'s hp:{victim.hp}")
            return True


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def create_enemy():
        rnd_name = random.choice(enemy_name)
        rnd_hp = random.randint(50, 100)
        rnd_damage = random.randint(5, 12)
        return Enemy(rnd_name, rnd_hp, rnd_damage)

    def enemy_attack(self, victim):
        victim.hp_1 -= self.damage
        if victim.hp_1 <= 0:
            print('You are defeated')
            game()
        else:
            print(f"{victim.name}'s hp:{victim.hp_1}")


def fight_choice():
    answer = input(f'{hero.name}, are you ready to fight {enemy.name}? (Yes or No)').capitalize()
    if answer == 'Yes':
        time.sleep(0.5)
        print('fighting...')
        time.sleep(2)
        result = hero.attack(enemy)
        if result == True:
            enemy.enemy_attack(hero)
            fight_choice()
    elif answer == 'No':
        rnd_num_2 = random.randint(1, 2)
        if rnd_num_2 == 1:
            time.sleep(0.5)
            print('running...')
            time.sleep(2)
            print('You have run away')
        elif rnd_num_2 == 2:
            time.sleep(0.5)
            print('running...')
            time.sleep(2)
            print("You could not run away")
            enemy.enemy_attack(hero)
            fight_choice()
    else:
        print('I do not understand you')
        fight_choice()


race_list = ['Shooter', 'Strongman']
enemy_name = ['Hobbit', 'Ghost', 'Nightmare', 'Zombie', 'Jack']
weapon_type_list = ['Sword', 'Axe', 'Magic stick']
weapon_rare = {1: 'regular', 2: 'rare', 3: "epic"}
armor_type_list = ['Helmet', 'Bib', 'Shield']
armor_rare = {1: 'regular', 2: 'rare', 3: "epic"}


def game():
    global hero, race, my_name, enemy
    my_name = input('Enter your nickname: ').capitalize()
    race = input(f'Enter your race: {race_list}: ').capitalize()
    hero = Hero.create_hero(my_name, race)

    while True:
        event = random.randint(1, 2)
        if event == 1:
            print("walking...")
            time.sleep(2)
            print('You have not met anyone')
        elif event == 2:
            print("walking...")
            time.sleep(2)
            enemy = Enemy.create_enemy()
            print(f'You have met {enemy.name}')
            time.sleep(1)
            print(f"{enemy.name}'s hp: {enemy.hp}, damage: {enemy.damage}")
            time.sleep(1)
            print(f"{hero.name}'s hp: {hero.hp_1}, damage: {hero.damage}, lvl: {hero.lvl}, exp: {hero.xp}")
            time.sleep(1)
            fight_choice()


game()
