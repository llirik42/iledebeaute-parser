from dataclasses import dataclass


@dataclass(frozen=True)
class Offer:
    cost: int
