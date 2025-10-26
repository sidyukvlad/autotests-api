import pytest
from fixtures.users import UserFixture
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema,  UpdateExerciseResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, assert_get_exercises_response, assert_update_exercise_response, assert_exercise_not_found_response
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus
import allure
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.suite(AllureFeature.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
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
    
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)  # Добавили story
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
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

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)  # Добавили story
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
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

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)  # Добавили story
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        delete_response = exercises_client.delete_exercise_api(
            exercise_id
        )
        assert_status_code(delete_response.status_code, HTTPStatus.OK)
        
        get_response = exercises_client.get_exercise_api(exercise_id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

        assert_exercise_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())
    
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)  # Добавили story
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercises(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
        function_course: CourseFixture
    ):
        query = GetExercisesQuerySchema(course_id = function_course.response.course.id)
        create_exercise_response = function_exercise.response
  
        get_exercises_response = exercises_client.get_exercises_api(query)
        get_exercises_response_data = GetExercisesResponseSchema.model_validate_json(get_exercises_response.text)

        assert_get_exercises_response(get_exercises_response_data, [create_exercise_response])
        validate_json_schema(get_exercises_response.json(), get_exercises_response_data.model_json_schema())


        

        


        
        
