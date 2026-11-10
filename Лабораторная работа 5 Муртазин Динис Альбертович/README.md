# Лабораторная работа 5
Модульное приложение «Алгоритмическая обработка числовых рядов».

## Как запустить:
python main.py --kind sine --n 20 --window 3 --alpha 0.3 --seed 7

## Режимы:
python main.py --kind random --n 10 --save data.json
python main.py --load data.json --window 5

## Аргументы:
--kind: random, sine, trend (тип ряда)
--n: количество точек
--window: размер окна для скользящей средней
--alpha: коэффициент для EMA
--seed: зерно для генератора случайных чисел
--save: сохранить ряд в JSON
--load: загрузить ряд из файла (JSON/TXT/CSV)