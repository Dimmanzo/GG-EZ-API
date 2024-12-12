# **GG-EZ - Esports Event Tracker API**

[View live project here!](#)

---

## **Project Rationale**

GG-EZ is an esports event tracker that helps users to browse through various esports events, view details about teams, players, and match schedules. It provides an organized way to track the ongoing and upcoming events, including real-time statistics and team information. This project serves as the backend API for the GG-EZ application, providing essential endpoints to fetch event details, manage users, and update event data.

---

## **Overview**

This project is built with Django and Django REST Framework to provide a secure, scalable API for the GG-EZ esports event tracker platform. The API allows the frontend (React application) to interact with the system and fetch, update, and delete event-related information.

The API includes endpoints for managing events, teams, matches, and players, with different permissions based on the user role (admin or default user).

---

## **Table of Contents**

- [Project Rationale](#project-rationale)
- [Project Structure](#project-structure)
- [Features](#features)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [User Stories](#user-stories)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Deployment](#deployment)
- [Cloning and Forking](#cloning-and-forking)
- [Credits](#credits)

---

## **Project Structure**

The project is structured into multiple Django apps for better maintainability and separation of concerns.

```
GG-EZ-API-main/
├── api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── permissions.py
├── events/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── matches/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── teams/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
└── manage.py
```

**Explanation of Key Folders and Files:**
- **api/**: Contains global configurations such as settings, URLs, and permission settings.
- **events/**, **matches/**, **teams/**, **users/**: These are the core apps for handling the database models, views, serializers..
- **manage.py**: The command-line utility for managing the Django project.

---

## **Features**

### **Existing Features:**
- **Event Management**: Admin users can create, read, update, and delete events. Public users can only view events.
- **Team and Player Information**: View teams, players, and associated data.
- **Search and Filter**: Events can be filtered and searched by various parameters such as name, description, and date.
- **User Roles**: Admin users have full access, while default users only have view permissions.

### **Features to be Added:**
- Event statistics and performance metrics for matches.
- Integration with the frontend React app.

---

## **User Stories**

**Event Management**
As an admin, I can manage events, including creating, updating, and deleting them, to keep the event information up to date.

**Event Viewing**
As a user, I can view a list of upcoming esports events, so I can stay informed about the scheduled events.

**Match Management**
As an admin, I can manage matches by creating, updating, and deleting them, so that I can ensure match information is accurate and current.

**Match Viewing**
As a user, I can view match details, including team information, scheduled time, and results, so that I can stay updated on ongoing and upcoming matches.

**Team Management**
As an admin, I can manage teams, including creating, updating, and deleting them, to keep the list of teams current and relevant.

**Team Viewing**
As a user, I can view team details, including team names, descriptions, and logos, so I can learn more about the participating teams.

**Player Management**
As an admin, I can manage player information, including creating, updating, and deleting player profiles, to ensure player data is accurate.

**Player Viewing**
As a user, I can view player profiles, including their name, role, and team information, to learn more about individual players.

---

## **Database Schema**

![Database Schema](media/dbschema.png)  

---

## **Setup Instructions**

### **Backend Setup**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the backend server:
   ```bash
   python manage.py runserver
   ```

### **Frontend Setup**
1. Follow the instructions in the frontend repository to set up React and connect to the API.

---

## **Technologies and Tools Used**
- **Django REST Framework**: For building the API.
- **PostgreSQL**: The relational database used to store project data.
- **Heroku**: For deployment.
- **Git**: For version control.

---

## **Deployment**

The project is deployed to **Heroku** with both the frontend and backend accessible for full application use.

---

## **Cloning and Forking**

### **Cloning**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project folder:
   ```bash
   cd GG-EZ-API-main
   ```

### **Forking**
1. On GitHub, navigate to the repository.
2. Click **Fork** in the top-right corner.
3. Create a fork under your account.

---

## **Credits**

- &&&