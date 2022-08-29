"""Setup the model schemas."""
from typing import List

from pydantic import BaseModel


class URLBase(BaseModel):
    """Define URLBase class."""

    target_url: str

    class Config:
        """Set config for this class."""

        orm_mode = True


class URL(URLBase):
    """Define URL class."""

    is_active: bool
    clicks: int


class URLListItem(URLBase):
    """A single URL item, with extra 'url' field."""

    url: str


class URLList(BaseModel):
    """List of URLs."""

    urls: List[URLListItem]


class URLInfo(URL):
    """Define URLInfo class."""

    url: str
    admin_url: str
