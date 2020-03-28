from typing import Dict

import uvicorn
from fastapi import FastAPI

from compare import compare

app = FastAPI(
    title="MC DMG Doge",
    description="Damage and stats calculator for Monumenta and MineCraft",
    version="0.1.0",
)


@app.get("/hi")
def read_root() -> Dict:
    return {"status": "Hello!"}


@app.post("/compare")
def compare() -> Dict:
    # gather post body and create args
    return compare({})


if __name__ == "__main__":
    print(" Starting mc_dmg_doge Server .... \n Please Wait until Server has fully set up")
    uvicorn.run(
        "mc_dmg_doge:app", host="0.0.0.0", port=8000, log_level="info", reload=False
    )
