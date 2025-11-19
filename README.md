

# 🐾 API Pets – CRUD com FastAPI + Supabase

API desenvolvida para gerenciar informações de pets, permitindo criar, listar, atualizar e excluir registros.
Projeto criado para o trabalho final da disciplina **Back-End Frameworks**, com deploy no Render e banco de dados no Supabase.

---

# 🚀 Link da API (Render)

🔗 **[https://api-pets-uypm.onrender.com](https://api-pets-uypm.onrender.com)**

📄 Documentação automática (Swagger UI):

🔗 **[https://api-pets-uypm.onrender.com/docs](https://api-pets-uypm.onrender.com/docs)**

---

# 📦 Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI**
* **Uvicorn**
* **Supabase (PostgreSQL)**
* **Pydantic**
* **Render (Deploy)**
* **Dotenv**

---

# 📁 Estrutura do Projeto

```
api-pets/
 ├── app/
 │    ├── main.py
 │    ├── database.py
 │    ├── models.py
 │    ├── routers/
 │    │     └── pets.py
 │    └── __init__.py
 ├── .env
 ├── requirements.txt
 └── README.md
```

---

# ⚙️ Como Rodar o Projeto Localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/api-pets.git
cd api-pets
```

---

### 2️⃣ Criar um ambiente virtual

```bash
python3 -m venv venv
```

Ativar:

**Linux/Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🔑 Variáveis de Ambiente (.env)

Crie um arquivo `.env` na raiz do projeto:

```
SUPABASE_URL="https://SEU_PROJETO.supabase.co"
SUPABASE_KEY="SUA_CHAVE_API"
```

Essas informações ficam disponíveis no site do Supabase.

⚠️ **Nunca exponha sua chave pública em repositórios!**
(Somente está no README do professor por ser um exercício.)

---

# ▶️ Rodar o servidor

```bash
uvicorn app.main:app --reload
```

API rodará em:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger)

---

# 🐶 Endpoints da API

### 📌 1. Listar todos os pets

**GET** `/pets`

**Resposta:**

```json
[
  {
    "id": 1,
    "nome": "Rex",
    "dono": "Carlos",
    "telefone": "119999999"
  }
]
```

---

### 📌 2. Buscar pet por ID

**GET** `/pets/{id}`

---

### 📌 3. Criar pet

**POST** `/pets`

**Exemplo:**

```json
{
  "nome": "Libra",
  "dono": "Gui",
  "telefone": "1131232413"
}
```

---

### 📌 4. Atualizar pet

**PUT** `/pets/{id}`

---

### 📌 5. Deletar pet

**DELETE** `/pets/{id}`

Resposta:

```json
{
  "message": "Pet deletado com sucesso!"
}
```

---

# 🧱 Banco de Dados (Supabase)

Tabela **pets**:

| coluna   | tipo | descrição          |
| -------- | ---- | ------------------ |
| id       | int8 | PK, auto increment |
| nome     | text | nome do pet        |
| dono     | text | nome do dono       |
| telefone | text | telefone do dono   |

---

# 🛠️ Deploy no Render

O projeto está configurado no Render como:

* **Environment:** Python
* **Start Command:**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

* Variáveis de ambiente configuradas pelo painel do Render

---

# 📌 Checklist do Professor

| Requisito                        | Status |
| -------------------------------- | ------ |
| CRUD completo                    | ✅      |
| Organização de pastas            | ✅      |
| Validações e tratamento de erros | ✅      |
| Retornos JSON apropriados        | ✅      |
| Uso de Supabase                  | ✅      |
| Deploy no Render                 | ✅      |
| Repositório GitHub               | ✅      |
| README completo                  | ✅      |

---

# 🧑‍💻 Autor

**Guilherme lopes **
Desenvolvedor Back-End
API criada para fins educacionais.

