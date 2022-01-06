from pytest import mark

@mark.smoke
@mark.two_door_body
class TwoDoorBodyTests:
    @mark.ui
    def test_two_door_body_browser(self, chrome_browser):
        chrome_browser.get("https://carfromjapan.com/article/industry-knowledge/10-fun-facts-coupe/")
        assert True

    @mark.two_test_door
    def test_left_door(self):
        assert True

    @mark.two_test_door
    def test_right_door(self):
        assert True

    @mark.two_door_trunk
    def test_trunk(self):
        assert True

    @mark.two_door_bumper
    def test_front_bumper(self):
        assert True

    @mark.two_door_bumper
    def test_rear_bumper(self):
        assert True
    
    @mark.two_door_panel
    def test_front_left_fender(self):
        assert True

    @mark.two_door_panel
    def test_rear_left_quarter(self):
        assert True
    
    @mark.two_door_panel
    def test_front_right_fender(self):
        assert True

    @mark.two_door_panel
    def test_rear_right_quarter(self):
        assert True