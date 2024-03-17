import unittest
from io import StringIO
from unittest.mock import patch
from Z2 import SurveyModule


class TestSurveyModule(unittest.TestCase):
    def test_survey_module(self):
        age_ranges = [18, 25, 35, 45, 60, 80, 100]
        input_data = [
            "Иванов Иван Иванович,22",
            "Петров Петр Петрович,30",
            "Сидоров Сидор Сидорович,40",
            "END"
        ]

        with patch("builtins.input", side_effect=input_data):
            survey_module = SurveyModule(age_ranges)
            survey_module.process_respondents()

        expected_output = ("35-44: Сергеев Сергей Сергеевич (40)\n25-34: Николаев Николай Николаевич (30)\n18-24: Иванов "
                           "Иван Иванович (22)\n")

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            survey_module.print_results()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
