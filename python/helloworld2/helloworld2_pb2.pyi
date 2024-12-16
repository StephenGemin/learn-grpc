from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Recipe(_message.Message):
    __slots__ = ("name", "ingredients", "meal_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    MEAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    ingredients: str
    meal_type: str
    def __init__(self, name: _Optional[str] = ..., ingredients: _Optional[str] = ..., meal_type: _Optional[str] = ...) -> None: ...

class TimeStampReply(_message.Message):
    __slots__ = ("current_time",)
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    current_time: str
    def __init__(self, current_time: _Optional[str] = ...) -> None: ...

class TimeRequest(_message.Message):
    __slots__ = ("timezone",)
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    def __init__(self, timezone: _Optional[str] = ...) -> None: ...
