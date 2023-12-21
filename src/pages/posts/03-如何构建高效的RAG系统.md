##  如何“学习AI”？

最近X上有推友重提这篇文章，是网友看过 Jeremy 教授的 fast.ai 深度学习课程后，把每节课提到的学习建议和忠告都总结了下来：https://forums.fast.ai/t/things-jeremy-says-to-do/36682/1

我让ChatGPT、Claude、Gemini翻译并总结了这篇文章，Gemini完成的更加出色，给出了26条关于学习方法和一些细节的建议（我建议，如果时间允许，可以看原文）：

1. **倾听：**仔细注意老师在整堂课中的建议和提示。
2. **不要被理论淹没：**专注于运行代码并对其进行实验，而不是一开始就陷入理论细节中。
3. **选择一个项目并把它做得精彩：**选择一个你感兴趣的项目，并投入额外的精力，确保对其进行优化和改进。
4. **探索不同的数据集：**不要局限于课程中提供的数据集；自己寻找数据集并对其进行实验。
5. **不要使你的代码过于复杂：**保持你的代码简单和有条理，避免不必要的复杂性。
6. **学习 Jupyter 快捷键：**熟悉 Jupyter 快捷键以提高你的效率。
7. **运行代码并对其进行实验：**不要只阅读代码；运行它并尝试不同的输入和参数来观察会发生什么。
8. **不要花几个小时试图立即理解所有理论：**可以先不理解所有内容；专注于实践方面，并随着时间的推移逐渐加深你的理解。
9. **阅读比赛获胜者的论文：**通过阅读比赛获胜者的论文来学习他人的成功经验，注意他们的方法和见解。
10. **使用你拥有的所有文本：**在处理 NLP 时，确保使用所有可用的文本，包括未标记的验证集，以增强模型的性能。
11. **学会发音希腊字母：**熟悉深度学习论文中常用的希腊字母的发音。
12. **非常习惯 PyTorch 张量：**培养对 PyTorch 张量和运算的扎实理解。
13. **应用广播规则：**在处理更高秩张量时学习并应用广播规则。
14. **不要假设库是正确的：**对库持怀疑态度；验证其正确性并了解其工作原理。
15. **不要担心你是否跟上了所有内容：**感到不知所措是正常的；专注于你能理解的内容，并逐渐建立你的知识。
16. **学会调试深度学习代码：**调试 DL 代码具有挑战性；确保你的代码简单，并检查中间结果以尽量减少错误。
17. **用玩具问题进行实验：**创建并解决玩具问题以深入了解深度学习的概念和技术。
18. **学习 Swift for TensorFlow：**抓住机会学习 Swift for TensorFlow，它为 DL 开发提供了优势。
19. **为 Swift for TensorFlow 生态系统做出贡献：**通过为代码、文档或讨论做出贡献来参与 Swift for TensorFlow 社区。
20. **使用 `compose` 进行函数组合：**使用 `compose` 函数熟悉函数组合的概念。
21. **谨慎的数据增强：**在增强数据时，仔细考虑转换及其对数据完整性和标签准确性的影响。
22. **尝试不同的架构：**尝试不同的神经网络架构以深入了解它们的性能特征。
23. **不要冻结批归一化层：**避免在微调期间冻结批归一化层，以确保适当的权重更新。
24. **尽可能以原始方式预处理数据：**作为一般规则，尽量减少对神经网络数据的预处理，以保留其原始信息和结构。
25. **学习 Swift for TensorFlow：**抓住机会学习 Swift for TensorFlow，它为 DL 开发提供了优势。
26. **自定义 Swift for TensorFlow：**Swift for TensorFlow 是完全可自定义的，允许你修改和扩展它以满足你的特定需求。

![](https://my-wechat.oss-cn-beijing.aliyuncs.com/GBiHzOKaUAAIhZg.jpeg)

## 如何构建高效的RAG系统

![Devv AI 是面向开发者的新一代 AI 搜索引擎](https://my-wechat.oss-cn-beijing.aliyuncs.com/image-20231218094549227.png)

程序员Jiayuan (Forrest)在X上分享了开发者搜索工具 devv.ai 是如何构建RAG系统的过程，内容十分硬核。

这里是Treads汇总：https://typefully.com/Tisoga/PBB58Vu



## MLC Chat

MLC Chat：在iPhone上离线运行7B最强LLM Mistral
中文不太行，速度很快，手机会发热
APP下载：https://apps.apple.com/gb/app/mlc-chat/id6448482937
Github：https://github.com/mlc-ai/mlc-llm

支持各种系统，能在各种设备上开发、优化和部署AI模型。包括iOS和安卓



## DreaMoving

DreaMoving是一个基于扩散模型的人类舞蹈视频生成框架。能够根据指导序列和简单的内容描述（仅文本提示、仅图像提示或文本和图像提示）生成高质量、高保真度的视频。

体验地址：[https://modelscope.cn/studios/vigen/video_generation/summary](https://t.co/xrsRBJnEKi)



## 苹果最新论文

苹果发的这个论文《使用有限的内存实现更快的 LLM 推理》。通过将将模型参数保存在闪存里，根据需要移动到DRAM。 使得能够运行的模型大小是**可用DRAM的两倍**，与传统的CPU和GPU加载方法相比，推理速度分别**提高了4-5倍和20-25倍**。

paper page: [https://huggingface.co/papers/2312.11514](https://t.co/SuqHJUQPO9)

## 《动手实战人工智能 Hands-on AI》

Tw93@HiTw93

这个《动手实战人工智能 Hands-on AI》写得很用心，作者从监督学习开始，带你入门机器学习和深度学习，他尝试剖析和推导每一个基础算法的原理，将数学过程写出来，同时基于 Python 代码对公式进行实现，做到公式和代码的一一对应。 

 [https://ai.huhuhang.com](https://t.co/1hDU5Ky2j7)

![Image](https://my-wechat.oss-cn-beijing.aliyuncs.com/GBjPdwrawAAMfRt.jpeg)

##  👉 机器学习调查



🔗 https://github.com/metrofun/machine-learning-surveys


有关主动学习、生物信息学、分类、度量学习、蒙特卡罗、多臂老虎机、多视图学习等方面的调查、教程和书籍的精选列表。

![Image](https://my-wechat.oss-cn-beijing.aliyuncs.com/GBxXnb-W4AA_uXW.png)
