from models.consumers.consumer import Consumer


class Farm(Consumer):

    def consume_water(self):
        return 2000