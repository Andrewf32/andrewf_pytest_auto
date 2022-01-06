from pytest import mark

@mark.smoke
@mark.four_door_body
class FourDoorBodyTests:
    @mark.ui
    def test_four_door_body_browser(self, chrome_browser):
        chrome_browser.get("https://cars.usnews.com/cars-trucks/best-midsize-sedans")
        assert True
        
    @mark.four_test_door
    def test_front_left_door(self):
        assert True

    @mark.four_test_door
    def test_front_right_door(self):
        assert True

    @mark.four_test_door
    def test_rear_left_door(self):
        assert True

    @mark.four_test_door
    def test_rear_right_door(self):
        assert True

    @mark.four_door_trunk
    def test_trunk(self):
        assert True

    @mark.four_door_bumper
    def test_front_bumper(self):
        assert True

    @mark.four_door_bumper
    def test_rear_bumper(self):
        assert True
    
    @mark.four_door_panel
    def test_front_left_fender(self):
        assert True

    @mark.four_door_panel
    def test_rear_left_quarter(self):
        assert True
    
    @mark.four_door_panel
    def test_front_right_fender(self):
        assert True

    @mark.four_door_panel
    def test_rear_right_quarter(self):
        assert True