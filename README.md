# **GG-EZ - Esports Event Tracker API**

[View Live Project Here!](https://gg-ez-api-ce7093aa17cf.herokuapp.com/)

---

## **Project Rationale**

GG-EZ is a powerful esports event tracker designed to simplify the way users follow esports tournaments, matches, teams, and players.  
This project serves as the backend API for the GG-EZ platform, handling all event-related data and user interactions.

The API is secure, scalable, and built with **Django** and **Django REST Framework**, enabling the frontend to fetch, update, and manage information seamlessly.

---

## **Overview**

This backend API supports:
- **Event Management**: Manage details of esports tournaments and matches.
- **Team and Player Data**: Retrieve team profiles and player statistics.
- **User Roles**: Admin users can create and modify events, while general users can browse event data.
- **Search and Filter**: Easily find specific events or teams using filters and keywords.

---

## **Table of Contents**

- [Project Rationale](#project-rationale)
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
- [Manual Testing](#manual-testing)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Deployment](#deployment)
- [Cloning and Forking](#cloning-and-forking)
- [Credits](#credits)

---

## **Project Structure**

The project follows a clean and modular structure for maintainability.

```
GG-EZ-API/
├── api/                  # Global configurations and settings
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
├── events/               # Events app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── teams/                # Teams app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── matches/              # Matches app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/                # Custom user management
│   ├── models.py
│   ├── serializers.py
│   └── views.py
└── manage.py             # Django management script
```

---

## **Features**

### **Core Features**
- **Event Management**:  
  Admins can create, edit, and delete esports events, while users can view them.

- **Matches**:  
  Manage match details like teams, schedules, and results.

- **Teams and Players**:  
  View team profiles, player names, and roles.

- **User Authentication**:  
  Role-based access ensures admins have more control while general users can only view data.

- **Search and Filtering**:  
  Find events, teams, and matches with keyword search and filters.

---

## **User Stories**

### **Admin User**
- As an admin, I can manage events, teams, and players to keep the information up-to-date.
- As an admin, I can delete outdated matches to maintain data accuracy.

### **General User**
- As a user, I can view a list of all esports events and match schedules.
- As a user, I can view details about my favorite teams and players.

---

## **Database Schema**

![Database Schema](media/dbschema.png)

---

## **Setup Instructions**

Follow these steps to set up the API locally:

### **1. Clone the Repository**

```bash
git clone <repository_url>
cd GG-EZ-API
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Set Up Environment Variables**

Create a `.env` file in the root directory and add:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your_database_url
```

### **4. Run Migrations**

```bash
python manage.py migrate
```

### **5. Create a Superuser**

```bash
python manage.py createsuperuser
```

### **6. Start the Development Server**

```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/`.

---

## **Manual Testing**

Below is a detailed table summarizing manual tests performed for **events**, **matches**, **teams**, **players**, and **users**.

| **Feature**                     | **Test Case**                                         | **Expected Outcome**                        | **Result** |
|---------------------------------|------------------------------------------------------|--------------------------------------------|------------|
| **Event Management**            | Admin creates a new event                            | Event is created and displayed in the list | ✅ Pass     |
|                                 | Admin updates an existing event                      | Event details are updated successfully     | ✅ Pass     |
|                                 | Admin deletes an event                               | Event is removed from the list             | ✅ Pass     |
|                                 | User views a list of events                          | Events are displayed correctly             | ✅ Pass     |
| **Match Management**            | Admin creates a new match                            | Match is created with correct details      | ✅ Pass     |
|                                 | Admin updates match details                          | Match information is updated               | ✅ Pass     |
|                                 | Admin deletes a match                                | Match is deleted from the database         | ✅ Pass     |
|                                 | User views a list of matches                         | Matches are displayed correctly            | ✅ Pass     |
| **Team Management**             | Admin creates a new team                             | Team is added with default logo if missing | ✅ Pass     |
|                                 | Admin updates team description                       | Team details are updated                   | ✅ Pass     |
|                                 | Admin deletes a team                                 | Team is removed from the database          | ✅ Pass     |
|                                 | User views team profiles                             | Teams and their players are displayed      | ✅ Pass     |
| **Player Management**           | Admin adds a player to a team                        | Player is linked to the correct team       | ✅ Pass     |
|                                 | Admin updates player role                            | Player role is updated successfully        | ✅ Pass     |
|                                 | Admin deletes a player                               | Player is removed from the team            | ✅ Pass     |
|                                 | User views player details                            | Player details (name, role, team) displayed| ✅ Pass     |
| **User Authentication**         | User registers with valid credentials                | Account is created successfully            | ✅ Pass     |
|                                 | User registers with mismatching passwords            | Validation error is returned               | ✅ Pass     |
|                                 | User logs in with correct credentials                | User is authenticated and logged in        | ✅ Pass     |
|                                 | User logs out                                        | User session is cleared                    | ✅ Pass     |
|                                 | Admin attempts restricted action (delete player)     | Action is allowed                          | ✅ Pass     |
|                                 | User attempts restricted action (delete player)      | Action is forbidden (HTTP 403)             | ✅ Pass     |
| **Search and Filtering**        | User searches for events by keyword                  | Matching events are displayed              | ✅ Pass     |
|                                 | User filters matches by status                       | Matches are filtered correctly             | ✅ Pass     |
| **Cloudinary Integration**      | Admin uploads an event image or team logo            | Image is stored on Cloudinary successfully | ✅ Pass     |
| **API Endpoints**               | GET `/events/`                                       | List of all events is returned             | ✅ Pass     |
|                                 | POST `/events/` (Admin only)                         | New event is created                       | ✅ Pass     |
|                                 | GET `/matches/`                                      | List of all matches is returned            | ✅ Pass     |
|                                 | PUT `/matches/<id>/`                                 | Match details are updated                  | ✅ Pass     |
|                                 | DELETE `/players/<id>/`                              | Player is removed successfully             | ✅ Pass     |

---

## **Technologies and Tools Used**

- **Django**: Backend framework
- **Django REST Framework**: API development
- **PostgreSQL**: Database
- **Cloudinary**: Media storage
- **Heroku**: Deployment platform
- **Gunicorn**: WSGI server for production
- **Whitenoise**: Serves static files in production

---

## **Deployment**

The API is deployed on **Heroku**.

To deploy the project:
1. Set up a Heroku app.
2. Add environment variables in the Heroku dashboard.
3. Push the code to Heroku:

```bash
git push heroku main
```

---

## **Cloning and Forking**

### **Cloning**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd GG-EZ-API
   ```

### **Forking**

1. On GitHub, click **Fork** at the top-right corner.
2. Follow the steps to create a fork under your GitHub account.

---

## **Credits**

- **Django Documentation**: Guidance on API best practices.
- **Cloudinary**: For efficient media management.
- **Heroku**: For seamless deployment and hosting.
- **Bootstrap**: For styling in frontend development.