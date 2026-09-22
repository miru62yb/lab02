#todo количество секунд
total_seconds = int(input("Введите количество секунд: "))
#todo количество часов
hours = total_seconds // 3600
#todo остаток секунд после вычисления часов
remaining_seconds = total_seconds % 3600
#todo количество минут
minutes = remaining_seconds // 60
#todo остаток секунд
seconds = remaining_seconds % 60
#todo результат
print(f"{hours} ч {minutes} мин {seconds} с")
