from pytest import mark

@mark.smoke
@mark.utility_features
class UtilityFeaturesTests:
    @mark.ui
    def test_utility_features_browser(self, chrome_browser):
        chrome_browser.get("https://www.worktruckwest.com/equipment/accessories-and-additional-equipment/")
        assert True
        
    @mark.utility_audio
    def test_stereo(self):
        assert True

    @mark.utility_audio
    def test_speakers(self):
        assert True

    @mark.utility_radio
    def test_radio(self):
        assert True

    @mark.utility_tool
    def test_gps(self):
        assert True

    @mark.utility_lighting
    def test_cabin_lighting(self):
        assert True

    @mark.utility_attachments
    def test_vehicle_attachments(self):
        assert True