# Quodroid_Challenge


## Overview
The project aims to create a system that can accept a detailed API call, execute the testing steps provided within as a Robot Framework test, and subsequently return the test output. This entails developing an application using Python and Django that exposes an API endpoint. The endpoint should accept a POST request structured to execute the detailed steps using the Robot Framework and return the results.

## Setup Instructions
1. Clone the repository from GitHub Repo URL : `https://github.com/trushashah14/Quodriod_Challenge.git`.
2. Navigate to the project directory: `cd testai_project`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:

- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply migrations:`python manage.py migrate`
7. Run the Django development server: `python manage.py runserver`
8. The Django server should now be running locally.


## Execution Instructions
1. Use a tool like Postman to send a POST request to the API endpoint.
2. Configure the request with the following details:

- Endpoint: `http://127.0.0.1:8000/testai/tests/v1/execute`
- Method: POST
- Headers: Content-Type: application/json
- Body:
```
{
    "tests": [
        {
            "title": "Open google.com",
            "steps": [
                "Open Browser https://google.com chrome"
            ]
        }
    ]
}
```

3. Send the request and observe the response for the test output.


## API Call Examples
### Request
```
POST /testai/tests/v1/execute HTTP/1.1
Host: http://127.0.0.1:8000
Content-Type: application/json

{
    "tests": [
        {
            "title": "Open google.com",
            "steps": [
                "Open Browser https://google.com chrome"
            ]
        }
    ]
}
```
### Response
```
{
    "Open google.com": true
}
```

## Contributors
- Trusha Shah

