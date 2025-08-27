import tkinter as tk
import random

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("100 спичек")
        self.geometry("900x500")
        self.im=tk.PhotoImage(file='pic.png')
        self.img =tk.Label(image=self.im)
        self.img.place(x=50,y=250)
        self.configure(background='MistyRose3')
        self.list_frame = tk.Frame(self)
        self.list_frame.pack(pady=20)
        self.label = tk.Label(self.list_frame, text="Спички: 100",font='Arial 12 bold', width=18)
        self.label.pack()
        self.entry = tk.Entry(self.list_frame)
        self.entry.pack()
        self.button = tk.Button(self.list_frame, text="Взять спички",font='Arial 12', width=11, command=self.take_matches)
        self.button.pack()
        self.remaining_matches = 100
        self.player_turn = True

    def take_matches(self):
        if self.remaining_matches == 0:
            return
        number = self.entry.get()
        number = int(number)
        if self.get_valid_input():
            self.remaining_matches -= number
            self.update_label()
            if self.remaining_matches == 0:
                self.show_result("Вы проиграли!")
                self.pg = tk.PhotoImage(file='проигрыш.png')
                self.pgg = tk.Label(image=self.pg)
                self.pgg.place(x=50, y=40)
            else:
                self.computer_turn()

    def get_valid_input(self):
        number = self.entry.get()
        try:
            number = float(number)
            if 1 <= number <= 10 and number <= self.remaining_matches:
                self.entry.delete(0, tk.END)
                return True

            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Неверный ввод")
                return False
        except ValueError:
            self.entry.delete(0, tk.END)
            return 0
            
    def computer_turn(self):
        if self.remaining_matches == 0:
            return
        number = self.remaining_matches - 1 if self.remaining_matches > 1 else 1
        number = min(number, random.randint(1, 10))
        if self.remaining_matches == 2:
            number = 1
        if self.remaining_matches == 3:
            number = 2
        if self.remaining_matches == 4:
            number = 3
        if self.remaining_matches == 5:
            number = 4
        if self.remaining_matches == 6:
            number = 5
        if self.remaining_matches == 7:
            number = 6
        if self.remaining_matches == 8:
            number = 7
        if self.remaining_matches == 9:
            number = 8
        self.remaining_matches -= number
        self.update_label()
        if self.remaining_matches == 0:
            self.show_result("Компьютер проиграл!")
            self.vg = tk.PhotoImage(file='выигрыш (1).png')
            self.vgg = tk.Label(image=self.vg)
            self.vgg.place(x=50, y=50)
        else:
            self.player_turn = True

    def update_label(self):
        self.label.config(text=f"Спички: {self.remaining_matches}")

    def show_result(self, message):
        result_label = tk.Label(self, text=message,font='Arial 12 bold', width=18)
        result_label.pack(pady=20)
        self.entry.destroy()
        self.button.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()

