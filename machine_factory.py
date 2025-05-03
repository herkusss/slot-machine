from slot_machine import ClassicSlotMachine

class SlotMachineFactory:
    @staticmethod
    def create_machine(machine_type):
        if machine_type == "classic":
            return ClassicSlotMachine()
        raise ValueError("Unknown machine type")
