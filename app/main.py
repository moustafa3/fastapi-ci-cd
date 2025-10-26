from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class SumRequest(BaseModel):
    # version pydantic v1 : utilise min_items via typing.List + Field
    numbers: list[float]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sum")
def sum_numbers(payload: SumRequest):
    if not payload.numbers:
        raise HTTPException(status_code=422, detail="numbers list cannot be empty")
    try:
        total = float(sum(payload.numbers))
        return {"sum": total}
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid input") from exc
