---
date: 2024/06/02
---

<img src="https://r2blog.zhanglearning.com/2024/06/ccaf952193ffbd04a4cebc77e342f041.png" width="800" />

<small>OpenAI 推出了 GPT-4o 模型，并将 GPTs 等高级工具免费提供给 ChatGPT 用户。</small>



Ai周刊：关注 Python、机器学习、深度学习、大模型等硬核技术

本期目录：

**大模型**
- huggingchat 新功能
- 腾讯推出“腾讯元宝”以及“腾讯元器”
- Mistral AI 发布了精通 80 多种编程语言的模型 Codestral
- 谷歌推出 Gemini 1.5 Pro 和 1.5 Flash

**工具库**
- ChatTTS：专门为对话场景设计的文本到语音 TTS 模型
- ChatGPT iOS App UI - Free Figma Template
- AI 开源搜索引擎：Perplexity-Inspired LLM Answer Engine

**知识库**
- 39 万 star 🌟的开源仓库学习编程
- 基于 llm.c 复现了 124M 参数的 GPT-4

**轻阅读**
- Today’s AI Isn’t Sentient
- 去年 OpenAI 董事会开除 Sam Altman 的内幕
- 长视频：我为什么从特斯拉辞职
- 从一年构建大型语言模型中学到的东西
- GPT 未来将是美国大学的标配


## 大模型

### [huggingchat 新功能](https://huggingface.co/chat/ "huggingchat 新功能")

huggingchat 现在支持工具调用了，目前共 6 个工具：
· web search 网页搜索：查询网络并在检索到的内容上执行与用户查询相关的 rag
· url fetcher url 获取器：从给定的 url 获取文本内容
· document parser 文档解析器：解析 pdf、文本、csv、json 等格式的内容
· image generation 图像生成：根据给定的文本提示生成图像
· image editing 图像编辑：根据给定的文本提示编辑图像
· calculator 计算器：一个简单的计算器，用于评估数学表达式

![](https://r2blog.zhanglearning.com/2024/06/0c3f26d060e43fc461c151f3382cb6e8.png)


### 腾讯推出“腾讯元宝”以及“腾讯元器”

![](https://r2blog.zhanglearning.com/2024/06/230e748485abaa8e38f7818d38cea447.png)


元器是制作元宝智能体的工具。

元器：https://yuanqi.tencent.com

元宝：https://yuanbao.tencent.com

### [Mistral AI 发布了精通 80 多种编程语言的模型 Codestral](https://huggingface.co/mistralai/Codestral-22B-v0.1 "Mistral AI 发布了精通 80 多种编程语言的模型Codestral")

- 模型大小为 22B
- 上下文长度为 32K
- 模型无法商用
- 在 RepoBench、Spider、FIM 基础测试上表现都很好

![](https://r2blog.zhanglearning.com/2024/06/8dfad7107461e6ffb14f944dc841985c.png)

### 谷歌推出 Gemini 1.5 Pro 和 1.5 Flash

提供更高的请求限制，并支持自定义模型调整。Gemini 1.5 Flash 针对高容量任务优化，现已提升到每分钟 1000 个请求且取消每日请求限制。还引入了 JSON schema 模式、移动端支持和 Google AI Studio 的浅色模式。

- Gemini 1.5 Flash and 1.5 Pro stable release and billing

- Higher rate limits on Gemini 1.5 Flash

- Gemini 1.5 Flash tuning

- JSON schema mode

- Mobile support and light mode in Google AI Studio
![](https://r2blog.zhanglearning.com/2024/06/048a6c58e7973adc9f21cc42e385f2fb.png)

## 工具库

### [ChatTTS：专门为对话场景设计的文本到语音 TTS 模型](https://github.com/2noise/ChatTTS "ChatTTS：专门为对话场景设计的文本到语音TTS模型")

该模型经过超过 10 万小时的训练，公开版本在 HuggingFace 上提供了一个 4 万小时预训练的模型。

专为对话任务优化，能够支持多种说话人语音，中英文混合等。

模型还能够预测和控制细粒度的韵律特征，如笑声、停顿和插话等，还能进行更细粒度的调整，如语速、音调和情感等。

ChatTTS 官网上线了，直接可以在线体验了

传送门：http://ChatTTS.com

另外还有人做了一个 ChatTTS Web UI，自己可以部署

ChatTTS Web UI: https://github.com/jianchang512/ChatTTS-ui

### [ChatGPT iOS App UI - Free Figma Template](https://www.figma.com/community/file/1377140124614731195/chatgpt-ios-app-ui-free-figma-template "ChatGPT iOS App UI - Free Figma Template")

### [AI 开源搜索引擎：Perplexity-Inspired LLM Answer Engine ](https://github.com/developersdigest/llm-answer-engine "AI 开源搜索引擎：Perplexity-Inspired LLM Answer Engine ")

受 Perplexity 启发的 LLM 搜索引擎开源项目，使用到的主要 API 包括：
- LLM API:  Groq, Mixtral
- Embeddings:  OpenAI Embeddings
- LLM 框架：Langchain.JS
- 搜索服务：Brave Search, Serper API

关于搜索服务：
· Brave Search：一个主动隐私安全的浏览服务，用于数据搜索和溯源
https://search.brave.com
· Serper API：Google Search API，用于视频和图像的搜索
https://serper.dev


## 知识库
### [39 万 star🌟的开源仓库学习编程](https://github.com/freeCodeCamp/freeCodeCamp "39万star🌟的开源仓库学习编程")

FreeCodeCamp 是一个非盈利社区，提供了一个开源的编程学习平台，帮助用户免费学习编程。

FFC 很适合自学编程的人，你可以在这里学习包括网页设计、JavaScript、前端库、数据可视化、后端开发等多个认证课程。


### [基于 llm.c 复现了 124M 参数的 GPT-4](https://github.com/karpathy/llm.c/discussions/481 "基于 llm.c 复现了 124M 参数的 GPT-4")

仅需 20 美刀💰和 90 分钟，前 OpenAI 创始成员
@karpathy 基于 llm.c 复现了 124M 参数的 GPT-4，并公布了如何在 A100 上从零开始复现运行的全部细节🥳👍


### [苹果公布了 2024 年“苹果设计大奖”入围作品](https://developer.apple.com/design/awards/ "苹果公布了 2024 年“苹果设计大奖”入围作品")


![](https://r2blog.zhanglearning.com/2024/06/e0d63752f8591730ddca5461e8cac00f.png)


## 轻阅读

[一位国内的 Python 开发者与一位诺贝尔经济学奖获得者的奇缘 ](https://frostming.com/2024/meet-with-paul/ "一位国内的Python开发者与一位诺贝尔经济学奖获得者的奇缘 ")

作者在 34 岁生日之际收到一封来自 2018 年诺贝尔经济学奖得主的邮件，邀请他见面。邮件中，这位经济学家表达了对作者开发的 Python 项目 PDM 的欣赏，并希望与作者交流 Python 学习和开发经验。作者起初怀疑邮件的真实性，但经过核实后确认了对方的身份。见面之前，经济学家还发了一封长信介绍自己的背景和计划要谈的话题，展现出谦恭的态度，让作者感到敬佩。

见面后，两人就 Python 初学者环境搭建、密钥管理和数字签名工具、Jupyter Notebook 在研究论文中的应用等话题进行了深入交流。经济学家对开源非常支持，并认为 Python 初学者仍然是一个庞大的群体，PEP 582 提案的拒绝令人遗憾。作者邀请经济学家到 PyCon China 做演讲，分享 Python 新手教学经验。

这次见面让作者感到荣幸和鼓舞，这是他第一次靠自己的工作和成就获得外界的认可，也是对他多年来 Python 学习和开发努力的肯定。

[Today’s AI Isn’t Sentient](https://time.com/collection/time100-voices/6980134/ai-llm-not-sentient/ "Today’s AI Isn’t Sentient")


李飞飞近日和 Etchemendy（斯坦福哲学教授，曾任斯坦福大学教务长）在《时代（Time）》上刊载新文章《No, Today’s AI Isn’t Sentient. Here’s How We Know》，明确指出当前技术路线无法制造有感知能力的 AI。

通用智能的一个重要特征是“感知力”，即拥有主观体验的能力——能够感受，比如说，饥饿的感觉，品尝苹果的味道，或者看到红色。感知力是通往通用智能的道路上的关键一步。

大型语言模型（LLM）是一个在硅芯片上编码的数学模型。它不是像人类一样的有形的生物。它没有像人类一样的“生命”，不需要吃喝，繁殖，体验情感，生病，最终死亡。

理解人类生成词语序列和 LLM 生成相同序列之间的本质区别非常重要。当我说“我饿了”时，我是在报告我感知到的生理状态。当一个 LLM 生成“我饿了”这个序列时，它只是在生成当前提示中词语序列最可能的完成方式。它所做的事情与它在不同的提示下生成“我不饿了”或“月亮是由绿奶酪做的”完全一样。这些都不是它（不存在的）生理状态的报告，只是概率上的完成方式。

我们还没有实现有感知的 AI，更大的语言模型也不会让我们实现。如果我们想在 AI 系统中再现这种现象，我们需要更好地理解感知如何在有形的生物系统中出现。我们不会在 ChatGPT 的下一代迭代中偶然发现感知。


[去年 openai 董事会开除 sam altman 的内幕](https://link.chtbl.com/tedai)

去年 openai 董事会开除 sam altman，公告里说：他（sam) 在与董事会的沟通中并不始终坦诚

openai 前独立董事 helen toner 终于打破沉默，公开说明了这句话到底是指什么

这里是短视频，toner 说了几个例子：
https://x.com/bilawalsidhu/status/1795534345345618298


[我为什么从特斯拉辞职](https://www.youtube.com/watch?v=R8Lj48PMYxY "我为什么从特斯拉辞职")

**离职原因：**

- **失去激情：** 在公司工作七年，做着重复性的工作，失去了工作的激情。
- **股票大涨后的心态变化：** 2019 年前入职的员工，经历了特斯拉股票的大涨，心态发生了变化，变得求稳，不再追求升职。
- **两次严重车祸：** 两年内经历了两次严重车祸，虽然没有受伤，但心理受到了很大的冲击，让他重新思考人生的意义。
- **人生目标不是财富最大化：** up 主认为舒适的心理状态、安全边际和寻找幸福才是他现阶段的人生目标。


### [从一年构建大型语言模型中学到的东西](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/ "从一年构建大型语言模型中学到的东西")

文章从操作的角度探讨了构建 LLM 应用的长期战略考虑，并将其分为数据、模型、产品和人员四个部分。

### [GPT 未来将是美国大学的标配]([https://openai.com/index/introducing-chatgpt-edu/](https://t.co/FHZMVTFEqY "GPT未来将是美国大学的标配"))

OpenAI 计划推出了 ChatGPT Edu，这是为大学量身定制的 ChatGPT 版本。它旨在将 AI 负责任地整合到校园中，提供高级功能，如数据分析、编码和文档总结。ChatGPT Edu 包括企业级安全性，支持 50 多种语言，并提供更高的消息限制。此举旨在增强教育和运营框架，使学生、教职员工和研究人员更容易获得 AI 技术。
![](https://r2blog.zhanglearning.com/2024/06/67156851493c92899b566b6940d01fa3.png)
