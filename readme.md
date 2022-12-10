### 背景

1. chatgpt是一个有趣的、聪明的AI机器人。
2. 很多人希望可以把这个机器人接入微信群聊里面。

## 介绍
本项目，使用python制作了一个微信群聊机器人。
1. 微信群聊机器人
2. 群聊里面，被艾特后，会基于被艾特的内容，发送对应的文本。
3. 可以使用chatgpt。
4. 也可自己定义机器人回复内容（比如自己写对话机器人）
5. 和微信通信，主要是模拟点击事件，而不是通过网页版微信（现在很多网页版微信都是无法登录的）。

## 功能展示
**B站视频链接：[https://www.bilibili.com/video/BV1i8411G7xC](https://www.bilibili.com/video/BV1i8411G7xC)**
1. 微信群聊里面，有人艾特机器人（这里的机器人名称叫小埋)。
2. 文本结构是：`@机器人名称 + 问题`。
3. 机器人会处理此文本，并且返回答案。

![](https://files.mdnice.com/user/7098/2afb7c41-16c7-4b6f-83cd-3e559ac3a124.png)


## 技术逻辑

### 交互逻辑
1. 机器人之所以可以检测是否被`提及到`。移动到被艾特的位置，复制文本，点击发送按钮等。
2. 都是使用cv里面的图像模板匹配。
3. 也就是需要预先对微信群聊的对话框做特征点标记。
4. 而所谓的标记，就是需要我们先做好模板（也就是把一些特征点，截图，保存）

### 获取文本并处理逻辑
1. 在定位到被艾特的位置后，会自动点击复制按钮，然后复制这段话。（这个时候是已经将文本放入window系统的剪切板）
2. 然后使用python的特定的包，提取window系统剪切板的文本。
3. 经过后端的机器人接口，对文本做处理。
4. 然后再放入window系统剪切板里面。
5. 到文本输入框里面，粘贴文本。
6. 最后点击发送。

## 程序的完整正向逻辑
### 1. 检测是否被@
如果被检测到，就继续

![](https://files.mdnice.com/user/7098/029f86b5-98d3-47b0-9594-d2ac08e97708.png)

### 2. 找到被@的文本位置
点击上图的红圈位置会定位到，在经过0.5秒后，对应的信息会被加深（有个深色条）。

就像是下图的红圈1和红圈2的区别。而红圈1就是我们刚才被艾特的文本。
![](https://files.mdnice.com/user/7098/2b8e4f96-9847-43f5-804c-d54a1bcb8236.png)

### 3. 鼠标点击复制
鼠标在定位到上图的绿圈之后，

点击右键，找到复制按钮，点击复制
![](https://files.mdnice.com/user/7098/48c240ec-13d7-41fa-81db-098208b0f7c5.png)


### 4. 处理文本

复制后的文本，会被从剪切板传递到python里面，然后python调用机器人接口，得到新内容，将新内容再次传递到剪切板

![](https://files.mdnice.com/user/7098/7815a87f-49bc-4024-b1ea-316e791b9bfa.png)

### 5. 定位聊天对话框
依靠下图的绿框的一排图标，可以定位到文本输入框的位置。

鼠标移到这个地方。

![](https://files.mdnice.com/user/7098/57c0517b-d064-40c1-9704-fa55beb6c9c7.png)



### 6. 粘贴内容

鼠标右键粘贴内容

![](https://files.mdnice.com/user/7098/73750523-28dd-486e-839d-0d8c0f3d2ec4.png)

### 7. 点击发送按钮

粘贴好之后，就是点击发送即可。


![](https://files.mdnice.com/user/7098/ffd130db-4ec1-4e88-85b3-45a9d27379a6.png)





# 如何使用
## 机器人名称

注意我这里叫【小埋】，你的可以改为你自己的，这个不是难点。

## 截图

使用这部分是最麻烦的，因为每个人的电脑分辨率不同，导致截图都是没办法复用的，因此你只能在你的电脑上，把下面截图都给再截图一遍。

![](https://files.mdnice.com/user/7098/8b56680d-ac88-42b2-adb9-1adf3ffb6841.png)

### 1. image_01_mention.png

这个是被提到的图片，你需要截图，内容上，最好和我截图一样。

### 2. image_02_usertextv2.png

这个截图很有技巧。因为在点击【被提到后】，需要等待那个消息框周围变深，然后才能截图。

因此建议，使用pyautogui辅助截图。

就是要把这个绿框截图给准确的截下来（当然你的机器人名称不叫小埋）
![](https://files.mdnice.com/user/7098/2b8e4f96-9847-43f5-804c-d54a1bcb8236.png)

截图成功最终的样子就是`images/image_02_usertextv2.png`。

注意这里是V2版本的奥，后面有V2！！！

### 3. image_03_copy.png

这个不难，就是鼠标放在被艾特的文本上的时候，右键，出现【复制】,然后这个时候截图。

### 4. image_04_input.png

这个也是不难，就是直接截图

### 5. image_05_send.png

这个就是右下角的【发送】按钮

## 安装依赖

```bash
pip install pyautogui
pip install pyperclip

# https://github.com/acheong08/ChatGPT
pip install revChatGPT --upgrade 
```
## 程序
上面基本上就ok了。最后直接运行`app.py`文件就行了。

1. 默认是简单回复模板。
2. 如果想要使用chatgpt模板，前提，你可以正常使用chatgpt,请最好先阅读[https://github.com/acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 包，整体上用这个包来处理chatgpt通信问题。
![](https://files.mdnice.com/user/7098/28f06163-a9cb-4be9-9416-9ab24544f0e9.png)


