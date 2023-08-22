from sqlalchemy import Column, Integer, String, ForeignKey, Table 
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

association_table = Table(
    "workout_exercise", 
    Base.metadata,
    Column("exercise_id", ForeignKey("exercise.id")),
    Column("workout_id", ForeignKey("workout.id")),
)

class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    workout_description = Column(String)
    exercises = relationship("Exercise", secondary=association_table, back_populates='workout')

    # "back_populates" added to Workout class. 

class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    exercise_description= Column(String)
    category = Column(String)
    weight = Column(Integer)
    units = Column(String)
    reps = Column(Integer)
    sets = Column(Integer)
    workout = relationship("Workout", secondary=association_table, back_populates='exercise')

    # "back_populates" added to Exercise class


# Do I need __repr__ methods for each class? 


