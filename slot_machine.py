from abc import ABC, abstractmethod
import random

class SlotMachine(ABC):
    def __init__(self, symbols, payout_table):
        self.symbols = symbols
        self.payout_table = payout_table

    @abstractmethod
    def spin(self):
        pass

    def calculate_payout(self, result, bet_amount):
        # Get the payout multiplier for the combination
        multiplier = self.payout_table.get(tuple(result), 0)
        # Return the payout as multiplier * bet_amount
        return multiplier * bet_amount

class ClassicSlotMachine(SlotMachine):
    def __init__(self):
        symbols = ['cherry', 'lemon', 'bell', 'star', 'seven']
        payout_table = {
            # Classic 3-in-a-row combinations (multiplier)
            ('cherry', 'cherry', 'cherry'): 2,    # 2x bet for three cherries
            ('lemon', 'lemon', 'lemon'): 3,        # 3x bet for three lemons
            ('bell', 'bell', 'bell'): 5,          # 5x bet for three bells
            ('star', 'star', 'star'): 10,         # 10x bet for three stars
            ('seven', 'seven', 'seven'): 20,     # 20x bet for three sevens
            
            # Mixed combinations (e.g., cherry + lemon, etc.)
            ('cherry', 'lemon', 'lemon'): 2,      # 2x bet for cherry + lemon + lemon
            ('cherry', 'cherry', 'lemon'): 3,     # 3x bet for two cherries and one lemon
            ('lemon', 'lemon', 'bell'): 4,        # 4x bet for lemon + lemon + bell
            ('star', 'star', 'lemon'): 6,         # 6x bet for star + star + lemon
            ('seven', 'seven', 'bell'): 12,      # 12x bet for two sevens and one bell

            # Two-in-a-row combinations
            ('cherry', 'cherry', 'lemon'): 4,     # 4x bet for cherry + cherry + lemon
            ('lemon', 'lemon', 'cherry'): 4,      # 4x bet for lemon + lemon + cherry
            ('star', 'bell', 'bell'): 5,          # 5x bet for star + bell + bell

            # Random combinations (higher multipliers)
            ('cherry', 'lemon', 'bell'): 3,       # 3x bet for cherry + lemon + bell
            ('cherry', 'bell', 'seven'): 4,       # 4x bet for cherry + bell + seven
            ('lemon', 'star', 'seven'): 5,        # 5x bet for lemon + star + seven
            ('star', 'cherry', 'bell'): 4,        # 4x bet for star + cherry + bell
            ('bell', 'star', 'lemon'): 6,         # 6x bet for bell + star + lemon
        }
        super().__init__(symbols, payout_table)



    def spin(self):
        result = [random.choice(self.symbols) for _ in range(3)]
        print(" | ".join(result))
        return result


# Example usage
if __name__ == "__main__":
    slot_machine = ClassicSlotMachine()
    result = slot_machine.spin()
    
    # Define the bet amount (example: 10 coins)
    bet_amount = 10
    
    # Calculate payout based on the result and bet amount
    payout = slot_machine.calculate_payout(result, bet_amount)
    print(f"Spin Result: {result}")
    print(f"Payout: {payout} coins")
