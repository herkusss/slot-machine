# Slot Machine Coursework Report

---

## 1. Introduction

**Goal of the coursework:**  
Build a Python application that simulates a slot-machine game while demonstrating core OOP principles, a design pattern, file I/O, unit testing, and a modern GUI.

**Topic & Application:**  
A desktop slot-machine simulator where the player:  
1. Enters their name.  
2. Loads an existing coin balance (or starts at 100 coins).  
3. Places bets and spins three “reels” of fruit and “7” symbols (PNG images).  
4. Wins or loses coins based on matching symbols; balance is saved to disk.

**How to run:**  
```bash
git clone https://github.com/yourusername/slot-machine.git
cd slot-machine
pip install -r requirements.txt
python gui_ctk.py
```

---

## 2. Body / Analysis

### 2.1 Object-Oriented Principles
The application employs the four pillars of OOP:

- **Encapsulation**: The `Player` class encapsulates the player's balance using a private `_balance` attribute, with access controlled via `get_balance()` and `set_balance()` methods. This ensures the balance cannot be modified directly, maintaining data integrity.

- **Inheritance**: The `ClassicSlotMachine` class inherits from the abstract `SlotMachine` class, which defines a common interface (`spin` method) and shared attributes (`symbols`, `payout_table`). This promotes code reuse and extensibility.

- **Polymorphism**: The `spin` method is implemented differently in `ClassicSlotMachine` but can be called uniformly through the `SlotMachine` interface, allowing flexibility for future machine types.

- **Abstraction**: The `SlotMachine` abstract base class hides implementation details, exposing only the necessary interface (`spin` and `calculate_payout`), simplifying interaction for the `Player` class.

### 2.2 Design Pattern: Factory
The **Factory Method** pattern is implemented in the `SlotMachineFactory` class. The static `create_machine` method takes a `machine_type` parameter and returns an instance of the appropriate slot machine (e.g., `ClassicSlotMachine` for `"classic"`). This centralizes object creation, making it easy to add new machine types without modifying client code. For example, adding a new machine type would only require extending the `if` conditions in `create_machine`.

### 2.3 Composition / Aggregation
The `Player` class demonstrates **composition** by containing a reference to a `SlotMachine` object (`self.machine`). This "has-a" relationship allows the player to interact with different slot machine instances without inheriting from them. The GUI (`SlotMachineCustomGUI`) also uses composition by embedding a `Player` object, which in turn contains the slot machine, forming a cohesive system.

### 2.4 File I/O
The `storage.py` module handles persistent storage using JSON:
- `save_balance`: Writes the player's balance to a `balance.json` file, updating or creating the file as needed.
- `load_balance`: Retrieves the player's balance from `balance.json`, defaulting to 100 coins if no record exists.
- `get_all_players`: Returns a list of all player names stored in the file.

This ensures that player progress is saved between sessions, with error handling for missing files using try-except blocks.

### 2.5 Testing
The `test_slot_machine.py` file contains a `unittest` suite to verify core functionality:
- **Initial balance**: Confirms the player starts with the correct balance (100 coins).
- **Balance decrease**: Ensures a bet reduces the balance correctly.
- **Negative bet**: Verifies that invalid bets raise a `ValueError`.
- **Balance persistence**: Tests saving and loading balances to/from `balance.json`.
- **Payout type**: Confirms payouts are integers.

These tests cover critical logic, though additional tests for edge cases (e.g., zero balance) could enhance coverage.

### 2.6 GUI Implementation
The GUI, implemented in `gui_ctk.py` using CustomTkinter, provides a modern, user-friendly interface:
- **Custom Window**: A borderless window with a draggable top bar, featuring a slot machine icon, title, and close button.
- **Name Entry Screen**: Prompts the user for their name, loading or initializing their balance.
- **Game Screen**: Displays the balance, three reel labels (showing PNG images for symbols), a bet entry field, a spin button, and a result label for win/loss feedback.
- **Visuals**: Uses resized PNG images (cherry, lemon, bell, star, seven) for reels, loaded dynamically from the `assets` folder.
- **Interactivity**: The `spin` method updates reel images, calculates payouts, adjusts the balance, and saves progress. If the balance reaches zero, the app closes after a brief delay.

The GUI enhances usability compared to the console-based `main.py`, though it assumes the presence of specific image files.

---

## 3. Results
The application successfully meets the coursework requirements:
- **Functionality**: Players can enter their name, place bets, spin reels, and see win/loss outcomes, with balances saved persistently.
- **OOP Principles**: Encapsulation, inheritance, polymorphism, and abstraction are clearly demonstrated.
- **Design Pattern**: The Factory Method pattern simplifies machine creation.
- **Testing**: Unit tests validate key behaviors, ensuring reliability.
- **GUI**: The CustomTkinter interface is visually appealing and intuitive, with dynamic image updates and error feedback.
- **File I/O**: JSON-based storage ensures persistent player data.

Limitations include:
- Only one machine type ("classic") is implemented.
- The GUI assumes specific asset files, which may cause errors if missing.
- Testing coverage could be expanded for edge cases.

---

## 4. Conclusions
The slot machine simulator effectively demonstrates OOP principles, the Factory Method pattern, file I/O, unit testing, and a modern GUI. The modular design, with separate concerns for game logic (`slot_machine.py`, `player.py`), storage (`storage.py`), and interface (`gui_ctk.py`, `main.py`), makes it maintainable and extensible. Future improvements could include:
- Adding new machine types (e.g., progressive jackpots) via the factory.
- Enhancing tests for edge cases like zero bets or corrupted JSON files.
- Implementing error handling for missing asset files in the GUI.
- Adding sound effects or animations to enhance the user experience.

Overall, the project showcases a robust application of Python programming concepts in a practical, engaging context.
