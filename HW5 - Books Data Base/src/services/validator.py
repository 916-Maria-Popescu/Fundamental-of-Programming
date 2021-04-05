class LibraryException(Exception):
    pass

class BookValidatorException(LibraryException):
    pass

class BookValidator:
    def validate_isbn (self, book):
        """
    Check if the isbn is valid
        isbn = 978-92-95055-02-5(example)
        An isbn consist of 13 digits (in 5 elements)
    ->Prefix: can only be either 978 or 979. It is always 3 digits in length
    ->Registration group: for the particular zone, may be between 1 and 5 digits in length
    ->Registrant:  for the particular publisher or imprint. This may be up to 7 digits in length
    ->Publication: for the particular edition and format of a specific title, may be up to 6 digits in length
    ->Check digit: the final single digit that mathematically validates the rest of the number """

        isbn_split = book.isbn.split('-')
        if len(book.isbn) != 17 or len(isbn_split) != 5:
            raise BookValidatorException('Invalid isbn')
        if isbn_split[0] != '978' and isbn_split[0] != '979':
            raise BookValidatorException('Invalid isbn - prefix (it can only be 978 or 979)!')
        if len(isbn_split[1]) == 0 or len(isbn_split[1]) > 5:
            raise BookValidatorException('Invalid isbn - The length of registration group may be between 1 and 5 digits')
        if len(isbn_split[2]) > 7:
            raise BookValidatorException('Invalid isbn -the length of the registrant element may be up to t digits')
        if len(isbn_split[3]) > 6:
            raise BookValidatorException('Invalid isbn -the length of the publication element may be up to 6 digits')
        if len(isbn_split[4]) != 1:
            raise BookValidatorException('Invalid isbn - the length of the check digit must be 1 digit')

    def dublicate_isbn(self, book, list):
        b = book.isbn
        for a in list:
            if b == a.isbn:
                raise Exception
