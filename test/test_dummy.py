import pytest, sys
from makesound import MakeSound

class Test_Dummy():

    @pytest.mark.smoke
    def test_sample(self):
        print("Hello this is pytest unittest")
        print(sys.executable)
    
    @pytest.mark.unit
    def test_sampletwo(self):
        m = MakeSound()
        assert m.oneNote("D3", 1000), True

