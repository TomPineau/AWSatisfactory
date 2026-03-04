from domain.Item import Item

class Recipe :

    # Constructor

    def __init__(self,
                 name : str,
                 inputs : dict,
                 outputs : dict,
                 craft_time : int
                 ) -> None :
        self.name : str = name
        self.inputs : dict = inputs
        self.outputs : dict = outputs
        self.craft_time : int = craft_time

    # Getters and setters

    def get_name(self) -> str :
        return self.name
    
    def set_name(self, value) -> None :
        self.name : str = value

    def get_inputs(self) -> dict :
        return self.inputs
    
    def set_inputs(self, value) -> None :
        self.inputs : dict = value

    def get_outputs(self) -> dict :
        return self.outputs
    
    def set_outputs(self, value) -> None :
        self.outputs : dict = value

    def get_craft_time(self) -> int :
        return self.craft_time
    
    def set_craft_time(self, value) -> None :
        self.craft_time : int = value
    
    # Methods

    def print(self) -> None :
        print(f"Recipe : name = {self.name}, craft_time = {self.craft_time}")
        print("Inputs :", end = "")
        for item, quantity in self.inputs.items() :
            print(f"\t{item.get_name()} : {quantity}")
        print("Outputs :", end = "")
        for item, quantity in self.outputs.items() :
            print(f"\t{item.get_name()} : {quantity}")