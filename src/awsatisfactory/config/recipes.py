from config.items import *
from domain.Recipe import Recipe
from domain.enum.MachineType import MachineType

# Basic Iron recipes

iron_ore_recipe: Recipe = Recipe("Iron Ore", MachineType.MINER, {iron_node: 1}, {iron_ore: 1}, 1)
iron_ingot_recipe: Recipe = Recipe("Iron Ingot", MachineType.SMELTER, {iron_ore: 1}, {iron_ingot: 1}, 2)
iron_plate_recipe: Recipe = Recipe("Iron Plate", MachineType.CONSTRUCTOR, {iron_ingot: 3}, {iron_plate: 2}, 6)
iron_rod_recipe: Recipe = Recipe("Iron Rod", MachineType.CONSTRUCTOR, {iron_ingot: 1}, {iron_rod: 1}, 4)
screw_recipe: Recipe = Recipe("Screw", MachineType.CONSTRUCTOR, {iron_rod: 1}, {screw: 4}, 6)
reinforced_iron_plate_recipe: Recipe = Recipe("Reinforced Iron Plate", MachineType.ASSEMBLER, {iron_plate: 6, screw: 12}, {reinforced_iron_plate: 1}, 12)

# Copper recipes

copper_ore_recipe: Recipe = Recipe("Copper Ore", MachineType.MINER, {copper_node: 1}, {copper_ore: 1}, 1)
copper_ingot_recipe: Recipe = Recipe("Copper Ingot", MachineType.SMELTER, {copper_ore: 1}, {copper_ingot: 1}, 2)
wire_recipe: Recipe = Recipe("Wire", MachineType.CONSTRUCTOR, {copper_ingot: 1}, {wire: 2}, 4)
cable_recipe: Recipe = Recipe("Cable", MachineType.CONSTRUCTOR, {wire: 2}, {cable: 1}, 2)

# Steel recipes

coal_ore_recipe: Recipe = Recipe("Coal Ore", MachineType.MINER, {coal_node: 1}, {coal_ore: 1}, 1)
steel_ingot_recipe: Recipe = Recipe("Steel Ingot", MachineType.FOUNDRY, {iron_ore: 3, coal_ore: 3}, {steel_ingot: 3}, 4)
steel_beam_recipe: Recipe = Recipe("Steel Beam", MachineType.CONSTRUCTOR, {steel_ingot: 4}, {steel_beam: 1}, 4)
steel_pipe_recipe: Recipe = Recipe("Steel Pipe", MachineType.CONSTRUCTOR, {steel_ingot: 3}, {steel_pipe: 2}, 6)

# Advanced recipes

modular_frame_recipe: Recipe = Recipe("Modular Frame", MachineType.ASSEMBLER, {reinforced_iron_plate: 3, iron_rod: 12}, {modular_frame: 2}, 60)
rotor_recipe: Recipe = Recipe("Rotor", MachineType.ASSEMBLER, {iron_rod: 5, screw: 25}, {rotor: 1}, 15)
stator_recipe: Recipe = Recipe("Stator", MachineType.ASSEMBLER, {steel_pipe: 3, wire: 8}, {stator: 1}, 12)

# Project Assembly recipes

smart_plating_recipe: Recipe = Recipe("Smart Plating", MachineType.ASSEMBLER, {reinforced_iron_plate: 1, rotor: 1}, {smart_plating: 1}, 30)
versatile_framework_recipe: Recipe = Recipe("Versatile Framework", MachineType.ASSEMBLER, {steel_beam: 30, modular_frame: 2.5}, {versatile_framework: 5}, 24)
automated_wiring_recipe: Recipe = Recipe("Automated Wiring", MachineType.ASSEMBLER, {stator: 1, cable: 20}, {automated_wiring: 1}, 24)