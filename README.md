## Features
- **GUI and CLI Interfaces**: Play via a modern GUI (`launcher.py`) or a simple CLI (`main.py`).
- **OOP Principles**: Implements encapsulation, abstraction, inheritance, and polymorphism.
- **Factory Method Pattern**: Dynamically creates slot machine instances.
- **Persistent Storage**: Saves and loads player balances using JSON (`storage.py`).
- **Unit Testing**: Core functionality tested with `unittest` (`test_slot_machine.py`).
- **Customizable**: Easily extensible to add new slot machine types or features.

## Requirements
- Python 3.8 or higher
- Required libraries (listed in `requirements.txt`):
  - `customtkinter`
  - `Pillow` (for image handling in GUI)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/slot-machine-game.git
   cd slot-machine-game
   ```
2. Install dependencies:
   ```bash
   python install_libs.py
   ```
   This script installs the required libraries from `requirements.txt`.
3. Ensure the `assets` folder with symbol images (`slot_icon.png`, `cherry.png`, `lemon.png`, `bell.png`, `star.png`, `seven.png`) is present in the project directory.

## How to Run
### GUI Version
1. Run the GUI application:
   ```bash
   python launcher.py
   ```
2. The GUI window will open. Enter your username and click "Start" to begin playing.

### CLI Version
1. Run the CLI application:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter your username and place bets.

## How to Use
### GUI
- **Enter Username**: Input your name in the entry field and click "Start".
- **Place Bet**: Enter a bet amount in the provided field (default is 10 coins).
- **Spin**: Click the "SPIN" button to spin the reels.
- **View Results**: The reels display symbols, and the result label shows win/loss information. Your balance updates automatically.
- **Exit**: Click the "✖" button in the top bar to close the application. Your balance is saved automatically.

### CLI
- **Enter Username**: Input your name when prompted.
- **Place Bet**: Enter a bet amount (or 0 to quit).
- **Spin**: The CLI displays the spin result and updates your balance.
- **Exit**: Enter 0 as the bet to save your balance and exit.

## Project Structure
- `launcher.py`: GUI implementation using `customtkinter`.
- `main.py`: CLI implementation.
- `slot_machine.py`: Defines the `SlotMachine` abstract class and `ClassicSlotMachine` implementation.
- `player.py`: Manages player data and game logic.
- `machine_factory.py`: Implements the Factory Method pattern for creating slot machines.
- `storage.py`: Handles saving/loading player balances to/from a JSON file.
- `test_slot_machine.py`: Unit tests for core functionality.
- `install_libs.py`: Script to install required libraries.
- `assets/`: Contains image files for the GUI (e.g., `cherry.png`).
- `requirements.txt`: Lists required Python libraries.

## OOP Pillars
- **Encapsulation**: The `Player` class protects the balance using `_balance` and provides `get_balance`/`set_balance` methods.
- **Abstraction**: The `SlotMachine` class is an abstract base class with a `spin` method implemented by `ClassicSlotMachine`.
- **Inheritance**: `ClassicSlotMachine` inherits from `SlotMachine`.
- **Polymorphism**: The Factory Method allows different slot machine types to implement `spin` differently.

## Design Pattern
The **Factory Method** pattern is used in `machine_factory.py` to create slot machine instances dynamically, enabling easy extension for new machine types (e.g., a "modern" slot machine with different symbols).

## Testing
Unit tests in `test_slot_machine.py` cover:
- Initial balance verification
- Negative bet handling
- Balance saving/loading
- Payout type checking

Run tests with:
```bash
python -m unittest test_slot_machine.py -v
```
