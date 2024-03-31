---
date: 2024/03/31
---

<img src="https://r2.zhanglearning.com/2024/03/506e102f011ce3740725bc02dfec3662.jpeg" width="800" />  


<small>无论您是歌手还是排行榜艺术家，我们都会打破您与您梦想创作的歌曲之间的障碍。不需要任何工具，只需要想象力</small>  


1、AI 创作音乐——Suno
2、开源大模型王座再易主，1320 亿参数 DBRX 上线
3、AI21 发布世界首个 Mamba 的生产级模型：Jamba
4、Google Gemini API Cookbook
5、claude-opus-to-haiku
6、仿 Duolingo 开源项目
7、开源全栈商城项目：C-Shopping 
6、动画算法与数据结构
9、一款开源、全能的下载工具

### 1、AI 创作音乐——Suno

https://app.suno.ai/

AI 音乐生成软件 Suno 发布 V3 版本，仅需要简单的描述，就可以生成 2min 长度、广播质量级别的音乐。正如 Suno 官网所显示：“无论您是歌手还是排行榜艺术家，我们都会打破您与您梦想创作的歌曲之间的障碍。不需要任何工具，只需要想象力。”

![](https://r2.zhanglearning.com/2024/03/129c4e17a115182de563977fd7b2a981.png)

Suno 创作音乐的小技巧：  
1、如果你想参考某个现有歌曲的节奏，可以在这个网站查询歌曲的 BPM 和 Key，作为提示词写进去。
https://songbpm.com

2、歌词里，可以在歌词段落前加[Verse]（主歌）、[Rap]（说唱）、[Chorus]（副歌/高潮）、[Intro]（印子）来告诉 AI 这段歌词应该怎么唱。

### 2、开源大模型王座再易主，1320 亿参数 DBRX 上线

这是迄今为止最强大的开源大语言模型，超越了 Llama 2、Mistral 和马斯克刚刚开源的 Grok-1。

DBRX 的基础（DBRX Base）和微调（DBRX Instruct）版本已经在 GitHub 和 Hugging Face 上发布，可用于研究和商业用途。人们可以自行在公共、自定义或其他专有数据上运行和调整它们，也可以通过 API 的形式使用。

基础版：https://huggingface.co/databricks/dbrx-base

微调版：https://huggingface.co/databricks/dbrx-instruct

GitHub 链接：https://github.com/databricks/dbrx

DBRX 在语言理解、编程、数学和逻辑等方面轻松击败了目前业内领先的开源大模型，如 LLaMA2-70B、Mixtral 和 Grok-1。

![](https://r2.zhanglearning.com/2024/03/8e858e361060a8a7196e08b18889ff6c.jpg)



### 3、AI21 发布世界首个 Mamba 的生产级模型：Jamba

网站：https://ai21.com/jamba

详细介绍：https://ai21.com/blog/announcing-jamba

模型：https://huggingface.co/ai21labs/Jamba-v0.1

开创性的 SSM - Transformer 架构

🧠 52B 参数，12B 在生成时处于活动状态
 👨‍🏫  16 位专家，生成过程中仅 2 个专家处于活跃状态
 🆕  结合了 Joint Attention 和 Mamba 技术
 ⚡️ 支持 256K 上下文长度
 💻  单个 A100 80GB 最多可容纳 140K 上下文
 🚀 与 Mixtral 8x7B 相比，长上下文的吞吐量提高了 3 倍

Jamba 结合了 Mamba 结构化状态空间（SSM）技术和传统的 Transformer 架构的元素，弥补了纯 SSM 模型固有的局限。

> Jamba 代表了在模型设计上的一大创新。这里的"Mamba"指的是一种结构化状态空间模型（Structured State Space Model, SSM），这是一种用于捕捉和处理数据随时间变化的模型，特别适合处理序列数据，如文本或时间序列数据。SSM 模型的一个关键优势是其能够高效地处理长序列数据，但它在处理复杂模式和依赖时可能不如其他模型强大。

![](https://r2.zhanglearning.com/2024/03/9717314adc212655927a1c0271bf80f9.jpeg)

### 4, Google Gemini API Cookbook

Google 官方 Gemini API 提供的指南和示例集合

https://github.com/google-gemini/gemini-api-cookbook

帮助开发者更好地理解和使用 Gemini API，包括如何构建应用程序、编写提示以及利用 API 的不同特性。

支持直接在 Google Colab 上运行或下载到用户选择的环境中运行。

提供了：

- 入门指南：提供了一个简短的入门指南，帮助开发者开始使用 Gemini API 进行构建。

- 快速开始：包括写作提示和使用 API 不同特性的快速开始教程。

- 示例应用：展示了可以使用 API 构建的不同应用的示例。

### 5、claude-opus-to-haiku

这个`claude-opus-to-haiku` ✍️最近非常火

以极低的成本和延迟获取 Claude 3 Opus 的品质。

给出一个任务示例，Claude 3 Opus 将教会 Haiku（成本低 60 倍，速度快 10 倍!!）如何完美完成这个任务。

而且它是开源的：https://github.com/mshumer/gpt-prompt-engineer

![](https://r2.zhanglearning.com/2024/03/9ab08f275d07b265b291457b0519b1d3.gif)

### 6、仿 Duolingo 开源项目

这是一个使用 Nextjs、React、Drizzle 和 Stripe 开发的仿 Duolingo 开源项目

https://github.com/AntonioErdeljac/next14-duolingo-clone
它的功能非常丰富，包含了：AI 语音、组件系统、认证系统、音效、生命值系统、积分/经验值系统、排行榜、任务等等。

### 7、开源全栈商城项目：C-Shopping 

国内商城项目虽多，但是用 Next.js 实现并开源的却很少见，C-Shopping 实现的功能很完善，非常适合 Next.js/React 开发者学习。

Web 全栈开源地址：https://github.com/huanghanzhilian/c-shopping
APP 开源地址：https://github.com/huanghanzhilian/c-shopping-rn
小程序版正在开发中…

技术栈：
    NextJs
    TailwindCss
    Headless UI
    MongoDB
    Redux - Toolkit - RTK Query
    JWT
    Docker/Vercel


### 8、动画算法与数据结构

https://www.ituring.com.cn/book/2954
本书是一本借助演示动画来讲解算法和数据结构的入门书。书中首先介绍阅读本书所需的最低限度的编程知识和基本概念。然后针对各个算法和数据结构，在指出其解决的问题后，通过空间结构、数据、时间结构（算法流程）、计算 4 个方面详细讲解。最后介绍相关的伪代码和应用示例。本书涉及的算法与数据结构较为全面，通过基于动画的可视化、详细的介绍和伪代码三方面进行讲解，帮助读者直观掌握各算法和数据结构的动作原理。

网站：https://anime.yufan.io/
实现代码：https://github.com/syhily/algorithm-anime
本仓库是动画算法与数据结构的网页源码

本支持页面包含[《动画算法与数据结构》](https://www.ituring.com.cn/book/2954)一书中创建的符号、动画和伪代码。有关详细解释，请参阅《动画算法与数据结构》书籍内容。
![](https://r2.zhanglearning.com/2024/03/fe6f297ab987003ce3452ceb24f5c74d.png)


### 9、一款开源、全能的下载工具

https://motrix.app/

支持 Windows、macOS、Linux，下载 HTTP、FTP、BT、磁力链接等资源

![](https://r2.zhanglearning.com/2024/03/c85a8a6ca9fdac244c925c69ddde89f2.png)

![](https://my-wechat.oss-cn-beijing.aliyuncs.com/WX20230912-203916-20231217213830903-20231222231724242.png)
