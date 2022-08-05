from faker import Faker
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod

fig, ax = plt.subplots()

fake = Faker()

class AbcBenchmark(ABC):
    @abstractmethod
    def calculate(self):
        ...


class FirstBenchmark(AbcBenchmark):
    def calculate(self):
        return 10


class SecondBenchmark(AbcBenchmark):
    def calculate(self):
        return 5


class ThirdBenchmark(AbcBenchmark):
    def calculate(self):
        return 20


x = {
    "benchmark_1": FirstBenchmark().calculate(),
    "benchmark_2": SecondBenchmark().calculate(),
    "benchmark_3": ThirdBenchmark().calculate(),
}

sorted_x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


ax.bar(sorted_x.keys(), sorted_x.values())
plt.show()
