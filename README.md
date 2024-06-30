# SQLAlchemy Mapped Stubs

This package provides type stubs for SQLAlchemy v2 "mapped" types, especially `Mapped` and `DynamicMapped` types, which IDEs and type checkers may not be able to infer correctly.

## Version

This stubs package version is 2.0.31.1, corresponding to SQLAlchemy version 2.0.31.

## Installation

You can install this package using pip:

```python
pip install sqlalchemy-mapped-stubs
```

## Usage

After installation, your type checker should automatically use these stubs when checking code that imports SQLAlchemy. No changes to your code are necessary.

This package provides type information for SQLAlchemy constructs, including:

- `DynamicMapped`: A type alias that provides correct typing for both class and instance contexts.
- Related types from `sqlalchemy.orm` such as `AppenderQuery` and `InstrumentedAttribute`.
- `Mapped`: A type alias that provides correct typing for both class and instance contexts.

## Example

```python
from sqlalchemy.orm import DynamicMapped, Mapped

class MyModel:
    items: Mapped[str]  # This will have incorrect type hints

class MyOtherModel:
    items: DynamicMapped[MyModel]  # This will now have correct type hints
    
# When Mapped is accessed on the class, it's an InstrumentedAttribute
print(type(MyModel.items))  # <class 'sqlalchemy.orm.attributes.InstrumentedAttribute'>

# When Mapped is accessed on an instance, it's a str
instance = MyModel()
print(type(instance.items))  # <class 'str'>


# When DynamicMapped is accessed on the class, it's an InstrumentedAttribute
print(type(MyOtherModel.items))  # <class 'sqlalchemy.orm.attributes.InstrumentedAttribute'>

# When DynamicMapped is accessed on an instance, it's an AppenderQuery
instance = MyOtherModel()
print(type(instance.items))  # <class 'sqlalchemy.orm.dynamic.AppenderQuery'>
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Disclaimer

This is an unofficial stubs package and is not affiliated with or endorsed by the SQLAlchemy project.