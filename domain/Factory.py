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

    def add_item(self, item : Item, quantity : float = 0) -> None :
        if item.is_infinite() :
            self.get_inventory()[item] = float('inf')
        else :
            self.get_inventory()[item] = self.get_inventory().get(item, 0) + quantity

    def show_inventory(self) -> None :
        print("Inventory :")
        for item, quantity in self.get_inventory().items() :
            print(f"{item.get_name()} : {quantity}")

    def simulate(self, minutes : int = duration_minutes) -> None :
        for machine in self.get_machines() :
            result : dict = machine.simulate(self.get_inventory(), minutes)
            print(f"Machine {machine.get_name()}")
            for item, quantity in result["total_inputs"].items() :
                self.get_inventory()[item] -= quantity
                print(f"\t{item.get_name()} : {quantity}")
            for item, quantity in result["total_outputs"].items() :
                print(f"\t{item.get_name()} : {quantity}")
                self.add_item(item, quantity)
            