# Exam Backend FastAPI

Backend FastAPI modulaire connecté à PostgreSQL, avec auth JWT, CRUD pour le frontend et intégration IA.

## Architecture du backend

```
app/
├── api/
│   ├── deps.py
│   ├── router.py
│   └── routes/
│       ├── auth.py
│       ├── db.py
│       ├── health.py
│       └── setup.py
├── core/
│   ├── config.py
│   └── security.py
├── db/
│   ├── base.py
│   └── session.py
├── models/
│   └── entities.py
├── schemas/
│   ├── auth.py
│   └── db.py
├── services/
│   ├── ai_service.py
│   └── db_ops.py
└── main.py
```

## 1) Installation

```bash
cd exam-backend-fastapi
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## 2) Configuration

Copier `.env.example` vers `.env` et adapter:

- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `CORS_ORIGINS`
- `IA_API_URL`

### Valeurs par défaut utilisées

- **Nom base de données**: `exam_creator`
- **Utilisateur PostgreSQL**: `exam_user`
- **Mot de passe PostgreSQL**: `exam_pass_123`
- **Hôte**: `localhost`
- **Port**: `5432`

URL complète par défaut:

`postgresql+psycopg2://exam_user:exam_pass_123@localhost:5432/exam_creator`

## 3) Lancer le backend

```bash
uvicorn app.main:app --reload --port 8001
```

## 4) Initialiser les données de base

```bash
curl -X POST http://localhost:8001/api/setup/init
```

## 5) Démarrer le frontend

Dans `exam-creator-frontend/.env`:

```env
VITE_API_URL=http://localhost:8001
```

Puis:

```bash
npm install
npm run dev
```

## Endpoints principaux

- `POST /api/auth/signup`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/auth/signup-options`
- `GET /api/auth/admin/users` (admin)
- `POST /api/auth/admin/users` (admin)
- `PATCH /api/auth/admin/users/{user_id}/role` (admin)
- `POST /api/db/query`
- `POST /api/db/insert`
- `POST /api/db/update`
- `POST /api/db/delete`

## Bootstrap administrateur

La création publique (`/api/auth/signup`) est limitée au rôle `etudiant`.
Le premier administrateur doit être créé en base:

```bash
python scripts/create_admin.py --email admin@ecole.com --password Admin123! --full-name "Super Admin"
```

Une fois connecté, l'admin peut créer des comptes admin/professeur/etudiant depuis l'interface admin.

Quand une `submission` passe à `status = "soumis"`, le backend tente une auto-correction IA via `IA_API_URL/api/corriger-copie`.
