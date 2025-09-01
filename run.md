\### Installation Guide ###



\#1. Clone the repository



* git clone https://github.com/your-username/your-repository.git
* cd your-repository



\#2. Create and activate the virtual environment



On Windows:



* python -m venv product\_list
* product\_list\\Scripts\\activate



On Linux/Mac



* python -m venv product\_list
* product\_list\\Scripts\\activate



\#3. Install dependencies



* pip install -r requirements.txt





\#4. Configure environment variables



* Create a .env file in the project root and add the following:

&nbsp;  OPENAI\_API\_KEY=your\_api\_key\_here



Important: Never expose your API key on GitHub.

Always use .env files and add .env to your .gitignore.



\#5. Run the application



In FastAPI (using uvicorn to run the application),
you can specify the desired port on the command line using the --port parameter.



* uvicorn app.main:app --reload --port 5000



\#6. And the interactive Swagger documentation at:



* The API will be available on: http://127.0.0.1:5000/docs
  You will need to enter the API key (found in the .env file).

&nbsp;   Click the Authorize button and enter the key.





\#7.Endpoints:



* GET /products          -> All products, search by pagination and limit
  GET /products/list     -> Products List - See a list of ids, search by pagination and limit
  GET /products/{id}     -> Returns specific product by ID



\#8. Best Practices Applied


* Error handling: HTTP 404 when product not found or invalid JSON.
  Automatic documentation: FastAPI generates interactive docs in /docs and /redoc.
  Modular structure: Separation of models, CRUD logic, and the main API.
  Inline comments: Explain the function of each part of the code.
  Local JSON: Simulates a database without the need to install a real DB.



