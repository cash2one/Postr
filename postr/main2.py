import tkinter
from tkinter.ttk import Notebook

# Widgets
from tkinter import Tk, Listbox, Frame, Button, Label

# Locations
from tkinter import LEFT, TOP, MULTIPLE, END, BOTTOM, RIGHT

# Widget helpers
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
from tkinter import filedialog
from tkinter import StringVar

from typing import Iterator
from postr.twitter_postr import Twitter


twitter = Twitter()


def setup(main_gui: Tk) -> Tk:
    main_gui.title('Postr')
    main_gui.geometry('800x400')

    # a fix for running on OSX - to center the title text vertically
    if main_gui.tk.call('tk', 'windowingsystem') == 'aqua':  # only for OSX
        s = tkinter.ttk.Style()
        # Note: the name is specially for the text in the widgets
        s.configure('TNotebook.Tab', padding=(12, 8, 12, 0))
    return main_gui


def setup_apis(page: Frame) -> Listbox:
    page_l = Frame(page)
    page_l.pack(side=LEFT, padx=20)

    api_box = Listbox(page_l, selectmode=MULTIPLE, width=15, height=8, font=('Times', 16))
    apis = ['Facebook', 'Tumblr', 'Instagram', 'Twitter', 'Reddit', 'Youtube', 'Discord', 'Slack']
    for api in apis:
        api_box.insert(END, api)
    api_box.pack(side=LEFT)
    return api_box


class GUI():
    def __init__(self) -> None:
        # setup the gui
        self.root = setup(Tk())
        self.gui = Notebook(self.root)

        # Misc variables for widgets
        self.filepath = StringVar()
        self.filepath.set('No file uploaded')
        self.io_error = StringVar()
        self.io_error.set('')

        # Setup the posting page
        page1 = Frame(self.gui)

        self.api_box = setup_apis(page1)
        self.setup_automation_buttons(page1)
        self.text_box = self.setup_text_box(page1)
        self.setup_IO_buttons(page1)
        self.gui.add(page1, text='Posting')

        # Setup the scheduling ppage
        page2 = Frame(self.gui)
        self.gui.add(page2, text='Scheduling')

        # Setup the analytics page
        page3 = Frame(self.gui)
        self.gui.add(page3, text='Analytics')

        # Setup the config parser page
        page4 = Frame(self.gui)
        self.gui.add(page4, text='Config')

        # Pack out gui
        self.gui.pack(expand=1, fill='both')

    def setup_text_box(self, page: Frame) -> ScrolledText:
        page_r = Frame(page)
        page_r.pack(side=RIGHT)

        comment_area = ScrolledText(master=page_r, wrap=tkinter.WORD, width=40, height=6, bg='grey')
        comment_area.insert(tkinter.INSERT, 'Enter your comment here')
        comment_area.pack()

        Button(page_r, text='Upload file', command=self.open_file_dialog).pack(side=TOP, anchor='s')
        Label(page_r, textvariable=self.filepath).pack(side=TOP, anchor='s')
        return comment_area

    def setup_automation_buttons(self, page: Frame) -> None:
        page_l = Frame(page)
        page_l.pack(side=LEFT)

        Button(page_l, text='Post text', command=self.post_text).pack(side=TOP)
        Button(page_l, text='Post picture w/text', command=self.post_pic).pack(side=TOP, anchor='s')
        Label(page_l, textvariable=self.io_error, fg='red').pack(side=BOTTOM, anchor='s')

    def setup_IO_buttons(self, page: Frame) -> None:
        page_r = Frame(page)
        page_r.pack(side=RIGHT)

        Button(page_r, text='Clear comment', command=self.clear_comment).pack(side=TOP, anchor='s')
        Button(page_r, text='Clear file', command=self.clear_file).pack(side=TOP, anchor='s')

    def api_iterator(self) -> Iterator[str]:
        api_cache = {
            0: 'Facebook', 1: 'Tumblr', 2: 'Instagram', 3: 'Twitter',
            4: 'Reddit', 5: 'Youtube', 6: 'Discord', 7: 'Slack',
        }
        selected_as_codes = self.api_box.curselection()
        api_list = [api_cache[code] for code in selected_as_codes]

        for api in api_list:
            yield api

    def post_text(self) -> None:
        text = str(self.text_box.get(1.0, END)).strip()

        if not text:
            self.io_error.set('Error: no text found')
            return

        self.io_error.set('')

        try:
            for api in self.api_iterator():
                if api == 'Twitter':
                    twitter.post_text(text)
                else:
                    pass
        except Exception:
            self.io_error.set('An API failed to post text')

    def post_pic(self) -> None:
        text = str(self.text_box.get(1.0, END))
        url = self.filepath.get()

        if url == 'No file uploaded':
            self.io_error.set('Error: no file found')
            return

        self.io_error.set('')

        try:
            for api in self.api_iterator():
                if api == 'Twitter':
                    twitter.post_photo(url, text)
                else:
                    pass
        except Exception:
            self.io_error.set('An API failed to post a photo')

    def clear_comment(self) -> None:
        self.text_box.delete('1.0', END)
        self.text_box.insert('1.0', 'Enter your comment here')

    def clear_file(self) -> None:
        self.filepath.set('No file uploaded')

    def open_file_dialog(self) -> None:
        self.filepath.set(filedialog.askopenfilename(
            initialdir='/', title='Select a file',
            filetypes=(('jpeg', '*.jpg'), ('png', '*.png'), ('All files', '*.*')),
        ))


if __name__ == '__main__':
    g = GUI()
    g.root.mainloop()
