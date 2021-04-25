import pykka
import time
from satelliteAPI import SatelliteAPI

class Satellite(pykka.ThreadingActor):
    def __init__(self, id):
        super().__init__()
        self.id = id
 
    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_failure(self, exception_type, exception_value, traceback):
        pass

    def on_receive(self, message):
        if message == 'get_status':
            
            start_time = time.time()
            status = SatelliteAPI.get_status()
            current = time.time() - start_time  
                
            return {
                'id' : self.id,
                'status' : status,
                'time' : current
            }
 

  

if __name__ == '__main__':
    my_actor_ref = Satellite.start()
    print(my_actor_ref.ask('get_status'))
    time.sleep(1)
    my_actor_ref.stop()

