import unittest
from roles.programmer import Programmer


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer()

    def test_develop_program(self):
        # 编写针对 `develop_program` 方法的测试
        pass

    def test_write_test(self):
        # 编写针对 `write_test` 方法的测试
        pass

if __name__ == '__main__':
    unittest.main()
