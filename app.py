import openai

# [https://platform.openai.com/docs/guides/gpt/chat-completions-api]
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant.yeah!"},
        {"role": "user", "content": "unixの考え方を教えて？"},
    ]
)

res_content = res["choices"][0]["message"]["content"]
print(res_content)