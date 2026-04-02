from pydantic import BaseModel, Field

class SubsystemState(BaseModel):
    name: str = Field(min_length=1)
    ecti: float = Field(ge=0.0, le=1.0)
    csm: float = Field(ge=0.0, le=1.0)
    stl_penalty: float = Field(ge=0.0, le=1.0)
    kaq: float = Field(ge=0.0, le=1.0)

class NetworkSnapshot(BaseModel):
    subsystems: list[SubsystemState]

class NetworkSummary(BaseModel):
    subsystem_count: int
    average_gmi: float
    drift: list[str]
    summary: str
