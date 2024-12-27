import numpy as np
import matplotlib.pyplot as plt

# Генерация случайной последовательности
np.random.seed(42)  # Для воспроизводимости
sequence = np.random.randint(0, 100, size=100000)

# Вычисление разностей между соседними элементами
differences = np.diff(sequence)

# Построение гистограммы
plt.figure(figsize=(8, 6))
plt.hist(differences, bins=10, color='skyblue', edgecolor='black')
plt.title('Гистограмма разностей соседних элементов случайной последовательности')
plt.xlabel('Значение разности')
plt.ylabel('Частота')
plt.grid(True, alpha=0.6)
plt.show()
