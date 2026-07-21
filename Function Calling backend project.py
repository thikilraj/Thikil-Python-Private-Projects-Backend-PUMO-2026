import json


# Function 1: Get weather
def get_weather(city):
    return {
        "city": city,
        "temperature": "22°C",
        "condition": "Rainy"
    }


# Function 2: Get user information
def get_user_info(name):
    return {
        "name": name,
        "status": "Active",
        "role": "User"
    }


# Function 3: Calculate
def calculate(a, b, operation):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    else:
        return "Invalid operation"


# Function calling router
def function_call(request):

    function_name = request["function"]
    arguments = request["arguments"]

    if function_name == "get_weather":
        return get_weather(**arguments)

    elif function_name == "get_user_info":
        return get_user_info(**arguments)

    elif function_name == "calculate":
        return calculate(**arguments)

    else:
        return {
            "error": "Function not found"
        }


# Example request
request = {
    "function": "get_weather",
    "arguments": {
        "city": "Coimbatore"
    }
}

# Execute function
result = function_call(request)

print("----- FUNCTION CALLING BACKEND -----")

print("Function Called:", request["function"])

print("Arguments:", request["arguments"])

print("\nOutput:")
print(json.dumps(result, indent=4))