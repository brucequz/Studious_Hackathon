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
