# Job Sites parser
the program fetch info from hh.ru and superjob.ru and get salary statistics

## System requirements:

python3.6

## Setup instruction:
```bash
$ pip install -r requirements.txt
```

## How to run:

```bash
$ python main.py
+HeadHunter Statistic---+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| python                | 1416             | 993                 | 162788.02        |
| java                  | 1776             | 800                 | 199443.75        |
| ruby                  | 209              | 106                 | 198311.32        |
| javascript            | 2538             | 1500                | 181316.67        |
+-----------------------+------------------+---------------------+------------------+

+SuperJob Statistic-----+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| python                | 13               | 8                   | 76625.0          |
| java                  | 32               | 6                   | 129916.67        |
| ruby                  | 1                | 1                   | 90000.0          |
| javascript            | 42               | 9                   | 70500.0          |
+-----------------------+------------------+---------------------+------------------+
```

Also, you can change search template and language list, by editing vars in main.py

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.

