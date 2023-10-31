import Lab2 as lab2
def test_find_min_max():
    input_arr=[64,34,25,12,22,11,90,98,91,13,47]
    result=lab2.find_min_max(input_arr)
    assert(result== 11, 98)
def test_calc_average():
    input_arr = [5,6,7]
    result=lab2.calc_average(input_arr)
    assert(result==6)

def test_calc_median_temperature():
    input_arr=[1,2,3,4,5]
    result=lab2.calc_median_temperature(input_arr)
    assert(result == 3)