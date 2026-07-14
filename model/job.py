from dataclasses import dataclass
from typing import List

@dataclass
class Job:
    company : str
    title : str
    location : str
    experience : str
    salary : str
    source : str
    apply_link: str
    posted_date: str
    skills: List[str]
    score: int = 0
    applied: bool = False

    