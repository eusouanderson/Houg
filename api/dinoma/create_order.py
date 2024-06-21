import requests

def create_order(shipping_speed, delivery_method_id, order_id, customer_name, customer_document, customer_email, webhook_url, items, nfe, address):
    url = "https://camisadimona.com.br/api/v2/order"
    api_key = "9450ae92ffc78b3289cab48e9b192b40"

    data = {
        "shipping_speed": shipping_speed,
        "delivery_method_id": delivery_method_id,
        "order_id": order_id,
        "customer_name": customer_name,
        "customer_document": customer_document,
        "customer_email": customer_email,
        "webhook_url": webhook_url,
        "items": items,
        "nfe": nfe,
        "address": address
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api-key": api_key
    }

    response = requests.post(url, json=data, headers=headers)

    try:
        response.raise_for_status()
        return response.json()  
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")  
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        raise


shipping_speed = "pac"
delivery_method_id = "177"
order_id = "1718977337"
customer_name = "Fulano da Silva"
customer_document = "123.456.789-13"
customer_email = "exemplo@gmail.com"
webhook_url = "https://option_webhook_url.com"

items = [
    {
        "name": "Camisa Polo P Branca",
        "sku": "12345",
        "qty": 2,
        "dimona_sku_id": "010603110108",
        "designs": ["url_front", "url_back"],
        "mocks": ["mock_front", "mock_back"]
    },
    {
        "name": "Camisa Polo M Branca",
        "sku": "12346",
        "qty": 2,
        "dimona_sku_id": "010603110109",
        "designs": ["url_front", "url_back"],
        "mocks": ["mock_front", "mock_back"]
    },
    {
        "name": "Camisa Polo G Branca",
        "sku": "12347",
        "qty": 2,
        "dimona_sku_id": "010603110110",
        "designs": ["url_front", "url_back"],
        "mocks": ["mock_front", "mock_back"]
    }
]

nfe = {
    "chave": "chave_com_44_digitos",
    "serie": "1",
    "numero": "1234",
    "link": "https://link_para_nfe"
}

address = {
    "name": "Receiver Name",
    "street": "Rua Buenos Aires",
    "number": "334",
    "complement": "Loja",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "zipcode": "20061000",
    "neighborhood": "Centro",
    "phone": "21 21093661",
    "country": "BR"
}

#response = create_order(shipping_speed, delivery_method_id, order_id, customer_name, customer_document, customer_email, webhook_url, items, nfe, address)

#print(response)
