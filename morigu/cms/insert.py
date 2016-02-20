# -*- coding: utf-8 -*-
from book.models import Book
b = Book(name='Beatles Blog', publisher='All the latest Beatles news.')
b.save()
