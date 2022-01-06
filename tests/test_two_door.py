from pytest import mark

from tests.two_door_car.mechanics.test_2_door_mechanics import TwoDoorMechanicsTests

@mark.parametrize(
        "condition,p_condition", 
        [
            ("New", "Clean"), 
            ("Used", "Clean"), 
            ("New", "Faulty"), 
            ("Used", "Faulty")
        ]
    )

@mark.two_door_engine
def test_two_door_engine(car_condition, part_condition):
    engine_tests = TwoDoorMechanicsTests()
    engine_tests.engine(car_condition, part_condition)


@mark.parametrize(
    "condition,p_condition", 
    [
        ("New", "Clean"), 
        ("Used", "Clean"), 
        ("New", "Faulty"), 
        ("Used", "Faulty")
    ]
)
@mark.two_door_drivetrain
def test_two_door_drivetrain(car_condition, part_condition):
    drivetrain_tests = TwoDoorMechanicsTests()
    drivetrain_tests.drivetrain(car_condition, part_condition)
