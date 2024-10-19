from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Initialize the image-classification pipeline
model_id = "nateraw/food"
classifier = pipeline("image-classification", model=model_id)

# Pydantic model for request
class ClassificationRequest(BaseModel):
    url: str

# Define the API endpoint
@app.post("/classify-image")
async def classify_image(request: ClassificationRequest):
    try:
        # Download the image from the provided URL
        img = request.url

        # Run the image through the classification pipeline
        result = classifier(img)

        # Extract the label with the highest score
        label = result[0]["label"]

        # Return the classification result
        return {"label": label}

    except Exception as e:
        return {"errorr": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000)