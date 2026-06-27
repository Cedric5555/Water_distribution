from models.treatments.water_treatment import WaterTreatment


class UVTreatment(WaterTreatment):

    def purify(self, amount):
        return amount * 0.98


    def cost(self):
        return 200