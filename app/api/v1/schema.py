from openai import BaseModel


class HealthOut(BaseModel):
    status: str
