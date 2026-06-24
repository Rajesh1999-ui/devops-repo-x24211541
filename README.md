# Simple Online Shop: Manage Products and Orders with Django
![Screenshot 2025-01-10 230656](https://github.com/user-attachments/assets/d1b57fdb-8a69-435e-965f-dc4b1d0bb86d)
![Screenshot 2025-01-10 225631](https://github.com/user-attachments/assets/7541f603-71d7-4707-8ba8-c79fe8aa7e80)


![Screenshot 2022-01-09 at 17-04-55 Django Online Shop](https://user-images.githubusercontent.com/71011395/148684469-79bfdb07-efa0-4dde-ad76-1f3277f833e6.png)


This project is a simple yet fully functional online shop built with Django. It provides a custom dashboard for managing products and orders. Users can like products, add them to their cart, and proceed to checkout. Order processing is supported, but payments are handled using a fake payment system.

---

## Features

The application supports two types of users: **regular users** and **managers**.

### Features Available to Regular Users:
- **Cart Management**: Users can add, update, and remove items from their cart.
- **Edit Personal Information**: Users can update their personal details.
- **Order History**: Users can view their past orders.
- **Favorites**: Users can like and save their favorite products.
- **Password Reset**: Users can reset their password using their registered email.

### Features Available to Managers:
Managers have access to all regular user features, along with additional capabilities through the custom dashboard available at [http://127.0.0.1:8000/accounts/login/manager](http://127.0.0.1:8000/accounts/login/manager).

- **Add Product**: Managers can add new products to the shop.
- **Edit and Delete Product**: Managers can modify or remove existing products.
- **Add New Category**: Managers can create new product categories.
- **Order Management**: Managers can view and manage all orders and order items.

---

## Technologies Used

- **Python 3**
- **Django**
- **crispy-bootstrap4** (for Bootstrap 4 forms)
- **django-crispy-forms** (for form rendering)
- **Pillow** (for image processing)
- **SQLite3** (default database for development)

---

## How to Run the Application

Follow these steps to set up and run the project on your local machine:

1. **Clone or Download the Project**:
   ```bash
   git clone https://github.com/saeidsaadatigero/online-shop
   cd online-shop-django
   ```

2. **Set Up a Virtual Environment**:
   - For Mac and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Apply migrations to create the database schema:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin)**:
   Create an admin account to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   Start the server using:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

---

## Manager Dashboard Access

To access the custom dashboard for managers, use the following credentials:
- **Email**: `admin@admin.com`
- **Password**: `admin`

---

## How to Contribute

Contributions are welcome! If you'd like to contribute to this project, follow these steps:

1. **Fork the Repository**:
   Fork the repository on GitHub.

2. **Create a New Branch**:
   Create a branch with a descriptive name for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**:
   Implement your changes and test them thoroughly.

4. **Commit and Push**:
   Commit your changes and push them to your forked repository:
   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your-feature-name
   ```

5. **Submit a Pull Request**:
   Open a pull request on GitHub and describe your changes in detail.

---

## License

This project is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

---

## App Preview

![Peek 2022-01-09 19-15](https://user-images.githubusercontent.com/71011395/148689722-6ceacc8f-81b7-48e0-a258-9d4e543d1e7c.gif)

---

Feel free to explore, contribute, and customize this project according to your needs!
