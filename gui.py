from tkinter import *
from tkinter import ttk
from api_calls import api_convert

window = Tk()
window.title("Currency Conversion Tool")

tabControl = ttk.Notebook(window)
convert_tab = Frame(tabControl)
rate_tab = Frame(tabControl)
tabControl.add(convert_tab, text='Convert')
tabControl.add(rate_tab, text='Exchange Rates')
tabControl.grid(row=0, column=0)


class Gui:
    def __init__(self):
        # Gui Labels ---------------------------------------------------------------------------------------------------

        self.amount_label = Label(convert_tab, text="Amount:", bg='white', font=('comic sans', 15))
        self.amount_label.grid(row=1, column=0, padx=8, pady=10)

        self.convert_from_label = Label(convert_tab, text="From:", bg='white', font=('comic sans', 15))
        self.convert_from_label.grid(row=1, column=1, padx=10, pady=10)

        self.convert_to_label = Label(convert_tab, text="To:", bg='white', font=('comic sans', 15))
        self.convert_to_label.grid(row=1, column=2, padx=10, pady=10)

        # User Input ---------------------------------------------------------------------------------------------------
        # Amount Entry
        self.amount_entry = Entry(convert_tab, width=12)
        self.amount_entry.grid(row=2, column=0, pady=10)

        # Drop Down Menu Options
        self.options = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY"]

        # Convert From Drop Down Button
        self.from_selected = StringVar()
        self.from_selected.set("USD")
        self.convert_from_choice = OptionMenu(convert_tab, self.from_selected, *self.options )
        self.convert_from_choice.grid(row=2, column=1)

        # Convert To Drop Down Button
        self.to_selected = StringVar()
        self.to_selected.set("USD")
        self.convert_to_choice = OptionMenu(convert_tab, self.to_selected, *self.options )
        self.convert_to_choice.grid(row=2, column=2)

        # Convert Button

        self.convert = Button(convert_tab, text='Convert', width=25,  command=self.run_convert)
        self.convert.grid(row=3, column=0, pady=10)

        # Conversion Result

        #self.result_display = f"{self.converted_amount} {self.to_selected}"
        self.result_label = Label(convert_tab, text="Click Convert to view converted currency", bg='white', font=('comic sans', 15))
        self.result_label.grid(row=4, column=0, pady=10, columnspan=3)

    def run_convert(self):
        #print(api_convert(self.to_selected.get(), self.from_selected.get(), self.amount_entry.get()))
        self.result_label.config(text=api_convert(self.to_selected.get(), self.from_selected.get(), self.amount_entry.get()))






gui = Gui()
window.mainloop()
