import openai

# [https://platform.openai.com/docs/guides/gpt/chat-completions-api]
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant.yeah!"},
        {"role": "user", "content": "unixの考え方を教えて？"},
        {"role": "assistant", "content": "Unixの設計哲学は、以下のようなものです。1. 単一の目的を持ったプログラムを作る。2. プログラム同士は、テキストベースでやり取りする。3. 新しい機能を実装する前に、既存のシステムを最大限に活用しようとする。4. プログラムは、権限を最小限に抑えて実行される。5. 出力は、可能な限りシンプルなテキスト形式で行われる。これらの考え方は、シンプルで柔軟性が高く、理解しやすいシステムを構築するために重要です。また、これらの考え方は、Unixが長期にわたって広く使われてきた一因でもあります。"},
        {"role": "user", "content": "要約してください"},
    ]
)

res_content = res["choices"][0]["message"]["content"]
print(res_content)