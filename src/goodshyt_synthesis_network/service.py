from .models import NetworkSnapshot, NetworkSummary, SubsystemState

class SynthesisService:
    def compute_gmi(self, state: SubsystemState) -> float:
        return round((state.ecti * 0.30) + (state.csm * 0.30) + ((1 - state.stl_penalty) * 0.20) + (state.kaq * 0.20), 4)

    def summarize(self, snapshot: NetworkSnapshot) -> NetworkSummary:
        gmis = {state.name: self.compute_gmi(state) for state in snapshot.subsystems}
        avg = round(sum(gmis.values()) / len(gmis), 4) if gmis else 0.0
        drift: list[str] = []
        for state in snapshot.subsystems:
            if state.ecti < 0.8:
                drift.append(f"{state.name}: low ECTI")
            if state.csm < 0.75:
                drift.append(f"{state.name}: low CSM")
            if state.stl_penalty > 0.3:
                drift.append(f"{state.name}: high STL penalty")
            if state.kaq < 0.7:
                drift.append(f"{state.name}: low KAQ")
        summary = f"Network average GMI is {avg} across {len(snapshot.subsystems)} subsystem(s)."
        return NetworkSummary(subsystem_count=len(snapshot.subsystems), average_gmi=avg, drift=drift, summary=summary)
