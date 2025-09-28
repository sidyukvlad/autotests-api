from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
      "name": { "type": "string" },
      "age": { "type": "number" }
    },
    "required": ["name"]
}

data = {
  "name": "A",
  # "age": 30
}

validate(instance=data, schema=schema)

schema = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "minLength":"5",
            "maxLength":"15"
        },
    "required": ["username"]
    }
}