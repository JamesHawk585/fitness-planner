from sqlalchemy import Column, Integer, String, ForeignKey, Table 
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

association_table = Table(
    "workout_exercise", 
    Base.metadata,
    Column("exercise_id", ForeignKey("exercise.id")),
    Column("workout_id", ForeignKey("workout.id")),
)

# __str__ is an instance methoid on a class. 

class Workout(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    workout_description = Column(String)
    exercises = relationship("Exercise", secondary=association_table)
    def __repr__(self):
        # using self in string interpolation gives the f string access tot he workout_name instance variable. 
        return f'Workout: {self.workout_name}\n Description: {self.workout_description}\n'
    


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
    def __repr__(self):
        return f'Exercise Name: {self.exercise_name} \n Exercise Description: {self.exercise_description}\n Category: {self.category}\n Weight: {self.weight}\n Units: {self.units}\n Repititions: {self.reps}\n Sets: {self.sets}'


