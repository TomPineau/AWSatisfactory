from domain.enum.MachineType import MachineType
from domain.Recipe import Recipe

class Machine:

    # Constants

    machine_base_power : dict = {
        MachineType.MINER: 5,
        MachineType.SMELTER: 4,
        MachineType.CONSTRUCTOR: 4,
        MachineType.FOUNDRY: 16,
        MachineType.ASSEMBLER: 15,
        MachineType.REFINERY: 30,
        MachineType.MANUFACTURER: 55
    }

    # Constructor

    def __init__(self,
                 name : str,
                 machine_type : MachineType,
                 recipe : Recipe,
                 overclock : float = 1.0,
                 elapsed_craft_time : int = 0
                 ) -> None :
        self.name : str = name
        self.machine_type : MachineType = machine_type
        self.recipe : Recipe = recipe
        self.base_power : float = self.machine_base_power.get(machine_type, 0)
        self.overclock : float = overclock
        self.elapsed_craft_time : int = elapsed_craft_time
        self._is_running : bool = False

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_machine_type(self) -> MachineType :
        return self.machine_type
    
    def set_machine_type(self, value) -> None :
        self.machine_type : MachineType = value

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

    def get_elapsed_craft_time(self) -> int :
        return self.elapsed_craft_time
    
    def set_elapsed_craft_time(self, value) -> None :
        self.elapsed_craft_time : int = value

    def is_running(self) -> bool :
        return self._is_running
    
    def set_is_running(self, value) -> None :
        self._is_running : bool = value

    # Methods

    def print(self) -> None :
        print(f"Machine : name = {self.name}, machine_type = {self.machine_type}, base_power = {self.base_power}, overclock = {self.overclock}, elapsed_craft_time = {self.elapsed_craft_time}")
        if self.get_recipe() is not None :
            self.get_recipe().print()

    def simulate(self, inventory : dict, minutes : int) -> None :
        recipe : Recipe = self.get_recipe()
        if recipe is None :
            print(f"Machine {self.get_name()} has no recipe assigned.")
            return
        
        recipe_inputs : dict = recipe.get_inputs()
        recipe_outputs : dict = recipe.get_outputs()

        # calculate available time including any leftover from previous calls
        total_time : int = self.get_elapsed_craft_time() + minutes * 60
        craft_time : float = recipe.get_craft_time() / self.get_overclock()
        max_craft_nb : int = int(total_time / craft_time)
        max_craft_nb_from_inputs : int = min(
            [inventory.get(item, 0) // quantity if not item.is_infinite() else max_craft_nb
             for item, quantity in recipe_inputs.items()]
        )

        craft_nb : int = min(max_craft_nb, max_craft_nb_from_inputs)
        total_craft_time : int = craft_nb * craft_time

        # update running state
        self.set_is_running(craft_nb > 0)

        # leftover time that didn't contribute to a full craft
        # leftover : int = total_time - total_craft_time
        leftover : int = total_time % craft_time
        # cap remaining time at craft_time to prevent accumulation beyond one craft
        leftover = min(leftover, craft_time)
        self.set_elapsed_craft_time(leftover)

        # print(f"Machine {self.get_name()}: total_time = {total_time}, elapsed_craft_time = {self.get_elapsed_craft_time()}, craft_time = {craft_time}, max_craft_nb = {max_craft_nb}, max_craft_nb_from_inputs = {max_craft_nb_from_inputs}, total_craft_time = {total_craft_time}, craft_nb = {craft_nb}")

        total_inputs : dict = {item: quantity * craft_nb for item, quantity in recipe_inputs.items()}
        total_outputs : dict = {item: quantity * craft_nb for item, quantity in recipe_outputs.items()}

        power_consumption : dict = {self.get_machine_type().value: self.get_base_power() * (total_craft_time / 3600)* self.get_overclock() ** 1.6}

        return {
            "craft_nb": craft_nb,
            "total_inputs": total_inputs,
            "total_outputs": total_outputs,
            "power_consumption": power_consumption}