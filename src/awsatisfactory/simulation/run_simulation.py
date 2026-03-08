from awsatisfactory.domain.Factory import Factory
from awsatisfactory.config.lines import *


def run_simulation() -> None:

    factory: Factory = Factory("My Factory")
    # factory.add_line(smart_plating_line)
    # factory.add_line(versatile_framework_line)
    factory.add_line(automated_wiring_line)

    minutes: int = 0
    duration: int = 2
    while minutes < duration:
        factory.simulate(1)
        minutes += 1
        factory.show_inventory()
    factory.show_power_consumption()
