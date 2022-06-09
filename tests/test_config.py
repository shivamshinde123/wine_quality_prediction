import pytest
## always start the function name with 'test' so that pytest can identify it


class NotInRangeError(Exception):
    
    def __init__(self,message="Value not in range"):
        self.message = message
        super().__init__(self.message)

def test_range_of_input_values():
    a = 5 
    with pytest.raises(NotInRangeError):
        if a not in range(10,20):
            raise NotInRangeError
