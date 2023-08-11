from starlette.applications import Starlette
from starlette.routing import Route
import endpoints


app = Starlette(
    debug=True,
    routes=[ Route("/take-screenshot", endpoint=endpoints.take_screenshot, methods=["GET"]), ]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4323)
