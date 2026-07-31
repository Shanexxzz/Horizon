---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 32 条内容中筛选出 10 条重要资讯。

---

1. [DeepSeek V4 Flash 0731 低价带来前沿级性能](#item-1) ⭐️ 9.0/10
2. [YC 开源 QM：多人智能体工作协作框架](#item-2) ⭐️ 8.0/10
3. [OpenAI 发布全栈战略，以构建充裕且可负担的人工智能](#item-3) ⭐️ 8.0/10
4. [无状态 MCP 2.0 重新点燃对模型上下文协议的兴趣](#item-4) ⭐️ 8.0/10
5. [smevals：用于模型、提示词和测试框架评估的小型评测套件](#item-5) ⭐️ 8.0/10
6. [OpenAI 下调 GPT-5.6 Luna 价格 80%，用 Sol 优化推理](#item-6) ⭐️ 8.0/10
7. [电梯算法探析：SCAN 调度与目的地派梯的设计权衡](#item-7) ⭐️ 7.0/10
8. [Go 提议为标准库 container 包添加泛型集合类型](#item-8) ⭐️ 7.0/10
9. [2026 年 Instagram 涨粉的 13 个实战策略](#item-9) ⭐️ 7.0/10
10. [MiniMax H3：面向动态设计与品牌的一体化视频生成工具](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Flash 0731 低价带来前沿级性能](https://artificialanalysis.ai/models/deepseek-v4-flash) ⭐️ 9.0/10

DeepSeek 发布了 DeepSeek V4 Flash 0731，这是 DeepSeek-V4 系列的预览版本，以极低的价格提供前沿级智能。社区分析显示，它在某些任务上可以与更昂贵的 GLM 5.2 和 Gemini 3.6 等模型匹敌甚至胜出。 此次发布意义重大，因为它在更低的价位上实现了前沿级性能，可能重塑 AI 模型的价格-性能格局。对于编码和生产力工具的开发者及重度用户来说，他们将从大幅降低的 token 成本中获益，而无需牺牲质量。 DeepSeek V4 Flash 是一个拥有 284B 参数的混合专家模型，激活参数为 13B，上下文窗口为 1M token，针对快速编码和智能体任务进行了优化。社区报告显示其输出价格约为每百万 token 0.28 美元，并且 Unsloth 无损 Q8 量化后仅 162GB，使其可以本地部署。

hackernews · theanonymousone · 7月31日 07:59 · [社区讨论](https://news.ycombinator.com/item?id=49120299)

**背景**: DeepSeek V4 Flash 0731 属于 DeepSeek-V4 开源权重模型系列，采用混合专家架构，每次只激活总参数的一小部分，从而在质量与效率之间取得平衡。GLM 5.2 和 Gemini 3.6 分别是 Z.ai 和 Google 近期推出的旗舰模型，以强大的推理和编码能力著称。AI 社区越来越关注价格-性能比而不仅仅是原始基准分数，因此低成本的前沿模型尤其具有颠覆性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash/modelcard">deepseek-v4-flash Model by Deepseek-ai | NVIDIA NIM</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek-v4-flash - ollama.com</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/">Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，用户称 DeepSeek V4 Flash 是‘很棒’的日常驱动模型，让全天候编码变得负担得起，不再有‘token 焦虑’。评论者强调它以每百万输出 token 约 0.28 美元的价格提供了前沿级性能，并猜测即将推出的 V4 Pro 可能与 Opus 5 竞争，同时提到即将发布的优化版 DeepSeek Harness 智能体框架。另有旁支讨论质疑 Hugging Face 大规模文件托管的经济性。

**标签**: `#deepseek`, `#ai-models`, `#price-performance`, `#coding-assistant`, `#frontier-ai`

---

<a id="item-2"></a>
## [YC 开源 QM：多人智能体工作协作框架](https://github.com/yc-software/qm) ⭐️ 8.0/10

Y Combinator 已将 QM 开源，这是一个面向工作的多人智能体（agent）协作框架，让团队能在共享房间内协调多个 AI 智能体，并支持按人设置作用域。该工具源于 YC 内部运行 50 多个智能体的经验，设计初衷是像 OpenClaw 或 Hermes 一样易于定制。 QM 解决了多智能体系统中作用域这一难题：共享房间加上按人设置作用域，为全公司范围的 AI 助手提供了一种可行的模式。这验证了多人智能体协作框架这一新兴类别，并可能影响未来工作场景中团队与 AI 的协作方式。 该框架是开源的，专为公司级使用而设计，为每位员工和每个项目提供类似 OpenClaw 的智能体。它采用共享房间加按人作用域的模型来协调智能体，同时保持个人上下文和权限的隔离。

hackernews · tosh · 7月31日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=49126604)

**背景**: 智能体框架（agent harness）是围绕大语言模型（LLM）的软件基础设施，通过管理工具、记忆、持久化和反馈循环，使其能够充当 AI 智能体。多智能体协调则是让多个 AI 智能体协作完成复杂任务的做法，通常会将工作分解给专门化的智能体。QM 基于这些理念，提供了一个多智能体环境，YC 在内部使用后现已将其开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qm.ycombinator.com/index.html">QM — Open-Source Agent Harness from YC</a></li>
<li><a href="https://www.linkedin.com/posts/y-combinator_weve-decided-to-open-source-a-multi-agent-activity-7489009583970193409-cn5p">We’ve decided to open-source a multi-agent harness we use ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者的态度既有热情也有怀疑。一位开发者称赞 QM 的“按人作用域加共享房间”是解决多智能体最难问题的合理方案，而另一位则指出理解这个产品做什么有难度，并希望与 Claude Cowork 等工具进行比较。一则关于智能体自行安排会议的幽默轶事，也凸显了自主智能体的潜力与隐忧。

**标签**: `#AI agents`, `#productivity`, `#collaboration`, `#YC`, `#work tools`

---

<a id="item-3"></a>
## [OpenAI 发布全栈战略，以构建充裕且可负担的人工智能](https://openai.com/index/building-abundant-intelligence) ⭐️ 8.0/10

OpenAI 发布了一篇题为《构建充裕智能》的博客文章，阐述了其开发人工智能的全栈方法。这篇文章介绍了该公司计划如何让先进的人工智能更强、更实惠且应用更广泛。 这一战略公告表明 OpenAI 打算整合人工智能整个技术栈，这可能会加速各行业对 AI 的采用，并使尖端智能成为低成本的大宗商品。它使 OpenAI 不仅仅是一个模型提供商，还成为一家全栈 AI 基础设施和应用公司。 文章摘要仅强调了“全栈方法”，但现有内容中没有具体的技术路线图。“充裕智能”的概念表明其重点是通过扩展 AI 基础设施来降低成本、扩大使用范围。

rss · OpenAI News · 7月31日 15:00

**背景**: 全栈 AI 是一种公司构建跨硬件、软件、模型和应用的集成方案，而不是只关注单一层面的战略。OpenAI 的做法似乎与谷歌等竞争对手一致，谷歌长期以来一直将其 AI 工作描述为全栈。其目标是使 AI 能力像电力一样无所不在且价格实惠，这种愿景常被称为“充裕智能”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/full-stack-ai-explainer/">A Google expert explains full-stack AI and full-stack development</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-06-30-understanding-the-full-stack-ai-approach-why-google-experts-consider-it-the-foundation-of-modern-inn">Understanding the Full-Stack AI Approach with Google Experts</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#Artificial Intelligence`, `#Technology`, `#Productivity`

---

<a id="item-4"></a>
## [无状态 MCP 2.0 重新点燃对模型上下文协议的兴趣](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

2026 年 7 月 28 日，Model Context Protocol 2.0 规范（又称 Stateless MCP）发布，将 MCP 从基于会话的有状态协议改为单请求的无状态协议。此前因 Claude Skills 而对 MCP 兴趣减弱的 Simon Willison 本周构建了三个 MCP 实现，包括 mcp-explorer 和 datasette-mcp。 这次规范更新大幅降低了构建 MCP 客户端和服务端的复杂度，使该协议对可扩展 Web 应用和较小的端侧模型更具吸引力。在被 Skills 抢走风头之后，它可能重振 MCP 在 AI 代理工具生态中的势头。 在新的无状态流程中，客户端通过一个 HTTP POST 请求即可完成工具调用，请求头包含 MCP-Protocol-Version 和 Mcp-Method，正文为 JSON-RPC；不再需要先初始化会话并跟踪 Mcp-Session-Id。这消除了服务端会话状态，也无需将同一会话的请求路由到同一台后端机器。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP 是 Anthropic 于 2024 年 11 月推出的开放标准，旨在规范 AI 助手连接外部工具和数据源的方式。它在 2025 年受到广泛关注，但后来被 Claude Skills 抢走了一部分风头，因为拥有终端和 curl 的代理框架可以更灵活地完成 MCP 的大部分工作。新的无状态设计旨在让 MCP 更简单，也更适合现代无服务器架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://newrelic.com/blog/ai/mcp-is-going-stateless">MCP is going stateless : What the new spec means for AI... | New Relic</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI tools`, `#agent workflows`, `#model context protocol`, `#developer tools`

---

<a id="item-5"></a>
## [smevals：用于模型、提示词和测试框架评估的小型评测套件](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 8.0/10

Simon Willison 与 Prime Radiant 发布了 smevals，这是一个新的开源工具，用于在不同模型配置上运行小型评测套件并给结果打分。该工具可通过 uvx 命令（如 run、grade、serve、build）使用，并已发布到 PyPI 和 GitHub。 smevals 降低了评估模型、提示词和测试框架的门槛，使个人开发者和小团队也能方便地运行有针对性的评测。它以轻量级、命令行驱动的工作流，补充了 EleutherAI 的 lm-evaluation-harness 等更重量级的框架。 该工具定义了清晰的术语：eval 是一组 task，每个 task 针对一个或多个 config 执行，run 与评分阶段分离，由执行一系列 check 的 grader 完成。用户可以在本地 Web 服务器查看结果，或通过 build 命令导出为静态 HTML。

rss · Simon Willison · 7月31日 21:15

**背景**: 评估大语言模型通常需要运行基准测试，并将输出与预期结果对比，这往往需要较重的基础设施。uvx 是 Astral 的 uv 项目提供的命令运行器，可以下载并运行 Python 工具，无需单独安装。smevals 顺应了轻量级评测框架的趋势；EleutherAI 的 lm-evaluation-harness 是另一个广泛使用的、面向 few-shot 基准评测的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/prime-radiant-inc/smevals">GitHub - prime-radiant-inc/smevals: A framework for running ...</a></li>
<li><a href="https://pypi.org/project/smevals/">smevals · PyPI</a></li>
<li><a href="https://docs.astral.sh/uv/guides/tools/">Using tools | uv - Astral</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#eval suite`, `#LLMs`, `#developer workflow`, `#open source`

---

<a id="item-6"></a>
## [OpenAI 下调 GPT-5.6 Luna 价格 80%，用 Sol 优化推理](https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布大幅下调 GPT-5.6 系列模型价格：Terra 降价 20%，Luna 降价 80%。他们还透露，使用 GPT-5.6 Sol 优化推理，将端到端服务成本降低了 20%；Luna 目前输入每百万 token 收费 0.20 美元，输出每百万 token 收费 1.20 美元。 Luna 的新定价使其比 Google 的 Gemini 3.1 Flash-Lite 更便宜，输入成本仅为 Anthropic 的 Claude Haiku 4.5 的五分之一，重塑了低成本 LLM 市场格局。利用 AI 模型优化自身的服务栈展示了一种新的效率循环，可能降低整个行业的成本。 OpenAI 将降价归功于 GPT-5.6 Sol 优化了前向传播，并用 Triton 和 Gluon 这两种开源 GPU 编程语言重写了生产环境的 kernel。这些内核改进加上更广泛的优化使服务成本降低了 20%，也为此次降价提供了支撑。

rss · Simon Willison · 7月30日 23:58

**背景**: 前向传播是神经网络中将输入数据转换为预测结果的过程，涉及大量矩阵运算和内存搬运，容易导致 GPU 闲置。推理优化技术，如重写 kernel、负载均衡和预计算，能够在服务大语言模型时降低延迟和成本。OpenAI 使用先进 AI 模型 GPT-5.6 Sol 来自动完成这一优化，彰显了 AI 辅助基础设施调优的日益增长趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Feedforward_neural_network">Feedforward neural network - Wikipedia</a></li>
<li><a href="https://nebius.com/blog/posts/inference-optimization-techniques-solutions">Inference optimization techniques and solutions</a></li>
<li><a href="https://www.ankursnewsletter.com/p/inference-optimization-strategies">Inference Optimization Strategies for Large Language Models: Current Trends and Future Outlook</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#GPT-5.6`, `#pricing`, `#efficiency`

---

<a id="item-7"></a>
## [电梯算法探析：SCAN 调度与目的地派梯的设计权衡](https://john.fun/elevators) ⭐️ 7.0/10

john.fun 上的一篇新文章探讨了电梯算法及其设计权衡，涵盖 SCAN 调度、目的地派梯和真实世界中的用户体验怪癖。该帖在 Hacker News 上获得了 806 分和 207 条评论，读者补充了技术背景和实际观察。 电梯调度是优化和系统思维的典型缩影，像 SCAN 这样的算法也被用于硬盘调度。这场讨论为关注产品与技术的读者提供了关于延迟、批处理和用户体验权衡的通用思维模型。 SCAN 又称电梯算法，是一种磁盘调度算法：电梯沿一个方向逐一响应请求，到达端点后再反向。目的地派梯系统通过楼层选择终端按目的地将乘客分组；但有评论者指出，这类算法的效果很大程度上取决于真实客流模式，例如午休时成群出发的情况。

hackernews · Jrh0203 · 7月31日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49124218)

**背景**: 电梯调度决定多部轿厢如何响应楼层呼叫，需要在等待时间、乘梯时间和能耗之间取得平衡。SCAN 类似磁盘读写臂的扫掠方式：沿一个方向服务请求直到端点再折返；而目的地派梯则根据乘客输入的楼层为他们分配特定电梯，从而减少停靠次数。奥的斯等厂商的安装方案中广泛使用了这一技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Destination_dispatch">Destination dispatch - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/scan-elevator-disk-scheduling-algorithms/">SCAN (Elevator) Disk Scheduling Algorithms - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 读者反响热烈：有人回忆高中时模拟电梯算法的经历，并将 SCAN 与磁盘调度联系起来；也有人用真实办公楼中的客流模式反驳文章对目的地派梯的批评。还有读者分享了电梯调度游戏，并吐槽无法取消误按的楼层按钮，技术讨论中夹杂着轻松的 UX 抱怨。

**标签**: `#algorithms`, `#systems thinking`, `#UX design`, `#optimization`, `#mental models`

---

<a id="item-8"></a>
## [Go 提议为标准库 container 包添加泛型集合类型](https://github.com/golang/go/issues/80590) ⭐️ 7.0/10

一个新提案（golang/go\#80590）建议在标准库的 container 包中添加泛型集合类型，例如集合（set）和类型化堆（typed heap）。该提案基于 Go 1.18 引入的泛型功能。 这件事意义重大，因为 Go 开发者长期希望有一流的泛型集合库，标准实现有助于提高代码复用、类型安全和生态一致性。它也引发了关于泛型在多大程度上契合 Go 设计哲学的广泛讨论。 该提案明确针对 container 包，社区评论指出集合（set）或类型化堆（typed heap）这类功能早该加入。此提案尚未被接受或发布；一些评论者担心在类型中混入修改方法不太符合 Go 的惯用风格，另一些人则希望 Go v2 能在更底层解决泛型问题。

hackernews · jabits · 7月31日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=49127031)

**背景**: Go 1.18 引入了泛型，使函数和类型可以通过类型参数与约束处理多种类型。然而，在 Go 中编写泛型集合类型仍存在许多陷阱，例如指针接收者约束以及处理 comparable 接口时的变通方法。标准库中的 container/heap 和 container/list 等容器早于泛型出现，依赖 interface\{\} 或手工包装，因此泛型版本将使其现代化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/doc/tutorial/generics">Tutorial: Getting started with generics - The Go Programming ...</a></li>
<li><a href="https://www.dolthub.com/blog/2024-07-01-golang-generic-collections/">Writing generic collection types in Go : the missing... | DoltHub Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持积极态度，例如“好饭不怕晚”和“终于来了！”，但也有人担心在现有语言上打补丁式地加入泛型并不理想，希望 Go v2 能从根本上解决。有人希望不要混入修改方法，还有人调侃 Go 正在重学其他语言二十多年前就学到的东西。

**标签**: `#golang`, `#generics`, `#programming`, `#standard library`, `#proposal`

---

<a id="item-9"></a>
## [2026 年 Instagram 涨粉的 13 个实战策略](https://buffer.com/resources/grow-on-instagram/) ⭐️ 7.0/10

Buffer 发布了一份指南，作者本人拥有超过 1.5 万粉丝，并帮助 Buffer 的 Instagram 账号增长至 10 万以上，其中列出了 13 条经过验证的 2026 年 Instagram 涨粉策略。 这很重要，因为 Instagram 上的自然触达竞争日益激烈，基于实证的可执行策略能帮助创作者和品牌在不依赖付费广告的情况下积累受众。它为创作者经济提供了一个可信、实用的资源。 该指南称这些策略“经过验证”，来自作者个人超过 1.5 万粉丝的经验以及 Buffer 账号超过 10 万粉丝的实践。摘要内容中未列出这 13 条策略的具体明细。

rss · Buffer · 7月31日 07:40

**背景**: 在创作者经济中，Instagram 粉丝是创作者和品牌重要的社交资产。Buffer 是一家知名的社交媒体管理平台，同时也会发布关于增长策略的教育内容。由于算法变化，Instagram 上的自然涨粉变得愈发困难，因此具体且经过验证的策略更有价值。

**标签**: `#Instagram`, `#audience growth`, `#social media strategy`, `#creator economy`, `#content marketing`

---

<a id="item-10"></a>
## [MiniMax H3：面向动态设计与品牌的一体化视频生成工具](https://www.producthunt.com/products/minimax) ⭐️ 6.0/10

MiniMax H3（又称 Hailuo 3.0）是 MiniMax 最新的人工智能视频生成模型，于 2026 年 WAIC 大会发布，现已在 Product Hunt 上作为面向动态设计与品牌的一体化视频生成工具推出。早期评测显示其支持 2K 分辨率、15 秒片段和原生音频。 该发布对设计师和品牌创作者意义重大，因为它提供了一个强大的 AI 工具，无需专业技能即可制作高质量动态图形，可能改变动画内容的制作方式。它也展示了 AI 视频生成技术正快速融入动态设计与品牌等专业创意流程。 关键功能包括 2K 视频生成、15 秒片段长度、原生音频、Omni Reference 风格控制、视频延长功能以及更优的角色一致性。早期定价信息已公布，但 Hailuo 及合作平台仍在逐步推出中。

rss · Product Hunt · 7月31日 03:17

**背景**: MiniMax 是一家总部位于上海的人工智能公司，以开发多模态 AI 模型和消费级应用而闻名，包括 AI 角色应用 Talkie 和 Xingye，以及视频生成服务 Hailuo AI。H3（又称 Hailuo 3.0）是 MiniMax 视频生成模型的最新版本，在 2026 年 WAIC 大会上首次亮相。动态设计（Motion Design）是本工具聚焦的领域，它是将排版、形状和图像等图形元素与运动相结合来制作动画视觉内容的学科。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group</a></li>
<li><a href="https://www.orcarouter.ai/blog/minimax-h3-hailuo-3-explained">MiniMax H3 (Hailuo 3.0): 2K AI Video, Explained - orcarouter.ai</a></li>
<li><a href="https://apidot.ai/blog/minimax-h3-review">MiniMax H3 Review: Features, Quality, Pricing and Early Tests</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#content creation`, `#motion design`, `#branding`, `#creator tools`

---