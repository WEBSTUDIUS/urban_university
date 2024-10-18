import runner2 as runner
import unittest as utest

class TournamentTest(utest.TestCase):

    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        self.tournament = runner.Tournament(90,
                                            runner.Runner('Andy', 10),
                                            runner.Runner('Bob', 9),
                                            runner.Runner('Ussain', 3))

    def tearDownClass(self):
        print('All results:', self.all_results)


if __name__ == '__main__':
    utest.main()
