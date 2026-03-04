# import sys, pathlib
# sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from domain.Item import Item
from domain.Recipe import Recipe
from domain.Factory import Factory
from domain.Machine import Machine
from domain.enum.MachineEnum import MachineEnum

def test() -> None:
    iron_ore: Item = Item("Iron Ore", True)
    coal_ore: Item = Item("Coal Ore", True)
    iron_ingot: Item = Item("Iron Ingot", False)

    inputs: dict = {iron_ore: 1}
    outputs: dict = {iron_ingot: 1}
    iron_ingot_recipe: Recipe = Recipe("Iron Ingot", inputs, outputs, 2)
    iron_ingot_recipe.print()

    constructor : Machine = Machine("Constructor 1", MachineEnum.CONSTRUCTOR, iron_ingot_recipe, 4)
    constructor.print()

    factory : Factory = Factory("Factory 1")
    factory.add_machine(constructor)
    factory.print()

if __name__ == "__main__":
    test()