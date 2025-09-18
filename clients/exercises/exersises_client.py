from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetExercisesRequestDict(TypedDict):
    id: str


class GetExerciseRequestDict(TypedDict):
    id: str


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения заданий

        :param query: Словарь с
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/")

    def get_exercise_api(self, exercise_id: str, query: GetExerciseRequestDict) -> Response:
        """
        Метод получения задания

        :param query: Словарь
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercise/{exercise_id}", query)

    def create_exercise_api(self, query: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания

        :param query: Словарь с
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises/", query)

    def update_exercise_api(self, exercise_id: str, query: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания

        :param query: Словарь
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/exercises/{exercise_id}", query)

    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод удаления курса.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/exercises/{exercise_id}")