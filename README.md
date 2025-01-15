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
- **Team and Player Data**: Retrieve team profiles and **player statistics** - (Future feature).
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
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Cloning and Forking](#cloning-and-forking)
- [Api Endpoints](#api-endpoints)
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
  - Role-based access ensures admins have more control while general users can only view data.
  - **Password Policy**:
    - **Minimum Length**: 8 characters.
    - **Must Include**:
      - At least **1 uppercase letter** (A-Z).
      - At least **1 lowercase letter** (a-z).
      - At least **1 digit** (0-9).
      - At least **1 special character** (e.g., `@`, `$`, `!`, `%`, `*`, `?`, `&`).
    - **Passwords Must Match**: During registration, both `password1` and `password2` must match.
    - Clear error messages are provided if the password does not meet these criteria.

- **Search and Filtering**:  
  Find events, teams, and matches with keyword search and filters.

---

## **User Stories**

### **Admin User**
- As an admin, I can **create, update, and delete events** so that the platform has up-to-date tournament information for users to view.  
- As an admin, I can **manage matches**, including adding schedules, updating results, and removing outdated matches to maintain accurate and relevant data.  
- As an admin, I can **add and manage teams**, including their descriptions and logos, to ensure the teams' profiles are complete and professional.  
- As an admin, I can **create and manage player profiles**, including assigning them to teams and defining their roles, so users have detailed information about players.  

### **General User**
- As a user, I can **browse a list of esports events** and filter by date or name so that I can easily find tournaments I’m interested in.  
- As a user, I can **view match schedules and results** to stay updated on ongoing and upcoming competitions.  
- As a user, I can **view detailed information about teams**, including their name, logo, and players, to learn more about the teams I follow.  
- As a user, I can **view player profiles**, including their names, roles, and assigned teams, to understand their contributions to the tournaments.  

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

### **Manual Testing**

Below is a detailed table summarizing manual tests performed for **events**, **matches**, **teams**, **players**, **users**, and **authentication endpoints**.

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
|                                 | User registers with a short username                 | Validation error is returned               | ✅ Pass     |
|                                 | User registers with a weak password                  | Validation error is returned               | ✅ Pass     |
|                                 | User logs in with correct credentials                | User is authenticated and logged in        | ✅ Pass     |
|                                 | User logs in with incorrect credentials              | Validation error is returned               | ✅ Pass     |
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
| **Authentication Endpoints**    | POST `/dj-rest-auth/registration/`                   | User is registered successfully            | ✅ Pass     |
|                                 | POST `/dj-rest-auth/login/`                          | User is logged in and token is returned    | ✅ Pass     |
|                                 | POST `/dj-rest-auth/logout/`                         | User is logged out successfully            | ✅ Pass     |
|                                 | GET `/current-user-role/`                            | Current user's details are returned        | ✅ Pass     |

---

## **Code Validation**

All code was tested with **CI Python Linter** to ensure compliance with PEP8 standards. While no significant issues were detected, it is worth noting that some lines exceed 79 characters due to unavoidable long URLs and other similar code elements that cannot be split without breaking functionality.

- **Models**: Verified for consistent naming conventions and clean logic.  
- **Serializers**: Ensured proper validation and field handling.  
- **Views**: Checked for proper use of DRF class-based views, query optimizations, and error handling.  
- **URLs and Permissions**: Confirmed logical routing and secure access control implementation.  

The project meets Python coding standards, ensuring maintainable, clean, and readable code, with a few exceptions where line length restrictions could not be adhered to due to technical limitations.

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

## **Dependencies**

This project uses the following Python dependencies listed in `requirements.txt`:

```
asgiref==3.8.1                        # ASGI support for Django
cloudinary==1.41.0                    # Cloudinary integration for media storage
cryptography==3.4.8                   # Cryptography library for secure operations
dj-database-url==2.3.0                # Database URL configuration utility for Django
dj-rest-auth==2.1.9                   # Django authentication for REST APIs
Django==5.1.3                         # The main Django framework for web development
django-allauth==0.50.0                # Django authentication system with social login
django-cloudinary-storage==0.3.0      # Storage backend for Cloudinary in Django
django-cors-headers==4.6.0            # CORS support for Django applications
django-filter==24.3                   # Filtering for Django ORM and REST Framework
django-heroku==0.3.1                  # Heroku-specific settings for Django projects
djangorestframework==3.15.2           # DRF for building REST APIs with Django
djangorestframework-simplejwt==5.3.1  # JWT authentication for DRF
gunicorn==23.0.0                      # WSGI HTTP server for deploying Django apps in production
oauthlib==3.2.2                       # OAuth1/OAuth2 library for secure authorization
pillow==11.0.0                        # Imaging library for handling images in Django
psycopg2==2.9.10                      # PostgreSQL adapter for Python
psycopg2-binary==2.9.10               # Binary package of psycopg2 for easier installation
PyJWT==2.10.1                         # JWT library for handling JSON Web Tokens
python-decouple==3.8                  # Configuration settings from environment variables
python3-openid==3.2.0                 # OpenID authentication for Django
pytz==2024.2                          # Timezone library for accurate timezone handling
requests-oauthlib==2.0.0              # OAuth support for the Requests library
setuptools==75.6.0                    # Python package installer for distributing code
sqlparse==0.5.3                       # SQL parsing library for database queries
whitenoise==6.8.2                     # Static file serving for Django in production
```

These packages are required for the proper functioning of the backend API. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

---

## **Deployment**

The GG-EZ API is deployed on **Heroku**. Below is a step-by-step guide for deploying the project to Heroku using both the CLI and the Heroku website.

---

### **1. Prerequisites**
Before deploying, ensure you have the following:
- A **Heroku account** ([Sign up here](https://signup.heroku.com/)).
- **Git** installed on your machine.
- **Heroku CLI** installed ([Download here](https://devcenter.heroku.com/articles/heroku-cli)).
- **PostgreSQL** installed (for local development, Heroku provides this via an add-on).

---

### **2. Set Environment Variables**

You will need to configure the following environment variables for deployment:

| Variable Name    | Description                                    | Example Value                                      |
|-------------------|------------------------------------------------|----------------------------------------------------|
| `SECRET_KEY`      | Django's secret key for cryptography          | `your-secret-key`                                  |
| `DEBUG`           | Enables/disables debug mode (use `False` for production) | `False`                                        |
| `ALLOWED_HOSTS`   | Hosts allowed to connect to the application   | `your-app.herokuapp.com`                           |
| `DATABASE_URL`    | PostgreSQL database URL                       | `postgres://username:password@host:port/dbname`     |
| `CLOUDINARY_URL`  | Cloudinary configuration for media storage    | `cloudinary://api_key:api_secret@cloud_name`       |
| `CLIENT_ORIGIN`   | Frontend URL (for CORS settings)              | `https://your-frontend-url.com`                    |

#### **Example `.env` File for Local Development**
To run the project locally, create a `.env` file in the root directory and add:
```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your-database-url
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
CLIENT_ORIGIN=http://localhost:3000
```

---

### **3. Deployment Steps on Heroku (CLI)**

1. **Log in to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a Heroku App**:
   ```bash
   heroku create your-app-name
   ```

3. **Add Heroku Postgres Add-on**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Add Buildpacks** (if required for static file handling and Python):
   ```bash
   heroku buildpacks:add heroku/python
   heroku buildpacks:add https://github.com/memcachier/heroku-buildpack-memcached.git
   ```

5. **Install Dependencies**:
   Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

6. **Push the Code to Heroku**:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

7. **Set Environment Variables**:
   - Go to the Heroku dashboard.
   - Select your app and navigate to **Settings > Config Vars**.
   - Add the environment variables listed above using this command:
     ```bash
     heroku config:set SECRET_KEY=your-secret-key
     ```

8. **Run Database Migrations**:
   ```bash
   heroku run python manage.py migrate
   ```

9. **Create a Superuser (Optional)**:
   ```bash
   heroku run python manage.py createsuperuser
   ```

10. **Collect Static Files**:
    Ensure that static files are collected using Whitenoise:
    ```bash
    heroku run python manage.py collectstatic --noinput
    ```

---

### **4. Deployment via Heroku Website (Optional)**

If you prefer deploying the project through the Heroku website, follow these steps:

1. **Log in to Heroku**:
   - Visit [Heroku](https://www.heroku.com/) and log in to your account.

2. **Create a New App**:
   - Navigate to the **Dashboard** and click **New > Create New App**.
   - Enter a name for your app (e.g., `gg-ez-api`) and choose your region.

3. **Connect Your GitHub Repository**:
   - Go to the **Deploy** tab in your app settings.
   - Under **Deployment Method**, select **GitHub**.
   - Search for your repository and connect it.

4. **Enable Automatic Deploys (Optional)**:
   - Once your repository is connected, you can enable **Automatic Deploys** from the main branch to streamline future updates.

5. **Manually Deploy the App**:
   - Scroll down to the **Manual Deploy** section and click **Deploy Branch** to deploy your app.

6. **Set Environment Variables**:
   - Go to the **Settings** tab and click **Reveal Config Vars**.
   - Add all required variables (e.g., `SECRET_KEY`, `DATABASE_URL`).

7. **Run Migrations**:
   - Open the **More > Run Console** option in the top-right corner.
   - Run the following commands:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser  # Optional
     python manage.py collectstatic --noinput
     ```

---

### **5. Testing the Deployment**

- Access your app using the Heroku URL:
  ```
  https://your-app-name.herokuapp.com
  ```
- Verify the following:
  - All API endpoints respond correctly.
  - Media uploads work via Cloudinary.
  - The app is fully functional and free of errors.

---

### **Common Pitfalls & Troubleshooting**

- **Heroku Build Failures**: If you encounter build failures, ensure all dependencies are correctly listed in `requirements.txt`. You can also try adding `whitenoise` for static files management.
- **Missing Environment Variables**: Ensure all necessary environment variables (like `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`) are set correctly. You can check for missing variables with:
  ```bash
  heroku config
  ```
- **Database Errors**: If you encounter issues with migrations or database connections, verify your PostgreSQL configuration and ensure the correct version is being used.

---

## Cloning and Forking

### Cloning

To clone the repository:

- On GitHub.com, navigate to the main page of the repository.
- Above the list of files, click **Code**.
- Copy the URL for the repository.
- Type `git clone`, and then paste the URL you copied earlier.
- Press **Enter** to create your local clone.

### Forking

To fork the repository:

- On GitHub.com, navigate to the main page of the repository.
- In the top-right corner of the page, click **Fork**.
- Under "Owner," select the dropdown menu and click an owner for the forked repository.
- Click **Create Fork**.

---

## **API Endpoints**

### **Events Endpoints**
1. **GET** `/events/`  
   - Retrieves a list of all events.
   - **Response**: List of events in JSON format.
   
2. **POST** `/events/` (Admin Only)  
   - Create a new event.  
   - **Required Payload**:  
     ```json
     {
       "name": "Event Name",
       "description": "Event Description",
       "start_date": "YYYY-MM-DD",
       "end_date": "YYYY-MM-DD",
       "image": "optional_image_url"
     }
     ```
   - **Response**: Event object in JSON format.

3. **GET** `/events/{id}/`  
   - Retrieves a specific event by ID.
   - **Response**: Event object in JSON format.

4. **PUT** `/events/{id}/` (Admin Only)  
   - Update an event by ID.
   - **Required Payload**: Updated event data.
   - **Response**: Updated event object in JSON format.

5. **DELETE** `/events/{id}/` (Admin Only)  
   - Delete an event by ID.
   - **Response**: Success message.

---

### **Matches Endpoints**
1. **GET** `/matches/`  
   - Retrieves a list of all matches.
   - **Response**: List of match objects in JSON format.

2. **POST** `/matches/` (Admin Only)  
   - Create a new match.
   - **Required Payload**:  
     ```json
     {
       "event": "event_id",
       "team1": "team1_id",
       "team2": "team2_id",
       "scheduled_time": "YYYY-MM-DD HH:MM:SS",
       "status": "upcoming"
     }
     ```
   - **Response**: Match object in JSON format.

3. **GET** `/matches/{id}/`  
   - Retrieve a specific match by ID.
   - **Response**: Match object in JSON format.

4. **PUT** `/matches/{id}/` (Admin Only)  
   - Update a match by ID.
   - **Required Payload**: Updated match data.
   - **Response**: Updated match object in JSON format.

5. **DELETE** `/matches/{id}/` (Admin Only)  
   - Delete a match by ID.
   - **Response**: Success message.

---

### **Teams Endpoints**
1. **GET** `/teams/`  
   - Retrieves a list of all teams.
   - **Response**: List of team objects in JSON format.

2. **POST** `/teams/` (Admin Only)  
   - Create a new team.
   - **Required Payload**:  
     ```json
     {
       "name": "Team Name",
       "description": "Team Description",
       "logo": "optional_logo_url"
     }
     ```
   - **Response**: Team object in JSON format.

3. **GET** `/teams/{id}/`  
   - Retrieves a specific team by ID.
   - **Response**: Team object in JSON format.

4. **PUT** `/teams/{id}/` (Admin Only)  
   - Update a team by ID.
   - **Required Payload**: Updated team data.
   - **Response**: Updated team object in JSON format.

5. **DELETE** `/teams/{id}/` (Admin Only)  
   - Delete a team by ID.
   - **Response**: Success message.

---

### **Player Endpoints**
1. **GET** `/players/`  
   - Retrieves a list of all players.
   - **Response**: List of player objects in JSON format.

2. **POST** `/players/` (Admin Only)  
   - Create a new player.
   - **Required Payload**:  
     ```json
     {
       "name": "Player Name",
       "role": "Player Role",
       "team": "team_id",
       "avatar": "optional_avatar_url"
     }
     ```
   - **Response**: Player object in JSON format.

3. **GET** `/players/{id}/`  
   - Retrieve a specific player by ID.
   - **Response**: Player object in JSON format.

4. **PUT** `/players/{id}/` (Admin Only)  
   - Update a player by ID.
   - **Required Payload**: Updated player data.
   - **Response**: Updated player object in JSON format.

5. **DELETE** `/players/{id}/` (Admin Only)  
   - Delete a player by ID.
   - **Response**: Success message.

---

### **User Authentication Endpoints**
1. **POST** `/dj-rest-auth/registration/`  
   - Register a new user.
   - **Required Payload**:  
     ```json
     {
       "username": "username",
       "email": "user@example.com",
       "role": "default_user or staff_user",
       "password1": "password",
       "password2": "password"
     }
     ```
   - **Response**: User object in JSON format.

2. **POST** `/dj-rest-auth/login/`  
   - User login.
   - **Required Payload**:  
     ```json
     {
       "username": "username",
       "password": "password"
     }
     ```
   - **Response**: Auth token in JSON format.

3. **POST** `/dj-rest-auth/logout/`  
   - Logout the user.
   - **Response**: Success message.

4. **GET** `/current-user-role/`  
   - Get current user's role.
   - **Response**: Current user's details in JSON format.

---

### **Notes**  
- **Response Format**: All responses will be in JSON format, unless specified otherwise.
- **Authentication**: Some endpoints (e.g., creating or deleting) require admin-level access. Use JWT for authentication.
- **Filtering and Searching**: Filtering is available for events, matches, and teams. You can filter by various fields such as name, date, status, etc.

---

## **Credits**

- **Django Documentation**: Guidance on API best practices.
- **Cloudinary**: For efficient media management.
- **Heroku**: For seamless deployment and hosting.
- **Bootstrap**: For styling in frontend development.