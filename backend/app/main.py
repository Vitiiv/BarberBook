from fastapi  import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"TESTANDO TESTANDO TESTANDO API API API API"}