### Steps to Run the Project

1. **Create a new directory for your project**  
   Run the following command to create a new directory named `Test`:
   ```bash
   mkdir Test
   ```

2. **Navigate into the new directory**  
   Move into the newly created `Test` directory:
   ```bash
   cd Test
   ```

3. **Create a virtual environment**  
   Create a virtual environment called `venv` using Python:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**  
   Activate the virtual environment to isolate your project dependencies:
   ```bash
   source venv/bin/activate
   ```

5. **Clone the project repository**  
   Clone the `mealMate` repository from GitHub:
   ```bash
   git clone https://github.com/Joe-26/mealMate.git
   ```

6. **Navigate into the cloned project directory**  
   Change to the `mealMate` directory:
   ```bash
   cd mealMate
   ```

7. **Install project dependencies**  
   Install the required Python dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

8. **Set up environment variables**  
   Open the `.env` file to configure the environment settings:
   ```bash
   nano .env
   ```

9. **Add your OpenAI API Key**  
   In the `.env` file, add the following line to set your OpenAI API key (replace `{Your API Key}` with your actual API key):
   ```bash
   OPENAI_API_KEY="{Your API Key}"
   ```

10. **Save and exit the file**  
    Save the changes and exit the editor by pressing `Ctrl+X`, then confirming with `Y` to save.

11. **Start the development server**  
    Finally, run the development server to start the application:
    ```bash
    python manage.py runserver
    ```
    This will start the application on the default local server (`localhost:8000`), and you can access it in your browser.
