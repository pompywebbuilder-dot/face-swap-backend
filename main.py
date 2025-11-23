from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/swap")
async def swap_faces(user: UploadFile = File(...), target: UploadFile = File(...)):
    # Dummy response (actual AI model बाद में जोड़ेंगे)
    return {"status": "success", "message": "Face swapped successfully!"}

@app.get("/")
def root():
    return {"message": "Face Swap Backend Running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
