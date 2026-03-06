from domain.enum.MachineEnum import MachineEnum
from domain.Recipe import Recipe

class Machine:

    # Constructor

    def __init__(self,
                 name : str,
                 machine_type : MachineEnum,
                 recipe : Recipe,
                 base_power : float,
                 overclock : float = 1.0,
                 craft_remaining_time : int = 0
                 ) -> None :
        self.name : str = name
        self.machine_type : MachineEnum = machine_type
        self.recipe : Recipe = recipe
        self.base_power : float = base_power
        self.overclock : float = overclock
        self.craft_remaining_time : int = craft_remaining_time

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_machine_type(self) -> MachineEnum :
        return self.machine_type
    
    def set_machine_type(self, value) -> None :
        self.machine_type : MachineEnum = value

    def get_recipe(self) -> Recipe :
        return self.recipe
    
    def set_recipe(self, value) -> None :
        self.recipe : Recipe = value

    def get_base_power(self) -> float :
        return self.base_power
    
    def set_base_power(self, value) -> None :
        self.base_power : float = value

    def get_overclock(self) -> float :
        return self.overclock
    
    def set_overclock(self, value) -> None :
        self.overclock : float = value

    def get_craft_remaining_time(self) -> int :
        return self.craft_remaining_time
    
    def set_craft_remaining_time(self, value) -> None :
        self.craft_remaining_time : int = value

    # Methods

    def print(self) -> None :
        print(f"Machine : name = {self.name}, machine_type = {self.machine_type}, base_power = {self.base_power}, overclock = {self.overclock}, craft_remaining_time = {self.craft_remaining_time}")
        if self.get_recipe() is not None :
            self.get_recipe().print()

    def simulate(self, inventory : dict, minutes : int) -> None :
        recipe : Recipe = self.get_recipe()
        if recipe is None :
            print(f"Machine {self.get_name()} has no recipe assigned.")
            return
        
        recipe_inputs : dict = recipe.get_inputs()
        recipe_outputs : dict = recipe.get_outputs()

        total_time : int = minutes * 60 + self.get_craft_remaining_time()
        craft_speed : float = recipe.get_craft_time() / self.get_overclock()
        max_craft_nb : int = int(total_time / craft_speed)
        max_craft_nb_from_inputs : int = min([inventory.get(item, 0) // quantity if not item.is_infinite() else max_craft_nb for item, quantity in recipe_inputs.items()])

        craft_nb : int = min(max_craft_nb, max_craft_nb_from_inputs)
        total_craft_time : int = craft_nb * craft_speed
        new_craft_remaining_time : int = minutes * 60 + self.get_craft_remaining_time() - total_craft_time
        self.set_craft_remaining_time(new_craft_remaining_time)

        print(f"Machine {self.get_name()}: total_time = {total_time}, craft_remaining_time = {self.get_craft_remaining_time()}, craft_speed = {craft_speed}, max_craft_nb = {max_craft_nb}, max_craft_nb_from_inputs = {max_craft_nb_from_inputs}, total_craft_time = {total_craft_time}, craft_nb = {craft_nb}")

        total_inputs : dict = {item: quantity * craft_nb for item, quantity in recipe_inputs.items()}
        total_outputs : dict = {item: quantity * craft_nb for item, quantity in recipe_outputs.items()}

        power_consumption : float = self.get_base_power() * total_craft_time * self.get_overclock() ** 1.6
        print(f"power_consumption = {power_consumption}")

        return {
            "craft_nb": craft_nb,
            "total_inputs": total_inputs,
            "total_outputs": total_outputs,
            "power_consumption": power_consumption}