# Python Api App
- Code copy from: https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/
- Init venv: `python3 -m venv venv`
- Install required package: `pip3 install -r requirements.txt`


# Add something for sonarqube testing
```
# For sonarqube testing
# Hardcoded credentials - security hotspot
"""
DATABASE_PASSWORD = "super_secret_password123"

# Duplicate function for code duplication detection
def duplicate_check(x):
    if x > 0:
        print("positive")
    else:
        print("negative")
        
def another_duplicate(x):  # same logic as above
    if x > 0:
        print("positive")
    else:
        print("negative")

# Complex nested conditions - complexity issue
@app.route('/', methods=['GET'])
def hello():
    a = 1
    b = 2
    if a > 0:
        if b > 0:
            if a + b > 0:
                if a * b > 0:
                    return 'Hello, World!'
    return 'Hello, World! From Version v0.0.5'

# Unused variable
result = "This variable is never used"
"""
```