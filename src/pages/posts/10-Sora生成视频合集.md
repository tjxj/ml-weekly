---
date: 2024/02/19
---

<img src="https://r2.zhanglearning.com/blog/2024/02/9b263d9df05cb2082f75c295cd75bd78.png" width="800" />  

<small>OpenCodeInterpreter：开源的代码解释器实现</small>

目录：

1、ollama 已支持 Google 的 Gemma 模型  
2、move.ai 推出了 Move API  
3、SoraWebui - playground  
4、Sora 生成视频合集  
5、OpenCodelnterpreter:开源的代码解释器实现  
6、AnimateLCM-SVD-xt 已推出  
7、Stability Al 推出图像提升增强工具  
8、每秒输出 500 个 Token 的项目 groq  
8、极速安装 Python package  
9、Apple 开源 MGIE  
10、Code Llama 70B  
11、一个全平台高速下载器  
12、2002 年 QQ 秀立项 PPT  
13、一行命令永久激活 Windows/Office   
14、Linux 教程学习项目  
15、python-mini-project  



### 1、Ollama 已支持 Google 的 Gemma 模型 

现在可以下载安装在你的电脑上运行 

2B 大小是 1.4G 

安装：[http://Ollama.com/library/gemma](https://t.co/fBLYjwm9Yt)



![](https://r2.zhanglearning.com/2024/02/50f39e8d950487e5324f46c538b706fa.jpeg)

### 2、move.ai 推出了 Move API

move.ai 推出了 Move API，一种从 2D 视频生成 3D 动作数据的简便方法。

🎥 只需一个摄像头进行拍摄

🔀 上传视频文件

💃 接收动作数据

将动作捕捉集成到生产工作流程、应用程序等中。

申请提前访问：https://move.ai/api

![](https://r2.zhanglearning.com/2024/02/f7c446dc55d9a6d6a1208912086e62f7.gif)





### 3、SoraWebui - playground

SoraWebui 是一个开源项目，通过允许用户使用文本在线生成视频，使用 OpenAI 的 Sora 模型简化视频创建，具有简单的一键网站部署功能。

https://sorawebui.com/zh/playground

![](https://camo.githubusercontent.com/42c08fac420946d9fcf58c581aa9506c2260674af9f32292e501dd5b0f3aab19/68747470733a2f2f736f726177656275692e636f6d2f737563636573735f6465706c6f792e6a7067)

### 4、Sora 生成视频合集

https://sorawebui.com/zh/videos
Sora 生成视频合集，附带提示词

![](https://r2.zhanglearning.com/blog/2024/02/9b263d9df05cb2082f75c295cd75bd78.png)

### 5、OpenCodeInterpreter：开源的代码解释器实现

可能大家对于 ChatGPT 里面的代码解释器（Code Interpreter）都印象深刻，可以让它生成一段代码，并且还能执行代码的结果，如果执行出错，还能继续优化代码重新执行。虽然以前也有人基于 GPT-4 的 API 实现，但是以前没有开源模型可以做到很好，因为这需要对模型专门进行微调才能做得到。

 现在有了开源的 OpenCodeInterpreter，不仅可以很好的生成代码和执行代码，甚至于某些方面的评分还超过了 GPT-4： “OpenCodeInterpreter-33B 在 HumanEval 和 MBPP 的平均（和增强版本）上分别达到了 83.2（76.4）的准确率，与 GPT-4 的 84.2（76.2）相当，并且通过从 GPT-4 合成的人类反馈进一步提升至 91.6（84.6）。” 

项目地址：https://opencodeinterpreter.github.io 

![geometric reasoning](https://r2.zhanglearning.com/blog/2024/02/8cdfa46da5b1380f84c974321318617c.png)

### 6、AnimateLCM-SVD-xt 已推出 

快速图像到视频生成 AnimateLCM-SVD-xt 通常可以通过 4 个步骤生成高质量的视频，而不需要无分类器的指导，因此与普通 SVD 模型相比可以节省 25 x 2 / 4 = 12.5 倍的计算资源

模型：https://huggingface.co/wangfuyun/AnimateLCM-SVD-xt

试玩：https://huggingface.co/spaces/wangfuyun/AnimateLCM

![](https://r2.zhanglearning.com/2024/02/91d82976492ea801acc272c4441a7c45.png)

### 7、Stability AI 推出图像提升增强工具

**Creative Upscaler** 可以**将图像升级到 4k 分辨率**，**并创造以前没有的新细节和赋予图像新生命**。 

**主要功能：** 

1、分辨率提升：将图像升级到 4K 分辨率，无论原始图像的大小如何。 

2、细节创造：不仅放大图像，还能“幻想”出原始图像中不存在的新细节，通过结合输入图像与文本提示，创造出清晰、高质量的图像效果。 

3、创造力调整：用户可以调整创造力水平，让 AI 在保持接近原始图像的基础上，创造出更多或更少的新细节。高创造力设置允许升级器创造出原本不存在的新细节。 

4、面向高质量转换：适用于将低质量图像完全重新想象、转换为高分辨率杰作，提供更锐利的细节和更逼真的纹理。 

5、原始图像保留：较低的创造力设置可以保留更多原始图像的特征，适用于需要细腻处理的场景。 

7、生命注入：**可以为平淡无奇的渲染带来生命**，通过创意升级器增强图像，使其显得更有吸引力。 

8、独特的 AI 技术应用：与大多数 AI 升级器不同，Creative Upscaler 结合文本提示和图像，创造出原本不存在的新细节，为图像赋予新的生命和可能性。 



体验：[https://creator.nightcafe.studio/stability-ai-creative-upscaler](https://t.co/SDkoJKStoz)



![image-20240227100036132](https://r2.zhanglearning.com/blog/2024/02/5dac5881a9d9ce33e91009225ee9b4fd.png)

![](https://r2.zhanglearning.com/blog/2024/02/02e887044a7d9226a1e09e4b49dc9f71.gif)

### 8、每秒输出 500 个 Token 的项目 groq

前几天那个每秒输出 500 个 Token 的项目 groq，公开了他们的 API，他们的输出速度比顶级运营商快 18 倍。得益于这个速度，甚至实现了完全实时的远程 AI 对话。Mixtral, 8x7B SMoE 可以达到 480 Token/S，价格为100万Token 0.27 美元。极限情况下他们用 Llama2 7B 甚至能实现 750 Token/S。目前他们还提供 100 万 Token 的免费试用。API 完全兼容 OpenAI API。 

这里尝试 groq：[https://wow.groq.com](https://t.co/rf79KcmWT7)

![](https://r2.zhanglearning.com/blog/2024/02/1244b8b513b091fa37e4ac5fec328551.png)

### 8、极速安装 Python package

地址：https://github.com/astral-sh/uv

官网：https://astral.sh/

优势：

⚖️ 用于常见 pip、pip-tools 和 virtualenv 命令的即插即用替代品。  
⚡️ 比 pip 和 pip-tools（pip-compile 和 pip-sync）快 10-100 倍。  
💾 磁盘空间高效，具有全局缓存以实现依赖项去重。  
🐍 可通过 curl、pip、pipx 等安装，uv 是一个静态二进制文件，无需 Rust 或 Python 即可安装。  
🧪 针对 PyPI 前 10,000 个包进行了大规模测试。 
🖥️ 支持 macOS、Linux 和 Windows。  
🧰 支持依赖版本覆盖和替代解决策略等高级功能。  
⁉️ 提供最佳错误消息，具有冲突跟踪解析器。  
🤝 支持广泛的高级 pip 功能，包括可编辑安装、Git 依赖项、直接 URL 依赖项、本地依赖项、约束、源代码分发、HTML 和 JSON 索引等等。  

使用方法：

第 1 步：`uv venv` 

第 2 步：`source .venv/bin/activate` 

第 3 步：`uv pip transformer`

![](https://r2.zhanglearning.com/blog/2024/02/deebc78570f14ada191f0bd5548aa50a.png)

### 9、Apple 开源 MGIE

Apple repo https://github.com/apple/ml-mgie 
Gradio https://github.com/tsujuifu/pytorch_mgie
 🤩 Apple 开源 MGIE！现在人们可以随意拍摄照片了。

 iPhone & 编辑 w.语言！

通过多模态大语言模型指导基于指令的图像编辑 #ICLR2024 焦点：https://openreview.net/forum?id=S1RKWSyZ2Y 

<video src="https://r2.zhanglearning.com/blog/2024/02/013a1bdd0b00fed47ecc19bf4d3c0fc3.mp4" controls="controls"></video>





### 10, Code Llama 70B

Code Llama 70B：用于代码生成的 LLM 的新的、性能更高的版本 - 与之前的 Code Llama 模型具有相同的许可证。 

下载模型： [https://bit.ly/3Oil6bQ](https://t.co/GApdj5PW83)  

• CodeLlama-70B
• CodeLlama-70B-Python
• CodeLlama-70B-Instruct

CodeLlama-70B-Instruct 在 HumanEval 上获得 67.8 分，使其成为当今性能最高的开放模型之一。 

https://ai.meta.com/blog/code-llama-large-language-model-coding/

![](https://r2.zhanglearning.com/blog/2024/02/da817fc645305653fd1cf1ee2b59b746.gif)

Code Llama 70B 型号可在与 Llama 2 和之前的 Code Llama 型号相同的许可下使用，以支持研究和商业用途。

🧮 最大 70B 参数
🔠 训练使用了 1TB token
🐍 微调 Python 版本和 Instruct 版本
✅ 允许商业用途
🪟 100K 上下文窗口
🤗 可用于 @huggingface

🔜 集成到 Hugging Chat 中
👩‍💻 支持代码文档生成，调试



### 11、一个全平台高速下载器

Gopeed 直译过来中文名叫做够快下载器，由 Golang+Flutter 开发，支持（HTTP、BitTorrent、Magnet）协议。

在 macOS 下实测，安装 Youtube 扩展后，可以下载油管视频。还支持百度网盘、Twitter media。 

下载地址：[https://github.com/GopeedLab/gopeed](https://t.co/lNg9YBl1CU)

![](https://r2.zhanglearning.com/blog/2024/02/b7a274407d5d41ced48b9e60d6ff93c0.png)

### 12、2002 年 QQ 秀立项 PPT

犬校有人分享了 2002 或 2003 年 QQ 秀立项的 PPT，这算账能力、推演能力太超前了。查了下写 PPT 的人，现在是元生资本创始合伙人许良 (Kurt Xu)。太厉害了，能从 2002 年在腾讯待到 2015 年，肉身投资的成功典范。

 [https://tuhw9h0z5l.feishu.cn/file/P3WPbzU01oMOfDxGIwyckrRdnIg](https://t.co/m0iBpmeaSv)

![](https://r2.zhanglearning.com/blog/2024/02/e609d338750572ec1025932b3dfa4215.png)

### 13、一行命令永久激活 Windows/Office

激活命令：irm [https://massgrave.dev/get](https://t.co/h3qFRQJlbH) | iex 

而且这个激活脚本代码竟然还放在 MS 自家的 GitHub 上：[https://massgrave.dev](https://t.co/IxCz1njTQv)。



![https://github.com/massgravel/Microsoft-Activation-Scripts](https://r2.zhanglearning.com/2024/02/0f8420228e612c6c934ee879f5e19e7a.jpeg)

![Image](https://r2.zhanglearning.com/2024/02/b315a7ef95b0000e1f48d95f9a13414e.jpeg)

![](https://r2.zhanglearning.com/2024/02/5e0af7009c83c3ff4c9ed318eb1f8bc5.jpeg)

### 14、Linux 教程学习项目

这是一个非常不错的 Linux 教程学习项目 linux-tutorial，主要内容包括 Linux 命令、Linux 系统运维、软件运维、精选常用 Shell 脚本、Docker 教程。 

电子书阅读 [https://dunwu.github.io/linux-tutorial/](https://t.co/Ej7aKkz8op) 

Docker 在这里 [https://github.com/dunwu/linux-tutorial/tree/master?tab=readme-ov-file#docker](https://t.co/sXvyKuBNlZ)

![Image](https://r2.zhanglearning.com/blog/2024/02/0e3beeb9fc3814e50dd51fe10bed5c65.jpeg)



### 15、python-mini-project

https://github.com/ndleah/python-mini-project

一系列简单的 Python 小项目，帮助你提高编程技能。

![](https://r2.zhanglearning.com/blog/2024/02/d69d8d6f266332b15224264316ecc53f.png)
