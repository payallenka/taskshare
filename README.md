# TaskShare

## Overview

This project is designed to manage users and tasks in a web application. It consists of two main components:
1. **User Authentication and Profile Management**
2. **Task Management**

The system allows users to register, log in, manage their profiles, and create, manage, and track tasks.

## Workflow Overview

The workflow is divided into two main parts:

1. **User Authentication and Profile Management**  
2. **Task Management**

### 1. User Authentication and Profile Management Workflow

This part of the system focuses on handling user registration, login, logout, and user profiles.

#### Step 1: User Registration

- When a new user wants to sign up for the application, they visit the **Registration Page** (`/register/`).
  
- The user is presented with a form asking for:
  - Username
  - Email
  - First Name
  - Last Name
  - Password
  - Password Confirmation

- Once the form is submitted, the system performs the following actions:
  1. Validates the form inputs (username, email, password, etc.).
  2. If valid, the system creates a new `User` instance in the database.
  3. A new `Profile` instance is automatically created and linked to the user, storing additional information like `bio` and `location`.

- After successful registration, the user is redirected to the **Login Page** (`/login/`).

#### Step 2: User Login

- The user can log in using their username and password by visiting the **Login Page** (`/login/`).
  
- Upon submission, the system checks the user’s credentials (username and password) using Django's authentication system. If the credentials are correct:
  1. A session is created for the user.
  2. The user is redirected to their **Profile Page** (`/profile/`).

#### Step 3: User Profile Management

- Once logged in, the user can view their personal profile on the **Profile Page** (`/profile/`).
  
- The **Profile Page** shows the user’s:
  - Username
  - Email
  - First Name
  - Last Name
  - Bio (added during registration or later)
  - Location (optional)
  
- The user cannot directly edit this page from the frontend; the profile can be updated by changing the information in the database (e.g., via the Django admin interface or custom edit views, which can be added as an extension).

#### Step 4: User Logout

- To log out, the user can visit the **Logout Page** (`/logout/`), where they are prompted to confirm logging out.
  
- After confirmation, the system:
  1. Ends the user’s session.
  2. Redirects the user to the homepage or another page as defined (e.g., `/`).

### 2. Task Management Workflow

This part of the system focuses on creating, viewing, and managing tasks. Task management is only available to logged-in users.

#### Step 1: Task Creation

- Once logged in, the user can navigate to the **Task List Page** (`/tasks/`), where all their existing tasks are listed.
  
- To create a new task, the user clicks the **Create Task** button, which directs them to a form where they can input details like:
  - Task Title
  - Task Description
  - Due Date (optional)
  
- When the form is submitted:
  1. A new `Task` instance is created in the database.
  2. The task is automatically associated with the logged-in user (using the `user` foreign key).
  
- After task creation, the user is redirected back to the **Task List Page** where they can view their newly added task.

#### Step 2: Task Listing

- The **Task List Page** (`/tasks/`) displays a list of all tasks associated with the logged-in user.
  
- For each task, the following details are shown:
  - Title
  - Description
  - Due Date (if available)
  - Completion Status (Completed/Incomplete)

#### Step 3: Task Completion

- Each task in the task list can be marked as **Complete** or **Incomplete** by the user. This is done by toggling the task's status.

- When the user marks a task as complete:
  1. The `completed` field of the task is updated in the database to `True`.
  2. The task status is displayed as "Completed" on the **Task List Page**.

- If the task is marked as incomplete, the system updates the `completed` field to `False`.

### 3. Interaction Between the Users and Tasks

The relationship between users and tasks is one-to-many. Each user can have multiple tasks, but each task is associated with only one user.

#### Data Flow:

1. **User Registration and Authentication**:
   - The user first creates an account via the registration page.
   - Upon successful registration, the system creates both a `User` instance and a `Profile` instance.

2. **Task Creation**:
   - After logging in, the user can create tasks.
   - Each task is associated with the logged-in user by saving the user ID in the `Task` model.

3. **Task Management**:
   - The user can view, create, or modify tasks on their personal task list.

4. **Profile Management**:
   - The user can view and modify their profile details via the Django admin interface (this can be extended with views to allow users to edit their profiles via the frontend).

## Detailed Workflow Example

### Example Scenario:

1. **User Registration**:
   - A new user visits the site and registers using the **Register Page** (`/register/`).
   - They enter their information, including a username, email, first name, last name, and password.
   - The user is successfully registered, and a `Profile` object is created in the database linked to this user.

2. **User Login**:
   - The user now logs in using the **Login Page** (`/login/`) with their credentials.
   - Upon successful login, the user is redirected to their **Profile Page** (`/profile/`).

3. **User Task Management**:
   - The logged-in user decides to add a new task.
   - They click the **Create Task** button and fill in the task details.
   - The system creates a new task linked to the user and displays it in the task list.

4. **Task Completion**:
   - The user marks the task as completed.
   - The task is updated with the new status in the database.

5. **User Logout**:
   - The user decides to log out, confirming the action on the **Logout Page** (`/logout/`).
   - The user is logged out and redirected to the homepage or another page as defined.

## Additional Notes

### Authentication Flow:

Django's built-in authentication system handles user login and session management:
- **Login**: After successful authentication, Django stores the session information in the browser cookies.
- **Logout**: The session is terminated, and the user is redirected to the desired page.


#### Licence
This project is open-source and available under the MIT License.

This file provides detailed instructions and workflow for contributors and developers working with the User and Task Management system. You can use this `README.md` in your project to make it easier for others to understand and contribute to the codebase.
