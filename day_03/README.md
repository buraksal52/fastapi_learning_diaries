# FastAPI Path Parameters

## Overview

Path parameters allow you to capture values directly from the URL and use them inside your path operation functions.

Example:

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

When a request is sent to:

```text
/items/42
```

FastAPI automatically extracts `42`, converts it to an integer, validates it, and passes it to the function.

---

## Type Validation

FastAPI uses Python type hints to validate path parameters.

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

If a user provides a value that cannot be converted to an integer, FastAPI automatically returns a validation error.

### Benefits

* Automatic data validation
* Type conversion
* Better editor support
* Automatic API documentation

---

## Path Order Matters

Specific routes should always be declared before dynamic routes.

Correct:

```python
@app.get("/users/me")
async def read_current_user():
    return {"user": "current"}
    
    
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

Why?

If `/users/{user_id}` is declared first, the path `/users/me` would be interpreted as:

```text
user_id = "me"
```

instead of calling the intended endpoint.

---

## Restricting Values with Enum

Sometimes you want to allow only predefined values.

FastAPI supports Python Enums for this purpose.

```python
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
```

Then use the enum as the parameter type:

```python
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}
```

Valid URLs:

```text
/models/alexnet
/models/resnet
/models/lenet
```

Any other value will trigger a validation error.

---

## Working with Enum Members

### Comparing Enum Members

```python
if model_name is ModelName.alexnet:
    ...
```

### Accessing the Actual Value

```python
model_name.value
```

Output:

```text
alexnet
```

### Returning Enum Values

You can return enum members directly in a response:

```python
return {"model_name": model_name}
```

FastAPI automatically converts them to their string values:

```json
{
  "model_name": "alexnet"
}
```

---

## Path Parameters Containing Paths

Sometimes a parameter needs to contain an entire file path.

Example:

```text
/files/home/user/document.txt
```

Use the `path` converter:

```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

Now FastAPI will capture the entire path after `/files/`.

---

## Key Takeaways

* Path parameters extract values from URLs.
* Type hints provide automatic validation and conversion.
* Route declaration order is important.
* Enums can restrict parameters to predefined values.
* Enum members can be compared and returned directly.
* The `path` converter allows capturing full file paths.

These features make FastAPI endpoints safer, cleaner, and easier to document.
