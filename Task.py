# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

import difflib
from sympy import *

# 1 Определить корни
x = Symbol('x')
# Не получилось с такой формулой
# func="-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30"
func = -12*x**4-18*x**3
res = solve(func)
for i in res:
    print(i)

# 2 Найти интервалы, на которых функция возрастает
a = difflib(func)
print(solve(0 < a))

# 3 Найти интервалы, на которых функция убывает
print(solve(a < 0))

# 4 Построить график
listPoints = []
for i in range(-10,11):
    x = i
    y = -12*x**4-18*x**3
    listPoints.append(y)
print(listPoints)
import matplotlib.pyplot as plt
plt.plot(range(-10, 11), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-10, 11), listPoints)

# 5 Вычислить вершину
korni = solve(a)
top = korni[0]
x = top
y = -12*x**4-18*x**3
print(top,y)

# 6 Определить промежутки, на котором f > 0
solve(0<func)

# 7 Определить промежутки, на котором f < 0
solve(func<0)