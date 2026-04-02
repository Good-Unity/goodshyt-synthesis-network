from fastapi import FastAPI
from .models import NetworkSnapshot, SubsystemState
from .service import SynthesisService

app = FastAPI(title="GoodShyt Synthesis Network", version="0.1.0")
service = SynthesisService()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "goodshyt-synthesis-network"}

@app.post("/gmi")
def gmi(state: SubsystemState) -> dict[str, float]:
    return {"gmi": service.compute_gmi(state)}

@app.post("/summarize")
def summarize(snapshot: NetworkSnapshot) -> dict[str, object]:
    return service.summarize(snapshot).model_dump()
