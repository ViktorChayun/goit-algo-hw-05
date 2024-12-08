"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951593/homework
    
    Необхідно створити функцію generator_numbers
        * яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. 
        * Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. 
        * Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

"""
from typing import Callable
import re

# повертає генератор, що ітерує по всіх дійсних числах у тексті
# рекомендація - використовувати регулярні вирази для пошуку дійсних чисел в тексті
def generator_numbers(text: str):
    pattern = r"\s\d+.\d+\s"
    figures = re.findall(pattern, text)
    for val in figures:
        yield float(val.strip())

# має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку 
# та приймати його як аргумент при виклику.
def sum_profit(text: str, func: Callable):
    return sum(val for val in func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")