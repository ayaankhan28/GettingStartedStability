import base64
import requests
import os
from PIL import Image

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

body = {
  "steps": 50,#Number of steps,More steps->better image->more time
  "width": 1024,#widht of image
  "height": 1024,#height of image
  "seed": 0,
  "cfg_scale": 5,
  "samples": 1,
  "text_prompts": [
    {
      "text": "PROMPT",#Write your prompt here
      "weight": 1
    },
    {
      "text": "blurry, bad",#Write keywords which needs to be excluded from output.
      "weight": -1
    }
  ],
}

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "YOUR_API_KEY",
}

response = requests.post(
  url,
  headers=headers,
  json=body,
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()



for i, image in enumerate(data["artifacts"]):
    with open(f'.{"PATH TO YOU IMAGE"}/img.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))


img = Image.open("./{"PATH TO YOU IMAGE"}/img.png")
img.show()
