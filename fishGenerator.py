class FishPRNG:
    def __init__(self, A0=342856, B0=2345667):
        """
        Инициализация генератора с начальными состояниями A0 и B0.
        """
        self.A = [0] * 55  # Состояние генератора A
        self.B = [0] * 52  # Состояние генератора B

        # Инициализация начальных состояний
        self.A[:2] = [A0 & 0xFFFFFFFF, B0 & 0xFFFFFFFF]
        self.B[:2] = [B0 & 0xFFFFFFFF, A0 & 0xFFFFFFFF]

        for i in range(2, 55):
            self.A[i] = (self.A[i - 1] + self.A[i - 2]) & 0xFFFFFFFF
        for i in range(2, 52):
            self.B[i] = (self.B[i - 1] + self.B[i - 2]) & 0xFFFFFFFF

    def next(self):

        """
        Генерация следующего числа последовательности.
        """
        # Шаг 1: Вычисление Ai и Bi
        Ai = (self.A[-55] + self.A[-24]) % (2**32)
        Bi = (self.B[-52] + self.B[-19]) % (2**32)

        # Обновляем состояния A и B
        self.A.append(Ai)
        self.B.append(Bi)
        self.A.pop(0)
        self.B.pop(0)

        # Шаг 3: Прореживание
        if Bi & 1 == 0:  # Пропускаем текущую пару, если младший бит Bi равен 0
            return self.next()

        # Используем текущие значения Cj и Dj
        Cj = Ai
        Dj = Bi

        # Шаг 4: Генерация 32-битного слова
        Ej = Cj ^ (Dj * self.B[1]) & 0xFFFFFFFF# Dj * D(j+1), берем следующий элемент B
        Fj = (self.B[1] * (Ej & Cj)) & 0xFFFFFFFF  # D(j+1) * (E(j) & C(j))
        Kj = Ej ^ Fj  # Генерация финального значения

        return Kj
    
    def run(self, n):
        lis = []
        for _ in range(n):
            num = self.next()
            lis.append(num)
        return lis
            

fish = FishPRNG(134561, 2436523)

a = fish.run(1000000)
