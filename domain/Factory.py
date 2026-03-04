from domain.Machine import Machine
from domain.Item import Item

class Factory :

    # Constants

    duration_minutes : int = 1

    # Constructor

    def __init__(self,
                 name : str,
                 inventory : dict = None
                 ) -> None :
        self.name : str = name
        self.machines : list[Machine] = []
        self.inventory : dict = inventory if inventory is not None else {}

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_machines(self) -> list[Machine] :
        return self.machines
    
    def set_machines(self, value) -> None :
        self.machines : list[Machine] = value

    def get_inventory(self) -> dict :
        return self.inventory
    
    def set_inventory(self, value) -> None :
        self.inventory : dict = value

    # Methods

    def print(self) -> None :
        print(f"Factory : name = {self.name}, inventory = {self.inventory}")
        print("Machines :")
        for machine in self.machines :
            machine.print()

    def add_machine(self, machine : Machine) -> None :
        self.get_machines().append(machine)

    def simulate(self, minutes : int = duration_minutes) -> None :
        for machine in self.get_machines() :
            result = machine.simulate(self.get_inventory(), minutes)
            