from datetime import datetime

from dataclasses import dataclass
from revChatGPT.revChatGPT import Chatbot


@dataclass
class ProcessTextOutput:
    status: bool = False
    text: str = None
class ProcessText:
    """默认回复消息模板
    1. 基于此模板 可以检查整个流程是否跑通
    2. 基于此模板 可以自定义自己的后端搜索方式（比如自己写文本搜索，自己实现机器人等）

    注意事项：
    1. 因为我的机器人叫小埋，用户在被艾特的时候，会包含你机器的名字，建议在处理文本的时候，抹掉机器人名称和@符号
    """

    def __init__(self) -> None:
        pass

    def trans(self, x: str) -> ProcessTextOutput:
        res = x.replace("@小埋 ", "")
        if len(res) > 0:

            try:

                res = f"[input]: {res}\n[datetime]: {datetime.now()}\n[result]: {res}"

                return ProcessTextOutput(
                    status=True,
                    text=res
                )
            except Exception as e:
                print("error 1")
                return ProcessTextOutput(
                    status=True,
                    text='error le'
                )
        else:
            return ProcessTextOutput()


class ProcessTextChatGpt:
    """
    这里提供了OpenAi的chatGpt模板
    只需要将config的session_token参数修改即可。

    注意事项：
    1. 因为我的机器人叫小埋，用户在被艾特的时候，会包含你机器的名字，建议在处理文本的时候，抹掉机器人名称和@符号

    """
    def __init__(self) -> None:
        config = {
            "session_token": "hello"
        }
        self.chatbot = Chatbot(config, conversation_id=None)

    def trans(self, x: str) -> ProcessTextOutput:
        res = x.replace("@小埋 ", "")
        if len(res) > 0:

            try:
                response = self.chatbot.get_chat_response(res, output="text")

                res = f"[input]: {res}\n[datetime]: {datetime.now()}\n[result]: {response.get('message', 'empty')}"

                return ProcessTextOutput(
                    status=True,
                    text=res
                )
            except Exception as e:
                print("error 1")
                return ProcessTextOutput(
                    status=True,
                    text='error le'
                )
        else:
            return ProcessTextOutput()
