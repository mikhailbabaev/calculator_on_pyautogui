import time

import pyautogui
import pytest

from main import check_os, theme_is, calculate_process


def test_calculate_process(monkeypatch):
    """Тестирует процесс вычислений в калькуляторе.

    1. Проверяется операционная система с помощью функции `check_os()`.
    2. Определяется тема калькулятора с помощью функции `theme_is()`,
        которая возвращает изображения кнопок в зависимости от темы.
    3. Для каждого выражения из списка `expressions`:
        - Мокируется ввод с помощью `monkeypatch` для имитации ввода.
        - Вызывается функция `calculate_process()`.

    Выражения для теста можно вносить в переменную expressions.
    """

    check_os()
    button_images = theme_is()

    if button_images:  # Если кнопки определены, продолжаем
        expressions = ['12+7', '45-23', '56*7', '100/5', 'exit']

        for expression in expressions:
            if expression != 'exit':
                monkeypatch.setattr('builtins.input', lambda _: expression)
                calculate_process(button_images)
            else:
                print("Выход из программы.")
                break
            pyautogui.click(button_images['CE'])
            time.sleep(0.5)
