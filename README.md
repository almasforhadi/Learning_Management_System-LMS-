# 🎓 Full Stack Learning Management System (LMS)

A **Full Stack Learning Management System (LMS)** built using **Django REST Framework (Backend)** and **React (Frontend)**.  
This project demonstrates **secure authentication**, **role-based authorization**, **course management**, **student enrollment**, and **dashboard reporting** using modern web technologies.

---

## 🚀 Project Objective

The goal of this project is to design and implement a **secure, role-based LMS platform** that evaluates real-world skills such as:

- Authentication & Authorization (JWT)
- REST API Development
- Frontend–Backend Integration
- Role-based Dashboards
- Secure Password Management

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **JWT Authentication**
- **SQLite / PostgreSQL**

### Frontend
- **React**
- **React Router**
- **Axios**
- **Bootstrap / Tailwind CSS**
- **Chart.js**

---

## 🔐 Authentication & Security

- User Registration & Login
- JWT Token Generation & Validation
- Secure Token Storage
- Role-Based Route Protection
- Logout Functionality
- Password Reset via Email (Token-based)

---

## 👥 User Roles & Permissions

| Role        | Permissions |
|-------------|------------|
| **Admin** | View system statistics, manage users & courses |
| **Instructor** | Create, edit, delete own courses |
| **Student** | Enroll in courses, view enrolled courses |

---

## 📚 LMS Core Features

### Course Management
- Create / Update / Delete Courses
- Course Category Management
- Instructor–Course Relationship

### Student Enrollment
- Course Enrollment System
- Enrolled Course Tracking

---

## 📊 Dashboard & Reports

### Admin Dashboard
- Total Users Count
- Role-wise User Statistics
- Total Courses
- Total Enrollments
- Graphical Reports (Charts)

### Instructor Dashboard
- Created Courses List
- Course Edit / Delete

### Student Dashboard
- Enrolled Courses Summary
- Course Access

---

## 🧑‍💻 Frontend Features

- JWT-based Authentication UI
- Protected Routes
- Role-Based Dashboards
- Course Listing & Enrollment UI
- Password Reset UI
- Profile View & Update
- Responsive & Clean UI Design

---

## 🔗 API Integration

- RESTful communication between React & Django
- Axios for API requests
- JWT Authorization Headers
- Loading & Error Handling

---

## 📁 Project Structure

```bash
backend/
 ├── accounts/
 ├── lms/
 ├── core/
 ├── manage.py

frontend/
 ├── src/
 │   ├── auth/
 │   ├── pages/
 │   ├── components/
 │   ├── context/
 │   ├── api/
 ```


##  Installation & Setup
###  Backend Setup
```bash
git clone <repository-url>
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```



## 🔑 Environment Variables

Create .env files for backend and frontend as needed: </br>
JWT Secret Key</br>
Email SMTP Credentials</br>
API Base URL</br>



👨‍💻 Author :</br>
Md. Almas Forhadi</br>
📧 Email: almasforhasi1999@gmail.com</br>
🔗 GitHub: https://github.com/almasforhadi</br>
🔗 LinkedIn: https://linkedin.com/in/almasforhadi</br>