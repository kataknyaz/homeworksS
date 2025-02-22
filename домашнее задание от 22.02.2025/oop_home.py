class Animal:
    def __init__(self, name, species, age, diet):
        self.name = name
        self.species = species
        self.__age = age 
        self.diet = diet
        
    def make_sound(self):
        print(f"{self.name} издает звук.")
    
    
class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur_color):
        super().__init__(name, species, age, diet)
        self.fur_color = fur_color
    
    def make_sound(self):
        print(f"{self.name} издает звук: 'Appp'.")
    
    
    
class Bird(Animal):
    def __init__(self, name, species, age, diet, wing_span):
        super().__init__(name, species, age, diet)
        self.wing_span = wing_span
        
    def make_sound(self):
        print(f"{self.name} говорит: 'чирик-чирик'.")
    
class ZooEmployee: 
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def feed_animal(self, animal):
        print(f"Работник зоопарка {self.name} кормит {animal.name} {animal.diet} ")    
        
        
class Visitor: 
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number

    def watch_animal(self, animal):
        print(f"Посетитель {self.name} смотрит на {animal.name}, который относится к {animal.species}")    



lion = Mammal("Симба", "лев", 5, "мясо", "бежевый, песочный")
bird = Bird("Кеша", "Попугай", 2, "пшено, зелень", "9-10 см")  

employee = ZooEmployee("Андрей", "кормящий")
visitor = Visitor("Екатерина", 28892)

employee.feed_animal(bird)
visitor.watch_animal(lion)

lion.make_sound()
bird.make_sound()
    
 