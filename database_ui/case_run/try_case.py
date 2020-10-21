import unittest
from case_run.position_elements import PositionElements as PE


class TryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def sum(self, a, b):
        return a + b

    def sun(self, a, b):
        return a - b

    def test_1_badiu(self):
        PE.start_url(PE)
        PE.get_url(PE,"http://www.baidu.com")
        PE.url_element(PE, "id", "kw").send_keys("python")
        PE.url_element(PE, "id", "su").click()

    # def test_1_case(self):
    #     num = self.sum(2, 3)
    #     self.assertEqual(num, 6)
    #
    # def test_2_case(self):
    #     num = self.sun(3, 4)
    #     self.assertEqual(num, -1)
