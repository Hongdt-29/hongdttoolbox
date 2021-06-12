from hongdttoolbox.lib import pushing_all_zeros_to_end_of_array
def test_resutl():
    assert(pushing_all_zeros_to_end_of_array([1,0,0,6,9,3],6)[-1])==0
