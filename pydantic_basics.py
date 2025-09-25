arr = {
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}

from pydantic import BaseModel,Field
# from pydantic.alias_generators import to_camel

class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

course_default_model = CourseSchema(
    id = "course-id",
    title = "course-title",
    maxScore = 100,
    minScore = 10,
    description = "course-description",
    estimatedTime = "1 week"
)

print("course_default_model:", course_default_model)

course_dict = {
    "id": "course-id",
    "title": "course-title",
    "maxScore": 100,
    "minScore": 10,
    "description": "course-description",
    "estimatedTime": "1 week"
}

course_dict_model = CourseSchema(**course_dict)

print("course_dict_model:", course_dict_model)

course_json = """
{
    "id": "course-id",
    "title": "course-title",
    "maxScore": 100000,
    "minScore": 10,
    "description": "course-description",
    "estimatedTime": "1 week"
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("course_json_model:", course_json_model)
print(course_json_model.model_dump())
print(course_json_model.model_dump_json(by_alias=True))