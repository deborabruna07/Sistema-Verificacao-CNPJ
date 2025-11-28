# Sistema de Verificação de CNPJ

Este projeto realiza **validação, consulta em API e armazenamento de CNPJs** a partir de arquivos Excel, integrando Python com um banco de dados MySQL.
O sistema lê planilhas contendo *Razão Social* e *CNPJ*, padroniza os dados, valida os números e salva no banco de dados.


# Funcionalidades

* Importar arquivo `.xlsx` com colunas:

  * Razão Social
  * CNPJ

* Remover caracteres especiais do CNPJ.
* Validar CNPJ.
* Inserir dados em um banco MySQL.
* Ler e manipular planilhas com `pandas` e `openpyxl`.

* Tratamento de erros comuns:

  * Indentação incorreta
  * Erros de sintaxe SQL
  * Parâmetros inválidos
  * Problemas na conexão com o banco

# Estrutura do Projeto

```
├── clientes.xlsx
├── clientes_teste.xlsx
├── db.py
├── .env
├── main.py
├── verificacao.py
├── requirements.txt
└── README.md
```

## ⚙️ Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```
### 2️⃣ Ativar o ambiente virtual

```bash
env/Scripts/Activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Variáveis de Ambiente (.env)

Crie um arquivo chamado .env na raiz do projeto e adicione:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=adicione_sua_senha
DB_DATABASE=adicione_sua_database
```

### 5️⃣ Como Rodar o Projeto

```python
python main.py
```
