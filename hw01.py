"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951593/homework
    
    Вимоги до завдання:
        * Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
        * fibonacci(n) обчислює n-те число Фібоначчі. 
            * Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
            * Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
        * Використання рекурсії для обчислення чисел Фібоначчі.

    ФУНКЦІЯ caching_fibonacci
        Створити порожній словник cache

        ФУНКЦІЯ fibonacci(n)
            Якщо n <= 0, повернути 0
            Якщо n == 1, повернути 1
            Якщо n у cache, повернути cache[n]

            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            Повернути cache[n]

        Повернути функцію fibonacci
    КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
    
    функція fibonacci всередині caching_fibonacci обчислює відповідні числа Фібоначчі, 
    зберігаючи попередні результати у кеші. 
    Це робить повторні виклики для тих самих значень n значно швидшими, оскільки вони просто повертають значення з кешу.
    Замикання дозволяє fibonacci(n) "пам'ятати" стан cache між різними викликами, 
    що є ключовим для кешування результатів обчислень
"""
def caching_fibonacci() ->int:
    cache = {}
    def fibonacci(n)->int:
        if n <=0:
            return 0
        elif n==1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610