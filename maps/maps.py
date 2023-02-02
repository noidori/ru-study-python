from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        rating_list = []
        for key in list_of_movies:
            if "," in key["country"] and key["rating_kinopoisk"] not in ("", "0"):
                rating_list.append(key.get("rating_kinopoisk"))
                rating_list = list(map(float, rating_list))
        return sum(rating_list) / len(rating_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def count_char(key: dict) -> int:
            if key["rating_kinopoisk"] not in "" and float(key["rating_kinopoisk"]) >= rating:
                return str(key["name"]).count("и")

            return 0

        result = sum(map(count_char, list_of_movies))

        return result
