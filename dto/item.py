from dataclasses import dataclass
from typing import Optional

from .offer import Offer


@dataclass(frozen=True)
class Item:
    title: str
    description: str
    image: Optional[str]
    offers: list[Offer]
