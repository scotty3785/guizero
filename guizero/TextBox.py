from tkinter import Entry, Text, StringVar, END
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

class TextBox(ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin):

    def __init__(self, master, text="", width=10, height=1, multiline=False, grid=None, align=None):

        # Description of this object (for friendly error messages)
        self.description = "[TextBox] object with text \"" + str(text) + "\""

        self._multiline = multiline

        # Set up controlling string variable
        self._text = StringVar()
        self._text.set( str(text) )

        # Create a tk Label object within this object
        if not self._multiline:
            self.tk = Entry(master.tk, textvariable=self._text, width=width)
        else:
            self.tk = Text(master.tk, width=width, height=height)
            self.tk.insert(END,self._text.get())

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)


    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        if self._multiline:
            return self.tk.get(1.0,END)
        else:
            return self._text.get()

    @value.setter
    def value(self, value):
        self._text.set( str(value) )
        if self._multiline:
            self.tk.delete(1.0,END)
            self.tk.insert(END,self._text.get())
        self.description = "[Text] object with text \"" + str(value) + "\""


    # METHODS
    # -------------------------------------------
    # Clear text box
    def clear(self):
        #self.tk.delete(1.0, END)
        self.value = ""

    # Append text
    def append(self, text):
        self.value = self.value + str(text)
        self.description = "[Text] object with text \"" + self.value + "\""


    # DEPRECATED METHODS
    # --------------------------------------------
    # Returns the text
    def get(self):
        return self.value
        utils.deprecated("TextBox get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self.value = text
        utils.deprecated("TextBox set() is deprecated. Please use the value property instead.")
