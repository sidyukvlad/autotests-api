from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExercisesRequestDict(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseRequestDict(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


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
    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        return self.get("/api/v1/exercises/")
    def get_exercise_api(self, query: GetExerciseRequestDict) -> Response:
        return self.get("/api/v1/exercise/", query)
    def create_exercise_api(self, query: CreateExerciseRequestDict) -> Response:
        pass
    def update_exercise_api(self, exercise_id: str, query: UpdateExerciseRequestDict) -> Response:
        pass
    def delete_exercise_api(self, exercise_id:str) -> Response:
        pass