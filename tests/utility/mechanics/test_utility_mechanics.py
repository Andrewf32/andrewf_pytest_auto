from pytest import mark

@mark.smoke
@mark.utility_mechanic
class UtilityMechanicsTests:
    @mark.ui
    def test_utility_features_browser(self, chrome_browser):
        chrome_browser.get("https://www.topmarkfunding.com/truck-engines/")
        assert True
        
    @mark.utility_engine
    def test_engine(self):
        assert True

    @mark.utility_drivetrain
    def test_drivetrain(self):
        assert True
    
    @mark.utility_brakes
    def test_front_brakes(self):
        assert True
    
    @mark.utility_brakes
    def test_rear_brakes(self):
        assert True

    @mark.utility_suspension
    def test_front_right_spring(self):
        assert True

    @mark.utility_suspension
    def test_front_right_spring(self):
        assert True

    @mark.utility_suspension
    def test_front_right_spring(self):
        assert True

    @mark.utility_suspension
    def test_front_right_spring(self):
        assert True

    @mark.utility_suspension
    def test_front_left_shock(self):
        assert True

    @mark.utility_suspension
    def test_rear_left_shock(self):
        assert True

    @mark.utility_suspension
    def test_front_right_shock(self):
        assert True

    @mark.utility_suspension
    def test_rear_right_shock(self):
        assert True