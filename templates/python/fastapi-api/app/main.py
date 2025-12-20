from fastapi import FastAPI

app = FastAPI(title="__APP_NAME__")


@app.get("/")
def root():
    return {"name": "__APP_NAME__", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
