import os
from awsatisfactory.domain.enum.MachineType import MachineType

BUCKET : str = os.environ.get("DATA_BUCKET", None)
BUCKET_SUB : str = os.environ.get("DATA_SUB_BUCKET", None)

ENERGY_CHARTS : str = "energy_charts"
PRICE : str = "price"

RAW_URL: str = "https://api.energy-charts.info"
DATASET: str = "price"
BIDDING_ZONE: str = "FR"

MACHINE_POWER_BASE : dict = {
        MachineType.MINER: 5,
        MachineType.SMELTER: 4,
        MachineType.CONSTRUCTOR: 4,
        MachineType.FOUNDRY: 16,
        MachineType.ASSEMBLER: 15,
        MachineType.REFINERY: 30,
        MachineType.MANUFACTURER: 55,
    }

DURATION : int = 1
