---
date: 2024/05/16
---

<img src="https://r2.zhanglearning.com/blog/2024/05/179e74101af5f06b1f6aa8e32241b51d.png" width="800" />  

<small>https://haitang.app/ 海棠诗社：每一首诗都有简介、注释、翻译、评价</small>  



机器学习周刊：关注 Python、机器学习、深度学习、大模型等硬核技术

本期目录：

[TOC]

## 大模型


### OpenAI 发布了最新大模型 GPT-4o

OpenAI 直接开放 GPT-4o，能力横跨语音、文本和视觉，免费用户也可以直接用！https://chatgpt.com/

在 API 方面，GPT-4o 的价格是 GPT-4-turbo 的一半，速度却是 GPT-4-turbo 的两倍，速率限制也高 5 倍。  

最惊艳的是 OpenAI 在现场的展示，在与 GPT-4o 语音对话过程中，三人随意打断，GPT-4o 反应极快，并且语气相当丰富，像极了在跟人类聊天


### 腾讯开源旗下混元文生图大模型

腾讯正式公布，旗下混元文生图大模型已完成升级，并对外开源。此次升级的模型采用了与 sora 相同的 dit 架构，不仅能够支持文生图，也能作为视频等多模态视觉生成的基础。这是业界首个中文原生的 dit 架构文生图开源模型，支持中英双语输入及理解，15 亿参数。

项目地址：https://dit.hunyuan.tencent.com

官网排队：https://image.hunyuan.tencent.com

github: https://github.com/tencent/hunyuandit

![](https://r2.zhanglearning.com/blog/2024/05/e1a4f1dd16f37df8cdff5049331f9c34.png)

### 直接在浏览器本地运行 Phi-3 模型

试玩：https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu

Phi3-WebGPU 正是为在浏览器端本地运行模型的探索：

🗂️ 模型下载约 2.3GB（下载一次并缓存）
🕒 加载模型时间：50 秒
🚀 推理速度：中文约 1.9 tokens/s，英文1.7 tokens/s
⏳ 首 token 返回延迟：20 秒

### DeepSeek-V2：尖端开源 MoE 模型！

体验：https://chat.deepseek.com/coder
模型下载：https://huggingface.co/deepseek-ai

![](https://r2.zhanglearning.com/blog/2024/05/40e0c0107a43298daf9bc67a5726201e.png)

 🌟 亮点：
> 在 AlignBench 中排名前 3，超过 GPT-4，接近 GPT-4-Turbo。
> 在 MT-Bench 中排名顶级，可与 LLaMA3-70B 相媲美，并优于 Mixtral 8x22B。
> 专攻数学、代码和推理。
> 支持 128K 上下文窗口。

 ✨ 特点：
> 创新架构，236B 中有 21B 活动参数。
> 无与伦比的 API 定价，同时保持真正的开源和无商业性。


![](https://r2.zhanglearning.com/blog/2024/05/caeace2e787d9ea9edef4761d236572f.png)

deepseek 较快的速度 + 不错的质量 + 超便宜的价格，这才是大模型作为新一代的基础设施该有的样子~


官方还开了一个仓库，专门收集集成 deepseek 的应用，大家也可以关注下：
https://github.com/deepseek-ai/awesome-deepseek-integration

### 阿里云发布通义千问 2.5
模型的理解能力、逻辑推理、指令遵循、代码能力分别提升 9%、16%、19%、10%。在权威基准 opencompass 上，通义千问 2.5 得分追平 gpt-4 turbo。
![](https://r2.zhanglearning.com/blog/2024/05/ddb655c7b79e1ae66745c433c7b7814b.png)

### 通义千问 Qwen1.5-110B 超 1000 亿参数

Qwen1.5-110B 是 Qwen1.5 系列中的新成员，也是该系列首个拥有超过 1000 亿参数的模型。

该模型在基础模型评估中表现出色，与 Meta-Llama3-70B 相媲美，并在聊天模型评估（包括 MT-Bench 和 AlpacaEval 2.0）中表现出色。

模型支持多语言，包括英语、中文、法语、西班牙语等，上下文长度可达 32K 令牌。

模型特性：

•架构：采用 Transformer 解码器架构，具有分组查询注意力（GQA）。
•性能：在标准评估和聊天模型评估中均展现卓越性能。
•多语言支持：支持多种语言，上下文长度可达 32K 令牌。

根据官方公布的评测结果

Qwen1.5-110B 模型的评测结果略略超过 Llama-3-70B 和 Mixtral-8×22B。

Qwen1.5-110B 模型在综合理解（MMLU）、数学推理（GSM8K 和 MATH）方面得分比 Llama-3-70B 略高一点点，是几个模型中最强的。而在复杂推理任务 ARC-C 上则略低于 Mixtral-8×22B 模型。在编程测试 HumanEval 得分则是远超另几个模型，而 MBPP 编程测试上则低于 Mixtral-8×22B 模型。

详细：https://qwenlm.github.io/blog/qwen1.5-110b/

![](https://r2.zhanglearning.com/blog/2024/05/6f4daf5ffcd0c6deee82c70135c21d5c.png)


### 零一万物开源了 yi-1.5 模型

 yi-1.5 有 6b、9b、34b 三个型号，都采用 apache 2.0 许可证。

- 模型在 4.1 万亿 token 上训练的
- 在 300 万个指令调优样本上进行了精细调整
- 34b 型号一些指标超过了 qwen 的 72b
- 6b 和 9b 型号也成功超越了 mistral 的 7b v0.2 版和 gemma 的 7b 型号

模型下载：https://huggingface.co/collections/01-ai/yi-15-2024-05-663f3ecab5f815a3eaca7ca8

![](https://r2.zhanglearning.com/blog/2024/05/b6c36b4e1b221f6a7322be003ebc5780.png)


### gemma 2b - 10m context 模型的代码实现

infiniattention 论文地址：
https://arxiv.org/abs/2404.07143

transformer-xl 论文地址：
https://arxiv.org/abs/1901.02860

模型下载地址：
https://huggingface.co/mustafaaljadery/gemma-10m-safetensor

github repo:
https://github.com/mustafaaljadery/gemma-2b-10m

对大模型上下文能达到 8k => 10m 大幅提升的技术说明：
大型语言模型（llms）在内存方面的最大瓶颈是键值（kv）缓存。在传统的多头注意力机制中，它呈二次方增长，因此限制了序列长度的大小。
本文的方法按照 infiniattention 所概述的，将注意力分割到局部注意力块中。采用这些局部注意力块，并对局部注意力块应用递归，以获得最终的 10m 上下文全局注意力的结果。
许多想法灵感来自于 transformer-xl 论文。


![](https://r2.zhanglearning.com/blog/2024/05/58be100b7b8d517714a47840740b7b80.png)


## 小工具


### lgm：生成高质量 3d 模型

支持文字生成模型、图片生成模型，分辨率 512*512，5 秒内即可生成。

在线体验：https://huggingface.co/spaces/ashawkey/lgm

项目地址：https://me.kiui.moe/lgm/  

github: https://github.com/3dtopia/lgm

![](https://r2.zhanglearning.com/blog/2024/05/18fd0ece58abc6bcc4c80e616832c19e.png)


### 手绘风 svg 的 react 渲染器

想做手绘风格的 ui 几乎没有门槛了🚀推荐用这个渲染手绘风 svg 的 react 渲染器：https://github.com/bowen7/react-rough-fiber

用法很简单，只要把 svg 图片用<roughsvg>组件包裹，就能把 svg 转成手绘风格。详细使用文档：https://react-rough-fiber.amind.app

![](https://r2.zhanglearning.com/blog/2024/05/685319b454099ea9a26e3d43f6b540aa.png)

### 一个免费的开源插画网站
网址：http://opendoodles.com

1.免费丰富的插画，支持在线编辑
2.支持导出 svg、png 等矢量图
3.如果需要更进一步的设计，支持定制服务

很有意思的地方是，作者分享了他做这个产品的初衷，在他刚开始做设计师的时候，周围没有人教，而且没钱买软件，因此不得不盗版软件、偷科技杂志里的光盘，学到了很多酷的平面设计。

现在做了 open doodles，这些插画资源遵循开放设计的理念，允许用户自由地复制、编辑、重新混合、分享或重新绘制，而不受版权或数据库法的限制。

![](https://r2.zhanglearning.com/blog/2024/05/2940b52a3854b2e65c03f4c880216bdf.png)

### v2ex 被丑头像包围了，丑头像生成器

- 生成：https://txstc55.github.io/ugly-avatar/
- 项目：https://github.com/txstc55/ugly-avatar

![](https://r2.zhanglearning.com/blog/2024/05/815fc5ac49df200bca3456e58f40dbf1.png)


### 如何下载视频号视频
方式一：
https://www.runningcheese.com/wechat-video-download

方式二：
https://github.com/lecepin/WeChatVideoDownloader/releases
![](https://r2.zhanglearning.com/blog/2024/05/57245566a5b31c9274036d74b626c9dd.png)

方式三：
https://github.com/putyy/res-downloader
  
网络资源嗅探资源下载器，支持：微信视频号下载、网页抖音无水印下载、网页快手无水印视频下载、酷狗音乐下载等网络资源拦截下载！

### 高性能的大数据无代码平台：teable

主要特点包括：

📊 表格界面：类似电子表格的操作方式，支持单元格编辑、公式、条件格式、图表等功能。  
🗂️ 丰富视图：除了表格视图，还提供看板、日历、画廊、表单、甘特图等多种数据展现方式。  
🚀 卓越性能：可以轻松处理数百万数据，支持批量操作，有自动索引优化。
👨‍💻 原生 #SQL 支持：可以使用 SQL 直接查询，兼容 #Metabase、#PowerBI 等 #BI 工具。  
🧠 AI Copilot：通过 AI 对话来辅助开发应用、生成图表、调整视图、设置自动化等。  
🔒 数据安全：支持数据本地存储，有完善的权限管理。  
⚡️ 实时协作：数据可实时更新，支持协作成员管理。  
🧩 可扩展：基于 #React，可以低成本定制和扩展应用。  
🤖 流程自动化：可通过 #AI 或可视化方式设计自动化流程。  
🗄️ 多数据库支持：兼容 #Sqlite、#PostgreSQL、#MySQL 等数据库。

可以将 Teable 视为 Airtable 的大数据替代品，在保留电子表格式的易用性的同时，还兼具传统数据库的高性能和稳定性，非常适合企业级的数据管理应用开发。

🌐 链接：https://github.com/teableio/teable  
🚀 一键部署：https://bja.sealos.run/?openapp=system-template%3FtemplateName%3Dteable


### 嵌套网页展示搜索结果的产品 globe

Globe: https://explorer.globe.engineer/

globe，已经接入了 Gorq，速度真的快的离谱。一秒钟展示一个概念的所有内容，加载的速度赶不上生成的速度。

![](https://r2.zhanglearning.com/blog/2024/05/78eaa329c2d86f29d6ec276b085020df.png)


### 一个微信聊天记录导出工具

https://github.com/LC044/WeChatMsg

提取微信聊天记录，将其导出成 HTML、Word、CSV 文档永久保存，对聊天记录进行分析生成年度聊天报告，还能 1:1 还原聊天界面！

## 知识库

### 推荐阅读：《你好 gpt-4o》

想了解 gpt-4o 的技术细节，推荐阅读官方的 hello gpt-4o

原文：https://openai.com/index/hello-gpt-4o/


### awesome 中文大模型@GitHub

awesome chinese llm 旨在收集和梳理中文 llm 相关的开源模型、应用、数据集及教程等资料，目前收录的资源已达 100+ 个！

github repo:
https://github.com/hqwu-hitcs/awesome-chinese-llm


### Gemini API Cookbook

Logan 大佬发布的 Gemini API 指南和示例的集合，包括用于编写提示和使用 API 不同功能的快速入门教程，以及可以构建的示例。
从账号申请开通、Gemini API 能力了解到实际接入过程，对接入测试工作帮助很大！

https://github.com/google-gemini/cookbook


## 随便看看

### openai 是如何连续三次羞辱 google 的：

1. chatgpt 在 2022/12 发布，导致 google 整个推翻 2023 年的计划

2. gpt-4 选在了 palm api (谁还记得它) 同一天发布

3. 最近的一次，gpt-4o 在 google i/o 之前一天发布
