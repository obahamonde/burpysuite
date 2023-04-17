from server import create_app
from fastapi.staticfiles import StaticFiles

app = create_app()

static = StaticFiles(directory="static", html=True)

app.mount("/", static, name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)