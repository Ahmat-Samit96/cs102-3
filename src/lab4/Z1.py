class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title

    def __str__(self):
        return self.title


class RecommendationSystem:
    def __init__(self, movies_file, history_file):
        self.movies = self.load_movies(movies_file)
        self.history = self.load_history(history_file)

    def load_movies(self, file_path):
        movies = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                movie_id, title = line.strip().split(',')
                movies.append(Movie(int(movie_id), title))
        return movies

    def load_history(self, file_path):
        history = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                viewed_movies = list(map(int, line.strip().split(',')))
                history.append(viewed_movies)
        return history

    def recommend_movie(self, user_history):
        candidate_users = self.filter_users(user_history)
        recommended_movies = self.get_recommended_movies(user_history, candidate_users)
        if recommended_movies:
            return recommended_movies[0]
        else:
            return "No recommendations available."

    def filter_users(self, user_history):
        candidate_users = []
        for idx, history in enumerate(self.history):
            common_movies = set(user_history) & set(history)
            if len(common_movies) >= len(user_history) / 2:
                candidate_users.append((idx, len(common_movies)))
        return sorted(candidate_users, key=lambda x: x[1], reverse=True)

    def get_recommended_movies(self, user_history, candidate_users):
        viewed_movies_set = set(user_history)
        recommendations = []

        for user_idx, common_movie_count in candidate_users:
            other_user_history = self.history[user_idx]
            other_user_unwatched_movies = list(set(other_user_history) - viewed_movies_set)

            if other_user_unwatched_movies:
                recommendations.extend(other_user_unwatched_movies)

        recommended_movies_count = {}
        for movie_id in recommendations:
            recommended_movies_count[movie_id] = recommended_movies_count.get(movie_id, 0) + 1

        sorted_recommendations = sorted(recommended_movies_count.items(), key=lambda x: x[1], reverse=True)

        recommended_movies = [movie_id for movie_id, count in sorted_recommendations]
        return [self.movies[movie_id - 1] for movie_id in recommended_movies]


if __name__ == "__main__":
    MOVIES_FILE = "movies.txt"  # Путь к файлу с фильмами
    HISTORY_FILE = "history.txt"  # Путь к файлу с историей просмотров

    system = RecommendationSystem(MOVIES_FILE, HISTORY_FILE)

    user_input = input("Введите идентификаторы просмотренных фильмов через запятую: ")
    user_history = list(map(int, user_input.split(',')))

    recommendation = system.recommend_movie(user_history)

    print("Рекомендация:")
    print(recommendation)
