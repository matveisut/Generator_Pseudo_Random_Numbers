import numpy as np
from scipy.stats import chi2

def frequency_block_test(bit_sequence, block_size=8):

    n = len(bit_sequence)

    # Разделяем последовательность на блоки
    num_blocks = n // block_size
    blocks = np.array(bit_sequence[:num_blocks * block_size]).reshape((num_blocks, block_size))

    # Подсчёт частоты единиц в каждом блоке
    proportions = blocks.mean(axis=1)

    # Расчёт статистики хи-квадрат
    chi_squared = 4 * block_size * np.sum((proportions - 0.5) ** 2)

    # Вычисление p-значения
    p_value = chi2.sf(chi_squared, df=num_blocks)

    # Решение о принятии гипотезы о случайности
    is_random = p_value >= 0.01  # Обычно используется уровень значимости 0.01

    return p_value

