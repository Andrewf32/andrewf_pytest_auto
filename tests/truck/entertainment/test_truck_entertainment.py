from pytest import mark

@mark.smoke
@mark.truck_entertainment
class TruckEntertainmentTests:
    @mark.ui
    def test_truck_entertainment_browser(self, chrome_browser):
        chrome_browser.get("https://www.truckandautoelegance.com/dvd-systems.html")
        assert True
   
    @mark.truck_audio
    def test_stereo(self):
        assert True

    @mark.truck_audio
    def test_speakers(self):
        assert True

    @mark.truck_tool
    def test_gps(self):
        assert True

    @mark.truck_lighting
    def test_cabin_lighting(self):
        assert True