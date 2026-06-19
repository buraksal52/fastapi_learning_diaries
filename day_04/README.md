# FastAPI Query Parameters

## Overview

Query parameters are values passed in the URL after the `?` symbol.

Example:

```text
/items/?skip=0&limit=10
```

In this URL:

* `skip` = 0
* `limit` = 10

Unlike path parameters, query parameters are not part of the URL path itself. They are commonly used for:

* Filtering data
* Pagination
* Searching
* Sorting

FastAPI automatically detects function parameters that are not part of the path and treats them as query parameters.

---

## Basic Query Parameters

```python
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Request:

```text
/items/?skip=5&limit=20
```

Response:

```json
{
    "skip": 5,
    "limit": 20
}
```

FastAPI automatically converts query parameter values to the specified Python types and validates them.

---

## Default Values

Query parameters can have default values.

```python
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    ...
```

If no values are provided:

```text
/items/
```

FastAPI uses:

```python
skip = 0
limit = 10
```

Default values make query parameters optional.

---

## Optional Query Parameters

A query parameter becomes optional when its default value is `None`.

```python
@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    q: str | None = None
):
    return {"item_id": item_id, "q": q}
```

Examples:

```text
/items/1
```

```text
/items/1?q=fastapi
```

If `q` is not provided, its value will be `None`.

---

## Type Conversion and Validation

FastAPI automatically converts query parameters to the declared type.

```python
@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    short: bool = False
):
    return {"short": short}
```

The following values are interpreted as `True`:

```text
?short=true
?short=True
?short=1
?short=yes
?short=on
```

Otherwise, FastAPI treats the value as `False`.

---

## Combining Path and Query Parameters

Path parameters and query parameters can be used together.

```python
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    ...
```

FastAPI automatically determines which parameters come from the path and which come from the query string.

Example:

```text
/users/10/items/book?q=python&short=true
```

Path Parameters:

* `user_id`
* `item_id`

Query Parameters:

* `q`
* `short`

---

## Required Query Parameters

A query parameter becomes required when no default value is provided.

```python
@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    needy: str
):
    return {"item_id": item_id, "needy": needy}
```

Valid request:

```text
/items/book?needy=value
```

Invalid request:

```text
/items/book
```

FastAPI returns a validation error because the required query parameter is missing.

---

## Mixing Required, Optional, and Default Parameters

```python
@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    needy: str,
    skip: int = 0,
    limit: int | None = None
):
    ...
```

In this example:

| Parameter | Type       | Required         |
| --------- | ---------- | ---------------- |
| needy     | str        | Yes              |
| skip      | int        | No (default = 0) |
| limit     | int | None | Optional         |

This allows you to build flexible API endpoints with different parameter requirements.

---

## Key Takeaways

* Query parameters appear after the `?` symbol in a URL.
* FastAPI automatically detects query parameters.
* Type hints provide automatic conversion and validation.
* Default values make query parameters optional.
* Parameters with `None` as the default value are optional.
* Parameters without a default value are required.
* Path parameters and query parameters can be used together.
* Boolean query parameters are automatically converted by FastAPI.
* Query parameters are commonly used for filtering, searching, and pagination.

Understanding query parameters is essential because they are widely used in real-world REST APIs for filtering and controlling responses.
