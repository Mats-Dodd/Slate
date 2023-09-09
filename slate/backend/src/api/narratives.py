from fastapi import FastAPI, HTTPException
from slate.backend.src.models.models import PrimaryUserNarrative, DescendantNarrative

app = FastAPI()

# In-memory storage
users_narratives = {}
descendants_narratives = {}


@app.post("/narrative/user/")
def submit_user_narrative(narrative: PrimaryUserNarrative):
    if narrative.user_id in users_narratives:
        raise HTTPException(status_code=400, detail="User narrative already exists")
    users_narratives[narrative.user_id] = narrative.narrative
    return {"message": "Narrative submitted successfully"}


@app.post("/narrative/descendant/")
def submit_descendant_narrative(narrative: DescendantNarrative):
    if narrative.user_id not in users_narratives:
        raise HTTPException(status_code=400, detail="Primary user does not exist")
    if narrative.user_id not in descendants_narratives:
        descendants_narratives[narrative.user_id] = []
    descendants_narratives[narrative.user_id].append({
        "descendant_name": narrative.descendant_name,
        "narrative": narrative.narrative
    })
    return {"message": "Descendant narrative submitted successfully"}


@app.get("/narrative/{user_id}/")
def get_narratives(user_id: str):
    user_narrative = users_narratives.get(user_id)
    if not user_narrative:
        raise HTTPException(status_code=404, detail="User not found")
    user_descendants = descendants_narratives.get(user_id, [])
    return {
        "user_narrative": user_narrative,
        "descendant_narratives": user_descendants
    }
