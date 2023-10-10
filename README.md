# agenda-back
Agenda app backend

This api includer 3 endpoints to create, get a list, or get a single Product object. 

To run this api:

1. Install the dependencies in a local virtual environment.
    - If you are using poetry just go to root folder and execute:
      `poetry install`
    - If you prefer pip a requirements.txt is provided. Use it to create a virtual environment with those dependencies.

2. Execute the app in a local server.
    - Open your virtual environment. 
        You can do it with poetry executing the command:
            `poetry shell`
    - From root directory, execute the uvicorn server command:
        `uvicorn challenge.main:app --reload`

4. Go to the OpenApi UI to interact with the api
    - Use your browser to access the fwollowing address: http://localhost:8000/docs
