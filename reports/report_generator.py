from services.water_network import WaterNetwork


class ReportGenerator:
    """
    Responsible only for creating reports.

    It does not calculate anything.
    It receives data from WaterNetwork.
    """

    def __init__(self, network: WaterNetwork):
        self._network = network


    def create_report(self):
        """
        Creates a formatted report
        about the current water system.
        """

        production = self._network.total_production()
        consumption = self._network.total_consumption()
        balance = self._network.water_balance()
        cost = self._network.treatment_cost()


        report = (
            "\n"
            "========== WATER DISTRIBUTION REPORT ==========\n"
            f"Total water produced: {production} m3\n"
            f"Total water consumed: {consumption} m3\n"
            f"Water balance: {balance} m3\n"
            f"Treatment cost: {cost} PLN\n"
            "===============================================\n"
        )

        return report