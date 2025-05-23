class Player:
    def __init__(self, name, balance, machine):
        self.name = name
        self._balance = balance
        self.machine = machine

    def play(self, bet):
        if bet <= 0:
            raise ValueError("Bet must be a positive number.")
        if bet > self._balance:
            print("Not enough balance.")
            return

        self._balance -= bet
        result = self.machine.spin()
        payout = self.machine.calculate_payout(result, bet)
        self._balance += payout
        
        print(f"Spin result: {result}")
        print(f"You won: {payout} coins.")
        print(f"New balance: {self._balance}")

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance
