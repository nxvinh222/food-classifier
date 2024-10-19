from transformers import pipeline; 

model_id = "nateraw/food"

classification_pipe = pipeline("image-classification", model=model_id)
print(classification_pipe('https://assets.epicurious.com/photos/642aebf9a2cf918d8b679f65/1:1/w_4380,h_4380,c_limit/PastaPomodoro_RECIPE_033023_50036.jpg'))
