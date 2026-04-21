"""
Arquivo principal - Entrada da aplicação
Responsável por orquestrar as camadas e iniciar a aplicação
"""

from src.entrypoints.cli import main_menu


def main():
    """Função principal da aplicação"""
    main_menu()


if __name__ == "__main__":
    main()
