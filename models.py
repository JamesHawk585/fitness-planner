from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Workouts(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    wortout_description = Column(String)

class Exercises(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True)
    exercise_description= Column(String)
    category = Column(String)
    weight = Column(Integer)
    units = Column(String)
    reps = Column(Integer)
    sets = Column(Integer)

class Workout_Exercises(Base): 
    __tablename__ = "workout_exercises"
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, foreign_key=True)
    exercise_id = Column(Integer, foreign_key=True)

