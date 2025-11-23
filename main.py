
import os
from fastapi import FastAPI, UploadFile, File
import uvicorn
from openai import OpenAI

# -----------------------------
# 1️⃣ Load API KEY from Render
# -----------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()

@app.post("/swap")
async def swap_faces(user: UploadFile = File(...), target: UploadFile = File(...)):
    # Dummy response (baad me model laga denge)
    return {
        "status": "success",
        "message": "Face swapped successfully!",
        "note": "AI model baad me integrate hoga"
    }

@app.get("/")
def root():
    return {"message": "Face Swap Backend Running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
