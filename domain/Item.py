class Item :

    # Constructor

    def __init__(self,
                 name : str,
                 is_infinite : bool = False
                 ) -> None :
        self.name : str = name
        self.is_infinite : bool = is_infinite

    # Getters and setters

    def get_name(self) -> str :
        return self.name

    def set_name(self, value) -> None :
        self.name : str = value

    def is_infinite(self) -> bool:
        return self.is_infinite

    def set_is_infinite(self, value) -> None:
        self.is_infinite : bool = value

    # Methods

    def print(self):
        print(f"Item : name = {self.name}, is_infinite = {self.is_infinite}")