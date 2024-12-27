class LFSR:
    def __init__(self, seed = 0x2349a234, taps = 0x80000005):
        # Инициализация seed и taps в виде списков битов
        self.seed = [int(bit) for bit in bin(seed)[2:].zfill(32)]
        self.taps = [int(bit) for bit in bin(taps)[2:].zfill(32)]
        self.length = len(self.seed)  # Длина регистра
        self.state = self.seed[:]     # Копируем начальное состояние регистра

    def step(self):
        # Вычисляем новый бит через XOR указанных taps
        new_number = []
        #вычисляется 32 новых бита, которые будут склеены в 10-ричное число
        for i in range(32):
            new_bit = 0
            for i in range(self.length):
                if self.taps[i] == 1:
                    new_bit ^= self.state[i]
            new_number.append(new_bit)
            # Сдвигаем регистр и добавляем новый бит
            self.state = [new_bit] + self.state[:-1]

        return int(''.join(map(str, new_number)), 2)    

    def run(self, cycles):
        # Генерация последовательности за указанное количество циклов
        output = []
        for _ in range(cycles):
            output.append(self.step())
        return output

lfsr = LFSR()
