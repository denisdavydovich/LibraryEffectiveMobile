import json
from typing import List, Dict


def load_books(file_path: str) -> List[Dict[str, str]]:
    """
    Загружает библиотеку из файла JSON.
    Если файл отсутствует или поврежден, возвращает пустую библиотеку.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(file_path: str, books: List[Dict[str, str]]) -> None:
    """Сохраняет список книг в файл JSON."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book(books: List[Dict[str, str]], title: str, author: str, year: str) -> None:
    """Добавляет новую книгу в библиотеку."""
    new_id = str(len(books) + 1)  # Простой способ генерировать ID.
    books.append({
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии"
    })


def remove_book(books: List[Dict[str, str]], book_id: str) -> bool:
    """
    Удаляет книгу из библиотеки по ID.
    Возвращает True, если книга была удалена, иначе False.
    """
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return True
    return False


def search_books(books: List[Dict[str, str]], query: str) -> List[Dict[str, str]]:
    """
    Ищет книги по ключевому слову в названии, авторе или году издания.
    Возвращает список найденных книг.
    """
    query = query.lower()
    return [book for book in books if
            query in book["title"].lower() or
            query in book["author"].lower() or
            query in book["year"]]


def update_status(books: List[Dict[str, str]], book_id: str, new_status: str) -> bool:
    """
    Обновляет статус книги по ID.
    Возвращает True, если статус обновлен, иначе False.
    """
    for book in books:
        if book["id"] == book_id:
            if new_status in ["в наличии", "выдана"]:
                book["status"] = new_status
                return True
    return False


def display_books(books: List[Dict[str, str]]) -> None:
    """Печатает список всех книг в библиотеке."""
    if not books:
        print("Библиотека пуста.")
    else:
        for book in books:
            print(f"[{book['id']}] {book['title']} - {book['author']} ({book['year']}) | Статус: {book['status']}")
