import uvicorn


def run():
    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=35000,
        reload=True,
    )
