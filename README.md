# FastAPI Backend — Products REST API

A simple REST API built with **FastAPI** and **Python** to manage a list of products.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **FastAPI** | Web framework |
| **Pydantic** | Data validation via `BaseModel` |
| **Uvicorn** | ASGI server to run the app |
| **CORS Middleware** | Allow requests from React frontend |

---

## 📁 Project Structure

```
fast-api-backend/
├── main.py       # All API routes & app setup
├── model.py      # Product data model
└── README.md
```

---

## 📦 Product Model

```python
class Product(BaseModel):
    id: int
    name: str
    age: int
```

---

## 🚀 Installation & Setup

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn
```

### 3. Run the server
```bash
uvicorn main:app --reload
```

The server will start at: **`http://127.0.0.1:8000`**

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main page |
| `GET` | `/products` | Get all products |
| `GET` | `/products/{id}` | Get product by ID |
| `POST` | `/products` | Add a new product |
| `PUT` | `/products/{id}` | Update a product |
| `DELETE` | `/products/{id}` | Delete a product |

---

## 🧪 Testing the API

Visit **Swagger UI** at:
```
http://127.0.0.1:8000/docs
```

Or **ReDoc** at:
```
http://127.0.0.1:8000/redoc
```

---

## 🔗 Frontend

This backend is connected to a **React + Vite** frontend running at `http://localhost:5173`.  
CORS is configured to allow requests from that origin.
