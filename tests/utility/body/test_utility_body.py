from pytest import mark

@mark.smoke
@mark.utility_body
class UtilityBodyTests:
    @mark.ui
    def test_utility_body_browser(self, chrome_browser):
        chrome_browser.get("https://www.knapheide.com/blog/open-service-body-or-enclosed-utility-body-which-to-choose/")
        assert True
        
    @mark.utility_door
    def test_left_door(self):
        assert True

    @mark.utility_door
    def test_left_rear_door(self):
        assert True

    @mark.utility_door
    def test_right_door(self):
        assert True

    @mark.utility_door
    def test_right_rear_door(self):
        assert True

    @mark.utility_bumper
    def test_front_bumper(self):
        assert True
    
    @mark.utility_bumper
    def test_rear_bumper(self):
        assert True

    @mark.utility_panel
    def test_left_fender(self):
        assert True

    @mark.utility_panel
    def test_left_quarter(self):
        assert True

    @mark.utility_panel
    def test_right_fender(self):
        assert True

    @mark.utility_panel
    def test_right_quarter(self):
        assert True

    @mark.utility_extra
    def test_utility_tool_attachments(self):
        assert True