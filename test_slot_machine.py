import unittest
from player import Player
from machine_factory import SlotMachineFactory

class TestSlotMachine(unittest.TestCase):

    def setUp(self):
        self.machine = SlotMachineFactory.create_machine("classic")
        self.player = Player("TestUser", 100, self.machine)

    def test_initial_balance(self):
        self.assertEqual(self.player.get_balance(), 100)

    def test_play_decreases_balance(self):
        # Simulate a bet and spin
        bet_amount = 10
        initial_balance = self.player.get_balance()
        self.player.play(bet_amount)  # assuming play() is implemented in Player
        self.assertTrue(self.player.get_balance() < initial_balance)

    def test_play_negative_bet(self):
        with self.assertRaises(ValueError):
            self.player.play(-5)

    def test_balance_saves_and_loads(self):
        from storage import save_balance, load_balance
        save_balance("TestUser", 123)
        loaded = load_balance("TestUser")
        self.assertEqual(loaded, 123)

    def test_payout_is_int(self):
        # Adjust payout calculation to include bet amount
        result = ["🍒", "🍒", "🍒"]
        bet_amount = 10  # Example bet
        payout = self.machine.calculate_payout(result, bet_amount)
        self.assertIsInstance(payout, int)  # Assert payout is an integer
        self.assertEqual(payout % 1, 0)  # Ensure payout is an integer (no decimals)

if __name__ == "__main__":
    unittest.main(verbosity=2)
