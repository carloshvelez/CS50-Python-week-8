class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError ("El número de galletas a depositar excede la capacidad restante")


    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError ("El número de galletas a retirar excede la cantidad actual")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("No se admiten número negativos")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n=0):
        self._size = n






def main():
    galleta = Jar()
    galleta.deposit(11)
    print(galleta)

if __name__ == "__main__":
    main()