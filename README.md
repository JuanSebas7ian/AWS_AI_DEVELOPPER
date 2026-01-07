# AWS AI Developer Course Project

This repository contains exercises and projects for the AWS AI Developer course, focusing on Amazon Bedrock integration and AI-powered applications.

## Project Structure

```
AWS_AI_DEVELOPPER/
├── q/                          # Task Tracker Web Application
│   ├── app.py                  # Flask web application
│   ├── task_tracker.py         # Command-line task manager
│   ├── templates/
│   │   └── index.html          # Web interface template
│   ├── requirements.txt        # Python dependencies
│   └── tasks.json             # Task storage (auto-generated)
├── exercise2/                  # Python virtual environment
├── genai-exercise1-text1.ipynb # Bedrock text generation exercise
├── genai-exercise1-text2.ipynb # Additional text exercises
├── genai-exercise1-video.ipynb # Video processing exercises
├── conexion.ipynb             # Connection setup notebook
└── requirements.txt           # Global project dependencies
```

## Features

### Task Tracker Application
- **Web Interface**: Flask-based web application for task management
- **Command Line Interface**: Terminal-based task tracker
- **Priority System**: Tasks organized by priority levels
- **Persistent Storage**: JSON-based task persistence
- **Real-time Updates**: Add and remove tasks dynamically

### AI Integration Exercises
- **Amazon Bedrock**: Text generation using Nova models
- **Model Configuration**: Temperature, token limits, and inference settings
- **Response Processing**: JSON response handling and parsing

## Quick Start

### Prerequisites
- Python 3.13+
- AWS CLI configured with appropriate credentials
- Access to Amazon Bedrock service

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AWS_AI_DEVELOPPER
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For the Task Tracker app:
```bash
cd q
pip install -r requirements.txt
```

### Running the Applications

#### Web Task Tracker
```bash
cd q
python app.py
```
Access at: http://localhost:5000

#### Command Line Task Tracker
```bash
cd q
python task_tracker.py
```

#### Jupyter Notebooks
```bash
jupyter notebook
```

## Usage Examples

### Task Management
- Add tasks with priority levels (1-5)
- View tasks sorted by priority
- Remove completed tasks
- Persistent storage across sessions

### AI Text Generation
```python
import boto3
import json

MODEL_ID = "amazon.nova-micro-v1:0"
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.invoke_model(
    modelId=MODEL_ID,
    body=json.dumps({
        "schemaVersion": "messages-v1",
        "messages": [{"role": "user", "content": [{"text": "Your prompt here"}]}],
        "inferenceConfig": {"maxTokens": 500, "temperature": 0.7}
    })
)
```

## Dependencies

### Core Dependencies
- Flask==2.3.3
- boto3 (for AWS services)
- jupyter (for notebooks)

### Development Tools
- Python 3.13.9
- Virtual environment support

## Configuration

### AWS Setup
1. Configure AWS credentials:
```bash
aws configure
```

2. Ensure Bedrock access in your AWS account
3. Set appropriate region (default: us-east-1)

### Environment Variables
- `AWS_REGION`: AWS region for Bedrock (default: us-east-1)
- `MODEL_ID`: Bedrock model identifier

## API Reference

### Task Manager Class
```python
class TaskManager:
    def add_task(name, priority)     # Add new task
    def remove_task(index)           # Remove task by index
    def load_tasks()                 # Load from JSON
    def save_tasks()                 # Save to JSON
```

### Flask Routes
- `GET /`: Display task list
- `POST /add`: Add new task
- `GET /remove/<index>`: Remove task

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes as part of the AWS AI Developer course.

## Support

For issues related to:
- **AWS Bedrock**: Check AWS documentation
- **Flask Application**: Review Flask logs
- **Dependencies**: Verify Python version and package installations

## Next Steps

- Implement user authentication
- Add task categories and tags
- Integrate more Bedrock models
- Add automated testing
- Deploy to AWS infrastructure