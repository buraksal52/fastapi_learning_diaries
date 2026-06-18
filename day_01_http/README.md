# HTTP Fundamentals

## 1. What is HTTP?

HTTP (HyperText Transfer Protocol) is a protocol used to transfer resources between clients and servers. These resources can be HTML documents, JSON data, images, videos, audio files, and many other types of content.

HTTP follows a client-server architecture. A client (such as a web browser or a mobile application) sends a request, and the server processes that request and returns a response.

Between clients and servers, there may also be intermediary components called **proxies**. Proxies can provide various services, such as:

* Caching
* Security
* Authentication and authorization
* Load balancing
* Traffic filtering

By handling these tasks, proxies help improve performance, reliability, and scalability.

### Main Characteristics of HTTP

#### Simplicity

HTTP is designed to be simple and human-readable.

#### Extensibility

New features can be added through headers and extensions without changing the core protocol.

#### Statelessness

HTTP is stateless, meaning the server does not remember information about previous requests. Each request is processed independently.

#### Connection-Based Communication

HTTP relies on underlying transport protocols such as TCP. Before HTTP messages can be exchanged, a TCP connection must be established.

---

## 2. HTTP Messages

HTTP communication consists of two types of messages:

* Request Messages
* Response Messages

### Request Message Structure

```http
GET / HTTP/1.1
```

Components:

* **GET** → HTTP method
* **/** → Requested path
* **HTTP/1.1** → HTTP version

### Response Message Structure

```http
HTTP/1.1 200 OK
```

Components:

* **HTTP/1.1** → HTTP version
* **200** → Status code
* **OK** → Status message

---

## 3. HTTP Request Methods

HTTP provides many request methods, but the most commonly used ones are:

| Method | Purpose                         |
| ------ | ------------------------------- |
| GET    | Retrieve data                   |
| POST   | Create new data                 |
| PUT    | Replace or update existing data |
| PATCH  | Partially update existing data  |
| DELETE | Remove data                     |

---

## 4. HTTP Response Status Codes

HTTP status codes are grouped into five categories.

### 1xx — Informational Responses

| Code | Meaning             |
| ---- | ------------------- |
| 100  | Continue            |
| 101  | Switching Protocols |
| 102  | Processing          |
| 103  | Early Hints         |

### 2xx — Successful Responses

| Code | Meaning                       |
| ---- | ----------------------------- |
| 200  | OK                            |
| 201  | Created                       |
| 202  | Accepted                      |
| 203  | Non-Authoritative Information |
| 204  | No Content                    |
| 205  | Reset Content                 |
| 206  | Partial Content               |
| 207  | Multi-Status                  |
| 208  | Already Reported              |

### 3xx — Redirection Messages

Examples:

| Code | Meaning           |
| ---- | ----------------- |
| 301  | Moved Permanently |
| 302  | Found             |
| 304  | Not Modified      |

### 4xx — Client Error Responses

| Code | Meaning               |
| ---- | --------------------- |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 422  | Unprocessable Content |

### 5xx — Server Error Responses

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |

---

## Conclusion

Understanding HTTP fundamentals is essential before learning FastAPI. Since FastAPI is built on top of HTTP concepts, having a solid understanding of requests, responses, methods, and status codes will make the learning process much easier.
