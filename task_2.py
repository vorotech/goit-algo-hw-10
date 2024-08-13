"""Module for solving the task 2."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import sympy as sp

def plot_show(n, a, b, f, function_expr):
    # Створення діапазону значень для x
    x = np.linspace(a-0.5, b+0.5, n)
    y = f(x)

    # Створення графіка
    _, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування $f(x) = {sp.latex(function_expr)}$ від {str(a)} до {str(b)}')
    plt.grid()
    plt.show()

def is_inside(a, b, x, y, f):
    """Перевіряє, чи знаходиться точка (x, y) всередині сірої зони."""
    if a <= x <= b:
        fx = f(x)
        if fx >= 0:
            return 0 <= y <= fx
        else:
            return fx <= y <= 0
    return False

def monte_carlo_simulation(f, a, b, n):
    """Функція для обчислення інтеграла методом Монте-Карло."""
    # Знаходимо мінімальне та максимальне значення функції на проміжку
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)
    min_y = min(min(y_vals), 0)
    max_y = max(max(y_vals), 0)
    
    count_inside = 0
    
    for _ in range(n):
        x = np.random.uniform(a, b)
        y = np.random.uniform(min_y, max_y)
        if is_inside(a, b, x, y, f):
            count_inside += 1
            
    area = (b - a) * (max_y - min_y)
    return (count_inside / n) * area

def verify_quad(f, a, b):
    """Функція для обчислення інтеграла та його похибки."""
    result, error = spi.quad(f, a, b)
    return result, error

def main():
    """Точка входу в програму."""
    
    # Символьне визначення функції
    x = sp.symbols('x')
    function_expr = x * sp.sin(x)

    # Перетворення символьного виразу у numpy-функцію
    f = sp.lambdify(x, function_expr, 'numpy')

    a, b = -3, 3 # Межі інтегрування

    # Виведення графіка
    plot_show(400, a, b, f, function_expr)
    
    # Виклик функцій для обчислення інтеграла
    monte_carlo_result = monte_carlo_simulation(f, a, b, 10000)
    verify_result, error = verify_quad(f, a, b)
    verify_analytical = -6 * np.cos(3) + 2 * np.sin(3)
    
    print(f"Інтеграл (Монте-Карло): {monte_carlo_result}")
    print(f"Інтеграл (sys.quad): {verify_result} (похибка: {error})")
    print(f"Інтеграл (Аналітичний): {verify_analytical}")


if __name__ == "__main__":
    main()
