# agenda-back
Agenda app backend

This api includer 3 endpoints to create, get a list, or get a single Product object. 

To run this api:

1. Install the dependencies in a local virtual environment.
    - If using poetry just go to root folder and execute poetry install.
    - If using pip a requirements.txt is provided. Use it to create a virtual environment with those dependencies.

2. Execute the app in a local server
    - Once in the root file, execute the uvicorn server command:
        `uvicorn challenge.main:app --reload`

3. Go to the OpenApi UI to interact with the apu
    Use your browser to access the fwollowing address: http://localhost:8000/docs
