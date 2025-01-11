from fastapi import FastAPI
from models import User, Expense
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

test_user = User("Test User", "abc123")

@app.get("/expenses")
def get_expenses():
    return test_user.get_expenses()

@app.post("/expense")
def add_expense(expense : Expense):
    test_user.add_expense(expense)
    return {"message": "Expense added successfully!"}
