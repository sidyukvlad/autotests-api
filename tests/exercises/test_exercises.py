import pytest
from fixtures.users import UserFixture
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema,  UpdateExerciseResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, assert_update_exercise_response
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus

pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self, 
        function_user: UserFixture,
        function_course: CourseFixture,
        exercises_client: ExercisesClient
    ):
        request = CreateExerciseRequestSchema(
            course_id = function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
    
    def test_get_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture
    ):
        create_exercise_response = function_exercise.response
        get_exercise_response = exercises_client.get_exercise_api(create_exercise_response.exercise.id)
        get_exercise_respons_data = GetExerciseResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_exercise_respons_data.exercise, create_exercise_response.exercise)

        validate_json_schema(get_exercise_response.json(), get_exercise_respons_data.model_json_schema())

    def test_update_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            function_exercise.response.exercise.id,
            request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

        


        
        
