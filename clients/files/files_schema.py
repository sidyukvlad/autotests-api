from pydantic import BaseModel, HttpUrl

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


# Добавили описание структуры запроса на создание файла
class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema

model = CreateFileRequestSchema(
    filename="file.txt",
    directory="test",
    upload_file="path/to/my/file.txt",
)

print(model.model_dump(exclude={"upload_file"}))