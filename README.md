### Steps to Run the Project

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
