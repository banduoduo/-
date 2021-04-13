import pytest
import yaml
from Calculator import Calculator


def get_datas():
    with open("./num.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_getdatas():
    with open("./num.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)


class TestCal:

    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    @pytest.mark.parametrize('a,b,expect', get_datas()['add'], ids=get_datas()['ids'])
    def test_add_int(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.4, 0.8, 1.2]], ids=['float22', 'float222'])
    def test_add_float(self, a, b, expect):
        assert expect == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [20, 10, 10]
    ], ids=['int1', 'int_1'])
    def test_less_int(self, a, b, expect):
        assert expect == self.calc.less(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.5, 0.1, 0.4], [1.8, 0.8, 1]], ids=['float1', 'float_1'])
    def test_less_float(self, a, b, expect):
        assert expect == self.calc.less(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1000, 1, 1000]
    ], ids=['int2', 'int_2'])
    def test_div_int(self, a, b, expect):
        assert expect == (self.calc.div(a, b))

    @pytest.mark.parametrize('a,b,expect', [
        [0.4, 0.2, 0.2], [10, 1, 10]
    ], ids=['float2', 'float2_2'])
    def test_div_float(self, a, b, expect):
        assert expect == self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0, 1, 0], [10, 0, 0]
    ], ids=['zero1', 'zero2'])
    def test_div_zero(self, a, b, expect):
        assert expect == self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1000, 1, 1000]
    ], ids=['int3', 'int_3'])
    def test_mul_int(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.4, 0.2, 0.08], [10, 1, 10]
    ], ids=['float3', 'float_3'])
    def test_mul_float(self, a, b, expect):
        assert expect == round(self.calc.mul(a, b), 2)
