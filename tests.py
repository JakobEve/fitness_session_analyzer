#Nothing in the requirements about testing but adding this would hurt my submission
import unittest
from main import Observation, Session, SessionAnalyzer
from data_generator import generate_fitness_data


class TestFitnessAnalyser(unittest.TestCase):
    #Short test to check if a session is correcly classified as resting
    def test_resting_classification(self):
        profile, raw_observations=generate_fitness_data(scenario="resting",seed=1)
        session=Session.from_raw_data(profile,raw_observations)
        result=SessionAnalyzer(session).analyze()
        self.assertEqual(result["classification"],"resting")


if __name__ == "__main__":
    unittest.main()