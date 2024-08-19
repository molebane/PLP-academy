
def get_user_info():
    # User for their name
    name = input("What is your name? ")
    
    # User for their age
    age = input("How old are you? ")
    
    # User for their location
    location = input("Where are you located? ")
    
    # Personalized message
    message = f"Hello, {name}! You are {age} years old and live in {location}. It's nice to meet you!"
    
    # Print the personalized message
    print(message)

get_user_info()
