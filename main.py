from models.water_sources.river import River
from models.water_sources.well import Well
from models.water_sources.reservoir import Reservoir

from models.consumers.house import House
from models.consumers.farm import Farm
from models.consumers.factory import Factory

from models.treatments.sand_filter import SandFilter
from models.treatments.uv_treatment import UVTreatment

from services.water_network import WaterNetwork
from reports.report_generator import ReportGenerator



def main():

    # -------------------------
    # Create water sources
    # -------------------------

    river = River(
        "Vistula River",
        10000,
        8000
    )

    well = Well(
        "Deep Well",
        5000,
        50
    )

    reservoir = Reservoir(
        "Main Reservoir",
        8000,
        6000
    )


    # -------------------------
    # Create consumers
    # -------------------------

    house = House("Family House")

    farm = Farm("Green Farm")

    factory = Factory("Textile Factory")


    # -------------------------
    # Create treatments
    # -------------------------

    sand_filter = SandFilter("Sand Filter")

    uv = UVTreatment("UV Treatment")


    # -------------------------
    # Create network
    # -------------------------

    network = WaterNetwork()


    # Add sources

    network.add_source(river)
    network.add_source(well)
    network.add_source(reservoir)


    # Add consumers

    network.add_consumer(house)
    network.add_consumer(farm)
    network.add_consumer(factory)


    # Add treatments

    network.add_treatment(sand_filter)
    network.add_treatment(uv)


    # -------------------------
    # Generate report
    # -------------------------

    report = ReportGenerator(network)

    print(report.create_report())



if __name__ == "__main__":
    main()