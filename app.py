from ui import *

from transtext import *
import pyperclip
import time
import pyautogui as pag


def main():
    pt = ProcessText()  # 处理文本

    # 定位到被提到的位置
    ml = CardLocation(config=CardConfig(template_file="images/image_01_mention.png", bias_type=BiasType.NoBias))
    # 定位到被艾特的位置
    ut = CardLocation(config=CardConfig(template_file="images/image_02_usertextv2.png", bias_type=BiasType.CenterBias))
    # 在被艾特的那个位置，右键，点击复制按钮
    cb = CardLocation(config=CardConfig(template_file="images/image_03_copy.png", bias_type=BiasType.NoBias))
    # 去消息回复框位置
    it = CardLocation(config=CardConfig(template_file="images/image_04_input.png", bias_type=BiasType.HeightBias))
    # 点击发送按钮
    seb = CardLocation(config=CardConfig(template_file="images/image_05_send.png", bias_type=BiasType.NoBias))

    limit_n = 3600  # 设置循环的上次次数
    times = 0
    sec_value = 1  # 每隔1秒，就去扫描是否被提到，如果被提到就逐步进行下面步骤

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

                    # 点击复制按钮
                    # 获得复制的文本

                    copy_text_value = pyperclip.paste()
                    clean_text_value = pt.trans(copy_text_value)

                    if clean_text_value.status:
                        pyperclip.copy(clean_text_value.text)
                        # 如何处理的文本没问题，那就继续
                        # 找到发送消息框
                        itv = it.get_location
                        if itv.status:
                            # 移动到发送框，点击
                            pag.moveTo(x=itv.x, y=itv.y)
                            pag.click()  # 激活发送框
                            pag.click(button='right')  # 呼出copy
                            pag.moveTo(x=itv.x + 3, y=itv.y + 3)
                            pag.click()  # 点击copy 按钮

                            # 最后点击发送按钮
                            sebv = seb.get_location
                            if sebv.status:
                                pag.moveTo(x=sebv.x, y=sebv.y)
                                pag.click()
                                print("done ~")

        time.sleep(sec_value)
        times += sec_value
        print(f"times: {times} / {limit_n}")


if __name__ == '__main__':
    main()
