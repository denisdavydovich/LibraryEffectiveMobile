from library import (
    load_books, save_books, add_book,
    remove_book, search_books, update_status, display_books
)


def menu_add_book(books: list, file_path: str) -> None:
    """Добавить книгу."""
    title = input("Название книги: ")
    author = input("Автор книги: ")
    year = input("Год издания: ")
    add_book(books, title, author, year)
    save_books(file_path, books)
    print("Книга успешно добавлена.")


def menu_remove_book(books: list, file_path: str) -> None:
    """Удалить книгу."""
    book_id = input("Введите ID книги для удаления: ")
    if remove_book(books, book_id):
        save_books(file_path, books)
        print("Книга успешно удалена.")
    else:
        print("Книга с таким ID не найдена.")


def menu_search_books(books: list) -> None:
    """Поиск книги."""
    query = input("Введите запрос для поиска (название, автор или год): ")
    found_books = search_books(books, query)
    if found_books:
        print("Найденные книги:")
        display_books(found_books)
    else:
        print("Книги не найдены.")


def menu_display_books(books: list) -> None:
    """Показать все книги."""
    print("Список книг:")
    display_books(books)


def menu_update_status(books: list, file_path: str) -> None:
    """Изменить статус книги."""
    book_id = input("Введите ID книги: ")
    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
    if update_status(books, book_id, new_status):
        save_books(file_path, books)
        print("Статус книги обновлен.")
    else:
        print("Ошибка: либо ID книги не найден, либо указан неверный статус.")


def main():
    file_path = 'storage.json'
    books = load_books(file_path)  # Загружаем книги при старте.

    # Словарь доступных команд
    menu_actions = {
        "1": lambda: menu_add_book(books, file_path),
        "2": lambda: menu_remove_book(books, file_path),
        "3": lambda: menu_search_books(books),
        "4": lambda: menu_display_books(books),
        "5": lambda: menu_update_status(books, file_path),
        "0": lambda: exit("Выход из программы. До свидания!")
    }

    while True:
        print("\n=== Меню ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")
        action = menu_actions.get(choice)

        if action:
            action()  # Выполнить соответствующую функцию
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()

