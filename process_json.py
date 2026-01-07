import json
import glob
from datetime import datetime

for file in glob.glob("*.json"):
    with open(file, 'r') as f:
        data = json.load(f)
    
    data['enabled'] = True
    
    for key in list(data.keys()):
        if 'timestamp' in key.lower() and isinstance(data[key], str):
            try:
                data[key] = int(datetime.fromisoformat(data[key].replace('Z', '+00:00')).timestamp())
            except:
                pass
    
    data.pop('legacy_setting', None)
    
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
