import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system",
             "content": "You are a personal tutor that specializes in electrical engineering"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# demo = gradio.Interface(fn=CustomChatGPT, inputs="text",
#                         outputs="text", title="Your Personal Tutor")

# demo.launch(share=True)
