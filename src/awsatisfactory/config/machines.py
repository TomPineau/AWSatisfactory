from awsatisfactory.domain.Machine import Machine
from awsatisfactory.domain.enum.MachineType import MachineType
from awsatisfactory.config.recipes import *

# Smart Plating machines

iron_miner_4 : Machine = Machine("Iron Miner 4", MachineType.MINER, iron_ore_recipe, 0.775)

iron_smelter_3 : Machine = Machine("Iron Smelter 3", MachineType.SMELTER, iron_ingot_recipe)
iron_smelter_4 : Machine = Machine("Iron Smelter 4", MachineType.SMELTER, iron_ingot_recipe, 0.55)

iron_rod_constructor_3 : Machine = Machine("Iron Rod Constructor 3", MachineType.CONSTRUCTOR, iron_rod_recipe)
iron_rod_constructor_4 : Machine = Machine("Iron Rod Constructor 4", MachineType.CONSTRUCTOR, iron_rod_recipe, 0.9)

screw_constructor_3 : Machine = Machine("Screw Constructor 3", MachineType.CONSTRUCTOR, screw_recipe)
screw_constructor_4 : Machine = Machine("Screw Constructor 4", MachineType.CONSTRUCTOR, screw_recipe, 0.85)

iron_plate_constructor_3 : Machine = Machine("Iron Plate Constructor 3", MachineType.CONSTRUCTOR, iron_plate_recipe, 0.6)

reinforced_iron_plate_assembler_2 : Machine = Machine("Reinforced Iron Plate Assembler 2", MachineType.ASSEMBLER, reinforced_iron_plate_recipe, 0.4)

rotor_assembler_1 : Machine = Machine("Rotor Assembler 1", MachineType.ASSEMBLER, rotor_recipe, 0.5)

smart_plating_assembler : Machine = Machine("Smart Plating Assembler", MachineType.ASSEMBLER, smart_plating_recipe)

# Versatile Framework machines

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

reinforced_iron_plate_assembler_1 : Machine = Machine("Reinforced Iron Plate Assembler 1", MachineType.ASSEMBLER, reinforced_iron_plate_recipe, 0.75)

modular_frame_assembler_1 : Machine = Machine("Modular Frame Assembler 1", MachineType.ASSEMBLER, modular_frame_recipe)
modular_frame_assembler_2 : Machine = Machine("Modular Frame Assembler 2", MachineType.ASSEMBLER, modular_frame_recipe, 0.25)

steel_ingot_foundry_1 : Machine = Machine("Steel Ingot Foundry 1", MachineType.FOUNDRY, steel_ingot_recipe)
steel_ingot_foundry_2 : Machine = Machine("Steel Ingot Foundry 2", MachineType.FOUNDRY, steel_ingot_recipe)
steel_ingot_foundry_3: Machine = Machine("Steel Ingot Foundry 3", MachineType.FOUNDRY, steel_ingot_recipe, 2.0/3.0)

steel_beam_constructor_1 : Machine = Machine("Steel Beam Constructor 1", MachineType.CONSTRUCTOR, steel_beam_recipe)
steel_beam_constructor_2 : Machine = Machine("Steel Beam Constructor 2", MachineType.CONSTRUCTOR, steel_beam_recipe)

versatile_framework_assembler : Machine = Machine("Versatile Framework Assembler", MachineType.ASSEMBLER, versatile_framework_recipe)

# Automated Wiring machines

iron_miner_5 : Machine = Machine("Iron Miner 5", MachineType.MINER, iron_ore_recipe, 0.1875)

coal_miner_3 : Machine = Machine("Coal Miner 3", MachineType.MINER, coal_ore_recipe, 0.1875)

copper_miner_1 : Machine = Machine("Copper Miner 1", MachineType.MINER, copper_ore_recipe)

steel_ingot_foundry_4 : Machine = Machine("Steel Ingot Foundry 4", MachineType.FOUNDRY, steel_ingot_recipe, 0.25)

steel_pipe_constructor_1 : Machine = Machine("Steel Pipe Constructor 1", MachineType.CONSTRUCTOR, steel_pipe_recipe, 0.38)

copper_ingot_smelter_1 : Machine = Machine("Copper Ingot Smelter 1", MachineType.SMELTER, copper_ingot_recipe)
copper_ingot_smelter_2 : Machine = Machine("Copper Ingot Smelter 2", MachineType.SMELTER, copper_ingot_recipe)

wire_constructor_1 : Machine = Machine("Wire Constructor 1", MachineType.CONSTRUCTOR, wire_recipe)
wire_constructor_2 : Machine = Machine("Wire Constructor 2", MachineType.CONSTRUCTOR, wire_recipe)
wire_constructor_3 : Machine = Machine("Wire Constructor 3", MachineType.CONSTRUCTOR, wire_recipe)
wire_constructor_4 : Machine = Machine("Wire Constructor 4", MachineType.CONSTRUCTOR, wire_recipe)

cable_constructor_1 : Machine = Machine("Cable Constructor 1", MachineType.CONSTRUCTOR, cable_recipe)
cable_constructor_2 : Machine = Machine("Cable Constructor 2", MachineType.CONSTRUCTOR, cable_recipe, 2.0/3.0)

stator_assembler_1 : Machine = Machine("Stator Assembler 1", MachineType.ASSEMBLER, stator_recipe, 0.5)

automated_wiring_assembler : Machine = Machine("Automated Wiring Assembler", MachineType.ASSEMBLER, automated_wiring_recipe)