import pykka
from satellite import Satellite
from satelliteAPI import SatelliteAPI
import time 


class Dispatcher(pykka.ThreadingActor):
    def __init__(self, my_arg=None):
        super().__init__()
        self.satelites = [Satellite.start(id) for id in range(100, 200)]

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_failure(self, exception_type, exception_value, traceback):
        pass

    def on_receive(self, message):

        responds = [ self.satelites[i-100].ask('get_status') for i in range(message['first_sat_id'], message['first_sat_id'] + message['range'])]

        return {
            'query_id' : message['query_id'],
            'map_id' : [respond for respond in responds if respond['status'] != SatelliteAPI.Status.OK and respond['time'] <= message['timeout']],
            'statistic' : len(list(filter(lambda x : (x['time'] <= message['timeout']), responds))) / len(responds)
        }


if __name__ == '__main__':
        
    my_actor_ref = Dispatcher.start()
    response = my_actor_ref.ask({
        'query_id' : 1,
        'first_sat_id' : 10,
        'range' : 50,
        'timeout' : 0.350
    })

    print(response)

    my_actor_ref.stop()