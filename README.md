# Проект асинхронного парсинга
# Стек технологий
Python, Scrapy

# Описание
Парсинг данных со страницы https://peps.python.org. Парсер подготавливает данные и сохраняет их в два файла формата csv в папку results.
первый файл — список всех PEP: номер, название и статус.
второй файл — сводку по статусам PEP, сколько найдено документов в каждом статусе (статус, количество).

# Как запустить проект локально:
## Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/KoaN1010101/scrapy_parser_pep.git
```
- Перейти в директорию проекта:
```
cd bs4_parser_pep
```
- Создать виртуальное окружение:
```
python -m venv venv
```
- Установить зависимости:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Запустить парсер
```
scrapy crawl pep
```

## Автор

Никулин Владимир
