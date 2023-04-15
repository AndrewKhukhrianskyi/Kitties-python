'''
Config - это файл, который хранит постоянные выражения (название приложения,
ширина и высота экрана и тп)

Правила оформления: названия переменных идет всегда с больших букв
(ex: HEIGHT = ...)
'''

# Параметры окна

TITLE = 'Анализатор текста v.1.0.0'

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 500

RESIZABLE_WINDOW_STATUS = False, False

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2

TEXT_FIELD_WIDTH = 45
TEXT_FIELD_HEIGHT = 10

REGEX_TEXT_WIDTH = 40
REGEX_TEXT_HEIGHT = 1

LABEL_WIDTH = 30

# Работа с текстом
ANALYZE_TEXT_LIST = ["Кол-во гласных букв:",
                     "Кол-во согласных букв:",
                     "Кол-во символов:",
                     "Часто встречаемая буква:",
                     "Редко встречаемая буква:",
                     "Не встречаемая буква:",
                     "Кол-во чисел:",
                     "Среднее арифметическое по кол-ву текста:"]

LANGUAGE_RU ='абвгдеёжзийклмнопрстюфхцчшщьъэюя'
LANGUAGE_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
LANGUAGE_EN = 'abcdefghijklmnopqrstuvwxyz'
