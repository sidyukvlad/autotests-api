import pytest
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture
from pydantic import BaseModel
from fixtures.courses import CourseFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentification_user)


@pytest.fixture
def function_exercise(
    function_user: UserFixture,
    function_course: CourseFixture
) -> ExerciseFixture:
    
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)

    return ExerciseFixture(request=request, response=response)
