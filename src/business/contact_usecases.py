"""
Usecases - Regras de negócio da aplicação
Camada de negócio
"""

import uuid
from typing import List
from src.entities.contact import Contact
from src.infrastructure.repository import ContactRepository


class ContactUseCases:
    """Orquestra as operações de negócio com contatos"""

    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def create_contact(self, name: str, phone: str, email: str) -> Contact:
        """Cria e salva um novo contato"""
        contact = Contact(
            id=str(uuid.uuid4()),
            name=name,
            phone=phone,
            email=email,
        )
        self.repository.add(contact)
        return contact

    def list_all_contacts(self) -> List[Contact]:
        """Lista todos os contatos"""
        return self.repository.get_all()

    def list_favorite_contacts(self) -> List[Contact]:
        """Lista apenas contatos favoritos"""
        all_contacts = self.repository.get_all()
        return [c for c in all_contacts if c.is_favorite]

    def mark_as_favorite(self, contact_id: str) -> None:
        """Marca um contato como favorito"""
        contact = self.repository.get_by_id(contact_id)
        if contact:
            contact.is_favorite = not contact.is_favorite
            self.repository.update(contact)

    def update_contact(self, contact_id: str, name: str = None, phone: str = None, email: str = None) -> None:
        """Atualiza dados de um contato"""
        contact = self.repository.get_by_id(contact_id)
        if contact:
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.repository.update(contact)

    def delete_contact(self, contact_id: str) -> None:
        """Deleta um contato"""
        self.repository.delete(contact_id)
