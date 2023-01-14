BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    lst = [',', '.', '!', ':', ';', '?']
    for i in range(start + size - 1, start, -1):
        if len(text) <= i or text[i] in lst and (text[i + 1] != '.' and text[i + 1] != '!' and text[i + 1] != '"'):
            stop = i
            break
    sr = text[start:stop + 1]
    return (sr, len(sr))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        data = file.read()
    exit = len(data)
    st = 0
    ls = 1
    while exit > 0:
        tup = _get_part_text(data, st, PAGE_SIZE)
        book[ls] = tup[0].strip()
        st += tup[1]
        ls += 1
        exit -= tup[1]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)