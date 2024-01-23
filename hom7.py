
from abc import ABC, abstractmethod  # Импортируем модуль ABC для определения абстрактных классов
import logging  # Импортируем модуль logging для добавления логгирования

# Создание Singleton логгера
class Logger:
    _instance = None  # Приватная переменная для хранения экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            cls._instance.logger.addHandler(logging.StreamHandler())
        return cls._instance


# Интерфейс для калькулятора
class Calculator(ABC):  # Создаем абстрактный класс
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass


# Реализация калькулятора комплексных чисел
class ComplexCalculator(Calculator):  # Наследуемся от абстрактного класса
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        result_real = self.real + other.real
        result_imag = self.imag + other.imag
        return ComplexCalculator(result_real, result_imag)

    def multiply(self, other):
        result_real = self.real * other.real - self.imag * other.imag
        result_imag = self.real * other.imag + self.imag * other.real
        return ComplexCalculator(result_real, result_imag)

    def divide(self, other):
        denominator = other.real**2 + other.imag**2
        result_real = (self.real * other.real + self.imag * other.imag) / denominator
        result_imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexCalculator(result_real, result_imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"


# Фабрика для создания экземпляров калькулятора
class CalculatorFactory:
    def create_calculator(self, real, imag):
        return ComplexCalculator(real, imag)


# Пример использования калькулятора с логгированием
def main():
    logger = Logger().logger  # Инициализация логгера
    calculator_factory = CalculatorFactory()  # Создание фабрики калькуляторов

    num1 = calculator_factory.create_calculator(3, 4)  # Создание комплексного числа 3 + 4j
    num2 = calculator_factory.create_calculator(1, 2)  # Создание комплексного числа 1 + 2j

    logger.info(f"Сложение: {num1} + {num2} = {num1.add(num2)}")  # Вывод результата сложения в лог
    logger.info(f"Умножение: {num1} * {num2} = {num1.multiply(num2)}")  # Вывод результата умножения в лог
    logger.info(f"Деление: {num1} / {num2} = {num1.divide(num2)}")  # Вывод результата деления в лог


if __name__ == "__main__":
    main()  # Вызов функции main при запуске файла
