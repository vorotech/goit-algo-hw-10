"""Module for solving the task 1."""

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Ініціалізація моделі
problem = LpProblem("Maximize_Production", LpMaximize)

# Визначення змінних
A = LpVariable('Lemonade', lowBound=0, cat='Integer')
B = LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція: максимізація загального виробництва Лимонаду і Фруктового соку
problem += lpSum([A, B]), "Total_Production"

# Обмеження
problem += (2 * A + B <= 100), "Water_Constraint"
problem += (A <= 50), "Sugar_Constraint"
problem += (A <= 30), "Lemon_Juice_Constraint"
problem += (2 * B <= 40), "Fruit_Puree_Constraint"

# Розв'язання моделі
problem.solve()

# Отримання результатів
print(f"Виробництву Лимонаду: {A.varValue}")
print(f"Виробництву Фруктового соку: {B.varValue}")
print(f"Разом: {problem.objective.value()}")
