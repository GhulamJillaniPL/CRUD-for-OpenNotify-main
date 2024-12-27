from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ISSLocation(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime
    message: str

class Astronaut(BaseModel):
    name: str
    craft: str

class AstronautData(BaseModel):
    message: str
    number: int
    people: List[Astronaut]