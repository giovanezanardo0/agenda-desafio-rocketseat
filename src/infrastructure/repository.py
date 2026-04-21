"""
Repository para persistência de contactos
Camada de infraestrutura
"""

import json
import os
from typing import List, Optional
from datetime import datetime
from src.entities.contact import Contact


class ContactRepository:
    """Responsável pela persistência de dados dos contatos"""
    
    def __init__(self, filepath: str = "src/data/contacts.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Cria o arquivo se não existir"""
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)

    def add(self, contact: Contact) -> None:
        """Adiciona um novo contato"""
        contacts = self._load()
        contacts.append(self._contact_to_dict(contact))
        self._save(contacts)

    def get_all(self) -> List[Contact]:
        """Retorna todos os contatos"""
        contacts_data = self._load()
        return [self._dict_to_contact(c) for c in contacts_data]

    def get_by_id(self, contact_id: str) -> Optional[Contact]:
        """Busca um contato pelo ID"""
        contacts = self.get_all()
        return next((c for c in contacts if c.id == contact_id), None)

    def update(self, contact: Contact) -> None:
        """Atualiza um contato existente"""
        contacts = self._load()
        for i, c in enumerate(contacts):
            if c["id"] == contact.id:
                contacts[i] = self._contact_to_dict(contact)
                break
        self._save(contacts)

    def delete(self, contact_id: str) -> None:
        """Remove um contato"""
        contacts = self._load()
        contacts = [c for c in contacts if c["id"] != contact_id]
        self._save(contacts)

    def _load(self) -> list:
        """Carrega dados do arquivo"""
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _save(self, data: list) -> None:
        """Salva dados no arquivo"""
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2, default=str)

    @staticmethod
    def _contact_to_dict(contact: Contact) -> dict:
        created_at = contact.created_at
        if isinstance(created_at, datetime):
            created_at = created_at.isoformat()
        return {
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "is_favorite": contact.is_favorite,
            "created_at": created_at,
        }

    @staticmethod
    def _dict_to_contact(data: dict) -> Contact:
        """Converte dicionário em Contact"""
        created_at_str = data.get("created_at")
        created_at = None
        if created_at_str:
            try:
                created_at = datetime.fromisoformat(created_at_str)
            except (ValueError, TypeError):
                created_at = None
        
        return Contact(
            id=data["id"],
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            is_favorite=data.get("is_favorite", False),
            created_at=created_at,
        )
