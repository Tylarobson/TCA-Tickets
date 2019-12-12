from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.tickets_image = PhotoImage(file="U:\\Practice\\ticket.gif")
        
        self.title("Tickets")
        self.configure(padx=10, pady=10)

        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_tickets_image_label()
        self.__add_buy_button()
        
    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure (  font="Arial 24",
                                        text="Entrance Ticket")

    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid (row=1, column=0, sticky=W)
        self.instruction_label.configure(text="How many tickets are needed?")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, pady=10)

    def __add_tickets_image_label(self):
        self.tickets_image_label = Label ()
        self.tickets_image_label.grid(row=2, column=3)
        self.tickets_image_label.configure(image=self.tickets_image, height=60, width=60)

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)
        self.buy_button.configure(text="buy")
        self.buy_button.configure(text="Submit")
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        num_tickets = int(self.tickets_entry.get())
        if (num_tickets == 1):
            messagebox.showinfo("Clicked","You have purchased 1 ticket")
        elif (num_tickets > 1):
            messagebox.showinfo("Clicked","You have purchased {} tickets".format(num_tickets))
        else:
            messagebox.showerror("Clicked", "You have entered an invalid number of tickets!")
    

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()