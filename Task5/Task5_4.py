from datetime import datetime, timedelta
import random

end = datetime.now()
start = end - timedelta(days=5 * 365)
dates = []
for _ in range(10):
    randays = random.randint(0, (end - start).days)
    dates.append(start + timedelta(days=randays))

for i in range(len(dates) - 1):
    d1 = dates[i]
    d2 = dates[i + 1]
    diff = abs((d2 - d1).days)
    print(f"{d1.strftime('%Y-%m-%d')} -> {d2.strftime('%Y-%m-%d')}: {diff} дней")

dates.sort()
print("\nВсе сгенерированные даты (отсортированы):")
for i, date in enumerate(dates, 1):
    print(f"{i}. {date.strftime('%Y-%m-%d')}")