import numpy as np
import math
from scipy.stats import chi2
import scipy.stats as stats
import numpy as np
from scipy.fftpack import fft
from scipy.stats import norm
import matplotlib.pyplot as plt

def draw_spectral_test(magnitudes, threshold):
    plt.figure(figsize=(10, 6))
    plt.plot(magnitudes, label="FFT Magnitudes", color="blue", alpha=0.7)
    plt.axhline(y=threshold, color="red", linestyle="--", label=f"Threshold = {threshold:.2f}")
    plt.title("Fourier Transform Magnitudes")
    plt.xlabel("Frequency Index")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

def spectral_test_with_plot(bits):

    # Step 1: Convert binary sequence to -1 and 1
    n = len(bits)
    seq = np.array([1 if b == '1' else -1 for b in bits])

    # Step 2: Apply Fast Fourier Transform (FFT)
    fft_values = fft(seq)
    magnitudes = np.abs(fft_values)[:n // 2]

    # Step 3: Calculate the expected number of peaks under the threshold
    threshold = np.sqrt(2.995732274 * n)  # 2.995732274 ≈ -ln(0.05)
    expected_peaks = 0.95 * (n / 2.0)

    # Step 4: Count the number of peaks below the threshold
    actual_peaks = np.sum(magnitudes < threshold)

    # Step 5: Compute the p-value using the normal distribution
    p_value = norm.sf(abs(actual_peaks - expected_peaks) / np.sqrt(0.95 * 0.05 * (n / 2.0)))

    return p_value, actual_peaks, expected_peaks, magnitudes, threshold

def frequency_bit_test(bits):

    n = len(bits)  # Длина последовательности

    # Подсчет числа единиц (1) и нулей (0)
    s = sum(1 if bit == '1' else -1 for bit in bits)

    # Расчет статистики теста
    s_obs = abs(s) / math.sqrt(n)

    # Вычисление p-value
    p_value = math.erfc(s_obs / math.sqrt(2))

    return p_value

def frequency_block_test(bit_sequence, block_size = 8):

    # Проверка входных данных
    if isinstance(bit_sequence, str):
        bit_sequence = [int(b) for b in bit_sequence]

    n = len(bit_sequence)
    if block_size <= 0 or block_size > n:
        raise ValueError("Размер блока должен быть больше 0 и меньше длины последовательности.")

    # Убедимся, что длина последовательности кратна размеру блока
    num_blocks = n // block_size
    adjusted_length = num_blocks * block_size
    bit_sequence = bit_sequence[:adjusted_length]  # Обрезаем лишние биты

    # Разделяем последовательность на блоки
    blocks = np.array(bit_sequence).reshape((num_blocks, block_size))

    # Подсчёт частоты единиц в каждом блоке
    proportions = blocks.mean(axis=1)

    # Расчёт статистики хи-квадрат
    chi_squared = 4 * block_size * np.sum((proportions - 0.5) ** 2)

    # Вычисление p-значения
    p_value = chi2.sf(chi_squared, df=num_blocks)

    return  p_value

def test_runs(bits):

    n = len(bits)

    # Подсчёт числа переходов (из 0 в 1 или из 1 в 0)
    num_runs = sum(1 for i in range(1, n) if bits[i] != bits[i - 1]) + 1
    
    # Количество нулей и единиц
    num_zeros = bits.count('0')
    num_ones = bits.count('1')

    # Расчёт математического ожидания и дисперсии числа переходов
    expected_runs = (2 * num_zeros * num_ones) / n + 1
    variance_runs = (2 * num_zeros * num_ones * (2 * num_zeros * num_ones - n)) / (n**2 * (n - 1))
    
    # Статистика теста (z-оценка)
    z = (num_runs - expected_runs) / (variance_runs**0.5)
    
    # Вычисление p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # Двусторонний тест
    
    return p_value

def print_all_tests(bits):
    print('frequency_bit_test - p-value',frequency_bit_test(bits))

    print('frequency_block_test - p-value',frequency_block_test(bits))

    print('test_runs - p-value',test_runs(bits))

    p_value, actual_peaks, expected_peaks, magnitudes, threshold  = spectral_test_with_plot(bits)

    print('spectral_test - p-value', p_value, 'наблюдаемые пики',actual_peaks, 'ожидаемые пики', expected_peaks)

    draw_spectral_test(magnitudes, threshold)

#print(frequency_bit_test(bits))

#print(frequency_block_test(bits))

#print(test_runs(bits))

#p_value, actual_peaks, expected_peaks = spectral_test_with_plot(bits)

#print(p_value, actual_peaks, expected_peaks)


