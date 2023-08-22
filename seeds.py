from models import Workouts, Exercises, Workout_Exercises
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

print("🌱 Seeding DB...")

engine = create_engine('sqlite:///fitness_data.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Exercises).delete()
session.query(Workouts).delete()
session.query(Workout_Exercises).delete()

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
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Planks", 
        exercise_description="Hold push-up position", 
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Situps", 
        exercise_description="Lie on bench. lift torso.", 
        category="Strength", 
        weight=0, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Jog", 
        exercise_description="Light run", 
        category="Cardio", 
        weight=1, 
        units="Miles", 
        reps=1, 
        sets=1),
    Exercises(
        exercise_name="Cycle", 
        exercise_description="Cycle in place", 
        category="Cardio", 
        weight=1, 
        units="Mile", 
        reps=1, 
        sets=1),
    Exercises(
        exercise_name="Latv Pulldowns", 
        exercise_description="Sit, pull bar to chest.", 
        category="Strength", 
        weight=160, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Shrugs", 
        exercise_description="Holds dumbells. Lift shoulders and hold.", 
        category="Strength", 
        weight=100, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Deltoid Raises", 
        exercise_description="Choose wight, lift dumbell sideways while isolating the deltoids.", 
        category="Strength", 
        weight=10, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Cable Flys", 
        exercise_description="Pull cables across chest.", 
        category="Strength", 
        weight=120, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercises(
        exercise_name="Cable Treicep Extensions", 
        exercise_description="Pull cable down and extend arms.", 
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
]

workouts = [
    Workouts(
        workout_name="push",
        workout_description="In the “push” workout you train all the upper body pushing muscles, i.e. the chest, shoulders and triceps."),
    Workouts(
        workout_name="Pull",
        workout_description="In the “pull” workout you train all the upper body pulling muscles, i.e. the back and biceps."), 
    Workouts(
        workout_name="Abs & Legs",
        workout_description="And in the “legs” workout you train the entire lower body, i.e. the quads, hamstrings, calves and abdominals."
    )
]

workout_exercises = [
    workout_id="???", 
    exercise_id="???"
]
