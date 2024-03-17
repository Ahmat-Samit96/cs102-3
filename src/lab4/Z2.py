class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class AgeGroup:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def format_output(self):
        if self.respondents:
            sorted_respondents = sorted(self.respondents, key=lambda r: (-r.age, r.name))
            respondents_str = ', '.join(str(respondent) for respondent in sorted_respondents)
            return f"{self.start}-{self.end}: {respondents_str}"

        return None


class SurveyModule:
    def __init__(self, age_ranges):
        self.age_groups = self.initialize_age_groups(age_ranges)

    def initialize_age_groups(self, age_ranges):
        age_groups = []
        for i in range(len(age_ranges) - 1):
            age_groups.append(AgeGroup(age_ranges[i], age_ranges[i + 1] - 1))
        age_groups.append(AgeGroup(age_ranges[-1], float('inf')))
        return age_groups

    def process_respondents(self):
        respondents = []
        while True:
            input_str = input("Введите данные респондента в формате '<ФИО>,<возраст>' (или 'END' для завершения): ")
            if input_str == 'END':
                break

            name, age_str = map(str.strip, input_str.split(','))
            age = int(age_str)
            respondents.append(Respondent(name, age))

        respondents.sort(key=lambda r: (r.age, r.name))

        for respondent in respondents:
            self.assign_respondent_to_group(respondent)

    def assign_respondent_to_group(self, respondent):
        for age_group in self.age_groups:
            if age_group.start <= respondent.age <= age_group.end:
                age_group.add_respondent(respondent)
                break

    def print_results(self):
        for age_group in reversed(self.age_groups):
            formatted_output = age_group.format_output()
            if formatted_output:
                print(formatted_output)


if __name__ == "__main__":
    AGE_RANGES = [18, 25, 35, 45, 60, 80, 100]

    survey_module = SurveyModule(AGE_RANGES)
    survey_module.process_respondents()
    survey_module.print_results()
