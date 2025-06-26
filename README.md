# DevOps Training Project 🚀

A simple FastAPI application designed for practicing DevOps skills including containerization, CI/CD, and cloud deployment.

## 🎯 **Project Goals**

This project is designed to practice:
- **Docker & Containerization** - Multi-stage builds and optimization
- **CI/CD Pipelines** - Automated testing and deployment
- **Cloud Deployment** - Google Cloud Platform (Cloud Run & VMs)
- **Infrastructure as Code** - Configuration management
- **Testing & Quality** - Automated testing and code quality checks

## 🏗️ **Architecture**

```
├── src/                    # Application source code
│   ├── app.py             # FastAPI application
│   └── config/            # Configuration management
├── tests/                 # Test suite
├── deploy/                # Deployment configurations
│   ├── docker/           # Docker configurations
│   ├── github/           # GitHub Actions workflows
│   └── gcp/              # Google Cloud Platform configs
└── pyproject.toml        # Poetry dependencies and project config
```

## 🛠️ **Tech Stack**

- **Backend**: FastAPI + Uvicorn
- **Language**: Python 3.11
- **Dependency Management**: Poetry
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud Platform**: Google Cloud Platform
- **Testing**: Pytest
- **Code Quality**: Black, Flake8

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.11+
- Poetry
- Docker (optional)
- Google Cloud SDK (for deployment)

### **Local Development**

1. **Clone and setup:**
```bash
git clone <repository-url>
cd devops-training
poetry install
cp .env.example .env
```

2. **Run the application:**
```bash
# Development with hot reload
poetry run uvicorn src.app:app --reload --port 8080

# Or using the app directly
poetry run python src/app.py
```

3. **Access the application:**
- API: http://localhost:8080
- Interactive API docs: http://localhost:8080/docs
- ReDoc documentation: http://localhost:8080/redoc

### **Testing**

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src tests/ --cov-report=html

# Code formatting
poetry run black src/ tests/

# Linting
poetry run flake8 src/
```

## 🐳 **Docker**

### **Build and run locally:**
```bash
# Build image
docker build -f deploy/docker/Dockerfile -t devops-training .

# Run container
docker run -p 8080:8080 devops-training
```

### **Using Docker Compose (optional):**
```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: deploy/docker/Dockerfile
    ports:
      - "8080:8080"
    environment:
      - ENVIRONMENT=development
```

## ☁️ **Cloud Deployment**

### **Google Cloud Run (Serverless)**

1. **Setup GCP:**
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com
```

2. **Deploy:**
```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/devops-app

# Deploy to Cloud Run
gcloud run deploy devops-app \
  --image gcr.io/YOUR_PROJECT_ID/devops-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### **Google Compute Engine (VM)**

```bash
# Create VM with startup script
gcloud compute instances create devops-vm \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --machine-type=e2-micro \
  --metadata-from-file startup-script=deploy/gcp/vm-startup-script.sh \
  --tags=http-server
```

## 🔄 **CI/CD Pipeline**

The project includes a GitHub Actions workflow that:

1. **Test Stage**: Runs pytest, linting, and security scans
2. **Build Stage**: Creates Docker image and pushes to GCR
3. **Deploy Stage**: Deploys to Google Cloud Run

### **Setup GitHub Secrets:**
```
GCP_PROJECT_ID=your-project-id
GCP_SA_KEY=your-service-account-json-key
```

## 📊 **API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Root endpoint with basic info |
| GET    | `/health` | Health check for monitoring |
| POST   | `/echo`  | Echo service that processes messages |
| GET    | `/info`  | Application and environment information |
| GET    | `/docs`  | Interactive API documentation |

### **Example Usage:**

```bash
# Health check
curl http://localhost:8080/health

# Echo endpoint
curl -X POST http://localhost:8080/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello DevOps!"}'
```

## 🧪 **Testing Strategy**

- **Unit Tests**: FastAPI endpoint testing with TestClient
- **Integration Tests**: Full request/response cycle testing
- **Code Coverage**: Maintaining >90% coverage
- **Linting**: PEP8 compliance with Black and Flake8
- **Security**: Vulnerability scanning with Trivy

## 📝 **Environment Variables**

| Variable | Description | Default |
|----------|-------------|---------|
| `ENVIRONMENT` | Application environment | development |
| `DEBUG` | Enable debug mode | true |
| `HOST` | Server host | 0.0.0.0 |
| `PORT` | Server port | 8080 |
| `SECRET_KEY` | Application secret key | changeme |

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Run tests: `poetry run pytest`
4. Format code: `poetry run black src/ tests/`
5. Commit changes: `git commit -am 'Add feature'`
6. Push to branch: `git push origin feature-name`
7. Submit a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎓 **Learning Resources**

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Poetry Documentation](https://python-poetry.org/docs/)

---

**Happy DevOps Learning! 🚀**