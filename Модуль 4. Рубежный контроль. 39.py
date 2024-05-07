import datetime
from collections import Counter
from typing import List

def most_common_months(dates: List[str], n: int) -> List[int]:
    # Извлекаем месяцы из дат
    months = [int(date.split('-')[1]) for date in dates]
    # Получаем n самых частых месяцев
    return [month for month, _ in Counter(months).most_common(n)]

# Пример использования функции
dates = ["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
print(most_common_months(dates, 2))
