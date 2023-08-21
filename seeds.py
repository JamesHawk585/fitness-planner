from models import Workouts, Exercises, Workout_Exercises
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

print("🌱 Seeding DB...")

engine = create_engine('sqlite:///fitness_data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Exercises).delete()

exercises = [
    Exercises(
        exercise_name="Bench Press", 
        exercise_description="Lie on bench, lift barbell to chest, extend arms.", 
        category="strength", 
        weight=150, 
        units="lb", 
        reps=10, 
        sets=2), 
    Exercises(
        exercise_name="Dumbell Press", 
        exercise_description="Lift barbells from shouder height, extend arms.", 
        category="strength", 
        weight=50, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Squat", 
        exercise_description="Bend knees, lower hips, stand up.", 
        category="strength", 
        weight=250, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Bicep Curls", 
        exercise_description="Choose wight, lift dumbell while isolating the bicep.", 
        category="strength", 
        weight=35, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Forearm Curls", 
        exercise_description="Flex wrists, lift weights.", 
        category="strength", 
        weight=30, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Deadlift", 
        exercise_description="Liftbarbell off ground while miantianing good posture. Stand tall.", 
        category="strength", 
        weight=200, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Pullups", 
        exercise_description="Hang, lift body, chin over bar.", 
        category="strength", 
        weight=0, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Cable Rows", 
        exercise_description="Sit, pull cable to torso.", 
        category="strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Planks", 
        exercise_description="Hold push-up position", 
        category="strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Situps", 
        exercise_description="Lie on bench. lift torso.", 
        category="strength", 
        weight=0, 
        units="lb", 
        reps=10, 
        sets=2),
]

