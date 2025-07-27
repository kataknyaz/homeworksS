import requests

async def generate_image(prompt: str) -> str:
    API_URL = "https://api.deepai.org/api/stable-diffusion"
    API_KEY = "https://neuroimg.art/api/v1/free-generate"  
    
    response = requests.post(
        API_URL,
        data={"text": prompt},
        headers={"api-key": API_KEY}
    )
    
    if response.status_code == 200:
        return response.json()["output_url"]
    else:
        raise Exception("Не удалось сгенерировать изображение")