import os
import time

import pyautogui

from buttons import light_button_images, dark_button_images


def check_os() -> None:
    """Проверяет операционную систему и открывает калькулятор в Windows."""
    if os.name == 'nt':
        os.system('calc')
    elif os.name == 'posix':
        if os.uname().sysname == 'Darwin':
            print('Вы обладатель macOS. К сожалению,'
                  'данная программа сейчас работает лишь на windows'
                  )
        else:
            print('Вы обладатель Linux. К сожалению,'
                  'данная программа сейчас работает лишь на windows'
                  )
    else:
        print('Неизвестная операционная система.')
    time.sleep(1)


def theme_is() -> str:
    """Определяет тему оформления, затем запрашивает выражение и
    выполняет его ввод в калькулятор с помощью кликов."""

    try:
        if pyautogui.locateCenterOnScreen('light_theme/1.png', confidence=0.9):
            return light_button_images
    except pyautogui.ImageNotFoundException:
        pass

    try:
        if pyautogui.locateCenterOnScreen('dark_theme/1.png', confidence=0.9):
            return dark_button_images
    except pyautogui.ImageNotFoundException:
        pass
    else:
        return None


def click_button(image: str) -> None:
    """
    Находит кнопку на экране и выполняет клик.

    :на вход image: Имя файла изображения кнопки.
    """
    location = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    if location:
        pyautogui.click(location)
        time.sleep(0.5)
    else:
        print(f'Кнопка {image} не найдена.')


def calculate_process(button_images: dict) -> None:
    """Запрашивает у пользователя выражение и выполняет его ввод в
    калькулятор с помощью кликов.

    на вход button_image: словарь путей к изображениям кнопок"""

    if not button_images:
        print('Не удалось определить тему оформления.'
              'Проверьте изображения кнопок.'
              )
    expression = input('Введите математическое выражение (например, 12+34=):')

    if expression.lower() == 'exit':
        print("Выход из программы.")
        exit()

    for char in expression:
        if char in button_images:
            click_button(button_images[char])
            time.sleep(0.5)
        else:
            print(f'Символ {char} не поддерживается.')
    click_button(button_images['='])


def main() -> None:
    """Основная функция программы."""
    check_os()
    button_images = theme_is()
    while True:
        calculate_process(button_images)


if __name__ == "__main__":
    main()
