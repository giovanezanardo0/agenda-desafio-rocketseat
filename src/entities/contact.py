"""
Entidade Contact - Modelo de dado da aplicação
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Contact:
    """Modelo de um contato na agenda"""
    id: str
    name: str
    phone: str
    email: str
    is_favorite: bool = False
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self):
        favorite_icon = "⭐" if self.is_favorite else ""
        return f"{favorite_icon} {self.name} - {self.phone} ({self.email})"
