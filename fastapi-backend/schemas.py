from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int]  # noqa: A003
    lastname: Optional[str]
    firstname: Optional[str]


class User(UserBase):
    email: Optional[str]
    password: Optional[str]
    street: Optional[str]
    house_number: Optional[int]
    zip_code: Optional[int]
    city: Optional[str]


class Content(BaseModel):
    book: Optional[bool]
    clothes: Optional[bool]
    toys: Optional[bool]
    electronics: Optional[bool]
    other: Optional[str]


class GiveboxBase(BaseModel):
    id: Optional[int]  # noqa: A003
    longitude: float
    latitude: float
    is_temporary: Optional[bool]
    title: Optional[str]
    opening_hours: Optional[str]
    extern_link: Optional[str]
    content: Optional[Content]
    street: Optional[str]
    house_number: Optional[int]
    zip_code: Optional[int]
    city: Optional[str]


class Givebox(GiveboxBase):
    maintenance_needed: Optional[bool]
    maintainer_info: Optional[str]
    description: Optional[str]
    last_confirmation_date: Optional[datetime]
    image_id: Optional[str]
    maintainers: List[User] = []


class Comment(BaseModel):
    user_id: Optional[int]
    user: Optional[User]
    box_id: Optional[int]
    box: Optional[Givebox]
    text: Optional[str]
    timestamp: Optional[datetime]


class Image(BaseModel):
    box_id: Optional[int]
    data: Optional[str]
    is_title_image: Optional[bool]
