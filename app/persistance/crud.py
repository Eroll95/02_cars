# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, session
# import logging
# from app.model.car import Car
#
# class CRUDService:
#     def __init__(self, engine, entity_type):
#         self._engine = engine
#         self._entity_type = entity_type
#
#     def create(self, item: type) -> None:
#         try:
#             Session = self._create_session()
#             session = Session()
#             session.add(item)
#             session.commit()
#         except Exception as e:
#             session.rollback()
#             logging.error(e)
#         finally:
#             session.close()
#
#     def read(self, item_id: int) -> type:
#         try:
#             Session = self._create_session()
#             session = Session()
#             item = session.query(self._entity_type).filter_by(id=item_id).first()
#             return item
#         except Exception as e:
#             session.rollback()
#             logging.error(e)
#         finally:
#             session.close()
#
#     def update(self, item: type) -> None:
#         try:
#             Session = self._create_session()
#             session = Session()
#             item = session.merge(item)
#             session.add(item)
#             session.commit()
#         except Exception as e:
#             session.rollback()
#             logging.error(e)
#         finally:
#             session.close()
#
#     def delete(self, item_id: int) -> None:
#         try:
#             Session = self._create_session()
#             session = Session()
#             item = session.query(self._entity_type).filter_by(id=item_id).first()
#             session.delete(item)
#             session.commit()
#         except Exception as e:
#             session.rollback()
#             logging.error(e)
#         finally:
#             session.close()
#
#     def list_all(self) -> list[type]:
#         try:
#             Session = self._create_session()
#             session = Session()
#             items = session.query(self._entity_type).all()
#             return items
#         except Exception as e:
#             session.rollback()
#             logging.error(e)
#         finally:
#             session.close()
#
#     def _create_session(self):
#         return sessionmaker(bind=self._engine)
#
#
# username = 'user1'
# password = 'user'
# database = 'db_1'
# port = 3307
# database_url = f'mysql://{username}:{password}@localhost:{port}/{database}'
# engine = create_engine(database_url, echo=True, future=True)
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# def print_all_cars():
#     crud_service = CRUDService(engine, Car)
#     cars = crud_service.list_all()
#     for car in cars:
#         print(car.model, car.price, car.mileage)
#
#
# print_all_cars()
