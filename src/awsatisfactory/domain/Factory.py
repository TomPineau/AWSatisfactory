from domain.Line import Line
from domain.Item import Item

from config.items import infinite_nodes

class Factory :

    # Constants

    duration_minutes : int = 1

    # Constructor

    def __init__(self,
                 name : str,
                 inventory : dict = {},
                 lines : list[Line] = []
                 ) -> None :
        self.name : str = name
        self.inventory : dict = inventory
        self.lines : list[Line] = lines
        self.power_consumption : dict = {}

        for node in infinite_nodes :
            self.add_node(node)

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_inventory(self) -> dict :
        return self.inventory
    
    def set_inventory(self, value) -> None :
        self.inventory : dict = value

    def get_lines(self) -> list[Line] :
        return self.lines
    
    def set_lines(self, value) -> None :
        self.lines : list[Line] = value

    # Methods

    def print(self) -> None :
        print(f"Factory : name = {self.name}, inventory = {self.inventory}")
        print("Machines :")
        for machine in self.get_lines() :
            machine.print()

    def add_line(self, line : Line) -> None :
        self.get_lines().append(line)

    def add_node(self, item : Item) -> None :
            self.get_inventory()[item] = float('inf')

    def add_item(self, item : Item, quantity) -> None :
        self.get_inventory()[item] = self.get_inventory().get(item, 0) + quantity

    def show_inventory(self) -> None :
        print("Inventory :")
        for item, quantity in self.get_inventory().items() :
            print(f"{item.get_name()} : {quantity}")
        print()

    def show_power_consumption(self) -> None :
        print("Power consumption :")
        for machine_type, power in self.power_consumption.items() :
            print(f"{machine_type} : {power} MW")

    def simulate(self, minutes : int = duration_minutes) -> None :
        for line in self.get_lines() :
            for machine in line.get_machines() :

                result : dict = machine.simulate(self.get_inventory(), minutes)
                
                # Consume inputs
                for item, quantity in result["inputs"].items() :
                    self.get_inventory()[item] -= quantity
                
                # Produce outputs
                for item, quantity in result["outputs"].items() :
                    self.add_item(item, quantity)
                
                # Consume power
                for machine_type, power in result["power_consumption"].items() :
                    self.power_consumption[machine_type] = self.power_consumption.get(machine_type, 0) + power

                print(f"Machine: {machine.get_name()}, elapsed_craft_time = {machine.get_elapsed_craft_time()}, craft_time = {machine.get_recipe().get_craft_time() / machine.get_overclock()}, craft_nb = {result['craft_nb']}, power_consumption = {result['power_consumption']}")
                self.show_inventory()