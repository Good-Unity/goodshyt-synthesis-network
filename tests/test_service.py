from goodshyt_synthesis_network.models import NetworkSnapshot, SubsystemState
from goodshyt_synthesis_network.service import SynthesisService


def test_gmi_is_bounded() -> None:
    service = SynthesisService()
    state = SubsystemState(name="core", ecti=0.95, csm=0.9, stl_penalty=0.1, kaq=0.85)
    value = service.compute_gmi(state)
    assert 0.0 <= value <= 1.0


def test_drift_summary_is_generated() -> None:
    service = SynthesisService()
    snapshot = NetworkSnapshot(subsystems=[SubsystemState(name="memory", ecti=0.72, csm=0.7, stl_penalty=0.35, kaq=0.6)])
    result = service.summarize(snapshot)
    assert result.drift
