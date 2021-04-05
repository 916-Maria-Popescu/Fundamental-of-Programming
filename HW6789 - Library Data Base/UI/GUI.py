from tkinter import *
from PIL import ImageTk, Image



class GUI:
    def __init__(self, book_service, client_service, rental_service):
        self.root = Tk()
        self.book_service = book_service
        self.client_service = client_service
        self.rental_service = rental_service

    def create_gui(self):

        my_image = ImageTk.PhotoImage(Image.open('C:\\Users\\Maria\\Desktop\\library1.png'))
        main_label = Label(self.root, image=my_image, height=899, width=989)
        main_label.pack()

        book_button = Button(main_label, text='Books', command=lambda: self.books_gui(main_label))
        book_button.place(height=70, width=160, relx=0.1, rely=0.3)

        client_button = Button(main_label, text='Client')
        client_button.place(height=70, width=160, relx=0.4, rely=0.3)

        rental_button = Button(main_label, text='Rentals')
        rental_button.place(height=70, width=160, relx=0.7, rely=0.3)

        undo_button = Button(main_label, text='UNDO')
        undo_button.place(height=90, width=90, relx=0.1, rely=0.52)

        redo_button = Button(main_label, text='REDO')
        redo_button.place(height=90, width=90, relx=0.4, rely=0.52)

        self.root.mainloop()

    def books_gui(self, parent):
        book_frame = Frame(parent)
        book_frame.place(height=899, width=989, relx=0.0001, rely=0.0001)
        #my_image = ImageTk.PhotoImage(Image.open('C:\\Users\\Maria\\Desktop\\library2.png'))
        #books_label = Label(self.root, image=my_image, height=700, width=675)
        #books_label.pack()



        add_button = Button(books_label, text='add a book')
        add_button.place(height=40, width=70, relx=0.08, rely=0.1)

        remove_button = Button()
        remove_button.place()

        update_button = Button()
        update_button.place()

        list_all = Button()
        list_all.place()

        exit_button = Button(books_label, text='exit', bg='red', command=lambda: books_label.destroy())
        exit_button.place(height=30, width=50, relx=0.9, rely=0.9)





    def clients_gui(self):
        pass

    def rentals_gui(self):
        pass



