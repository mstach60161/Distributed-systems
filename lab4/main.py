import pymongo
from dispatcher import Dispatcher
from station import Station


# def init_database():
#     myclient = pymongo.MongoClient("mongodb://localhost:8000/")
#     mydb = myclient["database"]
#     satellites = mydb['satellites']
#     satellites_errors = []
#     for id in range(100, 200):
#         satellites_errors.append({
#             'id' : id,
#             'number' : 0
#         })
#         satellites.insert_many(satellites_errors)
#     return mydb

# mydb = init_database()
# sasatellites = mydb['satellites']

# print(satellites.find({ 'id': 10 }))

dispatcher = Dispatcher.start()
station1 = Station.start('station1', dispatcher)
station1.tell(
    {
        'query_id' : 1,
        'first_sat_id' : 100,
        'range' : 10,
        'timeout' : 0.350
    }
)