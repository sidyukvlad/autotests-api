from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetExercisesQueryDict(TypedDict):
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения заданий

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercise/{exercise_id}")

    def create_exercise_api(self, query: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания

        :param query: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises/", query)

    def update_exercise_api(
        self, exercise_id: str, query: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод обновления задания

        :param query: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/exercises/{exercise_id}", query)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/exercises/{exercise_id}")
