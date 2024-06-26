from api.dinoma.create_order import create_order
from api.persons.users import login_user, register_user
from api.model.model import UserInput

from fastapi import FastAPI, Header, HTTPException
import uvicorn  


app = FastAPI()

@app.get("/", tags=["Start"])
def read_root():
    return {"message": "Hello, Houg!"}



@app.post("/v1/login", tags=["Login"])
def login(username: str = Header(...), password: str = Header(...)):
    response = login_user(username, password)
    if response["message"] == "Usuario ou senha invalidos":
        raise HTTPException(status_code=400, detail=response["message"])
    return response

@app.post("/v1/register", tags=["Register"])
def register(username: str = Header(...), password: str = Header(...), name: str = Header(...), telephone: str = Header(...)):
    response = register_user(username, password, name, telephone)
    if response["message"] == "Usuario ja existe":
        raise HTTPException(status_code=400, detail=response["message"])
    return response


@app.get("v1/third_party_registration", tags=["Auth"])
def third_party_registration():

    return


@app.post("v1/generate_image", tags=["Generate Image"])
def generate_image_from_text(text: str):
    api_url = 'https://api.example.com/generate_image'
    
    params = {
        'text': text
    }

    try:
        
        response = requests.get(api_url, params=params)
        
        response.raise_for_status()
        
        return response.content

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar imagem: {e}")

@app.post("v1/create_order", tags=["Create Order"])
def create_order(shipping_speed: str, delivery_method_id: int, order_id: int, customer_name: str, 
                customer_document: str, customer_email: str, webhook_url: str, items: list, nfe: str, address: str):
    
    response = create_order(shipping_speed, delivery_method_id, order_id, customer_name, customer_document, customer_email, webhook_url, items, nfe, address)
    
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
