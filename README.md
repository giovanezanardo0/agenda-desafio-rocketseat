# 📞 Agenda - Desafio Rocketseat

Projeto Python com arquitetura limpa para gerenciar uma agenda de contatos. A aplicação roda através de um menu interativo no terminal, permitindo criar, listar, editar, deletar e marcar contatos como favoritos.

## 🎯 Funcionalidades

- ✅ Adicionar novos contatos
- ✅ Listar todos os contatos
- ✅ Listar apenas contatos favoritos
- ✅ Marcar/desmarcar contato como favorito
- ✅ Editar informações de contatos
- ✅ Deletar contatos
- ✅ Persistência de dados em JSON

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas com separação de responsabilidades:

```
src/
├── main.py                      # Ponto de entrada da aplicação
├── entities/                    # Modelos de dados
│   └── contact.py              # Entidade Contact
├── business/                    # Lógica de negócio
│   └── contact_usecases.py      # Casos de uso/regras de negócio
├── infrastructure/              # Camada de persistência
│   └── repository.py            # Repositório de dados
└── entrypoints/                 # Interface com o usuário
    └── cli.py                   # Menu CLI interativo
```

### Fluxo de Dados

```
CLI (entrypoints) → Usecases (business) → Repository (infrastructure) → JSON Storage
```

## 📋 Requisitos

- **Python**: >= 3.12
- **Poetry**: 1.8.0+ (para gerenciar dependências)

## 📦 Dependências

| Pacote | Versão |
|--------|--------|
| python-dotenv | >= 1.2.2, < 2.0.0 |
| poetry-core | >= 2.0.0, < 3.0.0 |

## 🚀 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/agenda-desafio-rocketseat.git
cd agenda-desafio-rocketseat
```

### 2. Instale as dependências

Usando Poetry:

```bash
poetry install
```

Ou manualmente com pip:

```bash
pip install python-dotenv>=1.2.2
```

### 3. Verifique a versão do Python

```bash
python --version
# Deve retornar Python 3.12+ ou superior
```

## 🎮 Como Rodar

Execute a aplicação com:

```bash
python -m src.main
```

Isso iniciará o menu interativo no terminal:

```
========================================
📞 AGENDA DESAFIO ROCKETSEAT
========================================
1️⃣  Adicionar contato
2️⃣  Listar todos os contatos
3️⃣  Listar favoritos
4️⃣  Marcar/desmarcar favorito
5️⃣  Editar contato
6️⃣  Deletar contato
7️⃣  Sair
========================================
```

## 💾 Armazenamento de Dados

Os dados são persistidos em um arquivo `contacts.json` na raiz do projeto. Este arquivo é criado automaticamente na primeira execução.

**Estrutura do JSON:**
```json
[
  {
    "id": "uuid-do-contato",
    "name": "João Silva",
    "phone": "11 999999999",
    "email": "joao@example.com",
    "is_favorite": true,
    "created_at": "2024-04-20T15:30:45.123456"
  }
]
```

## 🔧 Estrutura do Projeto

### `entities/contact.py`
Define a entidade `Contact` com seus atributos e métodos de representação.

### `business/contact_usecases.py`
Implementa os casos de uso da aplicação:
- Criar contato
- Listar contatos
- Marcar como favorito
- Atualizar contato
- Deletar contato

### `infrastructure/repository.py`
Camada de persistência responsável por:
- Salvar contatos em JSON
- Carregar contatos do arquivo
- Atualizar dados
- Deletar dados

### `entrypoints/cli.py`
Interface de linha de comando que:
- Exibe menus interativos
- Captura entrada do usuário
- Chama os usecases apropriados
- Exibe resultados formatados

## 📝 Exemplo de Uso

```bash
$ python -m src.main

========================================
📞 AGENDA DESAFIO ROCKETSEAT
========================================
1️⃣  Adicionar contato
...
Escolha uma opção: 1

➕ ADICIONAR CONTATO
Nome: Giovane Zanardo
Telefone: 14 998038713
Email: giovane_gaz@hotmail.com
✅ Contato 'Giovane Zanardo' adicionado com sucesso!
```

## 🛠️ Desenvolvimento

### Rodando testes no futuro

Quando adicionarmos testes ao projeto:

```bash
poetry run pytest
```

### Formatando o código

```bash
# Com black (quando adicionado)
poetry run black src/
```

## 📜 License

Este é um projeto de estudos da Rocketseat.

---

**Feito com 💜 por Rocketseat 👋**

