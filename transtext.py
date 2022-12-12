from datetime import datetime

from dataclasses import dataclass
from revChatGPT.revChatGPT import Chatbot
import csv


def append_question2file(question: str) -> None:
    row = {'question': question,
           'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    with open(file="data/user_question.csv", mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerow(row)


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

        append_question2file(question=res)
        if len(res) > 0:

            try:
                notiy = "We're experiencing exceptionally high demand. Please hang tight as we work on scaling our systems."

                res = f"\n[input]: {res}\n[time]: {datetime.now().strftime('%m-%d %H:%M:%S')}\n[question]：{res}\n[result]:{notiy}"

                return ProcessTextOutput(
                    status=True,
                    text=res
                )
            except Exception as e:
                print("error 1")

                return ProcessTextOutput(
                    status=True,
                    text='\nsorry 我出错了~'
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
            "session_token":"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..TmvKhMBQM3GZCNR0.JA-B7qXeiAwA-gTWYr-SCpfIRQOqzEqYscYowKyizhj-7lEs0L5lur30k8l_JLgCqJgN8jggWh4mPZsT8Jj5o3P_rmYoY4CPts1bCgbZ3e0r0LaL1_IPqC4rjlZFvhz6K7ZiogqDz3OpdH5DrvH0n42x0wJxAbiRoCV-8xyeFqXZ1zyODn7JSZQc47ae_dzBx4wXIOEjJvgG3zG_U2cCCE6H-fI7NyGRA9IaRt-20iw1ve1QmVOWkgKPpz7NgdredDa0F0zlgO88wFZt-CzPZo0HmaczEGzZocwYmcdaEBET6maFTKwzsjBHkyHYz2suerpjOozAhcgPwlzO0P9Mt4KghfcBIhwyATIl8onpE7t_jGznKRWLrLyTPzJVXlKtjcv97-1guItdfxnGcDlGs7emsqofTzWPdZQTWmjvcjaWIFTpLLygPSY1qMXaMYBQlul9Cd0k9wrYfZ5ifUx3jHZfrwGToCy56AsnbdKT20ic4CO8NMQXL31-asBN_Y1EoTBZoz7511_sqfaEbjQNfmjZGRc21_F3BFas6w0MGghCajh_if5U3lderCb9ulRrFu9YHSCBcE2xMaDolY7nsQAdGQabOqBcQD0nhYMJw1RqS3YcNVCc79o5-CLRTLixNkJXGFHuWfVvdwH8u1EWdAmDnffiQMX0bP2j8JmXU2DtPzxxKzRjE1axGsRUHEVhiFi3PoO2PZjxFPg_RAZXvJ5E-pFMr1090Pjxe-br8_odI5lzUykqHcdwZub5sNpSoya1GkNhFVw67HQ4onRQoJ45Tup3gk80pWziSczmEY2HzeSxMY2LdjFzCglaUxcRFl4bPDmqms-2YTS5qaVGwEHlpXfwSQE0SCW6llfnYYlewkeG_83AspqwOokpUCqE2kN8EBVARlPEKChKTVA2YNr5Jq3VxVARlSB5BiYkquivMHy3shoDWeCNdKIytJM9nYrsGN3Zyamnr0FLKNrGLld9DzH4VMFOU-BdqK1nosyMVf6UpAglmwFoQgDMlTo_Fjsm_cOyhEMz27uRpd_tJ8AbjgnvwLkI6qN1iCYeqiJR0Fcy1df2BExxYpeSFICFNrKY7T5M_bXuejx1yGuTbwVZZOszWCqTTTAf6TcnIWs4NFiaRMESHwyF0aDtoGTDdxV7bGJ-GkjB2W-8HboA0VepC-6wuwoznet430_2doWVlrbHIoRYFFqpSL2L3T-rwatEASCzKN5jgxubEGayFmjYXa-8NI57-ddOeIYizrgxH0zkpp2AfxALYNTjvZJMowVhDaIBhT_-WlS53VUI2J25hoceUhtQZ_5BQycnsdpmx2LcTKNA1f0kB7I-uya_jfpyRe3jVaNX3txA8R0EaVVesvx3B2gM8jy_ph4yikk3X7it4eNUbozsQ4xNW3YtDBtGIS5R2aMXo0oQUh2sTNRBzYkEICoaWvUVCgDLjdsC6PkplRaT8DGXWsKyP6e_Moz0pKPwHCw0UKCqkQQ1X_cNntiDBRaP7_O13UkYD2RbrwrRCuYjeuf2dRYy4sAxKvv6SHdGojSO-q3sBWLLYGNoNuVTb9YgzZYZoxvokOsi1CGmsVkEc-cb-tjWf70_-ibkdbezhs6sRfrjM6bv23y-HaeEsmGt2rGzqR3xxDPFslQCRC97mw86VqcD3mx-1uutqAXvC-JYldXLP-4BCNVQB_7h9HsSeG_FUG4Mg3MD_JR6qUmSHP8rWbyph_33myqZtM27qfK8p35HBClvM89m9F5ydjG8pg2o-tIaQJFVQiBbne8BDMjgw-LohY7KBOazracwVxzDsICsFH0UHW6lZAFj1-bNBcWfCLxgZX7qNa2FTw6PeFUnw94S22yoPyXEVhUlF3rbaZv_NFw_KdC-_AceL10dZQud4QphQhsvlvtt_BdgamKncuKcgsIkfJdjsXILFxn732OdTnZpepvLiqvf58-PTdAOHu_JKqEh4VmcyO1sjS2uSbSzNLkVuwPya_MxbwLVhQWpbShxfEgTy4s6qyDV98Ev8TxTP1WHolhKu7BRXRiUBMZRjCIGKe0qG_zeuRMsX6s-ZNrzCwxe2ozKL0mYrVEso5BSfMpqf07H4-6EnGBFVmFHepvE1t67keYJIiWTip_V4rgs0V8R16a9mqMys95sWEyZmskZuOizqj4UXNw1g1XCtAP4AcXitLJkDb1Bnm4rsbp7Bl8SvO6PWJ5CVdr0mAdU5SbYzFukofE9XS9JZzFrdylvmOqrNtOTaCOMLTZ37o2qFu_NZNGDuNDWoGMdb1oSkegnotxiPtwfnfZX46pUH8DZzGGT6cUi6odwty8IK3NKxWgTj0TA0RLfEwVzwKnGcWB2lLQSZ28k6ZpL7fIqVDWA8WerbzvOJHz8ULbFjw.ETDCtnsgjMrYqNr9xv2kpw"
            # "session_token":

        }
        self.chatbot = Chatbot(config, conversation_id=None)

    def trans(self, x: str) -> ProcessTextOutput:
        res = x.replace("@小埋 ", "")
        append_question2file(question=res)

        if len(res) > 0:

            try:
                response = self.chatbot.get_chat_response(res, output="text")

                res = f"\n[input]: {res}\n[datetime]: {datetime.now()}\n[result]: {response.get('message', 'empty')}"

                return ProcessTextOutput(
                    status=True,
                    text=res
                )
            except Exception as e:
                print(e)
                res = f"\n[input]: {res}\n[datetime]: {datetime.now()}\n[result]: sorry~ 我出错了~"

                print("error 1")
                return ProcessTextOutput(
                    status=True,
                    text=res
                )
        else:
            return ProcessTextOutput()


if __name__ == '__main__':
    pt = ProcessTextChatGpt()
    pt.trans("nihao")
