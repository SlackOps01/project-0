#  HNG Stage 0 — Backend Task

## Description
This is my **HNG Stage 0** project built with **FastAPI**.  
It provides two endpoints:
- `/` → redirects to `/me`
- `/me` → returns my personal information and a random cat fact from an external API.

## Documentation
The api documentation can be found at **/me** endpoint


##  Features
- Built with **FastAPI**
- Uses **httpx** to fetch data from an external API
- Includes **rate limiting** with `slowapi`
- Supports **CORS**
- Returns responses in **JSON format**
- Timestamp uses **UTC ISO 8601 format**



## Dependencies
- FastAPI
- httpx
- slowapi
- uvicorn

## Local Setup Instructions
To run the project locally follow the steps below

### 1. Clone the repo
```
git clone https://github.com/SlackOps01/project-0.git
cd project-0
```

### 2. Create and activate a new virtual environment
```
python -m venv venv
source venv/bin/activate # On Mac-Os and Linix
./venv/scripts/activate # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application
```
uvicorn app:app --reload
```

### 5. Access the application
Visit https://localhost:8000/me

### 6. Example Response
```
{
  "status": "success",
  "user": {
    "email": "me@olanrewajusholarin.com",
    "name": "Olanrewaju Sholarin",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-16T09:45:00Z",
  "fact": "Cats sleep for 70% of their lives."
}
```




