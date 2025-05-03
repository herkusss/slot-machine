from machine_factory import SlotMachineFactory
from player import Player
import storage

def main():
    name = input("Enter your name: ")
    balance = storage.load_balance(name)
    machine = SlotMachineFactory.create_machine("classic")
    player = Player(name, balance, machine)

    while True:
        print(f"Balance: {player.get_balance()}")
        bet = int(input("Enter your bet (0 to quit): "))
        if bet == 0:
            break
        player.play(bet)

    storage.save_balance(name, player.get_balance())
    print("Game saved. Goodbye!")

if __name__ == "__main__":
    main()
