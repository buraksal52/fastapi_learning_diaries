# First FastAPI Application

On the second day, we build our first FastAPI application.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Let's examine the code step by step:

1. **`from fastapi import FastAPI`**

   * Imports the `FastAPI` class from the `fastapi` package.

2. **`app = FastAPI()`**

   * Creates an instance of the `FastAPI` class.
   * This instance represents our web application and is used to register routes, handle requests, and configure the API.

3. **`@app.get("/")`**

   * @ is a **decorator**.
   * It tells FastAPI that the function below should handle **GET requests** sent to the root path (`"/"`).
   * When a client sends a GET request to the root URL, FastAPI executes the associated function.

4. **`async def root():`**

   * Defines an **asynchronous** function named `root`.
   * Asynchronous functions allow FastAPI to handle multiple requests efficiently without blocking the server.

5. **`return {"message": "Hello World"}`**

   * Returns a Python dictionary.
   * FastAPI automatically converts this dictionary into a JSON response and sends it back to the client.
