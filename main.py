import os

def create_folder_structure(base_dir):
    # Create main project directories
    dirs = [
        base_dir,
        os.path.join(base_dir, "app"),
        os.path.join(base_dir, "app", "models"),
        os.path.join(base_dir, "app", "schemas"),
        os.path.join(base_dir, "app", "routers"),
        os.path.join(base_dir, "app", "services"),
        os.path.join(base_dir, "app", "tests"),
        os.path.join(base_dir, "app", "static"),
        os.path.join(base_dir, "app", "templates"),
        os.path.join(base_dir, "app", "main.py"),
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    print(f"Folder structure created in {base_dir}")

def create_dockerfile(base_dir):
    dockerfile_content = """
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Install dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the current directory contents into the container at /app
    COPY . .

    # Expose the FastAPI port
    EXPOSE 8000

    # Run FastAPI with Uvicorn
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    """
    
    dockerfile_path = os.path.join(base_dir, "Dockerfile")
    
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile_content)
    
    print(f"Dockerfile created in {base_dir}")

def create_docker_compose(base_dir):
    docker_compose_content = """
    version: '3.8'

    services:
      fastapi:
        build: .
        ports:
          - "8000:8000"
        volumes:
          - .:/app
        environment:
          - PYTHONUNBUFFERED=1
        networks:
          - fastapi_network

    networks:
      fastapi_network:
        driver: bridge
    """
    
    docker_compose_path = os.path.join(base_dir, "docker-compose.yml")
    
    with open(docker_compose_path, "w") as f:
        f.write(docker_compose_content)
    
    print(f"Docker Compose file created in {base_dir}")

def create_requirements_txt(base_dir):
    requirements_content = """
    fastapi
    uvicorn
    """
    
    requirements_path = os.path.join(base_dir, "requirements.txt")
    
    with open(requirements_path, "w") as f:
        f.write(requirements_content)
    
    print(f"requirements.txt created in {base_dir}")

def main():
    base_dir = "fastapi_project"  # Change this as needed
    create_folder_structure(base_dir)
    create_dockerfile(base_dir)
    create_docker_compose(base_dir)
    create_requirements_txt(base_dir)

if __name__ == "__main__":
    main()
