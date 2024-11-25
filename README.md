# LibraryEffectiveMobile

## Описание проекта
Эта программа позволяет управлять библиотекой книг: добавлять, удалять, искать, обновлять статус книг, а также просматривать их список. Она поддерживает хранение данных в формате JSON и имеет встроенные тесты для проверки основных функций.

### 📋 Возможности:
Добавление книги – добавление новой книги с указанием названия, автора и года издания.
Удаление книги – удаление книги по её уникальному ID.
Поиск книги – поиск по названию, автору или году издания.
Просмотр всех книг – вывод списка книг с их статусами.
Изменение статуса книги – обновление статуса книги ("в наличии" или "выдана").
Тестирование функций – проверка работы программы с использованием модульных тестов.

### 🚀 Как запустить?
1. Установите Python
2. Запуск программы
Скачайте файлы проекта.
Убедитесь, что все файлы в одной директории.
Запустите файл main.py

### 📂 Файлы проекта:
main.py – точка входа программы.
library.py – функции для работы с библиотекой (добавление, удаление, поиск и т. д.).
test_library.py – модульные тесты для проверки функциональности.
books.json – файл для хранения данных о книгах.

### 🧩 Как пользоваться?
Запустите программу.
Выберите действие из меню:
=== Меню ===
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Показать все книги
5. Изменить статус книги
0. Выход
Следуйте инструкциям на экране.

### 🛠 Тестирование
Для проверки работы программы выполните:

python test_library.py
Если тесты пройдут успешно, вы увидите сообщение: OK.

### Пример использования
1. Добавление книги
Введите:
1
Введите название, автора и год. Пример:

Название: Гарри Поттер
Автор: Джоан Роулинг
Год издания: 1997

Результат:
Книга добавлена!

2. Поиск книги
Введите:
3

Введите ключевое слово, например:
Толстой

Результат:
[1] Война и мир - Лев Толстой (1869) | Статус: в наличии

3. Изменение статуса
Введите:
5

Укажите ID книги и новый статус, например:
ID книги: 1

Новый статус: выдана

Результат:

Статус книги обновлен!

### 📝 Требования

Python 3.7+
Файл books.json для хранения данных.
