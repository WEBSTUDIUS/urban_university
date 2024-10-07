import runner
import unittest as utest

class RunnerTest(utest.TestCase):
    def setUp(self):
        pass

    def test_walk(self):
        runner1 = runner.Runner('John')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)


    def test_run(self):
        runner2 = runner.Runner('Tim')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)


    def test_challenge(self):
        runner3 = runner.Runner('Andy')
        runner4 = runner.Runner('Bob')

        for i in range(10):
            runner3.walk()
            runner4.run()

        self.assertNotEqual(runner3.distance, runner4.distance, 'distances not equal')


if __name__ == '__main__':
    utest.main()