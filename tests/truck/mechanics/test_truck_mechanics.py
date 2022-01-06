from pytest import mark

@mark.smoke
@mark.truck_mechanic
class TruckMechanicsTests:
    @mark.ui
    def test_truck_mechanics_browser(self, chrome_browser):
        chrome_browser.get("https://haynes.com/en-us/search?query=truck")
        assert True
   
    @mark.truck_engine
    def test_engine(self):
        assert True

    @mark.truck_drivetrain
    def test_drivetrain(self):
        assert True
    
    @mark.truck_brakes
    def test_front_brakes(self):
        assert True
    
    @mark.truck_brakes
    def test_rear_brakes(self):
        assert True

    @mark.truck_suspension
    def test_front_right_spring(self):
        assert True

    @mark.truck_suspension
    def test_front_right_spring(self):
        assert True

    @mark.truck_suspension
    def test_front_right_spring(self):
        assert True

    @mark.truck_suspension
    def test_front_right_spring(self):
        assert True

    @mark.truck_suspension
    def test_front_left_shock(self):
        assert True

    @mark.truck_suspension
    def test_rear_left_shock(self):
        assert True

    @mark.truck_suspension
    def test_front_right_shock(self):
        assert True

    @mark.truck_suspension
    def test_rear_right_shock(self):
        assert True