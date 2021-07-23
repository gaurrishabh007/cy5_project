# Import Module
import json
  
# Create  function
def cy5():
  
    # Create Dictionary
    value = {
        "firstName": "Rishabh",
        "lastName": "Gaur",
        "hobbies": ["playing", "problem solving", "coding"],
        "age": 20,
        "children": [
            {
                "firstName": "mohan",
                "lastName": "bansal",
                "age": 15
            },
            {
                "firstName": "prerna",
                "lastName": "Doe",
                "age": 18
            }
        ]
    }
  
    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)
  
  
# Call Function and Print it.
print(cy5())