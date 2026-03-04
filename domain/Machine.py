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
            return
        
        recipe_inputs : dict = recipe.get_inputs()
        recipe_outputs : dict = recipe.get_outputs()
        craft_nb : int = int((minutes * 60 - self.get_craft_remaining_time()) / (self.get_recipe().get_craft_time() / self.get_overclock()))
        total_inputs : dict = {item: quantity * craft_nb for item, quantity in recipe_inputs.items()}
        total_outputs : dict = {item: quantity * craft_nb for item, quantity in recipe_outputs.items()}

        
        # if self.get_craft_remaining_time() > 0 :
        #     time_to_simulate : int = min(self.get_craft_remaining_time(), minutes)
        #     self.set_craft_remaining_time(self.get_craft_remaining_time() - time_to_simulate)
        #     minutes -= time_to_simulate
        #     if self.get_craft_remaining_time() == 0 :
        #         for item, quantity in self.get_recipe().get_outputs().items() :
        #             inventory[item] = inventory.get(item, 0) + quantity
        # else :
        #     can_craft : bool = True
        #     for item, quantity in self.get_recipe().get_inputs().items() :
        #         if inventory.get(item, 0) < quantity :
        #             can_craft = False
        #             break
        #     if can_craft :
        #         for item, quantity in self.get_recipe().get_inputs().items() :
        #             inventory[item] = inventory.get(item, 0) - quantity
        #         self.set_craft_remaining_time(int(self.get_recipe().get_craft_time() / self.get_overclock()))
        #         self.simulate(inventory, minutes)