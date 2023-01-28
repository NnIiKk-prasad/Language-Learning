# -----Smart calculator using Open API-----
import openai
from win32com.client import Dispatch

openai.api_key = "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"
model_engine = "text-davinci-002"

def speak(str):
    tell = Dispatch("SAPI.SpVoice")
    tell.Speak(str)

while True:
    query = input("\nQuery: ")
    if query.lower() in ['exit', 'quit', 'end']:
        print("Thanks for visiting!!!")
        speak("Thanks for visiting!!!")
        break
    
    prompt = f"Evaluate below expression if you can:\n{query}"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    ans = completions.choices[0].text
    print(ans)
    speak(ans)