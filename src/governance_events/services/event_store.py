from typing import List

from src.governance_events.models.governance_event import GovernanceEvent


class EventStore:

    events: List[GovernanceEvent] = []

    @classmethod
    def add_event(cls, event: GovernanceEvent):
        cls.events.append(event)

    @classmethod
    def get_events(cls):
        return cls.events
