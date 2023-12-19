from dataclasses import dataclass


@dataclass(frozen=True)
class Brand:
    title: str
    href: str
