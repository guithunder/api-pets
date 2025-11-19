

# 🐾 API Pets — FastAPI + Supabase

Uma API simples para cadastrar, listar, atualizar e remover pets, utilizando **FastAPI**, **Supabase** e **Render**.

---

## 🚀 Link da API (Render)

🔗 **API Online:**
[https://api-pets-uypm.onrender.com/](https://api-pets-uypm.onrender.com/)

🔗 **Documentação Swagger:**
[https://api-pets-uypm.onrender.com/docs](https://api-pets-uypm.onrender.com/docs)

---

## 📁 Estrutura do Projeto

```
api-pets/
 ├── app/
 │    ├── __init__.py
 │    ├── main.py
 │    ├── database.py
 │    ├── models.py
 │    └── routers/
 │         └── pets.py
 ├── .env
 ├── requirements.txt
 └── README.md
```

---

## ⚙️ Tecnologias

* **Python 3.10+**
* **FastAPI**
* **Uvicorn**
* **Supabase (PostgreSQL)**
* **Pydantic**
* **Render (deploy)**

---

## 🔧 Como rodar localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/api-pets.git
cd api-pets
```

---

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
```

Ativar:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Crie o arquivo `.env`

Crie um arquivo `.env` na raiz e coloque:

```
SUPABASE_URL="https://yziiavkxztzssvhxhotb.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aWlhdmt4enR6c3N2aHhob3RiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MzU2MzkxOCwiZXhwIjoyMDc5MTM5OTE4fQ.SWkMxdY5V6R_ECiGHrkVK92SDQKere-WLX4XjzI-QpI"

```

---

### 5️⃣ Execute o servidor

Dentro da pasta `app/` ou a partir da raiz:

```bash
uvicorn app.main:app --reload
```

A API iniciará em:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

E a documentação interativa:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🐶 Endpoints

### 📌 Listar todos os pets

**GET** `/pets/`

### 📌 Buscar pet por ID

**GET** `/pets/{id}`

### 📌 Criar pet

**POST** `/pets/`

Body:

```json
{
  "nome": "Rex",
  "dono": "João",
  "telefone": "11999999999"
}
```

### 📌 Atualizar pet

**PUT** `/pets/{id}`

Body igual ao POST.

### 📌 Deletar pet

**DELETE** `/pets/{id}`

---

## 🗄️ Banco de Dados (Supabase)

A tabela `pets` deve conter:

| Coluna   | Tipo     |
| -------- | -------- |
| id       | int (PK) |
| nome     | text     |
| dono     | text     |
| telefone | text     |

---

## 🧪 Testar localmente via cURL

Criar pet:

```bash
curl -X POST http://127.0.0.1:8000/pets/ \
-H "Content-Type: application/json" \
-d '{"nome":"Bolt","dono":"Ana","telefone":"11988887777"}'
```

---

## ☁️ Deploy no Rende




depois




tambem voce pode acessar 

https://api-pets-uypm.onrender.com/docs

porque o senho ja pode testar la

e deixar o supabase no lado para conferir

lembrando de a perta o try it out


