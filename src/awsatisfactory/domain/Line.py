from domain.Machine import Machine

class Line :

    # Constructor

    def __init__(self,
                 name : str,
                 machines : list[Machine] = None
                 ) -> None :
        self.name : str = name
        self.machines : list[Machine] = []

        if machines is not None:
            self.add_machines(machines)

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_machines(self) -> list[Machine] :
        return self.machines
    
    def set_machines(self, value) -> None :
        self.machines : list[Machine] = value

    # Methods

    def print(self) -> None :
        print(f"Line : name = {self.name}")
        print("Machines :")
        for machine in self.machines :
            machine.print()

    def add_machine(self, machine : Machine) -> None :
        self.get_machines().append(machine)
        machine.set_line(self)

    def add_machines(self, machines : list[Machine]) -> None :
        for machine in machines :
            self.add_machine(machine)

    