import Lab2.bmi as bmi

def test_calcBMI_underweight():
    expected = -1
    result=bmi.calculate_bmi(1.73, 37)
    assert(result==expected)

def test_calcBMI_normalweight():
    expected = 0
    result=bmi.calculate_bmi(1.73, 57)
    assert(result==expected)

def test_calcBMI_overweight():
    expected = 1
    result=bmi.calculate_bmi(1.73, 97)
    assert(result==expected)



