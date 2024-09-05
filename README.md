# Student Management System

A web-based application built with Django and MySQL to manage student data efficiently.

## Features

- Add, update, and delete student records
- View student details
- Manage courses and enrollments
- User authentication system

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ruushy/Student-management-system-in-Django-and-mysql.git
   cd Student-management-system-in-Django-and-mysql
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**

   Set up your MySQL database and update the `DATABASES` setting in `settings.py`.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin panel for administrative tasks: `http://127.0.0.1:8000/admin/`.
- Use the student panel for tasks: `http://127.0.0.1:8000/students/`.
- Use the teacher panel for tasks: `http://127.0.0.1:8000/teacher/`.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.


## Contact

For any questions or feedback, please contact [thaliban659@gmail.com].
```

Feel free to customize this template to better fit your project's specifics and your preferences.