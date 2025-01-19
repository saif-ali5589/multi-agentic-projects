from pydantic import BaseModel, Field

class Questions(BaseModel):
    question: str = Field(..., pattern="^[a-zA-Z0-9 ]+$")
    type:str

class Answers(BaseModel):
    answer: str
    type: str

