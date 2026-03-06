# import sys, pathlib
# sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from domain.Item import Item
from domain.Recipe import Recipe
from domain.Factory import Factory
from domain.Machine import Machine
from domain.enum.MachineType import MachineType

def test() -> None:

    factory : Factory = Factory("Factory 1")
    
    iron_node: Item = Item("Iron Node", True)
    coal_node: Item = Item("Coal Node", True)
    iron_ore: Item = Item("Iron Ore", False)
    coal_ore: Item = Item("Coal Ore", False)
    iron_ingot: Item = Item("Iron Ingot", False)
    iron_plate: Item = Item("Iron Plate", False)
    iron_rod: Item = Item("Iron Rod", False)
    screw: Item = Item("Screw", False)
    reinforced_iron_plate: Item = Item("Reinforced Iron Plate", False)
    modular_frame: Item = Item("Modular Frame", False)
    steel_ingot: Item = Item("Steel Ingot", False)
    steel_beam: Item = Item("Steel Beam", False)
    versatile_framework: Item = Item("Versatile Framework", False)

    factory.add_node(iron_node)
    factory.add_node(coal_node)
    factory.show_inventory()

    iron_ore_recipe: Recipe = Recipe("Iron Ore", {iron_node: 1}, {iron_ore: 1}, 1)
    iron_ingot_recipe: Recipe = Recipe("Iron Ingot", {iron_ore: 1}, {iron_ingot: 1}, 2)
    iron_plate_recipe: Recipe = Recipe("Iron Plate", {iron_ingot: 3}, {iron_plate: 2}, 6)
    iron_rod_recipe: Recipe = Recipe("Iron Rod", {iron_ingot: 1}, {iron_rod: 1}, 4)
    screw_recipe: Recipe = Recipe("Screw", {iron_rod: 1}, {screw: 4}, 6)
    reinforced_iron_plate_recipe: Recipe = Recipe("Reinforced Iron Plate", {iron_plate: 6, screw: 12}, {reinforced_iron_plate: 1}, 12)
    modular_frame_recipe: Recipe = Recipe("Modular Frame", {reinforced_iron_plate: 3, iron_rod: 12}, {modular_frame: 2}, 60)
    coal_ore_recipe: Recipe = Recipe("Coal Ore", {coal_node: 1}, {coal_ore: 1}, 1)
    steel_ingot_recipe: Recipe = Recipe("Steel Ingot", {iron_ore: 3, coal_ore: 3}, {steel_ingot: 3}, 4)
    steel_beam_recipe: Recipe = Recipe("Steel Beam", {steel_ingot: 4}, {steel_beam: 1}, 4)
    versatile_framework_recipe: Recipe = Recipe("Versatile Framework", {steel_beam: 30, modular_frame: 2.5}, {versatile_framework: 5}, 24)

    iron_miner_1 : Machine = Machine("Iron Miner 1", MachineType.MINER, iron_ore_recipe)
    iron_miner_2 : Machine = Machine("Iron Miner 2", MachineType.MINER, iron_ore_recipe)
    iron_miner_3 : Machine = Machine("Iron Miner 3", MachineType.MINER, iron_ore_recipe)

    coal_miner_1 : Machine = Machine("Coal Miner 1", MachineType.MINER, coal_ore_recipe)
    coal_miner_2 : Machine = Machine("Coal Miner 2", MachineType.MINER, coal_ore_recipe)

    iron_smelter_1 : Machine = Machine("Iron Smelter 1", MachineType.SMELTER, iron_ingot_recipe)
    iron_smelter_2 : Machine = Machine("Iron Smelter 2", MachineType.SMELTER, iron_ingot_recipe)

    iron_rod_constructor_1 : Machine = Machine("Iron Rod Constructor 1", MachineType.CONSTRUCTOR, iron_rod_recipe)
    iron_rod_constructor_2 : Machine = Machine("Iron Rod Constructor 2", MachineType.CONSTRUCTOR, iron_rod_recipe, 0.75)

    screw_constructor_1 : Machine = Machine("Screw Constructor 1", MachineType.CONSTRUCTOR, screw_recipe)
    screw_constructor_2 : Machine = Machine("Screw Constructor 2", MachineType.CONSTRUCTOR, screw_recipe, 0.125)

    iron_plate_constructor_1 : Machine = Machine("Iron Plate Constructor 1", MachineType.CONSTRUCTOR, iron_plate_recipe)
    iron_plate_constructor_2 : Machine = Machine("Iron Plate Constructor 2", MachineType.CONSTRUCTOR, iron_plate_recipe, 0.125)

    reinforced_iron_plate_assembler : Machine = Machine("Reinforced Iron Plate Assembler", MachineType.ASSEMBLER, reinforced_iron_plate_recipe, 0.75)

    modular_frame_assembler_1 : Machine = Machine("Modular Frame Assembler 1", MachineType.ASSEMBLER, modular_frame_recipe)
    modular_frame_assembler_2 : Machine = Machine("Modular Frame Assembler 2", MachineType.ASSEMBLER, modular_frame_recipe, 0.25)

    steel_ingot_foundry_1 : Machine = Machine("Steel Ingot Foundry 1", MachineType.FOUNDRY, steel_ingot_recipe)
    steel_ingot_foundry_2 : Machine = Machine("Steel Ingot Foundry 2", MachineType.FOUNDRY, steel_ingot_recipe)
    steel_ingot_foundry_3: Machine = Machine("Steel Ingot Foundry 3", MachineType.FOUNDRY, steel_ingot_recipe, 2.0/3.0)

    steel_beam_constructor_1 : Machine = Machine("Steel Beam Constructor 1", MachineType.CONSTRUCTOR, steel_beam_recipe)
    steel_beam_constructor_2 : Machine = Machine("Steel Beam Constructor 2", MachineType.CONSTRUCTOR, steel_beam_recipe)

    versatile_framework_assembler : Machine = Machine("Versatile Framework Assembler", MachineType.ASSEMBLER, versatile_framework_recipe)

    factory.add_machine(iron_miner_1)
    factory.add_machine(iron_miner_2)
    factory.add_machine(iron_miner_3)
    factory.add_machine(coal_miner_1)
    factory.add_machine(coal_miner_2)
    factory.add_machine(iron_smelter_1)
    factory.add_machine(iron_smelter_2)
    factory.add_machine(iron_rod_constructor_1)
    factory.add_machine(iron_rod_constructor_2)
    factory.add_machine(screw_constructor_1)
    factory.add_machine(screw_constructor_2)
    factory.add_machine(iron_plate_constructor_1)
    factory.add_machine(iron_plate_constructor_2)
    factory.add_machine(reinforced_iron_plate_assembler)
    factory.add_machine(modular_frame_assembler_1)
    factory.add_machine(modular_frame_assembler_2)
    factory.add_machine(steel_ingot_foundry_1)
    factory.add_machine(steel_ingot_foundry_2)
    factory.add_machine(steel_ingot_foundry_3)
    factory.add_machine(steel_beam_constructor_1)
    factory.add_machine(steel_beam_constructor_2)
    factory.add_machine(versatile_framework_assembler)

    minutes : int = 0
    duration : int = 1
    while minutes < duration :
        factory.simulate(1)
        minutes += 1
        factory.show_inventory()
    factory.show_power_consumption()

if __name__ == "__main__":
    test()