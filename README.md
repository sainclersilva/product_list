### Documentation and strategic vision ###

# 1. Product API

This is a REST API built with Python/FastAPI, allowing the management and querying of 
products with detailed specifications.  
The API supports querying a single product, multiple products by IDs, 
and limiting the number of returned results.  
Authentication is done using an API key (hash).

---

# 2. Features

- Product listing with specifications (CPU, RAM, Storage, GPU, etc.)
- Query by product ID
- Query multiple products by ID
- Limit the number of returned items
- API key authentication (environment variable)
- Swagger UI auto-documentation

---

# 3. Libraries Used

- Python 3.12.10
- FastAPI → Framework for building REST APIs quickly and with automatic documentation.
- Uvicorn → ASGI server to run FastAPI applications with high performance.
- Pydantic → Provides data validation, serialization, and strict typing for models.
- Python-dotenv → Simplifies the management of environment variables from a .env file.

---

# 4. Project Diagram

product_comparator/
│
├── app/
│   ├── main.py             # API Main file
│   ├── models.py           # Data model (Pydantic)
│   ├── crud.py             # Functions to data read
│   └── data/
│       └── products.json   # Local Database - JSON
│
├── run.md                  # How to run the project
├── README.md               # Documentation and strategic vision
└── requirements.txt        # Project dependencies
|__ .env                    # API Key


# 5. Best Practices Applied

- Error handling: HTTP 404 when product not found or invalid JSON.
- Automatic documentation: FastAPI generates interactive docs in /docs and /redoc.
- Modular structure: Separation of models, CRUD logic, and the main API.
- Inline comments: Explain the function of each part of the code.
- Local JSON: Simulates a database without the need to install a real DB.


# 6. Using pagination and limit parameters in an API is a best practice for performance, 
#    scalability, and user experience:

  - Performance & Scalability:
  - Prevents the API from returning thousands of records at once, 
  - reducing server memory usage and response time.

# 6.1 User Experience:
- Frontend applications can render results gradually (paginated lists or infinite scroll), improving responsiveness and avoiding UI freezes.

# 6.2. Network Efficiency:
- Reduces payload size, bandwidth usage, and speeds up responses.

# 6.3 Security & Stability:
- Limits prevent accidental or malicious overloading of the server by requests for excessive data.


### Installation ###

 - To install, run the program and interact with the API, consult the run.md file
