class Playground:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self._name = f"{first_name} {last_name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, fullname):
        self._name = fullname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age cannot be negative')
        self._age = age

    @age.deleter
    def age(self):
        print('Deleting age...')
        del self._age


p1 = Playground("Funmi", "Java", 60)
print(p1.name, p1.age)
p1.age = 90
print(p1.name, p1.age)

del p1.age
print(p1.age)
