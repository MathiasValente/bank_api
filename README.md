# 🏦 Bank API — FastAPI, SQLAlchemy & PostgreSQL

A banking API built with **Python**, using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, designed with clean architecture principles, scalability, and best practices for modern back-end development.

This project simulates essential banking operations such as account creation, transactions, statements, and balance management, following a layered architecture (routers, services, models, schemas).

## 🚀 Technologies Used

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**
- **Uvicorn**
- **Git** (version control)
- **Poetry** (dependency management)

## 📁 Project Structure
```code
src/  
 ├── core/              # Security, settings, JWT, etc.  
 ├── dependencies/      # Database and authentication dependencies  
 ├── models/            # SQLAlchemy models  
 ├── routers/           # API routes  
 ├── schemas/           # Pydantic schemas  
 ├── services/          # Business logic  
 └── main.py            # Application entry point  
 ```

This architecture separates responsibilities and improves maintainability, scalability, and testability.

## 🧩 Features

### 🔐 Authentication
- JWT-based login  
- Protected routes  
- User dependency injection  

### 🧾 Accounts
- Create bank accounts  
- Retrieve user accounts  
- Generate full account statements  

### 💸 Transactions
- Deposit  
- Withdraw  
- Transfer between accounts  
- Transaction history ordered by timestamp  

### 📊 Statement
- List of transactions  
- Updated balance  
- Account details  
- Sorted by date    

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MathiasValente/bank_api
cd bank_api
```

### 2. Install dependencies using Poetry

```bash
poetry install
```

### 3. Activate the virtual environment

```bash
poetry shell
```

### 4. Configure the database  
Create a PostgreSQL database and update the connection URL in your environment variables or settings file.

#### 🔧 Environment Variables

Create a `.env` file in the project root based on the example below:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/bank_api
JWT_SECRET_KEY=your_secret_key_here
JWT_ALGORITHM=HS256
```

### 5. Run the application
```bash
uvicorn src.main:app --reload
```

### 6. Access the interactive documentation
Swagger UI:
```code
http://localhost:8000/docs
```  
ReDoc:
```code
http://localhost:8000/redoc
```

---

## 📌 Roadmap

- [ ] Add database migrations with Alembic
- [ ] Create automated tests
- [ ] Expand unit and integration test coverage
- [ ] Implement transaction limits
- [ ] Add pagination to statements
- [ ] Create Dockerfile and docker-compose setup  

## 🤝 Contributing

Suggestions, improvements, and feedback are always welcome.  
Feel free to open issues or submit pull requests.

## 📬 Contact

**Mathias Valente**  
LinkedIn: https://www.linkedin.com/in/MathiasValente  
Email: m.mvalente@outlook.com