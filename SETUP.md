# Setup Guide

## Prerequisites

- Python 3.12+
- AWS CLI
- AWS Account with Bedrock access

## Environment Setup

### 1. Python Environment
```bash
# Create virtual environment
python -m venv exercise2
cd exercise2
Scripts\activate  # Windows
# source bin/activate  # Linux/Mac
```

### 2. AWS Configuration
```bash
# Configure AWS credentials
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: us-east-1
# Default output format: json
```

### 3. Install Dependencies
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install dependencies with precompiled binaries for faster installation
pip install --prefer-binary -r requirements.txt

# Task Tracker specific
cd q
pip install --prefer-binary -r requirements.txt
```

### 4. Verify Bedrock Access
```bash
aws bedrock list-foundation-models --region us-east-1
```

## Running Applications

### Task Tracker Web App
```bash
cd q
python app.py
```

### Task Tracker CLI
```bash
cd q
python task_tracker.py
```

### Jupyter Notebooks
```bash
jupyter notebook
```

## Troubleshooting

### Common Issues

1. **AWS Credentials Not Found**
   - Run `aws configure`
   - Check `~/.aws/credentials`

2. **Bedrock Access Denied**
   - Verify IAM permissions
   - Check region availability

3. **Module Not Found**
   - Activate virtual environment
   - Install requirements: `pip install -r requirements.txt`

4. **Flask Port Already in Use**
   - Change port in app.py: `app.run(port=5001)`
   - Or kill existing process

### Dependencies Issues
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```