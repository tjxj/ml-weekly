---
date: 2024/03/24
---

<img src="https://r2.zhanglearning.com/2024/03/74d578e84628fc98845d98f49993c58d.JPG" width="800" />  

<small>苹果据称正在与Google进行讨论，准备将Google的Gemini模型接入到iPhone</small>

1、用Excel 学习 ChatGPT 工作原理  
2、LLM Pricing、定价与速度测试  
3、学习OpenCv、深度学习和人工智能  
4、2024 年最受欢迎 Mac 开源应用程序  
5、苹果发布了自己的大语言模型 MM1  
6、xAI 的 Grok-1 开源  
7、黄仁勋集齐 Transformer 论文七大作者  
8、Homebrew GUl  
9、微软 AI 程序员 AutoDev 登场  
10、苹果与Google大声密谋  
11、一个优雅的短链服务:Dub    
12、推荐两篇文章:养老金是如何计算?​程序员学习CPU及计算机组成原理  

### 1、用Excel 学习 ChatGPT 工作原理

网址：https://spreadsheets-are-all-you-need.ai

用一个Excel 表格来学习 ChatGPT 的工作原理，不用写任何代码，配有三个Youtube 视频，非常形象。

最让人震惊的是它用 Excel 实现了一个简易的 GPT2，可以下载：不过特别大，有 1.25 个G，大家如果感兴趣可以试试看。

Excel 太强大了，干啥都行。


![](https://r2.zhanglearning.com/2024/03/bf574a602bd3f3872725efbc4671600a.png)

### 2、LLM Pricing、定价与速度测试
一个监控常用大模型API价格的网站（PS：这个网站使用Claude 3 Sonnet辅助编程完成的）

网址：https://llm-price.com/

![](https://r2.zhanglearning.com/2024/03/5d4c49e20d153c1eac024850398951f3.png)

有网友测试了各LLM 定价与速度 💰 ，用实验来比较推理成本与速度

任务：文本生成。

实验设置：
• 每个模型 10 次运行
• 最大输出令牌1000个
• 计算每次运行的成本
• 计算每秒的令牌数

主要要点：
• groq 在成本+速度方面明显获胜
• 集群速度接近 75-150tps，约 0.10 美元



![](https://r2.zhanglearning.com/2024/03/a7a1f308d65cac9c6d3a3049b8fdec01.png)




### 3、学习OpenCV、深度学习和人工智能
🔗 https://github.com/spmallick/learnopencv

 👉 该存储库包含计算机视觉、深度学习和人工智能文章的代码。
![](https://r2.zhanglearning.com/2024/03/22f3431fb1066ff02200c3c6375ec049.png)


### 4、2024 年最受欢迎 Mac 开源应用程序
快来看看有木有你喜欢的
网址：https://indiegoodies.com/awesome-open-source-mac-apps

![](https://r2.zhanglearning.com/2024/03/f7fa3b31ad653cd499ed9a01ddc64069.png)
![](https://r2.zhanglearning.com/2024/03/f7fa3b31ad653cd499ed9a01ddc64069.png)



### 5、苹果发布了自己的大语言模型 MM1

苹果加入战场，发布了自己的大语言模型 MM1，这是一个最高有 30B 规模的多模态 LLM 。

**论文关键信息：**

图像分辨率、图像编码器的预训练数据和模型大小对性能有显著影响。

视觉-语言连接器的设计相比之下影响较小。

预训练数据的混合比例对于少样本和零样本（zero-shot）性能至关重要。

通过预训练和SFT，MM1模型在多个基准测试中取得了SOTA性能。

MM1模型展现了一些吸引人的特性，如上下文内预测、多图像推理和少样本学习能力。

**模型实现方案：**

架构组件和数据选择的消融实验：

图像编码器：研究了不同预训练图像编码器的影响，以及图像分辨率和图像标记数量的重要性。

**视觉-语言连接器：**

探讨了不同类型的视觉-语言连接器（如平均池化、注意力池化和C-Abstractor）对模型性能的影响。
预训练数据：使用了图像标题、交错的图像-文本和纯文本数据，研究了这些数据类型及其混合比例对模型性能的影响。

**模型构建和预训练：**

通过扩大模型规模（从3B到30B参数），包括密集模型和混合专家（mixture-of-experts，简称MoE）变体，构建了一系列性能优越的多模态模型。

在预训练过程中，使用了大规模的多模态数据集，并通过特定的数据混合比例来训练模型。

**性能评估和结果：**

评估了预训练模型在多个基准测试中的性能，包括图像标题和视觉问答（VQA）任务。
通过监督式微调（Supervised Fine-Tuning，简称SFT），在一系列多模态基准测试中取得了有竞争力的性能。

论文地址：https://arxiv.org/pdf/2403.09611.pdf

### 6、xAI 的 Grok-1 开源 

马斯克开放了Grok的架构和权重数据，共 318.24GB ，这个尺寸肯定没法在本地玩了

🌐page: https://x.ai/blog/grok-os
🧬code: https://github.com/xai-org/grok-1
📦model: https://academictorrents.com/details/5f96d43576e3d386c9ba65b883210a393b68210e

为了 Understand the Universe 理念，团队特意把参数设定成了圆周率  314B，这是目前规模最大的开源模型。

Tesla 开放的技术与供应链推动了全球特别是中国 EV 进步，现在 xAI 应该能继续推工国产大模型的创新了。





![](https://r2.zhanglearning.com/2024/03/46830bc01961a30a80357ebf2c2be4a2.png)



### 7、黄仁勋集齐 Transformer 论文七大作者

对话一小时，干货满满

全文：https://mp.weixin.qq.com/s/Vxmlgh_ldJNa5RNwFSHmUA

Transformer模型的出现极大提升了计算机处理语言的能力，对机器翻译、语音识别和文本摘要等任务带来了显著的改进。

这项成果是由八位曾在Google工作的AI科学家共同完成的，他们的初衷是改进谷歌的机器翻译服务。

他们是：

Ashish Vaswani：2016年加入谷歌大脑团队。2022年4月，与Niki Parmar共同创办了Adept AI，同年12月离开该公司，并共同创立了另一家人工智能初创公司Essential AI。

Niki Parmar：在谷歌大脑工作了四年，之后与Ashish Vaswani共同创立了Adept AI和Essential AI。

Jakob Uszkoreit：2008年至2021年在谷歌工作。2021年离开谷歌，并与他人共同创立Inceptive，该公司主营业务为人工智能生命科学，致力于使用神经网络和高通量实验来设计下一代RNA分子。

Illia Polosukhin：2014年加入谷歌，是八人团队中最早离开的人之一，于2017年同他人共同创立了区块链公司NEAR Protocol。

Noam Shazeer：曾于2000年至2009年间和2012年至2021年期间就职于谷歌。2021年，Shazeer离开谷歌并与前谷歌工程师Daniel De Freitas共同创立http://Character.AI。

Llion Jones：曾工作于Delcam、YouTube。2012年加入谷歌，担任软件工程师。后来离开谷歌，创办人工智能初创企业http://sakana.ai。

Lukasz Kaiser：曾任法国国家科学研究中心研究员。2013年加入谷歌。2021年，他离开谷歌，成为OpenAI的研究员。

Aidan Gomez：毕业于加拿大多伦多大学，Transformer论文发表时，他还是谷歌大脑团队的实习生。他是八人团队中第二个离开谷歌的人。2019年，他与他人共同创立了Cohere。

对话过程中，与会者关于Transformer模型的讨论集中在以下几个方面：

1、Transformer的独特价值和创新点：讨论强调了Transformer模型的核心创新——自注意力机制，这一机制使得模型能够高效处理长距离依赖问题，相比传统的RNN和CNN架构，在序列数据处理上更加高效和精确。Transformer的编码器-解码器结构和多头注意力机制在人工智能领域引发了重大变革。

2、模型的实际应用与影响：Transformer模型的应用已经远远超出了最初的预期，它不仅被应用于自然语言处理任务，如文本生成、情感分析和语言翻译，还扩展到了计算机视觉、音频处理等多个领域。这种跨领域的应用证明了Transformer架构的强大和灵活性。

3、对于未来发展的展望：与会者表达了对当前Transformer模型及其变种的局限性的认识，以及对未来发展的期待。他们讨论了需要超越Transformer的新技术，以实现更高效的计算和更强的AI能力。特别是对于规模定律的讨论，即模型性能随着规模的扩大而提升，但同时需要更多的计算资源。

4、计算资源的考量：讨论提到了随着Transformer模型规模的扩大，对计算资源的需求也随之增加。这引发了对于如何更经济高效地使用计算资源的讨论，包括未来可能需要的自适应计算技术，以便在特定问题上合理分配计算资源。

5、对AI和计算未来的哲学思考：对话中还包含了一些关于AI技术和加速计算未来方向的深层次思考，包括计算机技术的发展趋势、AI模型的经济性和规模以及如何通过技术进步解决社会问题。

![](https://r2.zhanglearning.com/2024/03/3d052698d3fb7dec4e6eed1aba190c89.png)

### 8、Homebrew  GUI

🎉终于有人为 Homebrew 做 GUI 了。

网址：https://github.com/milanvarady/Applite

Applite 免费开源的 mac 程序，旨在简化 Homebrew 安装和管理第三方应用，为非技术用户带来 Homebrew casks 的便利。
🔸一键安装、更新及卸载应用
🔹简洁用户界面（UI）
🔹免费开源
🔹精心挑选的高质量应用合集
🔹兼容现有 Brew 安装环境

![](https://r2.zhanglearning.com/2024/03/5107c8ebb3d099e17c7c8025b1743e0a.jpeg)

### 9、微软 AI 程序员 AutoDev 登场

微软推出的 Autodev 自动化 AI 驱动开发领域实现了重大创新（号称自主生成代码性能超GPT-4 30%），通过允许用户为 A| 设定复杂目标并在 Docker 容器中实现代码编写、测试等开发活动。

该框架在 Human Evil 数据集上展现了超过 90% 的代码与测试生成成功率。网友热议其对软件开发效率的潜在提升和专业技能保持的挑战，同时对通用人工智能的实际应用、控制和道德问题以及广泛自动化可能带来的社会影响表示深切关注

![](https://r2.zhanglearning.com/2024/03/ea09109a671ddaeb8912220e1668e9a3.jpeg)

### 10、苹果与Google大声密谋

据消息人士称，苹果据称正在与Google进行讨论，准备将Google的Gemini模型接入到iPhone，为iPhone 提供人工智能的技术支持！ 

两家公司正在积极谈判，以便让苹果获得Google生成式人工智能模型 Gemini 的授权。

![](https://r2.zhanglearning.com/2024/03/74d578e84628fc98845d98f49993c58d.JPG)



### 11、一个优雅的短链服务：Dub

https://github.com/dubinc/dub

- 开源免费
- 支持数据分析
- 设计和使用体验上都非常极简

- [Next.js](https://nextjs.org/) – framework
- [TypeScript](https://www.typescriptlang.org/) – language
- [Tailwind](https://tailwindcss.com/) – CSS
- [Upstash](https://upstash.com/) – redis
- [Tinybird](https://tinybird.com/) – analytics
- [PlanetScale](https://planetscale.com/) – database
- [NextAuth.js](https://next-auth.js.org/) – auth
- [BoxyHQ](https://boxyhq.com/enterprise-sso) – SSO/SAML
- [Turborepo](https://turbo.build/repo) – monorepo
- [Stripe](https://stripe.com/) – payments
- [Postmark](https://postmarkapp.com/) – emails
- [Vercel](https://vercel.com/) – deployments

![Image](https://r2.zhanglearning.com/2024/03/c3bf0af4c25bbd67a08e3e36cdd93fd5.jpeg)



### 12、推荐两篇文章：

养老金是如何计算的？

https://fookwood.com/posts/pension-calculation/



程序员学习了解CPU及计算机组成原理必看文章

https://plantegg.github.io/2021/06/01/CPU%E7%9A%84%E5%88%B6%E9%80%A0%E5%92%8C%E6%A6%82%E5%BF%B5/


![](https://my-wechat.oss-cn-beijing.aliyuncs.com/WX20230912-203916-20231217213830903-20231222231724242.png)
