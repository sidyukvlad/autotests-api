from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение заданий.
    """
    exercises: list[Exercise]


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
        return self.post("/api/v1/exercises", query)

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

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения задания в формате json.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде GetExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, request: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения заданий в формате json.

        :param request: Словарь формата GetExercisesQueryDict.
        :return: Ответ от сервера в виде GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query=request)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания задания.

        :param request: Словарь формата CreateExerciseRequestDict.
        :return: Ответ от сервера в виде CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь формата UpdateExerciseRequestDict.
        :return: Ответ от сервера в виде UpdateExerciseResponseDict.
        """
        response = self.update_exercise_api(
            exercise_id=exercise_id, query=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
