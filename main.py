import json

#Load in the specifications json file
with open('specifications.json', 'r') as f:
    json_object = json.loads(f.read())

print("Model: " + json_object['model_name'])