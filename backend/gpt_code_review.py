import openai

def review_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code review assistant."},
            {"role": "user", "content": f"Please review the following code:\n\n{code}"}
        ]
    )
    return response['choices'][0]['message']['content']
