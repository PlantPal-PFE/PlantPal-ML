
print("yeehaw")
import math

data = {"time" : 60} 


class Entretient:
    def __init__(self,recommentation):
        self.water_threshold = recommentation["water"]
        self.light_threshold = recommentation["light"]
        self.humidity_threshold = recommentation["humidity"]
        self.tmp_threshold = recommentation["tmp"]

    def entretient_eau(self,data):
        #   Must be watered
        #   Needs water
        #   Good water level

        #   Watered
        #   Watered early
        if data[-1] > self.water_threshold:
            return "Good water level"
        elif (math.mean(data[-3:])) < self.water_threshold: # Test si les 3 dernières valeurs sont inférieures au seuil
            return "Must be watered"
        elif data[-1] < self.water_threshold: #à voir si on prend le dernier élément
            return "Needs water"
        else:
            return "Error"


    def entretient_lumiere(self,data):
        if data[-1] > self.light_threshold-5 and data[-1] < self.light_threshold+5:
            return "Optimal light level"
        elif data[-1] > self.light_threshold-15 and data[-1] < self.light_threshold+15:
            return "good light level"
        elif data[-1] < self.light_threshold:
            return "Low light"
        elif data[-1] > self.light_threshold:
            return "Too much light"
        else:
            return "Error"

    def entretient_humidite(self,data):
        if data[-1] > self.humidity_threshold+15:
            return "High humidity"
        elif data[-1] > self.humidity_threshold-15 and data[-1] < self.humidity_threshold+15:
            return "Good humidity level"
        elif data[-1] < self.humidity_threshold-15: #à voir si on prend le dernier élément
            return "Low humidity"
        else:
            return "Error"

    def entretient_tmp(self,data):
        if data[-1] > self.tmp_threshold+5:
            return "High temperature"
        elif data[-1] > self.tmp_threshold-5 and data[-1] < self.tmp_threshold+5:
            return "Good temperature level"
        elif data[-1] < self.tmp_threshold-5:
            return "Low temperature"
        else:
            return "Error"
        
    def entretent_new_data(self, new_data):
        pass

    def entretient_daily(self):
        self.entretient_eau()
        self.entretient_lumiere()
        self.entretient_humidite()
        self.entretient_tmp()


recommentationMenthe = {"water" : 20, "light" : 60, "humidity" : 60, "tmp" : 60}
ent = Entretient(recommentationMenthe)
