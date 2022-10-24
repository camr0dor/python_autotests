import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 1000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Martin",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 1000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Chloe",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.get("https://petstore.swagger.io/v2/pet/1000", json={
  "id": 2000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Chloe",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

