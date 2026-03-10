from math import factorial

print([n ** 2 for n  in range(11)])

keys = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
             'Пятница', 'Суббота', 'Воскресенье']
print({keys[val]: val + 1 for val in range(len(keys))})

oldlist1 = ["Django", "FastAPI", "Numpy", "PYTHON",
           "Pandas", "FASTAPI", "Python", "random"]
print(set([t.lower() for t in oldlist1]))

oldlist2 = [1, 3, 4, 87, 98, 15, 7, 4]
print([even for even in oldlist2 if even % 2 == 0])

'''
print({key: factorial(key) for key in range(1, 6)})
'''

fact = lambda n: 1 if n <= 1 else n * fact(n - 1)
print({key: fact(key) for key in range(1, 6)})
