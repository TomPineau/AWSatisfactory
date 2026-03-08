from awsatisfactory.domain.Line import Line
from awsatisfactory.config.machines import *

# Smart Plating line

smart_plating_line: Line = Line(
    "Smart Plating Line",
    [
        iron_miner_4,
        iron_smelter_3,
        iron_smelter_4,
        iron_rod_constructor_3,
        iron_rod_constructor_4,
        screw_constructor_3,
        screw_constructor_4,
        iron_plate_constructor_3,
        reinforced_iron_plate_assembler_2,
        rotor_assembler_1,
        smart_plating_assembler,
    ],
)

# Versatile Framework line

versatile_framework_line: Line = Line(
    "Versatile Framework Line",
    [
        iron_miner_1,
        iron_miner_2,
        iron_miner_3,
        coal_miner_1,
        coal_miner_2,
        iron_smelter_1,
        iron_smelter_2,
        iron_rod_constructor_1,
        iron_rod_constructor_2,
        screw_constructor_1,
        screw_constructor_2,
        iron_plate_constructor_1,
        iron_plate_constructor_2,
        reinforced_iron_plate_assembler_1,
        modular_frame_assembler_1,
        modular_frame_assembler_2,
        steel_ingot_foundry_1,
        steel_ingot_foundry_2,
        steel_ingot_foundry_3,
        steel_beam_constructor_1,
        steel_beam_constructor_2,
        versatile_framework_assembler,
    ],
)

# Automated Wiring line

automated_wiring_line: Line = Line(
    "Automated Wiring Line",
    [
        iron_miner_5,
        coal_miner_3,
        copper_miner_1,
        steel_ingot_foundry_4,
        steel_pipe_constructor_1,
        copper_ingot_smelter_1,
        copper_ingot_smelter_2,
        wire_constructor_1,
        wire_constructor_2,
        wire_constructor_3,
        wire_constructor_4,
        cable_constructor_1,
        cable_constructor_2,
        stator_assembler_1,
        automated_wiring_assembler,
    ],
)
