from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber 


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50,  description="First name")
    last_name:  str = Field(max_length=50,  description="Last name")
    email:      EmailStr 
    # phone:      PhoneNumber = Field(min_length=10, max_length = 15, phone_format=)
    phone:      str = Field(min_length=10, max_length = 15)
    birthday:   date
    notes:      Optional[str] = Field(default=None, description="Contact notes")



class ContactResponse(ContactModel):
    id:         int
    first_name: str
    last_name:  str
    email:      str
    phone:      str
    birthday:   date 
    notes:      str

    class Config:
        from_attributes = True
