
# README - Projet P10: Créez une API sécurisée RESTful en utilisant Django REST

## Description
SoftDesk Support est une API RESTful sécurisée développée avec Django REST Framework, permettant de gérer un système de suivi de problèmes (issue tracking) pour des projets de développement.

### Fonctionnalités Principales

- **Gestion des utilisateurs** : Inscription, authentification JWT, respect du RGPD (vérification d'âge 15+, consentement)
- **Gestion de projets** : Création de projets (Back-end, Front-end, iOS, Android) avec système de contributeurs
- **Suivi des problèmes** : Création et gestion d'issues avec priorités (LOW/MEDIUM/HIGH), statuts (To Do/In Progress/Finished) et tags (BUG/FEATURE/TASK)
- **Commentaires** : Communication entre contributeurs via des commentaires sur les issues
- **Sécurité** : Système de permissions granulaires (seuls les auteurs peuvent modifier/supprimer leurs ressources)

## Prérequis
- Python 3.10+ installé sur votre système
- Git installé
- pip (gestionnaire de paquets Python)

## Installation et Configuration

### 1. Cloner le projet
```bash
git clone https://github.com/Pumpkin-09/OCProjetP10.git
cd SoftDesc
```

### 2. Créer un environnement virtuel
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate

# Sur macOS/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur de développement
```bash
python manage.py runserver
```


## Comptes de démonstration

### Superutilisateur (Admin)
Un superutilisateur a déjà été créé :
- **URL admin** : http://127.0.0.1:8000/admin/
- **Username** : admin
- **Password** : admin123

### Utilisateurs de test
Afin de réaliser des tests, 3 utilisateurs sont déjà implémentés dans la base de données :

| Username | Password |
|----------|----------|
| user1 | user1 |
| user2 | user2 |
| user3 | user3 |

## 5. Documentation des Points de Terminaison (Endpoints)
Un utilisateur ne peut voir que les ressources (projets, issues, commentaires) des projets auxquels il participe en tant que contributeur.
Un utilisateur ne peut pas voir les autres utilisateurs.

### 🔐 Authentification

| Méthode | Endpoint | Description | Corps de la Requête (JSON) |
|:---:|:---|:---|:---|
| POST | /api/token/ | Obtenir JWT token | `{"username": "<requis>",\"password": "<requis>"}` |
| POST | /api/token/refresh/ | Rafraîchir le token | `{"refresh": "<token_refresh>"}` |

**Exemple de réponse :**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**💡 Utilisation du token :**
- Dans Postman : **Authorization** → **Bearer Token** → Coller le token `access`
- Ou dans les headers : `Authorization: Bearer <votre_token_access>`

---

### 👤 Utilisateurs

| Méthode | Endpoint | Description | Corps de la Requête (JSON) |
|:---:|:---|:---|:---|
| POST | /api/user/ | Créer un utilisateur | `{"username": "<requis>", "email": "<requis>", "password": "<requis>", "date_of_birth": "YYYY-MM-DD", "can_be_contacted": de base false, "can_data_be_shared": de base false}` |
| GET | /api/user/ | Liste des utilisateurs | N/A |
| GET | /api/user/{id}/ | Détails d'un utilisateur | N/A |
| PATCH | /api/user/{id}/ | Modifier un utilisateur | `{"email": "..."}` |
| DELETE | /api/user/{id}/ | Supprimer un utilisateur | N/A |

---

### 📁 Projets

| Méthode | Endpoint | Description | Corps de la Requête (JSON) |
|:---:|:---|:---|:---|
| POST | /api/projects/ | Créer un projet | `{"title": "<requis>", "description": "<requis>", "project_type": "BACK-END|FRONT-END|IOS|ANDROID"}` |
| GET | /api/projects/ | Liste des projets | N/A |
| GET | /api/projects/{id}/ | Détails d'un projet | N/A |
| PATCH | /api/projects/{id}/ | Modifier un projet | `{"title": "...", "description": "..."}` |
| DELETE | /api/projects/{id}/ | Supprimer un projet | N/A |

---

### 🐛 Issues

| Méthode | Endpoint | Description | Corps de la Requête (JSON) |
|:---:|:---|:---|:---|
| POST | /api/projects/{project_id}/issues/ | Créer une issue | `{"title": "<requis>", "description": "<requis>", "assigned_user": <ID optionnel>, "project_status":<optionnel, TO DO de base> "TO DO|IN PROGRESS|FINISHED", "project_tag": "BUG|FEATURE|TASK", "project_priority": "LOW|MEDIUM|HIGH"}` |
| GET | /api/projects/{project_id}/issues/ | Liste des issues d'un projet | N/A |
| GET | /api/projects/{project_id}/issues/{id}/ | Détails d'une issue | N/A |
| PATCH | /api/projects/{project_id}/issues/{id}/ | Modifier une issue | `{"title": "...", "project_status": "IN PROGRESS"}` |
| DELETE | /api/projects/{project_id}/issues/{id}/ | Supprimer une issue | N/A |

---

### 💬 Commentaires

| Méthode | Endpoint | Description | Corps de la Requête (JSON) |
|:---:|:---|:---|:---|
| POST | /api/projects/{project_id}/issues/{issue_id}/comments/ | Créer un commentaire | `{"description": "<requis>"}` |
| GET | /api/projects/{project_id}/issues/{issue_id}/comments/ | Liste des commentaires d'une issue | N/A |
| GET | /api/projects/{project_id}/issues/{issue_id}/comments/{id}/ | Détails d'un commentaire | N/A |
| PATCH | /api/projects/{project_id}/issues/{issue_id}/comments/{id}/ | Modifier un commentaire | `{"description": "..."}` |
| DELETE | /api/projects/{project_id}/issues/{issue_id}/comments/{id}/ | Supprimer un commentaire | N/A |

---
