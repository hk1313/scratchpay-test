"""
from pydantic import BaseModel, Field

## Models
class UserList(BaseModel):
    id        : str
    username  : str
  
class UserEntry(BaseModel):
    username  : str = Field(..., example="potinejj")

class UserUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="Potine")
    last_name : str = Field(..., example="Sambo")
    gender    : str = Field(..., example="M")
    status    : str = Field(..., example="1")
class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")
"""