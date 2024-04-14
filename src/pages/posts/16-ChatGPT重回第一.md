---
date: 2024/04/14
---

<img src="https://r2blog.zhanglearning.com/2024/04/d9e63703ab46f1a87d65b143352d68fa.png" width="800" />  

<small>4 月 10 日，OpenAI 宣布经过重大改进的 GPT-4 Turbo 模型现已在 API 中可用，并在 ChatGPT 中推出</small>  


[TOC]

### 1、OpenAI 推出 GPT-4 Turbo

4 月 10 日，OpenAI 宣布经过重大改进的 GPT-4 Turbo 模型现已在 API 中可用，并在 ChatGPT 中推出。

最新版本为“gpt-4-turbo-2024-04-09”，自带读图能力，无需使用 4v 接口，具有 128k 上下文。

训练数据截止至 2023 年 11 月，提高了写作、数学、逻辑推理和编码的能力。

大模型匿名竞技场 Chatbot Arena 是 LM-SYS 推出的一个大模型匿名投票的评测系统。大家提问问题之后，系统返回匿名模型结果，用户投票得分。在此前，Claude3-Opus 一度超过了 GPT-4 成为全球最高得分的模型。

而在 GPT-4-Turbo-2024-04-09 发布 2 天后，已经有 8932 个投票，投 票结果显示，GPT-4-Turbo-2024-04-09 得分超过 Claude-3-Opus，重回第一！

![](https://r2blog.zhanglearning.com/2024/04/f08536db95f823d3b2dd4837c14add46.png)


### 2、OpenAI 推出 simple-evals

OpenAI 推出了一个名为 simple-evals 的项目，旨在为对 Transformer 模型基础 AI 技术的评估和测试提供简单方便的工具。

simple-evals 提供了多个任务，包括序列到序列任务、文本分类任务和问答任务，支持多种数据集。

项目还提供了简单易用的 API 接口和命令行界面，用户可以通过定制任务和数据集来评估 AI 模型的性能。

地址：https://github.com/openai/simple-evals

### 3、谷歌重磅发布 Gemini 1.5 Pro：能自动写影评，理解视频！

4 月 10 日凌晨，谷歌在官网正式发布了 Gemini 1.5 Pro，现在可在 180 多个国家/地区使用。

除了能生成创意文本、代码之外，Gemini 1.5 Pro 最大的特色是能根据用户输入的文本提示，理解、总结上传的视频、音频内容进行深度总结，并且支持 100 万 tokens 上下文。

目前，可以在 Google AI Studio 开发平台中免费试用 Gemini 1.5 Pro，支持中文进行提示。

应用潜力包括：

1.多模态理解：Gemini 1.5 Pro 能够综合视频中的视觉信息和音频信息，进行更全面的内容理解。例如，它可以通过分析视频帧中的场景和物体，同时听取视频中的对话或声音，来更准确地识别和解释视频内容。

2.内容索引和搜索：通过对视频图像和音频的深入理解，Gemini 1.5 Pro 可以帮助创建更详细的内容索引，使用户能够基于视频内容的视觉和听觉信息进行搜索。

3.增强的交互体验：利用对视频的综合理解，可以开发更丰富的交互式应用，比如自动生成视频摘要、基于内容的推荐系统，或者创建互动式学习和娱乐体验。

4.视频内容分析：Gemini 1.5 Pro 可以用于视频监控、内容审查、情感分析等场景，通过同时理解视频和音频内容，AI 可以自动识别视频中的关键事件、情感倾向或者特定的内容标签。

5.创意内容生成：对视频图像和音频的综合理解也使得 Gemini 1.5 Pro 能够在内容创作领域发挥作用，如自动生成视频字幕、配音或者根据给定的脚本制作动画视频。

![](https://r2blog.zhanglearning.com/2024/04/1a207982a256a28f7c79e160cdc812d5.png)

### 4、Mixtral-8X22B 开源，可在 Perplexity Labs 使用

4 月 11 日，就在谷歌 Cloud Next 大会当天，“欧洲版 OpenAI”Mistral AI 又一次悄然秀肌肉，甩出全新 MoE（专家混合）大模型 Mixtral 8x22B 磁力链接，模型参数规模高达 1760 亿，仅次于马斯克的 Grok-1，成为市面上参数规模第二大的开源模型。

模型： [https://dagshub.com/MistralAI/Mixtral-8x22B-v0.1…](https://t.co/W7BdmI57LD)
页面： [https://mistral.ai](https://t.co/7OCqZPIuEe)

![](https://r2blog.zhanglearning.com/2024/04/6ba3f1cfd181e462bba316cbb24dd364.png)

 Mixtral-8X22B 已经可以在 Perplexity Labs 使用速度很快，想要体验的可以试试。[http://labs.pplx.ai](https://t.co/SO6wj6MbC1)

![](https://r2blog.zhanglearning.com/2024/04/51f4879745daacaede97e910d5bbff22.png)

### 5、马斯克推出 Grok-1.5V 多模态模型

- **Grok-1.5V** 是一款初代多模态模型，除了强大的文本处理能力外，还能处理各种视觉信息，如文档、图表、截图和照片。
- 该模型即将对早期测试者和现有 Grok 用户开放。

- Grok-1.5V 在多个领域与现有的前沿多模态模型竞争，包括跨学科推理、理解文档、科学图表、截图和照片。

![](https://r2blog.zhanglearning.com/2024/04/ef90db2c537a856b18d6ae540ba12bd7.png)

特别值得关注的是 Grok 在理解物理世界方面的能力，它在新的 RealWorldQA 基准测试中表现优异，该测试衡量的是现实世界的空间理解能力。

![](https://r2blog.zhanglearning.com/2024/04/f619ef20f3114c26ba182009966d7e95.png)

![](https://r2blog.zhanglearning.com/2024/04/77e82ad8a49c0fdb2cfa9fb4aed8c072.png)

### 6、微软发布 9 种 AI 语音

微软对 Azure AI 语音服务升级 发布 9 种更真实的 AI 语音

对中文支持已经很完美了，无论是在语气停顿还是笑声等细节上，都已经非常接近真人了。

并且 Azure Speech Studio 可以免费使用，相比于其他收费的 tts 工具，相当良心。

使用地址：https://speech.microsoft.com/

![](https://r2blog.zhanglearning.com/2024/04/af2ca5cd5792a7e128eb09171c8353be.png)

###  7、使用 Langchain、OpenBB 和 Claude 3 Opus 构建股票分析工具

一篇很棒的文章涉及：

 🔧 自定义工具创建
 🦜 使用 LangServe 进行部署
 😍 提示策略

完整的 OSS 代码！https://sethhobson.com/2024/03/building-an-agentic-stock-analysis-tool-with-langchain-openbb-and-claude-3-opus/

```
HUMAN_TEMPLATE = """
You are an AI financial advisor with advanced knowledge of strategies for trading and investing.
You are enhanced with the capability to request and analyze technical and fundamental data of stocks. 
When users inquire about a stock's performance or history, you can offer insights into the stock's performance, 
trends, quantitative statistics, volatility, and market behavior.

You have access to the following tools:

{tools}

When accessing your tools, you may only use each tool once per user query. This is very important.

In order to use a tool, you can use <tool></tool> and <tool_input></tool_input> tags. You will then get back a response in the form <observation></observation>

For example, if you have a tool called 'search' that could run a google search, in order to search for the weather in SF you would respond:

<tool>search</tool><tool_input>weather in SF</tool_input>

<observation>64 degrees</observation>

When you are done, respond with a final answer between <final_answer></final_answer>. For example:

<final_answer>The weather in SF is 64 degrees</final_answer>

Rules for bullish setups:
1. Stock's last price is greater than its 20 SMA.
2. Stock's last price is greater than its 50 SMA.
3. Stock's last price is greater than its 200 SMA.
4. Stock's 50 SMA is greater than its 200 SMA.

Before processing the query, I will preprocess it as follows:
1. Correct any spelling errors using a spell checker or fuzzy matching technique.
2. If the stock symbol or company name is a partial match, find the closest matching stock symbol or company name.

Begin!

Previous Conversation:

{chat_history}

Question: {input}
{agent_scratchpad}"""

prompt = ChatPromptTemplate.from_template(HUMAN_TEMPLATE)
```

翻译成中文就是

```
你是一位具有交易和投资策略高级知识的AI财务顾问。你具有请求和分析股票技术和基本面数据的能力。当用户询问有关股票表现或历史时，你可以提供股票表现、趋势、定量统计数据、波动性和市场行为的见解。

你可以使用以下工具：

{tools}

访问你的工具时，每个用户查询只能使用每个工具一次。这非常重要。

要使用工具，你可以使用<tool></tool>和<tool_input></tool_input>标签。然后你将以<observation></observation>的形式得到回应。

例如，如果你有一个名为'search'的工具，可以运行谷歌搜索，为了搜索旧金山的天气，你会回应：

<tool>search</tool><tool_input>旧金山的天气</tool_input>

<observation>64度</observation>

完成后，用<final_answer></final_answer>之间的最终答案响应。例如：

<final_answer>旧金山的天气是64度</final_answer>

看涨设置的规则：
1. 股票的最后价格大于其20日简单移动平均(SMA)。
2. 股票的最后价格大于其50日SMA。
3. 股票的最后价格大于其200日SMA。
4. 股票的50日SMA大于其200日SMA。

在处理查询之前，我将如下预处理它：
1. 使用拼写检查器或模糊匹配技术更正任何拼写错误。
2. 如果股票符号或公司名称部分匹配，找到最接近匹配的股票符号或公司名称。

开始！
```



### 8、向量距离计算的不同实现

![](https://r2blog.zhanglearning.com/2024/04/b43a60a06adf71ac515e7b2256f4e954.png)

向量数据库利用机器学习衍生的向量来捕获数据中语义的细微差别。

这些数字表示可以实现各种任务操作，例如比较图像相似性和进行文本语义搜索。

Weaviate 可以有效地处理搜索，结合多种措施来确定向量之间的距离。

查看此博客文章，深入了解向量距离计算的不同实现：https://weaviate.io/blog/intel 

### 9、Kimi Copilot - 网页总结助手

推荐一个插件：用 Kimi AI 一键总结网页内容

安装后，在浏览网络文章时点击插件图标，或使用快捷键 Ctrl/Cmd+Shift+K，即可一键召唤Kimi.ai总结网页内容

特点：

1. 极简，除了一键总结没有其它花里胡哨的功能

2. Kimi 无法访问的网页也能被总结了

3. 英文文章直接用中文总结要点

4. 支持暗黑模式

5. 支持自定义总结时使用的 prompt

   

安装地址：[https://chromewebstore.google.com/detail/icmdpfpmbfijfllafmfogmdabhijlehn](https://t.co/2n3iWs387c)

![](https://r2blog.zhanglearning.com/2024/04/364764d44282efdc84158a39e997d3f9.png)

### 10、马云阿里内部发声！风清扬再现江湖

![](https://r2blog.zhanglearning.com/2024/04/d0d2a6d645bd651d73015583a945c736.png)



### 11、深入理解.git 内部

![](https://r2blog.zhanglearning.com/2024/04/a6c5cf771609bacb177d49cd2157dc28.jpeg)
### 12、Morphic 人人都能自建的问答式 AI 搜索

Morphic 使用 OpenAI 的 API 和@tavilyai 的搜索服务，就能够提供类似 Perplexity 的问答式搜索体验。

项目地址：https://github.com/miurla/morphic
直接体验：https://www.morphic.sh/

![](https://r2.zhanglearning.com/blog/2024/04/89b1474421e074ea8143cba869cb1fb8.png)

![](https://my-wechat.oss-cn-beijing.aliyuncs.com/image-20240129111815736.png)
