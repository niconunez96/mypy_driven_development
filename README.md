# Mypy driven development 🐍

## Index

0. [MyPy Config](#mypy-config)
1. [Optional](#optional)
2. [Literals](./src/literals.py)
3. [Union](./src/union_type.py)
4. [Final](#final)
5. [Data Classes](./src/dataclasses.py)
6. [Typed Dicts](#typed-dicts)
7. [Exhaustive checking](./src/exhaustive_checking/__init__.py)
8. [Protocol vs ABC](./src/protocol_vs_abc.py)
9. [Pattern Matching](./src/pattern_matching.py)
10. [Generics](./src/generics/__init__.py)

## What and Why

Python has started to add type annotation. Buuut type annotations are not useful by itself, to have a full typing experience you need **mypy**.

Well mypy is a static type checker that you need to run "manually", so type annotations and mypy do nothing on runtime.

Mypy is another tool that needs to be installed as flake8, black, isort.

Before jumping to mypy details, Who hates Java ?

![Homer](./assets/homer.gif)

why do we need **static typing** on a **dynamic typing** language ?

1. Security
2. Explicit APIs
3. Feedback loop

![Feedback loop](./assets/feedbackLoop.png)

## Mypy Config

[Mypy playground](https://mypy-play.net/?mypy=latest&python=3.10)

### Basic config

`pip install mypy`
[MyPy Config file](./mypy.ini)
[Config guide](https://mypy.readthedocs.io/en/stable/config_file.html)

### Configuring specific packages with custom rules

If we have a legacy project that we want to implement mypy, we can do it
progressively without creating a full blown migration PR.
Or if we want a more relax mypy config in our tests we can do it using this technique.

```ini
[mypy-module_name.directory.file]
; Custom configs goes here
disallow_untyped_defs = False
check_untyped_defs = True
ignore_errors = True
```

### Working with 3rd party libraries

1. Check if the library is inside https://github.com/python/typeshed, if so install it.
2. Define the library inside the stub directory if it is strictly necessary or does not add an extra overhead.
3. Ignore missing imports and Cast the return types of the library if necessary

We can bypass this error by doing

```
Skipping analyzing "celery": module is installed, but missing library stubs or py.typed marker  [import]mypy
See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-importsmypy
```

1. Add the following setting in mypy.ini

```ini
[mypy-celery.*]
ignore_missing_imports = True
```

2. Add stub directory with the needed types

```ini
[mypy]
python_version = 3.10
mypy_path = ./stubs/
```

## Optional

[Optional](./src/optional.py)

## Literals

[Literals](./src/literals.py)

## Union

[Union](./src/union_type.py)

## Final

[Final](./src/final_type.py)

## Data Classes

[Data Classes](./src/dataclasses.py)

## Typed Dicts

[Typed Dicts](./src/typed_dicts.py)

## Exhaustive checking

[Exhaustive checking](./src/exhaustive_checking/__init__.py)

## Protocol vs ABC

[Protocol vs ABC](./src/protocol_vs_abc.py)

## Pattern Matching

[Pattern Matching](./src/pattern_matching.py)
[Info](https://peps.python.org/pep-0636/#abstract)

## Generics

[Generics](./src/generics/__init__.py)
