In Entwicklung!
# 🚀 TeamFlow API: Aufgaben- & Team-Management

Eine vollständig containerisierte **Task- & Team-Management-API**, entwickelt mit dem Django REST Framework (DRF) und PostgreSQL. Dieses Projekt bietet ein robustes Backend für kollaboratives Projektmanagement mit Fokus auf rollenbasierte Zugriffskontrolle (RBAC) und automatisierte Dokumentation.

---

## 🛠 Tech Stack

* **Framework:** [Django 5.x](https://www.djangoproject.com/)
* **API Toolkit:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Datenbank:** PostgreSQL 15 (Containerisiert)
* **Orchestrierung:** Docker & Docker Compose
* **Dokumentation:** Swagger / OpenAPI (via `drf-spectacular`)
* **Testing:** Django Unit Tests

---

## ✨ Features

* **Docker-Workflow:** Setup der gesamten Umgebung mit nur einem Befehl.
* **Full CRUD API:** Umfassende Endpunkte für Teams, Projekte und Aufgaben.
* **Relationale Logik:** Aufgaben sind Teams zugeordnet; Mitglieder sehen nur relevante Daten.
* **Interaktive Doku:** Live Swagger UI zum Testen der Endpunkte im Browser.
* **Unit Tests:** Hohe Testabdeckung zur Sicherstellung der Geschäftslogik.
