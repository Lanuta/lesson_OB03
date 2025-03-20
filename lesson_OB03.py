class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        return f"{self.name} ест корм."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} чирикает!"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит!"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит!"


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"Смотритель {self.name} кормит {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"Ветеринар {self.name} лечит {animal.name}."


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def list_animals(self):
        return [animal.name for animal in self.animals]

    def list_staff(self):
        return [staff.name for staff in self.staff]

    def save_to_file_txt(self, filename="zoo_data.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for animal in self.animals:
                f.write(f"Animal, {animal.__class__.__name__}, {animal.name}, {animal.age}\n")
            for staff in self.staff:
                f.write(f"Staff, {staff.__class__.__name__}, {staff.name}\n")

    def load_from_file_txt(self, filename="zoo_data.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if parts[0] == "Animal":
                        self.animals.append(globals()[parts[1]](parts[2], int(parts[3])))
                    elif parts[0] == "Staff":
                        self.staff.append(globals()[parts[1]](parts[2]))
        except FileNotFoundError:
            print("Файл с данными не найден. Начинаем с пустого зоопарка.")


zoo = Zoo("Сафари")
zoo.add_animal(Bird("Попугай", 2))
zoo.add_animal(Mammal("Лев", 5))
zoo.add_animal(Reptile("Змея", 3))
zoo.add_staff(ZooKeeper("Андрей"))
zoo.add_staff(Veterinarian("Мария"))
zoo.save_to_file_txt()

new_zoo = Zoo("Новый зоопарк")
new_zoo.load_from_file_txt()
print("Животные в новом зоопарке:", new_zoo.list_animals())