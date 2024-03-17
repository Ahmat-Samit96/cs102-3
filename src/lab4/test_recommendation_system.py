import unittest
from io import StringIO
from unittest.mock import patch
from Z1 import RecommendationSystem


class TestRecommendationSystem(unittest.TestCase):
    def test_recommendation_system(self):
        movies_file_content = "1,Movie1\n2,Movie2\n3,Movie3\n4,Movie4"
        history_file_content = "2,1,3\n1,4,3\n2,2,2,2,2,3"

        with patch("builtins.open", side_effect=[StringIO(movies_file_content), StringIO(history_file_content)]):
            system = RecommendationSystem("movies.txt", "history.txt")

        user_input = "2,4"
        with patch("builtins.input", side_effect=[user_input]):
            recommendation = system.recommend_movie(list(map(int, user_input.split(','))))

        expected_output = "Movie3\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print(recommendation)
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
