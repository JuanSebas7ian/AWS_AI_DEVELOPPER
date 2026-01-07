# Exercise Documentation

## Exercise 1: Amazon Bedrock Text Generation

### Overview
Learn to use Amazon Bedrock for AI text generation using the Nova Micro model.

### Files
- `genai-exercise1-text1.ipynb`: Basic text generation
- `genai-exercise1-text2.ipynb`: Advanced text exercises  
- `genai-exercise1-video.ipynb`: Video processing exercises

### Key Concepts

#### Model Configuration
```python
MODEL_ID = "amazon.nova-micro-v1:0"
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
```

#### Request Structure
```python
{
    "schemaVersion": "messages-v1",
    "messages": [{"role": "user", "content": [{"text": "Your prompt"}]}],
    "inferenceConfig": {
        "maxTokens": 500,
        "topK": 20,
        "temperature": 0.7
    }
}
```

#### Response Handling
```python
response = bedrock.invoke_model(modelId=MODEL_ID, body=json.dumps(payload))
result = json.loads(response['body'].read())
text = result['output']['message']['content'][0]['text']
```

### Exercise Tasks

1. **Basic Text Rewriting**
   - Input: "You are very good at your job."
   - Goal: Rewrite in formal tone
   - Expected: "You exhibit exceptional proficiency in your professional responsibilities."

2. **Parameter Tuning**
   - Experiment with temperature (0.1 - 1.0)
   - Adjust maxTokens for different response lengths
   - Test topK values for creativity control

3. **Prompt Engineering**
   - System prompts for role-playing
   - Few-shot learning examples
   - Chain-of-thought reasoning

### Best Practices

- **Temperature**: 0.1-0.3 for factual, 0.7-0.9 for creative
- **MaxTokens**: Set appropriate limits to control costs
- **Error Handling**: Always wrap API calls in try-catch
- **Rate Limiting**: Implement delays for bulk requests

## Exercise 2: Task Management Application

### Overview
Build a full-stack task management application with Flask.

### Components

#### Backend (Flask)
- Task model with name and priority
- TaskManager for CRUD operations
- JSON persistence layer
- RESTful API endpoints

#### Frontend (HTML/CSS)
- Responsive design
- Form validation
- Dynamic task display
- Remove functionality

#### CLI Version
- Menu-driven interface
- Input validation
- Error handling

### Implementation Steps

1. **Model Design**
```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
```

2. **Data Persistence**
```python
def save_tasks(self):
    with open(self.filename, 'w') as f:
        json.dump([task.to_dict() for task in self.tasks], f)
```

3. **Web Routes**
```python
@app.route('/add', methods=['POST'])
def add_task():
    # Handle form submission
```

4. **Template Rendering**
```html
{% for task in tasks %}
    <div class="task">
        [Priority {{ task.priority }}] {{ task.name }}
    </div>
{% endfor %}
```

### Learning Objectives

- Flask application structure
- Template rendering with Jinja2
- Form handling and validation
- JSON data persistence
- CSS styling and responsive design
- Command-line interface design

## Connection Setup

### File: `conexion.ipynb`
- AWS SDK initialization
- Credential configuration
- Service client setup
- Connection testing

### Key Steps
1. Import boto3
2. Configure credentials
3. Create service clients
4. Test connectivity
5. Handle authentication errors

## Next Steps

1. **Enhanced Features**
   - User authentication
   - Task categories
   - Due dates
   - Search functionality

2. **AWS Integration**
   - Deploy to EC2
   - Use RDS for storage
   - Implement Lambda functions
   - Add CloudWatch monitoring

3. **AI Enhancements**
   - Smart task prioritization
   - Natural language task creation
   - Automated task suggestions
   - Sentiment analysis