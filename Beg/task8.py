# Task 8: Avengers - Classes & Objects
print("Task 8")
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")
        print("-" * 40)

    def is_leader(self):
        if self.leader:
            print(f"{self.name} is the leader of the Avengers!")
        else:
            print(f"{self.name} is not the leader of the Avengers.")


# Creating Avengers
captain_america = Avenger("Captain America", 105, "Male", "Super strength", "Shield", leader=True)
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 50, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# List of all Avengers
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Display info for each Avenger
for hero in avengers_team:
    hero.get_info()
    hero.is_leader()
