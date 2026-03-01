import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    

    @pytest.mark.parametrize('name', [
        '',
        'Радости и горести знаменитой Молль Флендерс, которая родилась в Ньюгетской тюрьме и в течение шести десятков лет своей разнообразной жизни (не считая детского возраста) была двенадцать лет содержанкой, пять раз замужем (из них один раз за своим братом), двенадцать лет воровкой, восемь лет ссыльной в Виргинии, но под конец разбогатела, стала жить честно и умерла в раскаянии. Написано по ее собственным заметкам'
    ])
    def test_add_new_book_with_invalid_length(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драма')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Дракула')

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        collector.set_book_genre('Дракула', 'Ужасы')

        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Гордость и предубеждение и зомби' in horror_books
        assert 'Дракула' in horror_books

    def test_get_books_for_children_returns_only_books_without_age_rating(self):

        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Малыш и Карлсон')
        collector.add_new_book('Ривизор')
        collector.add_new_book('Дракула')
        collector.add_new_book('Приключения Шерлока Холмса')

        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Малыш и Карлсон', 'Мультфильмы')
        collector.set_book_genre('Ривизор', 'Комедии')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')

        children_books = collector.get_books_for_children()

        assert len(children_books) == 3
        assert 'Дюна' in children_books
        assert 'Малыш и Карлсон' in children_books
        assert 'Ривизор' in children_books
        assert 'Дракула' not in children_books
        assert 'Приключения Шерлока Холмса' not in children_books

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        favorites = collector.get_list_of_favorites_books()
        assert 'Дюна' in favorites

    def test_add_book_in_favorites_twice_does_not_duplicate(self):

        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1

    def test_delete_book_from_favorites_removes_book(self):

        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        favorites = collector.get_list_of_favorites_books()
        assert 'Дюна' in favorites

        collector.delete_book_from_favorites('Дюна')

        assert len(favorites) == 0

