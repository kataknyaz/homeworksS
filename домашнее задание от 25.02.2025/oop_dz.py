class Vehicle:
    # Базовый класс, описывающий общее транспортное средство
    def __init__(self, brand, model, year, mileage):
        self._brand = brand  # Марка транспортного средства
        self._model = model  # Модель транспортного средства
        self._year = year  # Год выпуска
        self._mileage = mileage  # Пробег (в километрах)
    
    def get_info(self):
        # Возвращает строку с информацией о транспортном средстве
        return f"{self._year} {self._brand} {self._model}, Пробег: {self._mileage} км"
    
    def get_brand(self):
        # Возвращает марку транспортного средства
        return self._brand
    
    def get_model(self):
        # Возвращает модель транспортного средства
        return self._model

class Car(Vehicle):
    # Класс для легковых автомобилей
    def __init__(self, brand, model, year, mileage, body_type):
        super().__init__(brand, model, year, mileage)
        self._body_type = body_type  # Тип кузова
    
    def get_info(self):
        # Дополняет базовую информацию, добавляя тип кузова
        return super().get_info() + f", Тип кузова: {self._body_type}"

class Truck(Vehicle):
    # Класс для грузовиков
    def __init__(self, brand, model, year, mileage, load_capacity):
        super().__init__(brand, model, year, mileage)
        self._load_capacity = load_capacity  # Грузоподъёмность (в тоннах)
    
    def get_info(self):
        # Дополняет базовую информацию, добавляя грузоподъёмность
        return super().get_info() + f", Грузоподъёмность: {self._load_capacity} т"

class Motorcycle(Vehicle):
    # Класс для мотоциклов
    def __init__(self, brand, model, year, mileage, engine_volume):
        super().__init__(brand, model, year, mileage)
        self._engine_volume = engine_volume  # Объём двигателя (в см³)
    
    def get_info(self):
        # Дополняет базовую информацию, добавляя объём двигателя
        return super().get_info() + f", Объём двигателя: {self._engine_volume} см³"

class Fleet:
    # Класс для управления транспортным парком
    def __init__(self):
        self._vehicles = []  # Список транспортных средств
    
    def add_vehicle(self, vehicle):
        # Добавляет транспортное средство в парк
        self._vehicles.append(vehicle)
    
    def list_vehicles(self):
        # Выводит список всех транспортных средств
        for vehicle in self._vehicles:
            print(vehicle.get_info())
    
    def find_vehicle(self, brand=None, model=None):
        # Ищет транспортное средство по марке и/или модели
        found_vehicles = [
            v for v in self._vehicles
            if (brand is None or v.get_brand() == brand) 
            and (model is None or v.get_model() == model)
        ]
        return found_vehicles

# Пример использования
fleet = Fleet()

# Создаём объекты различных типов транспортных средств
car = Car("Toyota", "Corolla", 2020, 15000, "Sedan")
truck = Truck("Volvo", "FH16", 2018, 75000, 25)
motorcycle = Motorcycle("Yamaha", "MT-07", 2021, 5000, 689)

# Добавляем транспортные средства в парк
fleet.add_vehicle(car)
fleet.add_vehicle(truck)
fleet.add_vehicle(motorcycle)

# Выводим список всех транспортных средств
print("Список всех транспортных средств:")
fleet.list_vehicles()

# Поиск транспортного средства по марке
print("\nПоиск по марке 'Toyota':")
for vehicle in fleet.find_vehicle(brand="Toyota"):
    print(vehicle.get_info())   