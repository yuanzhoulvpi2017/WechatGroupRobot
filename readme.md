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
B站视频链接：https://www.bilibili.com/video/BV1i8411G7xC
1. 微信群聊里面，有人艾特机器人（这里的机器人名称叫小埋)。
2. 文本结构是：`@机器人名称 + 问题`
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



