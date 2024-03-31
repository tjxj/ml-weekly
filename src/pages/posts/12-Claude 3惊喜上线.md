---
date: 2024/03/12
---
<img src="https://r2.zhanglearning.com/blog/2024/03/adcd4619df37b2899137485d1f7b54e0.png" width="800" />  


<small>Anthropic 最新发布的 Claude 3 号称多方便暴打 GPT-4</small>

目录

1、NotionNext 静态博客系统

2、ComfyUI SUPIR 图像放大

3、MLX 框架在 Apple Silicon 上与本地数据聊天

4、适合 Claude 3 的编程 prompt

5、Cloudflare 发布 AI 防火墙

6、知识分享：网络协议

7、工具推荐:Git 客户端

8、北京大学 Open-Sora 计划

9、Claude 3 惊喜上线

10、Claude 3 Opus 的测试案例

11、0rama 全文搜索服务

12、D-ID Agents:真正的数字分身

13、CS-Ebook:经典计算机书籍推荐清单

14、桌面摆放的参考站点 Zetups

### 1、NotionNext 静态博客系统

一个使用 NextJS + Notion API 实现的，部署在 Vercel 上的静态博客系统。为 Notion 和所有创作者设计。

地址：https://github.com/tangly1024/NotionNext

![](https://r2.zhanglearning.com/blog/2024/03/244b603c8fdc4ac456f6e5c475efa605.png)

- **框架**: [Next.js](https://nextjs.org/)
- **样式**: [Tailwind CSS](https://www.tailwindcss.cn/)
- **渲染**: [React-notion-x](https://github.com/NotionX/react-notion-x)
- **评论**: [Twikoo](https://github.com/imaegoo/twikoo), [Giscus](https://giscus.app/zh-CN), [Gitalk](https://gitalk.github.io/), [Cusdis](https://cusdis.com/), [Utterances](https://utteranc.es/)
- **图标**: [Fontawesome](https://fontawesome.com/v6/icons/)

### 2、ComfyUI SUPIR 图像放大

ComfyUI SUPIR 一个 ComfyUI 的图像放大节点，演示效果看起来非常好，是 SUPIR 图像放大项目的 ComfyUI 实现。需要下载 10G 放大模型。 

项目地址：[https://github.com/kijai/ComfyUI-SUPIR?tab=readme-ov-file](https://t.co/TNKHyNEatP)

![](https://r2.zhanglearning.com/blog/2024/03/b665d5957fb0fd7a55bd7e9f56880fb4.gif)

### 3、MLX 框架在 Apple Silicon 上与本地数据聊天

项目地址：https://github.com/qnguyen3/chat-with-mlx

支持的数据：doc(x), pdf, txt and YouTube video via URL.
轻松集成：任何兼容 HuggingFace 和 MLX 的开源模型。

![](https://r2.zhanglearning.com/blog/2024/03/60467281483a99bbff0e15dd373ac795.gif)

### 4、适合 Claude 3 的编程 prompt

```
<prompt_explanation>
You are a world expert in making code run faster. You use any resource you can to do so.

Given some code, first, explain how the code works to me.

Next, for each part of the code, identify how long it might take to run.

After that, identify which parts are key candidates to speed up.

Then, make a table with axes 'Impact' and 'Complexity'. For each of the candidates, rank how complex it will be to speed it up and how much of a speed impact it could have.

After that, order the candidates by ranking.

Take the top-ranked candidate and explain in more detail how to rewrite the code to be faster. Then, rewrite the actual code. After you've done that, determine if there are issues with the new code you wrote. If so, move on. Otherwise, rewrite the code again to fix them.

Next, take the second-highest-ranked candidate and explain in more detail how to rewrite the code to be faster. Then, rewrite the actual code. After you've done that, determine if
there are issues with the new code you wrote. If so, move on. Otherwise, rewrite the code again to fix them.

Then do the same for the third-highest-ranked candidate.

Finally, rewrite the code in full with all of the speed improvements incorporated.
</prompt_explanation>

Here is the format you should respond in:
<response_format>
## Explanation:
$explanation

## Runtime Analysis: 
$runtime_analysis

## Key Candidates for Speed Up:
$candidates

## Impact and Complexity Table:
| Candidate | Impact | Complexity |
| --------- | ------ | ---------- |
$candidate_table

## Candidates Ordered by Ranking:
$ordered_candidates

## Detailed Explanation and Code Rewrite for Top Candidate: 
# Explanation
$top_candidate_explanation

# Code Rewrite
$top_candidate_code

# Issues with New Code: *(include this section only if they exist)*
$top_candidate_issues

# Code Rewrite, Try 2: *(include this section only if issues exist)*
$top_candidate_code_try2

## Detailed Explanation and Code Rewrite for Second-Highest Candidate: 
# Explanation
$second_candidate_explanation

# Code Rewrite
$second_candidate_code

# Issues with New Code: *(include this section only if issues exist)*
$second_candidate_issues

# Code Rewrite, Try 2: *(include this section only if issues exist)*
$second_candidate_code_try2

## Detailed Explanation and Code Rewrite for Third-Highest Candidate: 
# Explanation
$third_candidate_explanation

# Code Rewrite
$third_candidate_code

# Issues with New Code: *(include this section only if issues exist)*
$third_candidate_issues

# Code Rewrite, Try 2: *(include this section only if issues exist)*
$third_candidate_code_try2

## Full Code Rewrite with Speed Improvements:
$full_code_rewrite
</response_format>
```



### 5、Cloudflare 发布 AI 防火墙

https://blog.cloudflare.com/firewall-for-ai

Cloudflare 宣布开发了针对使用大型语言模型（LLM）的应用程序的防火墙，以防止滥用和攻击。

评论讨论了审查制度的影响、AI 模型的局限性以及检测提示注入攻击的挑战。

还就 AI 安全背景下提示注入和越狱的定义展开了辩论。

![*Firewall for AI 的工作方式类似于传统的 Web 应用程序防火墙。它部署在 LLM 应用程序前面，并扫描每个请求以识别攻击特征。*](https://r2.zhanglearning.com/blog/2024/03/3bb2a3fe4a187b966f0365ef2a98ea9b.png)

### 6、知识分享：网络协议

![](https://r2.zhanglearning.com/2024/03/8fd8251dd8bc1dc919334be5213c160a.gif)

1. HTTP（超文本传输协议）

HTTP 是用于获取诸如 HTML 文档之类资源的协议。它是 Web 上任何数据交换的基础，是一种客户端 - 服务器协议。

2. HTTP/3

HTTP/3是HTTP的下一个主要修订版。它运行在QUIC之上，QUIC是为移动重型互联网使用而设计的新传输协议。它依赖UDP而不是TCP，这使得网页响应更快。虚拟现实应用需要更多带宽来渲染复杂的虚拟场景，并将可能从迁移到由QUIC支持的HTTP/3中受益

3. HTTPS（超文本传输协议安全）

HTTPS 扩展了 HTTP 并使用加密进行安全通信。

4. WebSocket

WebSocket 是一种在 TCP 上提供全双工通信的协议。客户端建立 WebSocket 以从后端服务接收实时更新。与始终“拉取”数据的 REST 不同，WebSocket 使数据可以被“推送”。应用程序，如在线游戏、股票交易和消息应用程序利用 WebSocket 进行实时通信

5. TCP（传输控制协议）

TCP 旨在通过互联网发送数据包，并确保在网络上成功传递数据和消息。许多应用层协议都建立在 TCP 之上

5. UDP（用户数据报协议）

UDP 直接将数据包发送到目标计算机，无需先建立连接。UDP 通常用于时间敏感的通信，其中偶尔丢包比等待更好。语音和视频流量通常使用此协议发送。

7. SMTP（简单邮件传输协议）

SMTP 是一种标准协议，用于将电子邮件从一位用户传输给另一位用户

FTP（文件传输协议）

FTP 用于在客户端和服务器之间传输计算机文件。它具有用于控制通道和数据通道的独立连接

### 7、工具推荐：Git 客户端

一个颜值和实用性都不错的 Git 客户端，很酷，做得很好，特别对于多分支管理的场景下。 🤖 [https://gitbutler.com](https://t.co/4fuIjcYhCO)

![](https://r2.zhanglearning.com/blog/2024/03/9aa675cec15afe597e0e5bbf7ccaacf1.png)

### 8、北京大学 Open-Sora 计划

北京大学 Yuangroup 团队发起了一个 Open-Sora 计划旨在复现 OpenAI 的 Sora 模型

Open-Sora 计划通过视频 VQ-VAE、Denoising Diffusion Transformer 和条件编码器等技术组件，来实现 Sora 模型的功能。

该项目现在支持：

可变长宽比
可变分辨率
可变持续时间


Open-Sora 计划实现了以下几个关键组件和特性来复现 OpenAI 的视频生成模型：

1、视频 VQ-VAE（Vector Quantized-Variational AutoEncoder）：这是一个压缩视频到时间和空间维度的潜在表示的组件。它可以将高分辨率视频压缩成低维度的表示，便于后续的处理和生成。

2、去噪扩散变换器（Denoising Diffusion Transformer）：这个组件用于从潜在表示中生成视频，通过逐步减少噪声来恢复视频的详细内容。

3、条件编码器（Condition Encoder）：支持多种条件输入，允许模型根据不同的文本描述或其他条件生成视频内容。

此外，项目还实施了几项技术以增强视频生成的灵活性和质量：

1、可变长宽比：通过动态遮罩策略并行批量训练，保持灵活的长宽比。将高分辨率视频调整大小以使最长边为 256 像素，保持长宽比，然后在右侧和底部用零填充以达到统一的 256x256 分辨率。

2、可变分辨率：尽管在固定的 256x256 分辨率上训练，但在推理过程中，使用位置插值使得可以进行可变分辨率采样。这使得注意力基础的扩散模型能够处理更高分辨率的序列。

3、可变持续时间：利用视频 VQ-VAE 压缩视频到潜在表示，实现多持续时间的视频生成。通过将空间位置插值扩展到时空版本，以处理可变持续时间的视频。

项目地址：https://pku-yuangroup.github.io/Open-Sora-Plan/blo...…

GitHub: https://github.com/PKU-YuanGroup/Open-Sora-Plan





### 9、Claude 3 惊喜上线

Claude 3 惊喜上线了！有三个版本：Haiku（中杯）、Sonnet（大杯）、Opus（超大杯），能力依次从低到高 Sonnet（大杯）

Claude 3 Sonnet 是可以免费试用的

体验地址：[App unavailable \ Anthropic](https://claude.ai/chats)

![](https://r2.zhanglearning.com/blog/2024/03/c5187dab4f361ce5d7d629d653c50a36.jpeg)

Claude 还推出了一个包含多样化创意 prompt 的 prompt 库。这非常适合那些想要深入了解和充分利用 Claude 3 新功能的朋友们。🤓

https://docs.anthropic.com/claude/prompt-library

![](https://r2.zhanglearning.com/blog/2024/03/ae6b4d025395c17da16079ce5db88aba.jpeg)

### 10、Claude 3 Opus 的测试案例

这个 Claude 3 Opus 的测试案例让人印象深刻，作者将 2 小时的视频文稿和一些关键帧的截图一起扔给 API，最终生成了一篇不错的 HTML 格式的图片并茂的博文。

项目地址：https://github.com/hundredblocks/transcription_demo

Prompt：
用户：这里有一段视频的文字记录，包括不同时间戳的屏幕截图。
该文字记录是由 AI 语音识别工具生成的，可能包含一些错误/不当之处。
你的任务是将文字记录转换为一个 html 博客。
博客的写作风格，包括文字和代码之间的期望平衡，在<desired_writing_style>的屏幕截图中有所说明。 
博客的视觉风格，包括页面布局、字体、标题和图像样式，在<desired_visual_style>中有所描述。

{transcript_with_name}  
<desired_writing_style>
{desired_writing_style}
</desired_writing_style>
<desired_visual_style> 
{desired_visual_style}
</desired_visual_style>

这份文字记录有一些噪音。请按照以下指南将其重写为一个 html 格式的博客：
- 输出有效的 html
- 在适当的地方插入章节标题和其他格式
- 使用样式使图像、文本、代码、标注和页面布局、边距看起来像<desired_visual_style>中的示例
- 删除任何口头禅
- 如果有重复的信息，只呈现一次 
- 用<desired_writing_style>中显示的风格改写对话内容，包括标题，使叙述结构更容易理解
- 每个文字记录包含太多图像，所以你的输出应该只包括最重要的 1-2 张图像
- 选择能提供与文字记录相关的插图的图像
- 优先包含显示完整代码的图像，而不是部分代码
- 在相关时转录重要的代码片段和其他有价值的文本
- 如果某个图像有助于说明文字记录的某个部分，请包含它
- 要包含图像，请插入一个带有 src="frames/hh_mm_ss.jpg"的标签 (例如"frames/00_12_35.jpg"),准确复制文字记录中图像上方插入的时间戳 
- 为图像添加标题
- 不要添加任何无关信息：只包括在文字记录或图像中提到的内容

你的最终输出应该适合收录到教科书中。

助手:<!DOCTYPE html>

### 11、Orama 全文搜索服务

官网：https://oramasearch.com

Node.js 新版官网使用了 Orama，它是非常火的全文搜索服务，全世界节点很多，速度很快，typescript 编写，大小小于 2K。

大家可以在 Node.js 官网感受一下速度，非常快。

支持自部署，并且还有完全免费的计划，如果只是小型网站的搜索，用免费的也足够了，未来打算接入使用试试看。

开源地址：https://github.com/askorama/orama
![](https://r2.zhanglearning.com/2024/03/541f9608ebb4d399e6b553707e3f3b50.png)

### 12、D-ID Agents：真正的数字分身

用你的照片做虚拟人，再克隆上你的声音，再上传文件来同步你的知识库，能实现只有 2 秒延迟的视频对话。
我试了下，目前一直提示不在线，体验不到真实的效果。
使用地址：https://studio.d-id.com/agents

### 13、CS-Ebook：经典计算机书籍推荐清单

 一个高质量、经典计算机书籍推荐清单，特点为：只收集高质量，各方向经典书籍，不求书多，只求书精。
https://github.com/lining808/CS-Ebook

### ![](https://r2.zhanglearning.com/2024/03/6999d7b323afa8cd8ec3a0a059371987.png)14、桌面摆放的参考站点 Zetups

给大家推荐一个桌面摆放的参考站点 Zetups： [https://zetups.com](https://t.co/mUAuZB8y6w) 

这个网站收集了 40+ 彰显逼格的桌面摆放案例，同时还把图中的设备型号都标注出来了，对我这个没什么艺术细菌的人而言简直是宝藏！赶紧收藏起来，学起来！

![](https://r2.zhanglearning.com/blog/2024/03/c5957e416452487464b56cb4cd302b3e.png)
