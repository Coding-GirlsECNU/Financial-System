import json

from fastapi import FastAPI,status
from fastapi.responses import RedirectResponse,JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from pydantic import BaseModel

from db_utils import get_model_url

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TrainRequest(BaseModel):
    model_name: str
    config: Dict | None
    dataset: Dict | None
    mapping: List | None


@app.post("/train")
def train_model(request: TrainRequest):
    model = request.model_name
    url = get_model_url(model)
    cnf = json.dumps(request.dict())

    response = RedirectResponse(url=f"{url}?cnf={cnf}", status_code=status.HTTP_303_SEE_OTHER)
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8001)
