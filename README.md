\# Sentiment Analysis API for User Comments



This project is a \*\*RESTful API\*\* built with \*\*Django REST Framework\*\* that allows managing user comments and performing \*\*sentiment analysis\*\* on them.  

It uses \*\*TextBlob\*\* for NLP sentiment classification and \*\*JWT Authentication\*\* for secure access.



---



\## Features



\- Full \*\*CRUD\*\* for user comments (Create, Read, Update, Delete)  

\- Sentiment analysis: Positive / Negative / Neutral with confidence score  

\- Swagger \& Redoc documentation for all API endpoints  

\- JWT Authentication for secure access  



---



\## Technologies



\- Python 3.x  

\- Django 4.x  

\- Django REST Framework  

\- TextBlob  

\- drf-spectacular (Swagger \& Redoc)  

\- SQLite (or any preferred database)  



---



\## Installation



1\. Clone the repository:



```bash

git clone https://github.com/yourusername/sentiment-api.git

cd sentiment-api



2\. Create and activate a virtual environment:



python -m venv venv

source venv/bin/activate  # Linux / Mac

venv\\Scripts\\activate     # Windows



3\. Install dependencies:



pip install -r requirements.txt





4\. Apply migrations:



python manage.py migrate





5\. Create a superuser:



python manage.py createsuperuser





6\. Run the development server:



python manage.py runserver



API Access



* Swagger UI: http://127.0.0.1:8000/api/docs/



* Redoc UI: http://127.0.0.1:8000/api/redoc/



* JWT Token:



POST /api/token/

{

&nbsp;   "username": "your\_user",

&nbsp;   "password": "your\_password"

}





* Use the token in requests:



Authorization: Bearer <ACCESS\_TOKEN>



Example Sentiment Analysis Response

{

   "id": 1,

   "text": "This product is awesome!",

   "sentiment": "positive",

   "confidence": 0.95,

   "created\_at": "2025-11-21T09:10:21.244297Z"

}



Screenshots



1. Swagger UI: Shows all endpoints and request/response examples
   !\[Swagger UI](screenshots/swagger.png)
2. Redoc UI: Professional, well-organized API documentation
   !\[Redoc UI](screenshots/redoc.png)
3. Postman: CRUD requests with JWT authentication
   !\[Postman](screenshots/postman.png)



	

Resume Highlights



* Demonstrates Backend API development skills with Django REST Framework



* Shows experience with NLP sentiment analysis



* Highlights knowledge of JWT Authentication and API documentation



* Screenshots and live documentation make the project resume-ready
