from pydantic import BaseModel, Field

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1)

class SummarizeResponse(BaseModel):
    summary: str

class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1)

class TranslateResponse(BaseModel):
    translated: str

class EmailRequest(BaseModel):
    text: str = Field(..., min_length=1)

class EmailResponse(BaseModel):
    email: str
