import time, enum, random

class SatelliteAPI():

    class Status(enum.Enum):
        OK = 1
        BATTERY_LOW = 2
        PROPULSION_ERROR = 3
        NAVIGATION_ERROR = 4
    
    @staticmethod
    def get_status():
        
        try:
            time.sleep( (100 + random.randint(0, 400)) / 1000 )
        except:
            print("Error occured in get_status")
        
        p = random.uniform(0, 1)

        if p < 0.8:
            return SatelliteAPI.Status.OK
        elif p < 0.9:
            return SatelliteAPI.Status.BATTERY_LOW
        elif p < 0.95:
            return SatelliteAPI.Status.NAVIGATION_ERROR
        else:
            return SatelliteAPI.Status.PROPULSION_ERROR
