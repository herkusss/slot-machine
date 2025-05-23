import customtkinter as ctk
from PIL import Image
import random
import os
import storage
from machine_factory import SlotMachineFactory
from player import Player

class SlotMachineCustomGUI:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("600x400+500+250")
        self.app.overrideredirect(True)
        self.player = None
        self.reel_labels = []
        self.result_label = None

        slot_icon_path = os.path.join("assets", "slot_icon.png")
        img = Image.open(slot_icon_path)
        img = img.resize((32, 32))
        self.slot_icon = ctk.CTkImage(light_image=img, dark_image=img, size=(32, 32))

        self.symbol_images = self.load_symbol_images()

        self.top_bar = ctk.CTkFrame(self.app, height=50, corner_radius=0)
        self.top_bar.pack(fill="x", side="top")
        self.top_bar.pack_propagate(False)

        icon_label = ctk.CTkLabel(self.top_bar, image=self.slot_icon, text="")
        icon_label.pack(side="left", padx=(10, 0))
        title_label = ctk.CTkLabel(
            self.top_bar,
            text="Slot Machine",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold")
        )
        title_label.pack(side="left", padx=(5, 0))

        close_button = ctk.CTkButton(
            self.top_bar,
            text="✖",
            width=30,
            height=30,
            command=self.close_app,
            fg_color="#FF4444",
            hover_color="#CC3333",
            font=ctk.CTkFont(size=14)
        )
        close_button.pack(side="right", padx=5)

        self.top_bar.bind("<ButtonPress-1>", self.start_move)
        self.top_bar.bind("<B1-Motion>", self.do_move)

        self.init_name_screen()

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def do_move(self, event):
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.app.geometry(f"+{x}+{y}")

    def load_symbol_images(self):
        symbols = ["cherry", "lemon", "bell", "star", "seven"]
        images = {}
        for symbol in symbols:
            path = os.path.join("assets", f"{symbol}.png")
            img = Image.open(path)
            img = img.resize((96, 96))
            images[symbol] = ctk.CTkImage(light_image=img, dark_image=img, size=(96, 96))
        return images

    def init_name_screen(self):
        for widget in self.app.winfo_children():
            if widget is not self.top_bar:
                widget.destroy()

        ctk.CTkLabel(
            self.app,
            text="Enter Your Username",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold")
        ).pack(pady=30)

        self.name_entry = ctk.CTkEntry(
            self.app,
            placeholder_text="Enter your name",
            font=ctk.CTkFont(size=16)
        )
        self.name_entry.pack(pady=15)

        ctk.CTkButton(
            self.app,
            text="Start",
            command=self.start_game,
            font=ctk.CTkFont(size=16)
        ).pack(pady=15)

    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            return
        balance = storage.load_balance(name)
        machine = SlotMachineFactory.create_machine("classic")
        self.player = Player(name, balance, machine)
        self.init_game_screen()

    def init_game_screen(self):
        for widget in self.app.winfo_children():
            if widget is not self.top_bar:
                widget.destroy()

        content = ctk.CTkFrame(self.app, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=(10,20))

        self.balance_label = ctk.CTkLabel(
            content,
            text=f"Balance: {self.player.get_balance()} coins",
            font=ctk.CTkFont(family="Segoe UI", size=20)
        )
        self.balance_label.pack(pady=(0,20))

        reel_frame = ctk.CTkFrame(content, fg_color="transparent")
        reel_frame.pack(pady=(0,20))
        self.reel_labels.clear()
        for _ in range(3):
            lbl = ctk.CTkLabel(reel_frame, image=self.symbol_images["cherry"], text="")
            lbl.pack(side="left", padx=15)
            self.reel_labels.append(lbl)

        self.result_label = ctk.CTkLabel(
            content,
            text="",
            text_color="red",
            font=ctk.CTkFont(family="Segoe UI", size=14)
        )
        self.result_label.pack(pady=(20,20))

        self.entry_bet = ctk.CTkEntry(
            content,
            placeholder_text="Enter bet",
            width=150,
            font=ctk.CTkFont(size=16)
        )
        self.entry_bet.insert(0, "10")
        self.entry_bet.pack(pady=(0,20))

        spin_button = ctk.CTkButton(
            content,
            text="SPIN",
            command=self.spin,
            font=ctk.CTkFont(size=18),
            fg_color="#228B22",
            hover_color="#1E7A1E",
            text_color="white",
            width=200
        )
        spin_button.pack(pady=(0,10))

    def spin(self):
        try:
            bet = int(self.entry_bet.get())
            if bet <= 0:
                raise ValueError
        except ValueError:
            self.result_label.configure(text="Enter a valid bet.", text_color="red")
            return

        if bet > self.player.get_balance():
            self.result_label.configure(text="Insufficient balance.", text_color="red")
            return

        symbol_keys = list(self.symbol_images.keys())
        result = [random.choice(symbol_keys) for _ in range(3)]
        for i, symbol in enumerate(result):
            self.reel_labels[i].configure(image=self.symbol_images[symbol])

        payout = self.player.machine.calculate_payout(result, bet)
        
        self.player._balance = self.player.get_balance() - bet + payout
        self.balance_label.configure(text=f"Balance: {self.player.get_balance()} coins")

        if payout > 0:
            self.result_label.configure(text=f"You won {payout} coins!", text_color="green")
        else:
            self.result_label.configure(text="No win this time.", text_color="red")

        storage.save_balance(self.player.name, self.player.get_balance())

        if self.player.get_balance() == 0:
            self.result_label.configure(text="You ran out of coins!", text_color="red")
            self.app.after(1000, self.close_app)


    def close_app(self):
        self.app.quit()

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    gui = SlotMachineCustomGUI()
    gui.run()
