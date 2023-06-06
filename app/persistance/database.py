# from sqlalchemy import create_engine, __version__, Column, Integer, String, Date, DateTime, Enum, Numeric, Float,\
#     MetaData, ForeignKey
# from sqlalchemy.orm import relationship, declarative_base, sessionmaker
# from app.model.car import EngineType, CarBodyType, CarBodyColor, TyreType, TyreModel
# from tests.data.car_obj_data import CAR_1
# import logging
# from app.persistance.connection import MySQLConnectionPool
#
#
# username = 'user1'
# password = 'user'
# database = 'db_1'
# port = 3307
# database_url = f'mysql://{username}:{password}@localhost:{port}/{database}'
# engine = create_engine(database_url, echo=True, future=True)
# metadata_obj = MetaData()
# Base = declarative_base()
#
#
# # TODO Do it with a SQL Alchemy 2.0 way or alembic
#
# class Car(Base):
#     __tablename__ = 'Car'
#     id = Column(Integer, primary_key=True)
#     model = Column(String(50))
#     price = Column(Integer)
#     mileage = Column(Integer)
#     engine = relationship('Engine', uselist=False, back_populates='car')
#     wheel = relationship('Wheel', uselist=False, back_populates='car')
#     car_body = relationship('CarBody', uselist=False, back_populates='car')
#
#
# class Engine(Base):
#     __tablename__ = 'Engine'
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(EngineType), unique=True)
#     power = Column(Float)
#     engine_id = Column(Integer, ForeignKey('Car.id'))
#     car = relationship('Car', back_populates='engine')
#
#
# class Wheel(Base):
#     __tablename__ = 'Wheel'
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(TyreType), unique=True)
#     model = Column(String(20))
#     size = Column(Integer)
#     wheel_id = Column(Integer, ForeignKey('Car.id'))
#     car = relationship('Car', back_populates='wheel')
#
#
# class CarBody(Base):
#     __tablename__ = 'CarBody'
#     id = Column(Integer, primary_key=True)
#     color = Column(Enum(CarBodyColor), unique=True)
#     type = Column(Enum(CarBodyType), unique=True)
#     car_body_id = Column(Integer, ForeignKey('Car.id'))
#     car = relationship('Car', back_populates='car_body')
#
#
# # Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# new_car = Car(
#     model=CAR_1.model,
#     price=CAR_1.price,
#     mileage=CAR_1.mileage
# )
#
# new_engine = Engine(
#     type=CAR_1.engine.type.name,
#     power=CAR_1.engine.power
# )
#
# new_wheel = Wheel(
#     type=CAR_1.wheel.type.name,
#     model=CAR_1.wheel.model,
#     size=CAR_1.wheel.size
# )
#
# new_car_body = CarBody(
#     color=CAR_1.car_body.color.name,
#     type=CAR_1.car_body.type.name
# )
#
# # new_car.engine = new_engine
# # new_car.wheel = new_wheel
# # new_car.car_body = new_car_body
#
#
# # session.add(new_car)
# session.commit()
#
