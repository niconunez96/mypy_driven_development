def test_it_should_return_true():
    a = 1
    b = 2
    assert a == b


def test_it_should_return_false():
    a = "I'm a string"
    a = 15
    b = 16

    assert a == b
