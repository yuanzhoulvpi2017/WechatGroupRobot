from ui import *

from transtext import *
import pyperclip
import time
import pyautogui as pag
from tqdm import tqdm


def main():
    pt = ProcessText()  # 处理文本

    # 如果想要使用chatgpt
    # pt = ProcessTextChatGpt()

    mulitg = CardLocation(config=CardConfig(template_file="images/image_06_groupat.png", bias_type=BiasType.NoBias))

    # 定位到被提到的位置
    ml = CardLocation(config=CardConfig(template_file="images/image_01_mention.png", bias_type=BiasType.NoBias))
    # 定位到被艾特的位置
    ut = CardLocation(config=CardConfig(template_file="images/image_02_usertextv2.png", bias_type=BiasType.CenterBias))
    # 在被艾特的那个位置，右键，点击复制按钮
    cb = CardLocation(config=CardConfig(template_file="images/image_03_copy.png", bias_type=BiasType.NoBias))
    # 去消息回复框位置
    it = CardLocation(config=CardConfig(template_file="images/image_04_inputv2.png", bias_type=BiasType.HeightBias))
    # 点击发送按钮
    seb = CardLocation(config=CardConfig(template_file="images/image_05_send.png", bias_type=BiasType.NoBias))

    limit_n = 3600 * 8  # 设置循环的上次次数
    times = 0
    sec_value = 1  # 每隔1秒，就去扫描是否被提到，如果被提到就逐步进行下面步骤
    pbar = tqdm(total=limit_n, desc="--->")
    while True:
        if times > limit_n:
            break

        # 01 检查是否被提到
        mlv = ml.get_location
        if mlv.status:
            # 如果被提到
            # 移动到被提到的位置
            # 点击被提到
            # 休息0.5s
            pag.moveTo(x=mlv.x, y=mlv.y)
            pag.click()

            time.sleep(0.5)
            # 开始截图，以获得用户输入位置

            utv = ut.get_location
            if utv.status:
                # 如果找到用户输入的位置
                pag.moveTo(x=utv.x, y=utv.y)
                pag.click(button='right')

                # 找到复制按钮
                cbv = cb.get_location
                if cbv.status:
                    pag.moveTo(x=cbv.x, y=cbv.y)
                    pag.click()
                    # 这里其实已经复制好了。
                    copy_text_value = pyperclip.paste()

                    # 然后移动到头像中间，并且右键点击艾特
                    back_x_value, back_y_value = 60, 30
                    ## 这里是将鼠标移动到头像位置
                    pag.moveTo(x=cbv.x - back_x_value, y=cbv.y - back_y_value)
                    ## 在头像上，右键呼出艾特人选项
                    pag.click(button='right')
                    ## 呼出艾特人选项之后
                    pag.moveTo(x=cbv.x - back_x_value + 2, y=cbv.y - back_y_value + 2)
                    ## 点击艾特人的那个选项
                    pag.click()
                    # # pag.moveTo(x=cbv.x+200, y=cbv.y+200)

                    # 这里是开始处理文本
                    clean_text_value = pt.trans(copy_text_value)
                    # print(clean_text_value)

                    if clean_text_value.status:
                        # 将处理好的文本，放到window系统的剪切板里面。
                        pyperclip.copy(clean_text_value.text)

                        # 如果上方的pt.trans处理时间很短，就会遮盖住下面的模板，无法匹配内容（会导致找不到发消息的框），因此这里需要休息0.4秒
                        time.sleep(0.4)
                        # 如何处理的文本没问题，那就继续
                        # 找到发送消息框
                        itv = it.get_location
                        # print(itv.status)
                        if itv.status:
                            # 移动到发送框，点击
                            at_other_x, at_other_y = 400, 0 # 这里位置上做了偏移
                            pag.moveTo(x=itv.x, y=itv.y)
                            ## 因为被艾特之后，发送框里面会有被艾特的人的姓名，如果这个人的姓名太长的话，无法在文本输入框里面输入内容。
                            pag.moveTo(x=itv.x + at_other_x, y=itv.y + at_other_y)
                            pag.click()  # 激活发送框
                            # time.sleep(0.3)

                            pag.click(button='right')  # 呼出copy
                            pag.moveTo(x=itv.x + at_other_x + 3, y=itv.y + at_other_y + 3)
                            pag.click()  # 点击copy 按钮

                            # 最后点击发送按钮
                            sebv = seb.get_location
                            if sebv.status:
                                pag.moveTo(x=sebv.x, y=sebv.y)
                                pag.click()
                                print("done ~")

        else:
            multigv = mulitg.get_location
            if multigv.status:
                pag.moveTo(x=multigv.x, y=multigv.y)
                pag.click()

        time.sleep(sec_value)
        pbar.update(1)
        # times += sec_value
        # print(f"times: {times} / {limit_n}")


if __name__ == '__main__':
    main()
