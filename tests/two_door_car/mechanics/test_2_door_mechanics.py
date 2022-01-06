from pytest import mark
import time

@mark.smoke
@mark.two_door_mechanic
class TwoDoorMechanicsTests:
    @mark.ui
    def test_two_door_mechanics_browser(self, chrome_browser):
        chrome_browser.get("https://haynes.com/en-us/search?query=coupe")
        assert True


    def engine(self, car_condition, part_condition):
        if car_condition == 'New':
            if part_condition == 'Clean':
                print("\n\nEngine passes inspection")
                assert True
            elif part_condition == 'Faulty':
                print("\n\nEngine is faulty, send back to manufacturer")
                assert False
        elif car_condition == 'Used':
            if part_condition == 'Clean':
                print("\n\nUsed engine is good to go")
                assert True
            elif part_condition == 'Faulty':
                print("\n\nUsed engine is faulty, send back to manufacturer")
                assert False
        else:
            assert False


    @mark.two_door_drivetrain
    def drivetrain(self, car_condition, part_condition):
        if car_condition == 'New':
            if part_condition == 'Clean':
                print("\n\nDrivetrain passes inspection")
                assert True
            elif part_condition == 'Faulty':
                print("\n\nDrivetrain is faulty, send back to manufacturer")
                assert False
        elif car_condition == 'Used':
            if part_condition == 'Clean':
                print("\n\nUsed drivetrain is good to go")
                assert True
            elif part_condition == 'Faulty':
                print("\n\nUsed drivetrain is faulty, send back to manufacturer")
                assert False
        else:
            assert False
    
    # @mark.two_door_brakes
    # def test_brakes(self, car_condition, front, rear):
    #     assert True

    # @mark.two_door_suspension
    # def test_springs(self, car_condition, left_front, left_rear, right_front, right_rear):
    #     assert True

    # @mark.two_door_suspension
    # def test_shocks(self, car_condition, left_front, left_rear, right_front, right_rear):
    #     assert True


    
    # @mark.two_door_brakes
    # def test_rear_brakes(self, car_condition):
    #     assert True

    # @mark.two_door_suspension
    # def test_front_right_spring(self, car_condition):
    #     assert True

    # @mark.two_door_suspension
    # def test_front_right_spring(self, car_condition):
    #     assert True


    # @mark.two_door_suspension
    # def test_rear_left_shock(self):
    #     assert True

    # @mark.two_door_suspension
    # def test_front_right_shock(self):
    #     assert True

    # @mark.two_door_suspension
    # def test_rear_right_shock(self):
    #     assert True


# if car_condition == 'New':
#             if part_condition == 'Clean':
#                 print("\n\nEngine passes inspection")
#                 assert True
#             elif part_condition == 'Faulty':
#                 print("\n\nEngine is faulty send back to manufacturer")
#                 assert False
#         elif car_condition == 'Used':
#             if part_condition == 'Clean':
#                 print("\n\nUsed engine is good to go")
#                 assert True
#             elif part_condition == 'Faulty':
#                 print("\n\nUsed engine is faulty send back to manufacturer")
#                 assert False
#         else:
#             assert False