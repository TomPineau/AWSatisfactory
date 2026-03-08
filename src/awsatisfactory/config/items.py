from awsatisfactory.domain.Item import Item

# Nodes (Items that can be mined infinitely)

iron_node: Item = Item("Iron Node", True)
copper_node: Item = Item("Copper Node", True)
coal_node: Item = Item("Coal Node", True)

infinite_nodes: list[Item] = [iron_node, copper_node, coal_node]

# Iron based items

iron_ore: Item = Item("Iron Ore")
iron_ingot: Item = Item("Iron Ingot")
iron_plate: Item = Item("Iron Plate")
iron_rod: Item = Item("Iron Rod")
screw: Item = Item("Screw")
reinforced_iron_plate: Item = Item("Reinforced Iron Plate")

# Copper based items

copper_ore: Item = Item("Copper Ore")
copper_ingot: Item = Item("Copper Ingot")
wire: Item = Item("Wire")
cable: Item = Item("Cable")

# Steel based items

coal_ore: Item = Item("Coal Ore")
steel_ingot: Item = Item("Steel Ingot")
steel_beam: Item = Item("Steel Beam")
steel_pipe: Item = Item("Steel Pipe")

# Advanced items

modular_frame: Item = Item("Modular Frame")
rotor: Item = Item("Rotor")
stator: Item = Item("Stator")

# Project Assembly items

smart_plating: Item = Item("Smart Plating")
versatile_framework: Item = Item("Versatile Framework")
automated_wiring: Item = Item("Automated Wiring")
