import pytest


class TestCalculator:

    def setup_class(self):
        print("TestCalculator setup_class")

    def teardown_class(self):
        print("TestCalculator teardown_class")

    def setup(self):
        print("TestCalculator setup")

    def teardown(self):
        print("TestCalculato teardown")

    @pytest.mark.parametrize(("a", "b", "c"), [(10, 5, 0.2), (0.3, 0.5, 0.4), (1000, 3000, 5)])  # int float
    def test_add(self, a, b, c):
        return a + b + c

    @pytest.mark.parametrize(("a", "b"), [(10, 5), (0.3, 0.5)])
    def test_less(self, a, b):
        return a - b

    @pytest.mark.parametrize(("a", "b", "c"), [(10, 5, 1000), (0.3, 0.5, 10), (1000, 3000, 0.02)])
    def test_mul(self, a, b, c):
        return a * b * c

    @pytest.mark.parametrize(("a", "b"), [(10, 5), (5000, 25)])
    def test_div(self, a, b):
        return a / b
