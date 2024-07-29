
class Converter:

    def km_to_miles(self, km):
        return str(round(km / 1.609, 2)) + " Miles"

    def miles_to_km(self, m):
        return str(round(m * 1.609, 2)) + " Km"
