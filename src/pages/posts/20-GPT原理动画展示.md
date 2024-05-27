---
date: 2024/05/27
---

<img src="https://r2.zhanglearning.com/blog/2024/05/9c7250733ae8fade24f6c9c58a4a214c.png" width="800" />  

<small>冷知识：2024 年已过 40%</small>  



机器学习周刊：关注 Python、机器学习、深度学习、大模型等硬核技术

本期目录：

[TOC]


## 大模型
### [Google 发布生成式 AI 视频模型 Veo](https://deepmind.google/technologies/veo/)

![](https://r2.zhanglearning.com/blog/2024/05/ef5a73c6813fd5bc98924537cd9eece1.png)
Google 在 I/O 开发者大会上宣布了它的生成式 AI 视频模型 Veo，能以不同视觉和电影风格生成长度超过 1 分钟的 1080p 分辨率视频。

Google 称，Veo 具有自然语言的高级理解能力，能理解“延时拍摄（timelapse）”或“空中镜头（aerial shots of a landscape）”等电影术语，用户可用文本、图像或基于视频的提示导向他们想要的输出。

Veo 的视频输出更一致和连贯，能展现人和物的更真实运动。类似 OpenAI 的 Sora，Veo 将首先提供给电影制作人和内容创作者试用。

![[veo_example_014_jellyfish 1.mp4]]

Prompt: A lone cowboy rides his horse across an open plain at beautiful sunset, soft light, warm colors
### [一览主流 llm 性能、速度和价格的对比网站](http://artificialanalysis.ai)
分享一个可以一览主流 llm 性能、速度和价格的对比网站，方便大家选择适合自己的模型

性能最好：gpt-4o
速度最快：gemini 1.5 flash
价格最低：llama 3-8b，主要 deepseek 没做评测。

![](https://r2.zhanglearning.com/blog/2024/05/ce8b206b672ade86e7159e9df040e758.png)

### [国内外 AI 大语言模型 API 价格对比](https://aigcrank.cn/llmprice/)


AIGCRank 大语言模型 API 价格对比是一个专门汇总和比较全球主要 AI 模型提供商的价格信息的工具。可以轻松查找和比较 OpenAI、Claude、Mixtral、Kimi、星火大模型、通义千问、文心一语、Llama 3、GPT-4、AWS 和 Google 等国内外主要 API 提供商的最新价格，确保找到最适合您项目的模型定价。
![](https://r2.zhanglearning.com/blog/2024/05/acefe82250c33e7d6df3a6f2988a30c1.png)

## 工具
### [开源的 AI 导航站模板](https://github.com/6677-ai/tap4-ai-webui)
Tap4 AI Web UI 是一款开源的 AI 导航站模板，项目非常轻量级，维护简单，可一键部署到 Vercel！

功能
- 国际化
- SEO 友好（支持 i18n）
- 动态 sitemap.xml（支持 i18n）
- 快速发布
- 使用 NEXT 14 和 app 路由（react 服务器组件）
- Supabase serverless 数据库

这两年 AI 导航站的流量非常大，大家如果也想做 AI 导航站，不妨拿去白嫖吧！


### [2024 GitHub 加速器：开源 AI 11 个项目](https://github.blog/2024-05-23-2024-github-accelerator-meet-the-11-projects-shaping-open-source-ai/)

GitHub 加速器宣布了 2024 年入选的 11 个开源 AI 项目，它们代表了全球开源 AI 领域的创新和加速发展。项目包括机器学习和 AI 框架、生物学和疾病发现、模型训练和微调工具、仿真、部署和全生产化系统、多模态和 3D AI 能力，以及从可穿戴设备到 AI 驱动机器人的新兴接口和设备。 

11 个入选的开源 AI 项目： 

- Unsloth AI@UnslothAI 由 Daniel Han 和 Michael Han 创立，旨在使自定义 AI 模型更易访问。Unsloth 通过新兴技术和能力，使其比竞争对手快 2-5 倍，内存使用减少 70%，同时保持模型的性能和准确性。 

- Giskard@giskard_ai  由 Alex Combessie 和 Weixuan XIAO 创立，是一个用于测试和评估 LLMs 的开源库。Giskard 旨在提高开源 AI 模型的质量，推动整体采用、研究、透明度和问责性。 

- A-Frame@aframevr 由 Diego Marcos 共同创建和维护，是一个框架，旨在使任何人在网络浏览器中都能轻松开发 AR/VR 和 3D 内容。A-Frame 专注于集成 AI 工作流程，例如 3D 高斯溅射和生成性 AI，以创建图像和环境。 

- Nav2 由机器人专家 Steve Macenski 创立，是 Robot Operating System (ROS) 导航框架的先驱。Nav2 是全球部署最广泛的自主移动机器人（AMR）导航解决方案，被 100 多家公司信赖。 

- OpenWebUI@OpenWebUI 由 Tim Baek 创立，旨在为 AI 和 LLMs 构建最佳用户界面，为那些互联网访问受限的人提供利用 AI 技术的机会。OpenWebUI 通过 Web 界面本地运行 LLMs，使 AI 和 LLMs 更安全、更私密。 

- LLMware AI 由 Namee Oberst 创立，她与 CEO Darren Oberst 和 Stefan Bachhofner 一起，旨在为金融和法律机构构建安全和敏感的 LLM AI Agent 和 RAG 模型。 
- LangDrive 由 Michael Vandi 和 Spmatika 创立，他们在 CMU 攻读硕士学位期间构建了一个 LLM 电子邮件代理。LangDrive 是一个简单的框架，通过 API 和配置文件训练和部署生产级别的微调语言模型。 
- HackingBuddyGPT 由 Andreas Happe 和 Jurgen Cito 创立，旨在帮助道德黑客和安全专业人员利用 LLMs 使世界更安全。HackingBuddyGPT 是一个自主的黑客伙伴，具有人在环路中的基础设施。 
- Web-Check 由 Alicia Sykes 创立，她是一位开源倡导者，旨在通过基于任何网站或服务器的开放数据提供 AI 驱动的安全洞察，使互联网更安全。 
- Marimo@marimo_io 由 Akshay Agrawal 和 Myles Scolnick 共同创立，旨在解决数据科学和机器学习 Notebook 使用中的所有问题。Marimo 是一个下一代 Python Notebook，为 AI/ML 开发者提供可复现、可维护和可生产的 Notebook。 

- Talkd AI @talkd_ai  由 Vinicious Mesel 创立，他开始兼职开发 Talkd AI，以构建一个统一的 LLM 聊天 API，为多个 LLMs 和上下文提供抽象层。Talkd AI 旨在促进和传播 LLMs 中 RAG 技术的使用方法。

### [一个帮助你思考的集合工具&框架：](https://untools.co/)
![](https://r2.zhanglearning.com/blog/2024/05/886037029b6ac6741ab87e8f56203cb5.png)


### [AI 智能图像分割](https://segmentify.app/zh)
<video src="https://teamaker-1251887421.cos.ap-guangzhou.myqcloud.com/segany.mp4" />  




### [一个只做渐变色的 CSS 库](https://uigradients.com/#RainbowBlue)
Ulgradients 是一个主打渐变风网站，设计师可根据自己风格来选择搭配，直接获得对应渐变配色的 CSS 代码，相当方便对于大大提高了前端开发的效率。
![](https://r2.zhanglearning.com/blog/2024/05/29a8acbe51894fc5a82f1895844730ca.png)

### [一款专为英语学习打造的视频播放器](https://github.com/solidSpoon/DashPlayer?tab=readme-ov-file)

为英语学习者量身打造的视频播放器，助你通过观看视频、沉浸真实语境，轻松提升英语水平。

![](https://r2.zhanglearning.com/blog/2024/05/83dafdc4202f3c9216b29aacf7c24a52.png)


## 知识库
### [Phi-3 CookBook](https://github.com/microsoft/Phi-3CookBook)

Phi-3 是微软开发的一系列开放 AI 模型，是目前功能最强大、性价比最高的小型语言模型，分为 mini、small、vision 和 medium 等版本。 

关于 Phi-3 入门的 Phi-3 CookBook，主要内容：
· Phi-3 介绍和快速上手
· Phi-3 推理、微调和评测

### [生成式人工智能常识科普图](https://cartography-of-generative-ai.net/)

https://cartography-of-generative-ai.net/genai_cartography.pdf
![](https://r2.zhanglearning.com/blog/2024/05/29c405073c52d7fbf9033dd5103e66bb.png)

这张图非常有意思！

**把生成式人工智能 GenAI 的核心内容 & 高频议题，绘制在了一张可视化图里**。通过这张图，你可以感受到整个 GenAI 世界的运转逻辑，也会大致明**白大模型是如何生成文字和图片**的~

### [LaTeX 入门与进阶](https://latex.lierhua.top/zh/) 


![](https://r2.zhanglearning.com/blog/2024/05/0c6af9633427f19533d5cdb15e3376d4.png)

### [前端开发的知识总结](https://spacexcode.com/)


![WX20240517-100517.png](https://r2.zhanglearning.com/blog/2024/05/a2ca75fe8fb94a750ce27e3a44172bef.png)



### [手把手带你从头实现 LLaMa 3](https://github.com/naklecha/llama3-from-scratch)



**llama3 implemented from scratch** 最近在 GitHub 社区非常出圈，Star 狂飙！

这个项目用 **图示 + 代码** 的方式，从头演示了如何理解和实现 LLaMa 3 的完整过程，非常生动、详细且硬核 👍
![](https://r2.zhanglearning.com/blog/2024/05/ea75afe08f8d63a41c242981c1bd48fd.png)

### [什么是 GPT？工作原理动画展示](https://arthurchiao.art/blog/visual-intro-to-transformers-zh/)


3Blue1Brown 是一个专注于数学教育的 YouTube 频道，视频制作精良且非常擅**用直观的动画和图表，讲清楚复杂抽象的数学话题**，以及由此拓展的机器学习、深度学习等等。

3Blue1Brown 在 B 站也有官方账号，而且有 200 多万粉丝啦！最近更新的视频都与大模型有关，整个系列还在持续更新中。

**如果你想直观地搞清楚 GPT 原理，那 3Blue1Brown 这个系列的视频，应该是全球最好的学习资料了，甚至没有之一。**

@arthurchiao  做了另一件非常有意义的工作 —— **将视频整理成了「动图 + 文字」的可视化版本**，而且还是中文！！相当于一份学霸的要点笔记，帮助你能更清晰地 get 到原视频的要点，彻底搞清楚 Transformer 内部工作原理。


![](https://r2.zhanglearning.com/blog/2024/05/420605b7e622aad62e8223a3117ce817.gif)

### [OpenAI 前首席科学家分享 30 篇顶级 AI 论文](https://arc.net/folder/D0472A20-9C20-4D3F-B145-D2865C0A9FEE)
OpenAI 前首席科学家 Ilya sutskever 大佬分享的约 30 篇顶级 AI 研究论文清单爆火🔥💥，据说看完可以掌握当前人工智能最为关键的 90% 的知识！

包括 Transformer 架构、RNN、LSTM、神经网络复杂度、计算机视觉等领域


![](https://r2.zhanglearning.com/blog/2024/05/e970c498f07639e2f9b9400f90373999.png)

## 轻阅读
[公开写作的好处和坚持不懈](https://www.usmacd.com/cn/public_writing/)

![](https://r2.zhanglearning.com/blog/2024/05/008826f3f810e91a2656dfc7654206e6.png)





近期学到的一个技能：相信别人已经做过。很多问题的解决方案，这个世界上已经存在过。一定有这个世界上某个团队某个人已经思考的非常透彻，可能在书籍里，在历史里，在故事里，或者藏在互联网深处。如果找信息带来的价值远大于自己思考实践才能验证，那就先思考我应该在哪里找到这个解决方案。B**y Nin19536@X**






12 亿人没有护照、10 亿人没做过飞机、但有近 11 亿人可以上网。大学文化水平人数 2.18 亿，包含本科大专高职。理解这些数据，可以避免很多无意义的争吵。今天把上面数据都溯源了一下，都是官方发布的数据。截止 19 年底中国普通护照人数有 2 亿左右，也就是 12 亿人没有护照。23 年 9 月民航局公布的粗略数据表示中国乘坐过飞机的人仅为 3 亿多，也就是 10 亿多人没有坐过飞机。截止 23 年底，中国网民数量是 10.92 亿。2020 年人口普查，大学文化程度的人口为 21836 万人，包含高职、大专、本科及以上。**By 熊猫学经济@weibo**