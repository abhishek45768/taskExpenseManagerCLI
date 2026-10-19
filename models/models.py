import dataclasses

@dataclasses.dataclass
class Expenses:
    id: int
    title: str
    amount: float
    category: str
    date: str   