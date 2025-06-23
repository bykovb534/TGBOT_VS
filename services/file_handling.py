import os
import sys

BOOK_PATH = "book/book.txt"
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text, start, page_size):
    a = ',.!?;:'
    txt = ''
    kon = start+page_size
    if kon > len(text):
        txt = text[start: len(text)]
        dl = len(text)-start
    else:
        for i in range(kon-1, start, -1):
            if text[i] in a:
                if text[i+1] in a:
                    continue
                txt = text[start: i+1]
                dl = i-start+1
                break
    return txt, dl

book: dict[int, str] = {}
PAGE_SIZE = 1050
# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    pass
    start = 0
    num = 1
    with open(path, 'r', encoding='utf-8') as inf:
        text = inf.read()
        while start < len(text):
            page_text, dl = _get_part_text(text, start, PAGE_SIZE)
            if page_text:
                book[num] = page_text.lstrip()
                num+=1
                start+=dl
            else:
                break

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))