---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 33 条内容中筛选出 10 条重要资讯。

---

1. [AMD 收购 Taalas，将模型蚀刻进硅以提升 AI 推理性能](#item-1) ⭐️ 8.0/10
2. [马里奥赛车角色展示帕累托前沿：优化取舍的思维模型](#item-2) ⭐️ 8.0/10
3. [Qwen3.8 Max 登顶 Artificial Analysis Agentic Index](#item-3) ⭐️ 8.0/10
4. [谷歌 DeepMind WeatherNext 2 AI 模型实现气旋预报突破](#item-4) ⭐️ 8.0/10
5. [AI 时代，品味成为最终的不同之处](#item-5) ⭐️ 7.0/10
6. [OpenAI 改进 GPT-5.6 Sol，并向免费用户开放 GPT-5.6 Luna](#item-6) ⭐️ 7.0/10
7. [AI Agent 权限游戏数据：人类漏掉 1/3 威胁](#item-7) ⭐️ 7.0/10
8. [OpenAI 携手美国心理学会，推动青少年心理健康与负责任 AI](#item-8) ⭐️ 7.0/10
9. [Meta 发布 Muse Code，用于长周期编码任务的终端代理](#item-9) ⭐️ 7.0/10
10. [HubSpot AEO 与 Ahrefs Brand Radar：AI 可见性工具对比](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AMD 收购 Taalas，将模型蚀刻进硅以提升 AI 推理性能](https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344) ⭐️ 8.0/10

2026 年 8 月 6 日，AMD 宣布达成协议收购总部位于多伦多的 AI 芯片初创公司 Taalas。Taalas 的芯片将模型权重直接刻入硅片（硬接线），相比通用 GPU 有望将推理性能提升一个数量级或更多。 这笔交易可能重塑 AI 硬件格局，让推理更便宜、更快速，从而增强 AMD 相对于 NVIDIA 和谷歌 TPU 生态的竞争力。它也表明一种战略押注：面向特定模型的专用硅片将比通用加速器更重要。 Taalas 成立于 2023 年，创始人是前 AMD 和 NVIDIA 工程师、Tenstorrent 创始人 Ljubisa Bajic。由于芯片是为单一 AI 模型蚀刻的，模型快速迭代可能导致芯片量产时已落后一个或多个版本；不过，如果成本足够低，廉价推理仍会有市场。

hackernews · itvision · 8月6日 20:23 · [社区讨论](https://news.ycombinator.com/item?id=49201970)

**背景**: AI 推理是指用训练好的模型处理新数据并生成输出，通常作为软件运行在通用 GPU 上。将模型蚀刻进硅片，相当于把模型的结构和权重固化成专用硬件（类似 ASIC），用灵活性换取速度和效率。这与 Etched AI 的 Sohu 芯片思路相同——后者是专为 Transformer 自回归推理设计的 ASIC。AMD 的这笔收购看起来是为了在快速增长的 AI 推理市场中实现差异化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/06/amd-buys-taalas-startup-that-hardwires-ai-models-into-its-silicon.html">AMD buys Taalas, startup that hardwires AI models into its silicon</a></li>
<li><a href="https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344">AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon</a></li>
<li><a href="https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/">Etched AI Sohu vs NVIDIA: Transformer ASIC vs... | Spheron Blog</a></li>

</ul>
</details>

**社区讨论**: 评论区里既有兴奋也有质疑：有人认为未来‘寓言级’智能可能以当前百倍速度出现，让人感到迷失；也有人惊讶于 OpenAI 和 Anthropic 没有抢先收购。多位用户指出模型快速迭代的问题——固定硅片可能还没投产就已过时；还有人认为 AI 讨论常混淆‘峰值性能’与‘可靠性能’，而后者才是真正重要的。

**标签**: `#AMD`, `#AI hardware`, `#inference acceleration`, `#tech acquisition`, `#AI infrastructure`

---

<a id="item-2"></a>
## [马里奥赛车角色展示帕累托前沿：优化取舍的思维模型](https://www.mayerowitz.io/blog/mario-meets-pareto) ⭐️ 8.0/10

博客文章《马里奥遇见帕累托》借助《马里奥赛车》的角色选择来解释帕累托前沿，在速度与加速度的取舍坐标上标出库巴、奇诺比奥等角色。文章将这一前沿概念提炼为一种适用于任何多目标决策场景的实用思维模型。 文章将抽象的优化概念嵌入广为人知的游戏中，让非经济学背景的读者和工程师都能轻松理解帕累托思维。它提供了在产品开发、工程决策和个人选择中评估取舍的清晰框架——在这些场景里，往往不存在“唯一最优解”。 帕累托前沿由那些未被严格支配的角色构成——想要更高速度就必须牺牲加速度，反之亦然。文章很可能用散点图来呈现这一关系，而社区评论还把同一框架扩展到了《魔兽世界》装备优化和《超级马里奥赛车》速通中。

hackernews · theanonymousone · 8月6日 11:24 · [社区讨论](https://news.ycombinator.com/item?id=49195231)

**背景**: 帕累托前沿以意大利经济学家维尔弗雷多·帕累托的名字命名，指的是这样一组结果：其中任何一个选项都无法在不损害另一个目标的前提下改善某个目标。这是多目标优化中的核心概念，位于前沿上的解被称为“非受支配解”。在《马里奥赛车》这类游戏中，每个角色都有速度、加速度、重量和操控等数值属性，因此选择角色本质上就是在权衡取舍。前沿展示了可能实现的最优边界——边界之外的选项至少在一个维度上明显更差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_efficiency">Pareto efficiency - Wikipedia</a></li>
<li><a href="https://yuri.is/n/pareto-frontier/">Pareto Frontier | Yuri Vishnevsky</a></li>
<li><a href="https://www.investopedia.com/terms/p/pareto-efficiency.asp">Understanding Pareto Efficiency: Theory and Production ...</a></li>

</ul>
</details>

**社区讨论**: 评论区的反应很热烈。开发者 jerf 指出，帕累托概念能帮人判断“想要安全就必然牺牲用户体验”这类说法何时成立——只有当你已经处于前沿上时才成立。还有人分享了相关实践，例如用帕累托剪枝来优化《魔兽世界》的装备搭配、在速通中刻意选择处于前沿边缘的库巴/大金刚，并称赞这篇文章比以往的技术链接更容易理解。

**标签**: `#Pareto frontier`, `#decision-making`, `#optimization`, `#mental models`, `#trade-offs`

---

<a id="item-3"></a>
## [Qwen3.8 Max 登顶 Artificial Analysis Agentic Index](https://artificialanalysis.ai/?intelligence=agentic-index) ⭐️ 8.0/10

阿里巴巴的旗舰大语言模型 Qwen3.8 Max 现已在 Artificial Analysis Agentic Index 上排名第一，超过 Opus Max 等模型。该排名反映了它在智能体工作流中的强劲表现，社区测试也凸显了其故障排查与诊断能力。 这标志着中国 AI 模型在智能体能力方面已达到与西方顶尖系统相当的水平，而智能体能力是 AI 实际落地应用的关键领域。同时，这也让开源权重发布更加引人关注，因为 Qwen3.8-27B 等本地和小型模型有望为开发者与爱好者带来接近旗舰级的性能。 Agentic Index 衡量工具使用、规划、自主性和复杂问题解决能力，但具体排名存在波动：有社区用户截图显示 Qwen 先以 55.4 分位居第一，后来又以 58.4 分排在 Opus Max（59.2 分）之后。阿里巴巴已宣布将于下周发布 Qwen3.8-Max 和 Qwen3.8-27B 的开源权重。

hackernews · apitman · 8月6日 18:44 · [社区讨论](https://news.ycombinator.com/item?id=49200652)

**背景**: Agentic AI（智能体 AI）指能够追求目标、使用工具并采取行动、具有一定自主程度的人工智能系统，通常运行在人类设定的目标与约束之内。Artificial Analysis 的 Agentic Index 是评估模型在智能体工作流中表现的综合性基准，与一般智力测试给出不同信号。Qwen 是阿里巴巴的大语言模型系列，以开源和专有许可证分发，最新版本强调编程与自主开发能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/capabilities/agentic">Agentic Index - Artificial Analysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-max-release-date-specs-how-to-access-2026">Qwen 3.8-Max: Release Date, Specs, and How to Access It (2026) | Yotta Labs</a></li>

</ul>
</details>

**社区讨论**: 社区反应复杂但总体积极：有人认为中国已经追赶上来是最重要的结论，并期待 27B 本地模型能在设备端运行持续性智能体；也有人用真实测试验证了 Qwen 的故障排查能力。不过，多位用户质疑基准测试的可靠性，指出排名波动，并认为将 Opus 5 评为最佳会让榜单失去公信力，还指出在另一项 Intelligence Index 中 Opus 仍居首位。

**标签**: `#AI models`, `#Qwen`, `#benchmarks`, `#agentic AI`, `#China tech`

---

<a id="item-4"></a>
## [谷歌 DeepMind WeatherNext 2 AI 模型实现气旋预报突破](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10

谷歌 DeepMind 和谷歌研究院发布了 WeatherNext 2，这是一个基于 AI 的最先进中期天气预报模型系列，在气旋预测方面实现了突破。该模型被称为公司迄今最先进的天气预报系统。 这一里程碑展示了 AI 对气象学日益增长的影响，有望改善预警系统、能源交易和灾害应对。它也凸显了基础模型正在进入传统语言和图像处理之外的科学领域。 WeatherNext 2 被描述为谷歌 DeepMind 最先进的 AI 中期预报模型，能够加速天气预报。报道指出，它有望通过更快、更准确的预测来重塑能源交易和飓风预报。

rss · Google DeepMind · 8月6日 15:06

**背景**: 中期天气预报通常预测未来 15 天以内的天气，传统上依赖基于物理的数值模拟，计算成本高昂。像 WeatherNext 2 这样的 AI 模型直接从历史天气数据中学习，能够更快地生成预报。此类模型可应用于气旋追踪、可再生能源规划及其他气候相关任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/science/weathernext/">WeatherNext 2 — Google DeepMind</a></li>
<li><a href="https://www.linkedin.com/news/story/google-deepmind-model-speeds-up-weather-forecasting-6765700/">Google DeepMind model speeds up weather forecasting | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#weather forecasting`, `#DeepMind`, `#machine learning`, `#climate tech`

---

<a id="item-5"></a>
## [AI 时代，品味成为最终的不同之处](https://notashelf.dev/posts/taste-is-all-thats-left) ⭐️ 7.0/10

短文《品味是唯一剩下的》提出，当 AI 使技术执行逐渐过时，品味将成为定义人类技能的关键和最终的区别因素。它重新定义了在创意和技术工作中人类判断力的价值。 这一观点很重要，因为它将焦点从生产能力转向策展和判断能力，这些尚未被自动化。它影响了创作者、开发者和技术人员，暗示品味将成为 AI 驱动经济中的主要竞争优势。 这篇短文在 Hacker News 上获得了显著关注，得到 201 分和 158 条评论，显示了强烈的社区参与度。评论者提出了对 LLM 产出“无信号”内容的担忧、评估 AI 生成代码质量的困难，以及品味是否真的能被培养的疑问。

hackernews · tsak · 8月6日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49199346)

**背景**: “品味”这一概念在设计和技术领域长期被讨论，指的是做出在美学和功能上更优选择的能力。随着 AI 工具能生成代码、图像和文本，产出行为正在被自动化，而选择和指导的行为则成为人类独特的贡献。这篇文章加入了关于 AI 将如何重塑创意和技术职业的持续讨论。

**社区讨论**: 评论中既有共鸣也有质疑。一些用户赞同品味的重要性，引用苏珊·桑塔格关于“坎普”的笔记等哲学参考；另一些人对 LLM 的实际局限表示沮丧，指出生成的文章往往“几乎无信号”，且由 AI 代理构建的项目可能缺乏内部质量。也有人质疑，如果最终输出可用，品味是否还重要。

**标签**: `#AI`, `#creativity`, `#taste`, `#software-development`, `#philosophy`

---

<a id="item-6"></a>
## [OpenAI 改进 GPT-5.6 Sol，并向免费用户开放 GPT-5.6 Luna](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) ⭐️ 7.0/10

OpenAI 宣布改进 ChatGPT 中的 GPT-5.6 Sol，提升其在日常对话中的准确性和一致性，同时将 GPT-5.6 Luna 的访问权限扩大到免费用户，为其提供不限次数的日常聊天。据公告和用户讨论，免费用户还获得了推理（“Think”）切换开关的使用权。 让免费用户也能使用具备推理能力的模型，标志着 AI 商品化的重要一步，可能影响数以百万计用户的日常 AI 使用方式。这也表明 OpenAI 正在应对更廉价模型和开源替代品带来的竞争压力，进而重塑付费层级的价值主张。 GPT-5.6 Sol 目前为符合条件的付费套餐提供 Medium、High 和 Extra High 三种推理选项，而 GPT-5.6 Sol Pro 则为 Pro 订阅用户服务。GPT-5.6 Luna 是 GPT-5.6 系列中速度最快、成本最低的型号，拥有 105 万 token 的上下文窗口，输入价格低至每百万 token 0.20 美元，输出价格为每百万 token 1.20 美元，为该系列最低。

hackernews · OpenAI News · 8月6日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=49199357)

**背景**: GPT-5.6 系列包含多个针对不同需求定制的模型：GPT-5.6 Sol 是 OpenAI 最先进的模型，在编程、科学研究和网络安全方面能力更强，被称为其“迄今最强的网络安全模型”；而 GPT-5.6 Luna 则是速度最快、成本最低的层级。这类推理模型擅长逐步解决问题，但计算成本高昂，因此向免费用户开放这一能力意义重大。此次更新延续了 OpenAI 让越来越强大的模型进入免费层的趋势，正逐步模糊免费与付费服务之间的界限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/">Improving GPT‑5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt">GPT-5.6 in ChatGPT | OpenAI Help Center</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极，但对影响存在分歧。有用户认为向免费用户开放推理功能的影响将超过所有付费模型和编程智能体之和；另有用户认为这是商品化压力下的应对之举，并预测未来将转向 B2B 营销、付费 API 和免费聊天界面。还有人反驳“绝望之举”的说法，指出 Claude 长期向免费用户提供中端模型，也有人从公告措辞中读出 OpenAI 已把 ChatGPT 模型视为 AGI 的意味；部分用户则希望未来不再需要手动选择推理级别。

**标签**: `#AI`, `#ChatGPT`, `#OpenAI`, `#Product Update`, `#Free Access`

---

<a id="item-7"></a>
## [AI Agent 权限游戏数据：人类漏掉 1/3 威胁](https://scalex.dev/blog/ai-agent-permissions-stats/) ⭐️ 7.0/10

一份对 AI Agent 授权游戏（超过 4 万次游玩、40.9 万次决策）的统计分析显示，人类在批准 AI Agent 命令时漏掉了约三分之一的危险命令。用户在决定是否允许操作时，有时会忽略终端历史记录，尤其是 npm run 等命令上方的日志。 这项研究提供了经验数据，说明“人在环路”的审批机制对 AI Agent 而言并不可靠，对“用户确认就能防止危险操作”的假设提出了挑战。随着 AI Agent 在真实任务中拥有更多自主权，这一发现促使开发者设计比简单授权弹窗更强大的安全防护。 批评者指出，该游戏存在人为时间压力、没有真实后果，且部分提示被模糊地标记为危险或安全，可能影响结果可信度。数据来自约 4 万次游玩中的 40.9 万次决策，游戏作者还表示，npm run 命令上方的历史日志通常被玩家忽略。

hackernews · Wirbelwind · 8月6日 11:58 · [社区讨论](https://news.ycombinator.com/item?id=49195468)

**背景**: AI Agent 是能够自主执行任务的软件，有时会代替用户运行终端命令。为防止危险操作，系统通常会让用户逐条批准命令，但这会产生“授权疲劳”（permission fatigue），用户可能会快速且机械地点击同意。这个游戏最初以“Continue? Y/N”交互式练习的形式发布在 Hacker News 上，目的是在模拟但游戏化的场景中测试人们识别恶意或风险命令的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/soytuber/ghes-key-rotation-bug-bounty-program-refocus-ai-agent-permission-fatigue-d8i">GHES Key Rotation, Bug Bounty Program Refocus, AI Agent ...</a></li>
<li><a href="https://modernorange.io/item/48308376">Show HN: Continue? Y/N: A 60-second game about AI agent ...</a></li>

</ul>
</details>

**社区讨论**: 评论区总体持批评态度：多名用户认为游戏提示存在误导、人为时间压力以及没有真实后果，使“漏掉 1/3”的结论没有意义；作者则回应称即使事先有警告，威胁仍会被漏掉，且历史日志常被忽略。还有人借此批评“不断询问用户、希望用户永不犯错”并不是真正的安全模式，而更像一种推卸责任的法律流程而非实际保护。

**标签**: `#AI safety`, `#human oversight`, `#AI agents`, `#security`, `#empirical data`

---

<a id="item-8"></a>
## [OpenAI 携手美国心理学会，推动青少年心理健康与负责任 AI](https://openai.com/index/openai-and-apa-partner-to-advance-responsible-ai) ⭐️ 7.0/10

OpenAI 宣布与美国心理学会（APA）建立合作伙伴关系，共同制定基于证据的指导方针、资源和保障措施，以促进青少年心理健康领域中 AI 的负责任使用。 此次合作直接回应了人们对 AI 影响青少年（一个特别容易受到心理健康问题影响的群体）的日益加剧的担忧。它标志着将心理学研究融入 AI 产品设计与政策制定的趋势，可能影响创作者和教育者对待青少年 AI 安全的方式。 该合作将重点为面向青少年的 AI 工具的创作者、教育者和开发者提供实用资源。APA 将贡献其在心理学研究和临床实践方面的专长，帮助为涉及青少年的 AI 交互设定基于证据的保障措施。

rss · OpenAI News · 8月6日 06:00

**背景**: 美国心理学会（APA）是美国最大的心理学家科学和专业组织，在儿童与青少年发展方面拥有深厚专长。随着聊天机器人和辅导系统等 AI 工具在青少年生活中日益普及，人们对其心理健康影响的担忧也与日俱增。此次合作旨在弥合快速发展的 AI 技术与基于研究的心理健康标准之间的差距。

**标签**: `#AI ethics`, `#mental health`, `#youth`, `#partnership`, `#responsible AI`

---

<a id="item-9"></a>
## [Meta 发布 Muse Code，用于长周期编码任务的终端代理](https://www.producthunt.com/products/meta) ⭐️ 7.0/10

Meta 通过 Product Hunt 发布了 Muse Code，这是一款面向长周期编码任务的终端 AI 代理。公告将其定位为提升开发者生产力的实用工具，但未详细说明具体功能。 此次发布让 Meta 加入了竞争激烈的终端代理市场，该市场已有 OpenAI 的 Codex、Claude Code 和 Gemini CLI。对开发者而言，更多竞争意味着更好的工具和更多的 AI 辅助编码选择。 Product Hunt 列表几乎没有提供 Muse Code 的技术细节，例如底层模型、价格或支持的编程语言。重点强调‘长周期’编码，意味着该代理旨在处理需要持续上下文和可靠性的复杂多步骤任务。

rss · Product Hunt · 8月6日 02:35

**背景**: 终端 AI 编码代理是命令行工具，可以直接在代码库中读取、写入和执行代码，而基于聊天的助手只能提供代码建议。长周期编码任务对 AI 来说尤为困难，因为模型需要在漫长而繁杂的轨迹中保持准确性和上下文，正如最近的基准测试以及 OpenAI 长达 25 小时的 Codex 运行示例所指出的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bradagi/awesome-cli-coding-agents">GitHub - bradAGI/awesome-cli-coding-agents: Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them. Covers open-source tools (Pi, OpenCode, Aider, Goose), platform agents (Claude Code, Codex, Gemini CLI), parallel runners, autonomous loops, and agent infrastructure. · GitHub</a></li>
<li><a href="https://developers.openai.com/blog/run-long-horizon-tasks-with-codex">Run long horizon tasks with Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#coding agent`, `#developer productivity`, `#Meta`, `#product launch`

---

<a id="item-10"></a>
## [HubSpot AEO 与 Ahrefs Brand Radar：AI 可见性工具对比](https://blog.hubspot.com/marketing/hubspot-vs-ahrefs-aeo) ⭐️ 6.0/10

HubSpot 发布了一篇文章，将自家的 AEO 工具与 Ahrefs Brand Radar 进行对比，指出两者都能追踪品牌在 AI 回答中的可见度，但方法不同。文章认为，正确选择取决于营销人员在获得数据后需要做什么，并强调 HubSpot AEO 能帮助团队将 AI 可见度洞察转化为行动。 随着越来越多的买家跳过传统搜索，直接使用 ChatGPT、Gemini 或 Perplexity 获取推荐，营销人员需要能展示品牌在 AI 回答中表现并指导行动的工具。这一对比有助于营销人员在偏重行动的 HubSpot AEO 与偏重广泛监测和竞品分析的 Ahrefs Brand Radar 之间做出选择。 HubSpot AEO 提供可见度评分、提示词追踪、引用分析和优先级建议，其中 CRM 信息提示等高级功能需要 Marketing Hub Pro 或 Enterprise 版本。Ahrefs Brand Radar 可追踪任意品牌在超过 4.05 亿个搜索提示词中的表现，支持自定义提示词，并提供覆盖多个 AI 平台的超过 4.76 亿个自然提示词。

rss · HubSpot Marketing · 8月6日 11:00

**背景**: 答案引擎优化（AEO）是一种内容优化实践，目的是让 ChatGPT、Gemini、Perplexity 等 AI 引擎能够理解、信任并在回答中引用某个品牌。HubSpot AEO 内置于 HubSpot 营销平台，强调直接在内容工具中基于洞察采取行动；而 Ahrefs Brand Radar 则侧重于监测和探索任意品牌的 AI 可见度，非常适合竞争研究。这两款工具反映了不同工作流：一个用于改进自身内容，另一个用于调研更广泛的 AI 可见度格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hubspot.com/products/marketing/aeo-guide">Show Up in AI Search with Answer Engine Optimization (AEO) | HubSpot</a></li>
<li><a href="https://ahrefs.com/brand-radar">Ahrefs Brand Radar: See ANY brand&#x27;s AI visibility</a></li>
<li><a href="https://help.ahrefs.com/en/articles/11064852-what-is-brand-radar-and-how-to-use-it">What is Brand Radar, and how to use it? | Help Center - Ahrefs</a></li>

</ul>
</details>

**标签**: `#AEO`, `#AI search`, `#content strategy`, `#HubSpot`, `#Ahrefs`

---