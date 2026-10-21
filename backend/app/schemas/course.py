from pydantic import BaseModel, ConfigDict



class CourseCreateRequest(BaseModel):
    """课程创建模型"""

    name: str
    code: str
    description: str | None = None
    status: int = 1


class CourseUpdateRequest(BaseModel):
    """课程更新模型(可选)"""

    name: str | None = None
    code: str | None = None
    description: str | None = None
    status: int | None = None


class CourseResponse(BaseModel):
    """课程返回数据模型"""

    id: int
    name: str
    code: str
    description: str | None = None
    status: int

    model_config = ConfigDict(from_attributes=True)  # 允许从ORM对象中读取数据
