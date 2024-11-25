import unittest
from library import (
    add_book, remove_book, search_books, update_status
)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """
        Создаем библиотеку для тестов.
        """
        self.books = [
            {"id": "1", "title": "Война и мир", "author": "Лев Толстой", "year": "1869", "status": "в наличии"},
            {"id": "2", "title": "Преступление и наказание", "author": "Федор Достоевский", "year": "1866", "status": "выдана"},
            {"id": "3", "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": "1967", "status": "в наличии"},
        ]

    def test_add_book(self):
        """
        Тестируем добавление книги.
        """
        add_book(self.books, "1984", "Джордж Оруэлл", "1949")
        self.assertEqual(len(self.books), 4, "Книга не добавлена в библиотеку")
        self.assertEqual(self.books[-1]["title"], "1984", "Название книги некорректно")
        self.assertEqual(self.books[-1]["author"], "Джордж Оруэлл", "Автор книги некорректен")
        self.assertEqual(self.books[-1]["status"], "в наличии", "Статус книги должен быть 'в наличии'")

    def test_remove_book(self):
        """
        Тестируем удаление книги по ID.
        """
        result = remove_book(self.books, "2")
        self.assertTrue(result, "Книга с ID 2 должна быть удалена")
        self.assertEqual(len(self.books), 2, "Размер библиотеки после удаления некорректен")
        self.assertFalse(any(book["id"] == "2" for book in self.books), "Книга с ID 2 осталась в библиотеке")

        result_invalid = remove_book(self.books, "99")
        self.assertFalse(result_invalid, "Удаление несуществующей книги должно возвращать False")

    def test_search_books(self):
        """
        Тестируем поиск книг.
        """
        results = search_books(self.books, "Толстой")
        self.assertEqual(len(results), 1, "Поиск по автору 'Толстой' должен вернуть одну книгу")
        self.assertEqual(results[0]["author"], "Лев Толстой", "Автор найденной книги некорректен")

        results_year = search_books(self.books, "1967")
        self.assertEqual(len(results_year), 1, "Поиск по году '1967' должен вернуть одну книгу")
        self.assertEqual(results_year[0]["year"], "1967", "Год найденной книги некорректен")

        results_not_found = search_books(self.books, "Шекспир")
        self.assertEqual(len(results_not_found), 0, "Поиск несуществующей книги должен вернуть пустой список")

    def test_update_status(self):
        """
        Тестируем обновление статуса книги.
        """
        result = update_status(self.books, "1", "выдана")
        self.assertTrue(result, "Статус книги с ID 1 должен обновиться")
        self.assertEqual(self.books[0]["status"], "выдана", "Статус книги с ID 1 должен быть 'выдана'")

        result_invalid_id = update_status(self.books, "99", "в наличии")
        self.assertFalse(result_invalid_id, "Обновление статуса для несуществующей книги должно вернуть False")

        result_invalid_status = update_status(self.books, "1", "потеряна")
        self.assertFalse(result_invalid_status, "Обновление статуса на некорректный должно вернуть False")
        self.assertNotEqual(self.books[0]["status"], "потеряна", "Статус книги с ID 1 не должен измениться на некорректный")


if __name__ == "__main__":
    unittest.main()
