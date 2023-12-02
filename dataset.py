import pandas as pd
import matplotlib.pyplot as plt

# Загрузите данные
data = pd.read_csv("C:\Users\Nuriya\Downloads\archive\complete.csv")

# Постройте гистограмму распределения наблюдений по времени
plt.hist(data["date_time"])
plt.xlabel("Время")
plt.ylabel("Количество наблюдений")
plt.show()

