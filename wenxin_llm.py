#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wenxin_llm.py
@Time    :   2023/09/22 14:27:55
@Author  :   Logan Zou 
@Version :   1.0
@Contact :   loganzou0421@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   基于 LangChain 定义文心模型调用方式

账号：18698561860
密码：mys@0127
'''

import json
import time
from typing import Any, List, Mapping, Optional, Dict, Union, Tuple
import requests
from langchain.llms.base import LLM
from langchain.utils import get_from_dict_or_env
from pydantic import Field, root_validator
from langchain.callbacks.manager import CallbackManagerForLLMRun

def get_access_token(api_key : str, secret_key : str):
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    这个函数用于获取百度 API 的访问令牌（access_token），需要提供 API Key 和 Secret Key。
    它构造一个 HTTP POST 请求，通过请求百度的 OAuth2.0 服务来获取 access_token。
    """
    # 指定网址
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=M5FyRIOidgS6vksP2ze2fW6S&client_secret=kchfPjwf39WUZeWRWEGjRMnB1hAv1cVt"
    # 设置 POST 访问
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # 通过 POST 访问获取账户对应的 access_token
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

# 继承自 langchain.llms.base.LLM
class Wenxin_LLM(LLM):
    # 原生接口地址，文心大模型 API 的地址
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant"
    # 默认选用 ERNIE-Bot-turbo 模型，即目前一般所说的百度文心大模型
    model_name: str = "ERNIE-Bot-turbo"
    # 访问时延上限
    request_timeout: float = None
    # 温度系数，影响生成文本的随机性
    temperature: float = 0.1
    # API_Key
    api_key: str = None
    # Secret_Key
    secret_key : str = None
    # access_token
    access_token: str = None
    # 必备的可选参数
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)

    def init_access_token(self):
        if self.api_key != None and self.secret_key != None:
            # 两个 Key 均非空才可以获取 access_token
            try:
                self.access_token = get_access_token(self.api_key, self.secret_key)
            except Exception as e:
                print(e)
                print("获取 access_token 失败，请检查 Key")
        else:
            print("API_Key 或 Secret_Key 为空，请检查 Key")

    # _call方法，其接受一个字符串，并返回一个字符串，即模型的核心调用
    def _call(self, prompt : str, stop: Optional[List[str]] = None,
                run_manager: Optional[CallbackManagerForLLMRun] = None,
                **kwargs: Any):

        # 如果 access_token 为空，初始化 access_token
        if self.access_token == None:
            self.init_access_token()

        # API 调用 url
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={}".format(self.access_token)

        # 配置 POST 参数
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",# user prompt
                    "content": "{}".format(prompt)# 输入的 prompt
                }
            ],
            'temperature' : self.temperature
        })

        # 设置请求头
        headers = {
            'Content-Type': 'application/json'
        }

        # 发起请求
        response = requests.request("POST", url, headers=headers, data=payload, timeout=self.request_timeout)

        # 处理响应
        if response.status_code == 200:
            # 返回的是一个 Json 字符串
            js = json.loads(response.text)
            return js["result"]
        else:
            return "请求失败"

   # " '@property'是一个Python中的装饰器（decorator），它用于将一个方法转换为一个只读属性。" \
   # "当你使用 @ property装饰器时，你可以像访问属性一样访问这个方法，而不是调用它。"
    # 首先定义一个返回默认参数的方法
    @property
    def _default_params(self) -> Dict[str, Any]:
        """获取调用Ennie API的默认参数。"""
        normal_params = {
            "temperature": self.temperature,
            "request_timeout": self.request_timeout,
            }
        # print(type(self.model_kwargs))
        return {**normal_params}

    @property
    def _llm_type(self) -> str:
        return "Wenxin"

    @property
    # _identifying_params方法，用于打印LLM信息
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {**{"model_name": self.model_name}, **self._default_params}
