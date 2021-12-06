from nianiania import convertor

def test_regular_word():
    x = convertor("perfecto")
    assert x=="pirficti"

def test_using_letter_q():
    x = convertor("queso")
    assert x=="quisi"

def test_more_than_one_vocal_next_to():
    x = convertor("bien")
    assert x=="bin"

def test_large_string():
    x = convertor("por que no te vas bien a la puta que te pario")
    assert x=="pir qui ni ti vis bin i li piti qui ti piri"

def test_conjunction_with_an_y():
    x = convertor("pedro y pablo")
    assert x=="pidri i pibli"

def test_add_a_q_when_c_plus_vocal():
    x = convertor("casa")
    assert x=="quisi"

def test_it_has_to_respect_upper_and_low():
    x = convertor("LA CONCHA DE MI MADRE")
    assert x=="LI QUINCHI DI MI MIDRI"