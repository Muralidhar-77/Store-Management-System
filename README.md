# Grocery Store Management System

A web-based application for managing products and orders in a grocery store. Built with Flask (Python) for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- Manage products (add, delete, view)
- Manage units of measurement (UOM)
- Create and view orders
- Dashboard with order summary
- Responsive frontend UI

## Folder Structure

```
backend/
    create_conn.py         # Database connection setup
    products_dao.py        # Product data access logic
    order_dao.py           # Order data access logic
    uom_dao.py             # Unit of measurement data access logic
    server.py              # Flask server with API endpoints

frontend/
    index.html             # Dashboard page
    manage-product.html    # Product management page
    order.html             # Order creation page
    css/                   # Stylesheets
    js/                    # JavaScript files
    img.png                # Store image/logo

README.md                  # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- MySQL database

### Setup

1. **Clone the repository**

2. **Configure the database**

   - Update `backend/create_conn.py` with your MySQL credentials and database name.

3. **Install Python dependencies**

   ```
   pip install flask mysql-connector-python
   ```

4. **Create required tables in MySQL**

   Example schema:
   ```sql
   CREATE TABLE units (
       unit_id INT PRIMARY KEY AUTO_INCREMENT,
       unit_name VARCHAR(50)
   );

   CREATE TABLE products (
       product_id INT PRIMARY KEY AUTO_INCREMENT,
       p_name VARCHAR(100),
       unit_id INT,
       price_per_unit FLOAT,
       FOREIGN KEY (unit_id) REFERENCES units(unit_id)
   );

   CREATE TABLE orders (
       order_id INT PRIMARY KEY AUTO_INCREMENT,
       customer_name VARCHAR(100),
       total FLOAT,
       datetime DATETIME
   );

   CREATE TABLE order_details (
       order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
       order_id INT,
       product_id INT,
       quantity FLOAT,
       total_price FLOAT,
       FOREIGN KEY (order_id) REFERENCES orders(order_id),
       FOREIGN KEY (product_id) REFERENCES products(product_id)
   );
   ```

5. **Run the backend server**

   ```
   cd backend
   python server.py
   ```

   The Flask server will start on `http://127.0.0.1:5000`.

6. **Open the frontend**

   - Open `frontend/index.html` in your browser.
   - The frontend communicates with the backend via REST APIs.

## API Endpoints

- `/getProducts` - Get all products
- `/getUOM` - Get all units of measurement
- `/insertProduct` - Add a new product
- `/deleteProduct` - Delete a product
- `/getAllOrders` - Get all orders
- `/insertOrder` - Create a new order

## Customization

- Update styles in `frontend/css/custom.css` and `frontend/css/sidebar-menu.css`.
- Modify frontend logic in `frontend/js/custom/`.

