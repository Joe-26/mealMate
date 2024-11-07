# Project Name: **MealMate**

<img width="1822" alt="Screenshot 2024-11-07 at 12 35 23 PM" src="https://github.com/user-attachments/assets/c0dd307a-6214-4456-b2c0-4fd811599c9e">

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [Design Schema](#design-schema)
5. [Installation Guide](#installation-guide)


## Project Overview

**MealMate** is a web application built with Django, designed to generate recipes suggestions using AI, based on food ingredients, calorie limit and cuisine.. This project aims to help those people who have some random ingredients at their home and want to utilize the ingredients to cook something at home. The application is scalable, modular, and follows best practices for Django development.

### Key Features:
- **User Authentication**: Sign up and login.
- **RESTful API**: Built with Django REST Framework for easy integration.
- **Previous History**: Shows previous ingredients & generated recipes.
- **Responsive Design**: Optimized for desktop and mobile devices.

## Technologies Used
- **Django**: The main web framework for building the project.
- **OpenAPI**: For generating receipes.
- **MySQL**: Relational database for data storage.
- **HTML/CSS/JavaScript**: Frontend for user interface.
- **Tailwind**: Frontend framework for responsive design.
- **Git/GitHub**: Version control and collaboration.

## Design Schema
![AI Recipe Generator drawio](https://github.com/user-attachments/assets/2e900613-e76e-4d8a-96f6-3b7d16c59649)

## Installation Guide
Follow these steps to get your project up and running locally.

### Prerequisites:
- Python 3.x
- pip (Python package installer)
- Virtual Environment (optional but recommended)

1. Open a terminal & Run the following command to create a new directory named `Test`:
   ```bash
   mkdir Test
   ```

2. Move into the newly created `Test` directory:
   ```bash
   cd Test
   ```

3. Create a virtual environment called `venv` using Python:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment to isolate your project dependencies:
   ```bash
   source venv/bin/activate
   ```

5. Clone the `mealMate` repository from GitHub:
   ```bash
   git clone https://github.com/Joe-26/mealMate.git
   ```

6. Change to the `mealMate` directory:
   ```bash
   cd mealMate
   ```

7. Install the required Python dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

8. Open the `.env` file to configure the environment settings:
   ```bash
   nano .env
   ```

9. In the `.env` file, add the following line to set your OpenAI API key (replace `{Your API Key}` with your actual API key):
   ```bash
   OPENAI_API_KEY="{Your API Key}"
   ```

10. Save the changes and exit the editor by pressing `Ctrl+X`, then confirming with `Y` to save.

11. Finally, run the development server to start the application:
    ```bash
    python manage.py runserver
    ```
This will start the application on the default local server (`localhost:8000`), and you can access it in your browser.
