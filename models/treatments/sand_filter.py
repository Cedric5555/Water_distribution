from models.treatments.water_treatment import WaterTreatment


class SandFilter(WaterTreatment):

    def purify(self, amount):
        return amount * 0.95


    def cost(self):
        return 100