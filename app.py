from fastapi import FastAPI, HTTPException, status, Request
from datetime import datetime, timezone, timedelta
import httpx
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler, Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

cat_facts_url = "https://catfact.ninja/fact"

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["*"]
)

@app.get("/")
@limiter.limit("10/minute")
def home(request: Request):
    raise HTTPException(
        status_code=status.HTTP_303_SEE_OTHER,
        detail="Go to /me endpoint"
    )


@app.get("/me")
@limiter.limit("10/minute")
def get_profile(request: Request):
    try:
        cat_api_request = httpx.get(cat_facts_url)
        cat_api_response = cat_api_request.json()
        ng_tz = timezone(timedelta(hours=1))
        return{
            "status": "success",
            "user": {
                "email": "olanrewajusholarin5@gmail.com",
                "name": "Olanrewaju Sholarin",
                "stack": "Python/FastAPI"
            },
            "timestamp": datetime.now(ng_tz).isoformat(),
            "fact": cat_api_response['fact']
        }
    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Error fetching data from cat facts api"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured!"
        )