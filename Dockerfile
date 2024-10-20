FROM python:3.12.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pip if it's not available in the slim image (usually already included)
RUN python -m ensurepip --upgrade

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# # Expose port 8000 for the FastAPI app
EXPOSE 8000

# # Run the FastAPI app using Uvicorn server when the container launches
# CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
