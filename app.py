from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
# Llama-3.2-1B-Instruct-GGUF

with model.chat_session():
    print(model.generate("你好，請問Python適合用在哪些方面", max_tokens=1024))
