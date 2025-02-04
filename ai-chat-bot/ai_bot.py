from customization import personal_name

import groq

API_KEY = "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" # Personal API key
bot_name = "AI"

# Initialize Groq API client
client = groq.Client(api_key=API_KEY)

# Function to get AI response from Groq API
def get_ai_response(u_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": u_input}]
        )
        return response.choices[0].message.content  # Corrected access
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit' to quit.")

    y_or_no = input("\nWould you like to customize your bot? Type Yes or No: ").lower()
    if y_or_no in ["y", "yes"]:
        bot_name = personal_name()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print(f"{bot_name}:", response)

