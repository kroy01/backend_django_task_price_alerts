# Price Alert Application

## Overview

This application allows users to set price alerts for cryptocurrencies. Users will receive an email when the target price is achieved.

## Setup

### Docker Setup

1. Ensure Docker and Docker Compose are installed on your system.

2. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/price-alert-app.git
   cd price-alert-app


3. Create a .env file in the root of the project and add the following environment variables:
    ```bash
   POSTGRES_DB=price_alert_db
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_password
4. Run the application using Docker Compose:
    ```bash
   docker-compose up
5. Apply database migrations and create a superuser:
    ```bash
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser

## Endpoints
### User Endpoints
* Register : 'POST /users/register/'
* Login : 'POST /api-token-auth/'
### Alert Endpoints
* Create Alert: : 'POST /alerts/create/'
  * Example request body:
  ```json
    {
    "coin": "bitcoin",
    "target_price": 33000
    }

* Delete Alert: : 'DELETE /alerts/delete/\<int:pk>/'
* Fetch Alerts: 'GET /alerts/'