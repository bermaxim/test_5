import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

amplitude_x = 1  # Амплитуда по оси x
amplitude_y = 1  # Амплитуда по оси y
frequency_x = 2  # Частота колебаний по оси x
frequency_y = 3  # Частота колебаний по оси y
phase_shift = np.pi / 2  # Сдвиг фазы по оси x
time = np.linspace(0, 2 * np.pi, 100)  # Массив значений времени от 0 до 2π с равным шагом

fig, ax = plt.subplots()
line, = ax.plot([], [])

# Функция для инициализации графика
def initialize_figure():
    ax.set_xlim(-amplitude_x, amplitude_x)  # Установка пределов оси x
    ax.set_ylim(-amplitude_y, amplitude_y)  # Установка пределов оси y
    return line,

# Функция для обновления графика на каждом кадре
def update_figure(frame):
    angle = frame * 0.1  # Вычисление угла поворота фигуры
    x = amplitude_x * np.sin(frequency_x * time + phase_shift)  # Вычисление координаты x
    y = amplitude_y * np.sin(frequency_y * time + angle)  # Вычисление координаты y
    line.set_data(x, y)  # Установка новых координат для линии
    return line,

# Создание анимации
ani = animation.FuncAnimation(fig, update_figure, frames=180, init_func=initialize_figure, blit=False)

plt.xlabel('X')  # Название оси x
plt.ylabel('Y')  # Название оси y
plt.title('Анимированная фигура Лиссажу')  # Заголовок графика
plt.grid(True)  # Включение сетки на графике
plt.show()  # Отображение графика