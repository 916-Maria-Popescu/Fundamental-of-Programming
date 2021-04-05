"""
    Entity class should be coded here
"""

class Book:
    def __init__(self, isbn, author, title):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    @property
    def isbn(self):
        return self.__isbn

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title


    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @author.setter
    def author(self, author_name):
        self.__author = author_name

    @title.setter
    def title(self, title_name):
        self.__title = title_name

    def __str__(self) -> str:
        if self.__title==" ":
            return ("isbn: {0}, author: {1}").format(self.__isbn, self.__author)
        else:
            return ("isbn: {0}, author: {1}, title: {2}").format(self.__isbn, self.__author, self.__title)






