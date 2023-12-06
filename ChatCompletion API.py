import openai
# 导入所需库
# # 注意，此处我们假设你已根据上文配置了 OpenAI API Key，如没有将访问失败
# completion = openai.ChatCompletion.create(
#     # 创建一个 ChatCompletion
#     # 调用模型：ChatGPT-3.5
#     model="gpt-3.5-turbo",
#     # message 是你的 prompt
#     messages=[
#         # 第一个消息是系统消息，角色为 "system"，内容为 "You are a helpful assistant."，用于指导模型的行为。
#         {"role": "system", "content": "You are a helpful assistant."},
#         # 第二个消息是用户消息，角色为 "user"，内容为 "Hello!"，是用户的输入。
#         {"role": "user", "content": "Hello!"}
#     ]
# )
#
# print(completion["choices"][0]["message"]["content"])


# 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="gpt-3.5-turbo", temperature = 0):
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]

