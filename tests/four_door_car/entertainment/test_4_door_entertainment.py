from pytest import mark

@mark.smoke
@mark.four_door_entertainment
class FourDoorEntertainmentTests:
    @mark.ui
    def test_four_door_entertainment_browser(self, chrome_browser):
        chrome_browser.get("https://www.cartoys.com/car-entertainment/car-stereo")
        assert True
        
    @mark.four_door_audio
    def test_stereo(self):
        assert True

    @mark.four_door_audio
    def test_speakers(self):
        assert True

    @mark.four_door_tool
    def test_gps(self):
        assert True

    @mark.four_door_lighting
    def test_cabin_lighting(self):
        assert True