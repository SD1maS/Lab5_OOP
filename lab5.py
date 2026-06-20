class PassengerCar:
    def __init__(self, brand: str, model: str, price: float, fuel_consumption: float, max_speed: int):
        if price < 0 or fuel_consumption < 0 or max_speed < 0:
            raise ValueError("Характеристики автомобіля не можуть бути від'ємними.")
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed

    def get_info(self) -> str:
        return f"{self.brand} {self.model} (Ціна: ${self.price}, Витрати: {self.fuel_consumption} л/100км, Швидкість: {self.max_speed} км/год)"

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.get_info()}"

class EconomyCar(PassengerCar):
    pass

class BusinessCar(PassengerCar):
    def __init__(self, brand: str, model: str, price: float, fuel_consumption: float, max_speed: int, has_wifi: bool = True):
        super().__init__(brand, model, price, fuel_consumption, max_speed)
        self.has_wifi = has_wifi

    def get_info(self) -> str:
        base_info = super().get_info()
        wifi_status = "Так" if self.has_wifi else "Ні"
        return f"{base_info}, Wi-Fi: {wifi_status}"


class Minivan(PassengerCar):
    def __init__(self, brand: str, model: str, price: float, fuel_consumption: float, max_speed: int, passenger_seats: int):
        super().__init__(brand, model, price, fuel_consumption, max_speed)
        if passenger_seats < 2:
            raise ValueError("Мінівен повинен мати хоча б 2 пасажирських місця.")
        self.passenger_seats = passenger_seats


class TaxiPark:
    
    def __init__(self):
        self.cars: list[PassengerCar] = []

    def add_car(self, car: PassengerCar) -> None:
        self.cars.append(car)

    def calculate_total_value(self) -> float:
        return sum(car.price for car in self.cars)

    def sort_by_fuel_consumption(self) -> None:
        self.cars.sort(key=lambda car: car.fuel_consumption)

    def find_cars_by_speed_range(self, min_speed: int, max_speed: int) -> list[PassengerCar]:
        if min_speed > max_speed:
            raise ValueError("Мінімальна межа швидкості не може бути більшою за максимальну.")
        return [car for car in self.cars if min_speed <= car.max_speed <= max_speed]


def main():
    parking = TaxiPark()

    try:
        parking.add_car(EconomyCar("Daewoo", "Lanos", 4000.0, 9.0, 160))
        parking.add_car(EconomyCar("Renault", "Logan", 7000.0, 6.5, 170))
        parking.add_car(BusinessCar("Toyota", "Camry", 25000.0, 8.5, 210))
        parking.add_car(BusinessCar("Mercedes", "E-Class", 45000.0, 7.0, 240, has_wifi=True))
        parking.add_car(Minivan("Volkswagen", "Transporter", 18000.0, 10.5, 180, passenger_seats=8))

        print("\033[1mСклад таксопарку:\033[0m")
        for car in parking.cars:
            print(car)

        total_value = parking.calculate_total_value()
        print(f"\n\033[1mЗагальна вартість автопарку:\033[0m ${total_value}")

        print("\n\033[1mСортування за витратами палива (від найменших):\033[0m")
        parking.sort_by_fuel_consumption()
        for car in parking.cars:
            print(f"{car.brand} {car.model} — {car.fuel_consumption} л/100км")

        min_s, max_s = 170, 200
        print(f"\n\033[1mПошук авто зі швидкістю в діапазоні {min_s} - {max_s} км/год:\033[0m")
        found_cars = parking.find_cars_by_speed_range(min_s, max_s)
        if found_cars:
            for car in found_cars:
                print(f"{car.brand} {car.model} — {car.max_speed} км/год")
        else:
            print("Автомобілів із заданою швидкістю не знайдено.")

    except ValueError as e:
        print(f"Помилка даних: {e}")
    except Exception as e:
        print(f"Непередбачувана помилка: {e}")


if __name__ == "__main__":
    main()