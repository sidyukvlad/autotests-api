from clients.errors_schema import ValidationErrorSchema
from tools.assertions.base import assert_equal

def assert_validation_error_schema(actual:ValidationErrorSchema, expected:ValidationErrorSchema):
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")