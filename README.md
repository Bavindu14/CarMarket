# CarMarket

## Overview
CarMarket is a Django-based web application that allows users to list, browse, and bid on vehicles. It includes features such as vehicle creation, detailed listings with images, search functionality, and user authentication.

## Features
- User registration and login.
- List new vehicles with details (make, model, year, price, etc.) and multiple images.
- Search vehicles by make, model, or year.
- View vehicle details and place bids (for authenticated users).
- Edit or delete listings (for owners only).
- Owner contact details visible to owners or admins.

## Installation

### Prerequisites
- Python 3.11.0
- Django 3.2.25
- Git

### Setup
1. Clone the repository:# CarMarket
   git clone https://github.com/Bavindu14/CarMarket.git
   cd CarMarket
2. Create a virtual environment and activate it:
    python -m venv venv
    venv\Scripts\activate  # On Windows
3. Install dependencies:
   pip install django==3.2.25
4. Apply migrations:
   python manage.py migrate
5. Create a superuser (for admin access):
   python manage.py createsuperuser
6. Run the development server:
   python manage.py runserver
   
## Usage
- Access the app at `http://127.0.0.1:8000/`.
- Register or log in to list vehicles or place bids.
- Use the search bar on the vehicle list page to find specific vehicles.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

## License
[Add license if applicable, e.g., MIT License]

## Group 8
Bavindu Gunasinghe (226044G)
Ravindu Weerasekara (226133E)
Naveen Sandeepa	(226067E)


