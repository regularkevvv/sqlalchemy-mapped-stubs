from typing import Any, TypeAlias, TypeVar, overload

from sqlalchemy.orm import AppenderQuery, InstrumentedAttribute

T = TypeVar("T")


class DynamicMappedClass(InstrumentedAttribute[T]):
    """Class to allow DynamicMapped to have a different type when is class or instance."""

    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[T]: ...

    @overload
    def __get__(self, instance: object, owner: Any) -> AppenderQuery[T]: ...

    def __get__(
        self, instance: object | None, owner: Any
    ) -> InstrumentedAttribute[T] | AppenderQuery[T]: ...


DynamicMapped: TypeAlias = DynamicMappedClass[T] | Any


class MappedClass(InstrumentedAttribute[T]):
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[T]: ...

    @overload
    def __get__(self, instance: object, owner: Any) -> T: ...

    def __get__(
        self, instance: object | None, owner: Any
    ) -> InstrumentedAttribute[T] | T: ...


Mapped: TypeAlias = MappedClass[T] | Any
