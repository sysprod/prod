import unittest
import hello


class TestHello(unittest.TestCase):

    def test(self):
        self.name = "name"
        self.want = "Hello, name!"
        self.got = hello.Hello(self.name)
        self.assertEqual(self.got, self.want)


if __name__ == '__main__':
    unittest.main()
