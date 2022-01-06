from pytest import mark

@mark.smoke
@mark.truck_body
class TruckBodyTests:
    @mark.ui
    def test_truck_body_browser(self, chrome_browser):
        chrome_browser.get("https://stylethattruck.com/what-is-the-anatomy-of-a-pickup-truck/")
        assert True
        
    @mark.truck_door
    def test_front_left_door(self):
        assert True

    @mark.truck_door
    def test_front_right_door(self):
        assert True

    @mark.truck_door
    def test_rear_left_door(self):
        assert True

    @mark.truck_door
    def test_rear_right_door(self):
        assert True

    @mark.truck_bed
    def test_bed(self):
        assert True

    @mark.truck_bumper
    def test_front_bumper(self):
        assert True

    @mark.truck_bumper
    def test_rear_bumper(self):
        assert True
    
    @mark.truck_panel
    def test_front_left_fender(self):
        assert True

    @mark.truck_panel
    def test_rear_left_quarter(self):
        assert True
    
    @mark.truck_panel
    def test_front_right_fender(self):
        assert True

    @mark.truck_panel
    def test_rear_right_quarter(self):
        assert True