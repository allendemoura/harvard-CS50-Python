class Boy:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name}, {self.role}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("name is shorn")
        self._name = name

def main():
    name = input("name? ")
    role = input("role? ")
    boy = Boy(name, role)
    print(boy)

main()