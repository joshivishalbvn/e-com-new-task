# E-Commerce Order/Inventory Management System

This is a Django-based project that provides RESTful APIs for managing an e-commerce system. It includes product management, order handling, customer management, and more. Below are the steps to set up, run, and understand the project.

## Features

1. **Models**
   - Product
   - Product Images
   - Customer
   - Order and Order Items

2. **API Endpoints**
   - CRUD operations for Products
   - Add and delete images for Products
   - Create orders with multiple products
   - List orders with product details, quantities, subtotal, and total

3. **Custom Logic**
   - Deduct stock from Product when an order is created
   - Prevent orders with quantities exceeding available stock
   - Disallow duplicate products
   - Ensure price and stock are non-negative
   - Allow multiple images for products
   - Pagination, filtering, and search for Products
   - Send email notifications on order creation

4. **Utilities**
   - Seed command for initializing the database and creating a superuser

---

## Setup Instructions

### Prerequisites

- Python 3.9+
- Django 4.x
- Django REST Framework
- Postgres (or any supported database)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements/base.txt
   ```

3. Set up variables:

   Configure the following variables in your settings file for testing purposes:

   ```python
   SECRET_KEY = 'your-secret-key'
   DEBUG = True
   EMAIL_HOST = 'your-email-host'
   EMAIL_PORT = your-email-port
   EMAIL_HOST_USER = 'your-email-user'
   EMAIL_HOST_PASSWORD = 'your-email-password'
   EMAIL_USE_TLS = True
   DATABASE_URL = 'your-database-url'
   ```

4. Run the seed command to set up the database and create a superuser:

   ```bash
   python manage.py seed
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the APIs at `http://127.0.0.1:8000/`.

---

## Seed Command

The `seed` command automates the following:

- Runs `makemigrations` and `migrate` to set up the database schema.
- Prompts the user to create a superuser for admin access.
- python3 manage.py seed 

## API Documentation

This project does not currently use Swagger for API documentation. Instead, API endpoints can be tested using Postman or any other API client.

For detailed API examples and testing, refer to the API Endpoints Overview below.

---

## API Endpoints Overview

### Product APIs

- **List/Create/Update/Delete Products**:
  - `GET /products/` - List all products
  - `POST /products/` - Create a new product
  - `PUT /products/<id>/` - Update a product
  - `DELETE /products/<id>/` - Delete a product

- **Add/Delete Images**:
  - `POST /products/<product_id>/images/` - Add an image
  - `DELETE /products/<product_id>/images/<image_id>/` - Delete an image

### Order APIs

- **Create Order**:
  - `POST /orders/` - Create an order with customer and item details

- **List Orders**:
  - `GET /orders/` - List all orders with details

---

## Pagination, Filtering, and Search

### Product Filtering

- Filter by price and stock availability:
  ```
  GET /products/?price=<min>,<max>&stock=<min>,<max>
  ```

- Search by name and description:
  ```
  GET /products/?search=<query>
  ```

---

## Conclusion

This project is a robust foundation for an e-commerce system with advanced features like image management, stock validation, and email notifications. Contributions and improvements are welcome!
