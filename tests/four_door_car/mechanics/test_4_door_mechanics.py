from pytest import mark

@mark.smoke
@mark.four_door_mechanic
class FourDoorMechanicsTests:
    @mark.ui
    def test_four_door_mechanics_browser(self, chrome_browser):
        chrome_browser.get("https://haynes.com/en-us/car-manuals/car-makes?gclid=Cj0KCQiAoNWOBhCwARIsAAiHnEicXcE_fFZlXzzRuADvD_VgAjZMs76Qboc3tJGi3hG3t7Kf7l6gq3gaAuvOEALw_wcB")
        assert True
        
    @mark.four_door_engine
    def test_engine(self):
        assert True

    @mark.four_door_drivetrain
    def test_drivetrain(self):
        assert True
    
    @mark.four_door_brakes
    def test_front_brakes(self):
        assert True
    
    @mark.four_door_brakes
    def test_rear_brakes(self):
        assert True

    @mark.four_door_suspension
    def test_front_right_spring(self):
        assert True

    @mark.four_door_suspension
    def test_front_right_spring(self):
        assert True

    @mark.four_door_suspension
    def test_front_right_spring(self):
        assert True

    @mark.four_door_suspension
    def test_front_right_spring(self):
        assert True

    @mark.four_door_suspension
    def test_front_left_shock(self):
        assert True

    @mark.four_door_suspension
    def test_rear_left_shock(self):
        assert True

    @mark.four_door_suspension
    def test_front_right_shock(self):
        assert True

    @mark.four_door_suspension
    def test_rear_right_shock(self):
        assert True