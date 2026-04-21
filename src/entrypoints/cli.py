"""
CLI - Interface de linha de comando
Camada de entrypoints
"""

from src.business.contact_usecases import ContactUseCases
from src.infrastructure.repository import ContactRepository


class AgendaCLI:
    """Interface de menu da agenda no terminal"""

    def __init__(self):
        self.repository = ContactRepository()
        self.usecases = ContactUseCases(self.repository)

    def run(self):
        """Executa o menu principal"""
        while True:
            self._show_menu()
            choice = input("\nEscolha uma opção: ").strip()

            if choice == "1":
                self._add_contact()
            elif choice == "2":
                self._list_contacts()
            elif choice == "3":
                self._list_favorites()
            elif choice == "4":
                self._mark_favorite()
            elif choice == "5":
                self._update_contact()
            elif choice == "6":
                self._delete_contact()
            elif choice == "7":
                print("Saindo... Até logo! 👋")
                break
            else:
                print("❌ Opção inválida!")

    def _show_menu(self):
        """Exibe o menu principal"""
        print("\n" + "="*40)
        print("📞 AGENDA DESAFIO ROCKETSEAT")
        print("="*40)
        print("1️⃣  Adicionar contato")
        print("2️⃣  Listar todos os contatos")
        print("3️⃣  Listar favoritos")
        print("4️⃣  Marcar/desmarcar favorito")
        print("5️⃣  Editar contato")
        print("6️⃣  Deletar contato")
        print("7️⃣  Sair")
        print("="*40)

    def _add_contact(self):
        """Adiciona um novo contato"""
        print("\n➕ ADICIONAR CONTATO")
        name = input("Nome: ").strip()
        phone = input("Telefone: ").strip()
        email = input("Email: ").strip()

        if name and phone and email:
            contact = self.usecases.create_contact(name, phone, email)
            print(f"✅ Contato '{contact.name}' adicionado com sucesso!")
        else:
            print("❌ Dados incompletos!")

    def _list_contacts(self):
        """Lista todos os contatos"""
        contacts = self.usecases.list_all_contacts()
        if not contacts:
            print("\n📭 Nenhum contato cadastrado.")
            return

        print("\n📋 TODOS OS CONTATOS:")
        for contact in contacts:
            print(f"  {contact}")

    def _list_favorites(self):
        """Lista apenas contatos favoritos"""
        contacts = self.usecases.list_favorite_contacts()
        if not contacts:
            print("\n📭 Nenhum contato favorito.")
            return

        print("\n⭐ CONTATOS FAVORITOS:")
        for contact in contacts:
            print(f"  {contact}")

    def _mark_favorite(self):
        """Marca/desmarca um contato como favorito"""
        contacts = self.usecases.list_all_contacts()
        if not contacts:
            print("\n📭 Nenhum contato cadastrado.")
            return

        print("\n⭐ SELECIONE UM CONTATO:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")

        try:
            choice = int(input("Escolha o número: "))
            if 1 <= choice <= len(contacts):
                contact = contacts[choice - 1]
                self.usecases.mark_as_favorite(contact.id)
                status = "adicionado aos" if not contact.is_favorite else "removido dos"
                print(f"✅ Contato {status} favoritos!")
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")

    def _update_contact(self):
        """Edita um contato existente"""
        contacts = self.usecases.list_all_contacts()
        if not contacts:
            print("\n📭 Nenhum contato cadastrado.")
            return

        print("\n✏️  SELECIONE UM CONTATO PARA EDITAR:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")

        try:
            choice = int(input("Escolha o número: "))
            if 1 <= choice <= len(contacts):
                contact = contacts[choice - 1]
                print("\n(Deixe em branco para manter o valor atual)")
                name = input(f"Novo nome [{contact.name}]: ").strip() or contact.name
                phone = input(f"Novo telefone [{contact.phone}]: ").strip() or contact.phone
                email = input(f"Novo email [{contact.email}]: ").strip() or contact.email

                self.usecases.update_contact(contact.id, name, phone, email)
                print("✅ Contato atualizado com sucesso!")
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")

    def _delete_contact(self):
        """Deleta um contato"""
        contacts = self.usecases.list_all_contacts()
        if not contacts:
            print("\n📭 Nenhum contato cadastrado.")
            return

        print("\n🗑️  SELECIONE UM CONTATO PARA DELETAR:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")

        try:
            choice = int(input("Escolha o número: "))
            if 1 <= choice <= len(contacts):
                contact = contacts[choice - 1]
                confirm = input(f"Tem certeza que deseja deletar '{contact.name}'? (s/n): ").strip().lower()
                if confirm == "s":
                    self.usecases.delete_contact(contact.id)
                    print("✅ Contato deletado com sucesso!")
                else:
                    print("❌ Operação cancelada!")
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")


def main_menu():
    """Função para iniciar a CLI"""
    cli = AgendaCLI()
    cli.run()
