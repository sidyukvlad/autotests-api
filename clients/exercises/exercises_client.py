from clients.api_client import APIClient
from httpx import Response
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExerciseResponseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
    GetExercisesResponseSchema,
)

from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения заданий

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, query: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания

        :param query: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/exercises",
            query.model_dump(by_alias=True)
        )

    def update_exercise_api(
        self, exercise_id: str, query: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод обновления задания

        :param query: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/exercises/{exercise_id}",
            query.model_dump(by_alias=True)
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения задания в формате json.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде GetExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self, request: GetExercisesQuerySchema
    ) -> GetExercisesResponseSchema:
        """
        Метод получения заданий в формате json.

        :param request: Словарь формата GetExercisesQueryDict.
        :return: Ответ от сервера в виде GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query=request)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        """
        Метод создания задания.

        :param request: Словарь формата CreateExerciseRequestDict.
        :return: Ответ от сервера в виде CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь формата UpdateExerciseRequestDict.
        :return: Ответ от сервера в виде UpdateExerciseResponseDict.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, query=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
