import pykka
import time

class Station(pykka.ThreadingActor):
    def __init__(self, name, dispatcher):
        super().__init__()
        self.name = name
        self.dispatcher = dispatcher
 
    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_failure(self, exception_type, exception_value, traceback):
        pass

    def on_receive(self, message):
        self.ask_and_print_response(message)
 
    def ask_and_print_response(self, message):
        start_time = time.time()
        response = self.dispatcher.ask(message)
        result_time = time.time() - start_time
        
        print('station: ', self.name)
        print('time: ', result_time)
        print('amount of errors: ', len(response['map_id']))
        print()

        for item in response['map_id']:
            print(item['id'], ': ',item['status'])




# if __name__ == '__main__':
#     my_actor_ref = Satellite.start()
#     print(my_actor_ref.ask('get_status'))
#     time.sleep(1)
#     my_actor_ref.stop()
