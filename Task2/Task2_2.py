dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
key = set(dct.keys())
val = set(dct.values())
print("Множество ключей:", key, "\nМножество значений:", val)
uniti  = set(list(dct.keys()) + list(dct.values()))
print("Объединение множеств", uniti)