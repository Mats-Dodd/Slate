
from pydantic import BaseModel, constr


class PrimaryUserNarrative(BaseModel):
    user_id: str  # Unique identifier
    narrative: constr(max_length=1000)


class DescendantNarrative(BaseModel):
    user_id: str  # The primary user's ID to which this narrative relates
    descendant_name: str
    narrative: constr(max_length=200)

    