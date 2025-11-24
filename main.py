from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from openai import OpenAI
from io import BytesIO

# Load API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"status": "Your Face Swap backend is running!"}


@app.post("/swap-face")
async def swap_face(source: UploadFile = File(...), target: UploadFile = File(...)):
    source_bytes = await source.read()
    target_bytes = await target.read()

    result = client.images.edit(
        model="gpt-image-1",
        image=source_bytes,
        mask=None,
        prompt="Swap the face with the target image.",
        target_image=target_bytes,
        size="1024x1024"
    )

    return {"image": result.data[0].url}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)

