
## Creating a class and instances ##
class Person:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

    def is_edu(self):
        if self.personality is "sober":
            return "Has GED certificate and bachelor degree."
        elif self.personality is "callous":
            return "Never sat in a classroom."

    def is_felon(self):
        if self.personality is "sober":
            return True
        elif self.personality is "callous":
            return False

p1 = Person("Katie Wood", "sober")
p2 = Person("John Sabre", "callous")

print(p1.is_felon())
print(p2.is_felon())
print(p1.is_edu())
print(p2.is_edu())

## Creating a class and instances ##