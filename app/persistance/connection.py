from mysql.connector import pooling
from pythonlangutil.singleton import Singleton
import json

# TODO Do it via Builder pattern
# Should I add the .env file to remote git repo?


#
# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class MySQLConnectionPool(metaclass=Singleton):
#     def __init__(self):
#         with open('db_config.json') as f:
#             config = json.load(f)
#
#         self._pool = pooling.MySQLConnectionPool(
#             pool_name='my_pool',
#             pool_size=5,
#             pool_reset_session=True,
#             **config
#         )
#
#     def get_connection(self):
#         return self._pool.get_connection()
#
#     def close(self):
#         self._pool.close()
#
