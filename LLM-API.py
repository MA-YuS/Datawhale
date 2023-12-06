# import os
# import openai
# from dotenv import load_dotenv, find_dotenv
#
# # 读取本地/项目的环境变量。
#
# # find_dotenv()寻找并定位.env文件的路径
# # load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# # 如果你设置的是全局的环境变量，这行代码则没有任何作用。
# _ = load_dotenv(find_dotenv())
#
# # 如果你需要通过代理端口访问，你需要如下配置
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ["HTTP_PROXY"] = 'http://127.0.0.1:7890'
#
# # 获取环境变量 OPENAI_API_KEY
# openai.api_key = os.environ['OPENAI_API_KEY']
# print(openai.api_key)
#
#
# # 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
# def get_completion(prompt, model="gpt-3.5-turbo", temperature = 0):
#     '''
#     prompt: 对应的提示词
#     model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
#     '''
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, # 模型输出的温度系数，控制输出的随机程度
#     )
#     # 调用 OpenAI 的 ChatCompletion 接口
#     return response.choices[0].message["content"]
#
# content = get_completion('你好')
# print()


#
# #%%
# '百度文心大模型'
# import requests
# import json
#
# def get_access_token():
#     """
#     使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
#     """
#     # 指定网址
#     url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=" \
#           "client_credentials&client_id=ogHP9ZdRVbZBrd8Q04wDgBmd&client_secret=wSChV8FZo3FrgTkeqr13lBhewcD7bAPn"
#     # 设置 POST 访问
#     payload = json.dumps("")
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#     }
#     # 通过 POST 访问获取账户对应的 access_token
#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response.json().get("access_token")
# access_token = get_access_token()
# print(access_token)
#
# #%%
# def get_wenxin(prompt):
#     # 调用接口
#     url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=24.f575048ea29de47b742976292a96861f.2592000.1702803246.282335-43132826"
#     # 配置 POST 参数
#     payload = json.dumps({
#         "messages": [
#             {
#                 "role": "user",# user prompt
#                 "content": "{}".format(prompt)# 输入的 prompt
#             }
#         ]
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     # 发起请求
#     response = requests.request("POST", url, headers=headers, data=payload)
#     # 返回的是一个 Json 字符串
#     js = json.loads(response.text)
#     print(js)
#     print(js["result"])
# get_wenxin("你好")



# #%%
# '星火大模型'
# '调用原生星火 API'
# import SparkApi
# #以下密钥信息从控制台获取
# appid = "52565fa0"     #填写控制台中获取的 APPID 信息
# api_secret = "YzIxYjVmZDI1YmQwYzExMDZiMTRmYzlh"   #填写控制台中获取的 APISecret 信息
# api_key ="0bbacecce2a36133fca15a2ecaef33df"    #填写控制台中获取的 APIKey 信息
#
# #用于配置大模型版本，默认“general/generalv2”
# domain = "general"   # v1.5版本
# # domain = "generalv2"    # v2.0版本
#
# #云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
# # Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址
#
#
# # 首先定义一个从用户输入 prompt 生成传入参数的函数：
# def getText(role, content, text = []):
#     # role 是指定角色，content 是 prompt 内容
#     jsoncon = {}
#     jsoncon["role"] = role
#     jsoncon["content"] = content
#     text.append(jsoncon)
#     return text
# # 接着，我们将一个用户输入 prompt 封装为这样一个传入参数列表：
# question = getText("user", "你好")
# # print(question)
#
# # 然后再调用 SparkApi.py 中封装的 main 函数即可：
# response = SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
# # print(response)
#
# #%%
# import requests
#
# api_url = "http://127.0.0.1:8000/spark"
# headers = {"Content-Type": "application/json"}
# data = {
#     "prompt" : "你好",
#     "temperature" : 0.2,
#     "max_tokens" : 3096}
#
# response = requests.post(api_url, headers=headers, json=data)
# print(response.text)


# #%%
# import zhipuai
# zhipuai.api_key = "f68ab56a16882f43fde6bdbed9b6405d.mwL4rUdKktuNJq4h" #填写控制台中获取的 APIKey 信息
#
# model = "chatglm_std" #用于配置大模型版本
#
# # 智谱的调用传参和其他类似，也需要传入一个列表，列表中包括 role 和 prompt，
# # 首先定义一个从用户输入 prompt 生成传入参数的函数：
# def getText(role, content, text = []):
#     # role 是指定角色，content 是 prompt 内容
#     jsoncon = {}
#     jsoncon["role"] = role
#     jsoncon["content"] = content
#     text.append(jsoncon)
#     return text
# # 接着，将一个用户输入 prompt 封装为一个传入参数列表：
# question = getText("user", "你好")
# print(question)
#
# # 请求模型
# response = zhipuai.model_api.invoke(
#     model=model,
#     prompt=question
# )
# print(response)
#
# #%%
# from zhipuai_llm import ZhipuAILLM
#
# zhipuai_model = ZhipuAILLM(model="chatglm_std", temperature=0, zhipuai_api_key=zhipuai.api_key)
#
# zhipuai_model.generate(['你好'])



 #%%
import warnings
warnings.filterwarnings('ignore')

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# 这里我们将参数temperature设置为0.0，从而减少生成答案的随机性。
# 如果你想要每次得到不一样的有新意的答案，可以尝试调整该参数。
llm = ChatOpenAI(temperature=0.0)

#初始化提示模版
prompt = ChatPromptTemplate.from_template("描述制造{product}的一个公司的最佳名称是什么?")

#将大语言模型(LLM)和提示（Prompt）组合成链
chain = LLMChain(llm=llm, prompt=prompt)

#运行大语言模型链
product = "大号床单套装"
chain.run(product)




