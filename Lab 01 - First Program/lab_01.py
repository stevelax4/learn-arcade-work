class Monster:
    def __init__(self):
        self.name = ""
        self.health = 100

    def decrease_health(self, lost_health):
        self.health -= lost_health
        print(self.name + "is now at " +  str(self.health) + " health ")
        if self.health < 1:
            print("The Monster Dies")


def main():
    gorp = Monster()
    gorp.name = "Gorp"
    gorp.decrease_health(100)

main()

class Cat:


    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print(self.name + "  says \"meow\"")

def main():
    my_cat = Cat()
    my_cat.name = "Buttercup"
    my_cat.color = "orange"
    my_cat.weight = 5
    my_cat.meow()


main()