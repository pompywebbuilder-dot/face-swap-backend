import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "Backend Running Successfully"}

# MAIN WORKING ROUTE (Frontend uses this route)
@app.post("/swap-image")
async def swap_image(
    source_image: UploadFile = File(...),
    target_image: UploadFile = File(...)
):
    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt="swap these faces naturally",
            image=[
                source_image.file,
                target_image.file
            ],
            size="1024x1024"
        )

        return {"output_url": result.data[0].url}

    except Exception as e:
        return {"error": str(e)}
