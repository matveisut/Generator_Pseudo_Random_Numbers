import math
import seaborn
import random
  # Произвольное начальное состояние

class LFSR:
    def __init__(self, seed = 0x2349a234, taps = 0x80000005):
        # Инициализация seed и taps в виде списков битов
        self.seed = [int(bit) for bit in bin(seed)[2:].zfill(32)]
        self.taps = [int(bit) for bit in bin(taps)[2:].zfill(32)]
        self.length = len(self.seed)  # Длина регистра
        self.state = self.seed[:]     # Копируем начальное состояние регистра

    def step(self):
        # Вычисляем новый бит через XOR указанных taps
        new_bit = 0
        for i in range(self.length):
            if self.taps[i] == 1:
                new_bit ^= self.state[i]
        # Сдвигаем регистр и добавляем новый бит
        self.state = [new_bit] + self.state[:-1]
        # Преобразуем текущее состояние регистра в десятичное число
        return int(''.join(map(str, self.state)), 2)

    def run(self, cycles):
        # Генерация последовательности за указанное количество циклов
        output = []
        for _ in range(cycles):
            output.append(self.step())
        return output

# Пример использования 32-битного полинома
  # Порождающий полином
lfsr = LFSR()

# Генерация 50 десятичных чисел псевдослучайной последовательности
sequence_lsfr = lfsr.run(50)
print(sequence_lsfr)
