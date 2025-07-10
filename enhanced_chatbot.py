# Enhanced Rule-Based Chatbot with Functions
import re
import random
from datetime import datetime

def get_greeting_response():
    """Return a random greeting response"""
    greetings = ["Hi there!", "Hello!", "Greetings!", "Nice to see you!"]
    return random.choice(greetings)

def get_time_response():
    """Return current time"""
    return f"The current time is {datetime.now().strftime('%H:%M')}."

def get_date_response():
    """Return current date"""
    return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

def get_help_response():
    """Return help information"""
    return """I can respond to:
- Greetings (hi, hello)
- Time/date questions
- Weather questions (basic)
- Math calculations
- Tell jokes
Type 'quit' to exit."""

def calculate_expression(expression):
    """Evaluate simple math expressions"""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "I couldn't understand that math expression."

def tell_joke():
    """Return a random joke"""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    return random.choice(jokes)

def handle_math_query(user_input):
    """Handle math-related queries"""
    math_keywords = ['calculate', 'what is', 'math', '+', '-', '*', '/', 'plus', 'minus', 'times', 'divided']
    if any(word in user_input for word in math_keywords):
        # Extract the math expression
        expression = re.sub(r'[^0-9+\-*/(). ]', '', user_input)
        if any(char.isdigit() for char in expression):  # Check if there are numbers
            return calculate_expression(expression)
    return None

def handle_weather_query(user_input):
    """Handle weather-related queries"""
    weather_keywords = ['weather', 'rain', 'sunny', 'temperature']
    if any(word in user_input for word in weather_keywords):
        return "I'm not connected to live weather data, but you can check a weather website or app!"
    return None

def process_user_input(user_input):
    """Process user input and return appropriate response"""
    user_input = user_input.lower()
    
    if user_input == 'quit':
        return "Goodbye! Have a great day!", True
    
    # Check for specific patterns
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return get_greeting_response(), False
        
    if 'how are you' in user_input:
        return "I'm just a computer program, but I'm functioning well! How about you?", False
        
    if 'your name' in user_input:
        return "I'm SimpleBot, a rule-based chatbot.", False
        
    if 'time' in user_input:
        return get_time_response(), False
        
    if 'date' in user_input:
        return get_date_response(), False
        
    if 'help' in user_input:
        return get_help_response(), False
        
    if 'joke' in user_input:
        return tell_joke(), False
        
    # Handle math queries
    math_response = handle_math_query(user_input)
    if math_response:
        return math_response, False
        
    # Handle weather queries
    weather_response = handle_weather_query(user_input)
    if weather_response:
        return weather_response, False
        
    # Default response if no patterns match
    return "I'm not sure how to respond to that. Try asking something else or type 'help'.", False

def enhanced_chatbot():
    """Main chatbot function"""
    print("Hello! I'm an enhanced chatbot. Type 'quit' to exit or 'help' for options.")
    
    while True:
        user_input = input("You: ")
        response, should_exit = process_user_input(user_input)
        print(f"Chatbot: {response}")
        
        if should_exit:
            break

# Start the enhanced chatbot
if __name__ == "__main__":
    enhanced_chatbot()