---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 41 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，Luna 定价大幅下调](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，token 价格全面下调](#item-2) ⭐️ 9.0/10
3. [openai-python v3.18.0 新增 GPT-6 Sol 与 Luna 模型标识符](#item-3) ⭐️ 8.0/10
4. [Artificial Analysis 评测 Claude Opus 5.5：单任务成本减半](#item-4) ⭐️ 8.0/10
5. [Claude Opus 5.5 与 GPT-6 Sol/Luna 发布，价格腰斩](#item-5) ⭐️ 8.0/10
6. [GPT-6 Astra 据称破解 2005 年悬而未决的 Enigma 密文](#item-6) ⭐️ 7.0/10
7. [WordPress 修复可致条件性 RCE 的未认证路径遍历漏洞](#item-7) ⭐️ 7.0/10
8. [OpenAI 为 GPT-6 推出增强版提示缓存](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，Luna 定价大幅下调](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 正式发布 GPT-6 Sol 与 Luna 两款模型，官方将其定位为以不同的能力与成本组合，把前沿智能带入日常工作。最受关注的变化是价格：社区与第三方平台指出，GPT-6 Luna 的价格大约只有 GPT-5.6 Luna 的一半，OpenRouter 上标价为每百万输入 token 0.10 美元、每百万输出 token 0.50 美元。 一款接近前沿水平的模型价格降到上一代 Luna 的一半，直接改变了智能体编程、批量处理和各类高并发任务的经济账，也给 Claude Code、Codex 等订阅方案带来正面竞争压力。对开发者和 AI 工具创作者来说，选择标准不再只是“哪个模型最聪明”，而是“每花一美元能买到多高的智能”，这会重塑工具链、教学内容和产品定价。 GPT-6 Sol 并非单一模型，而是一个变体家族：Artificial Analysis 列出了六种配置，其中 GPT-6 Sol \(max\) 以 48 的智能得分居首，GPT-6 Sol \(high\) 速度最快，约为每秒 138 个 token。GPT-6 Luna 拥有 1,050,000 token 的上下文窗口，最大输出为 128,000 token；OpenAI 还说明，Sol 与 Luna 的欧盟数据驻留仅在 Standard 处理模式下可用。

hackernews · OpenAI News · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: 前沿模型指的是某一时点最先进的通用人工智能系统，依靠海量数据和大规模算力训练，在推理、多模态理解和自主任务执行方面处于领先位置。OpenAI 近期密集推进 GPT-6 系列：GPT-6 Astra 于 2026 年 9 月早些时候发布，被宣传为多项任务上的“世界最强模型”，而此次 Sol 与 Luna 把该系列拆分为高能力档（Sol）和定位在其之下、主打速度与成本效率的档位（Luna）。Hacker News 上相关讨论获得 1130 分、约 590 条评论，且讨论异常聚焦于实际成本与工作流问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-luna">GPT - 6 Luna - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-sol">GPT-6 Sol: Release Intelligence, Performance &amp; Price</a></li>

</ul>
</details>

**社区讨论**: 评论者总体认可这次发布，但围绕“如何选模型”展开争论：Simon Willison 认为 Luna 价格只有 GPT-5.6 Luna 的一半“是件大事”，并贴出并排的鹈鹕/SVG 基准输出；m\_fayer 则罕见地描述了 Compatible 到 5.6 Sol “手感”的体验，担心技术更强的继任者在协作时反而没那么自然。jeffnash 对比了 Claude Code 与 Codex 各档订阅的使用额度经济性（目前更看好 Codex，部分原因是 20x 方案下 ChatGPT 用量基本不限），leokennis 认为从普通用户角度看 ChatGPT Plus 如今“就是能用”，kumarvvr 则询问哪款模型最适合担任只负责实现想法、不给建议的纯结对程序员。

**标签**: `#AI models`, `#OpenAI`, `#LLM`, `#AI coding tools`, `#creator economy`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，token 价格全面下调](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，这是其公开呼吁“为前沿技术减速（pacing the frontier）”之后的首个模型发布，并对所有 token 类别全面降价：缓存读取从每百万 token 0.50 美元降至 0.20 美元，输入 token 从 5 美元降至 4 美元，输出 token 从 25 美元降至 20 美元，缓存写入从 6.25 美元降至 5 美元。官方还宣称新模型的表达风格明显更自然，早期测试者称它会把最重要的信息放在前面，使其在长时间协作中更像一个可靠的“工作搭档”。 对一线前沿模型进行两位数的降价，会直接改变所有基于 Anthropic API 构建智能体或长上下文流水线的开发者的成本收益计算，也会迫使其他实验室在价格而不只是跑分上作出回应。发布时机还加剧了一场持续争论：公开主张放缓前沿技术发展的实验室，是否同时又能不断推出更强、更便宜的模型。 降幅最大的是缓存读取，从每百万 token 0.50 美元降至 0.20 美元，降幅达 60%，而这一类目对智能体和重复提示词负载尤为关键；输入与输出 token 各降 20%，缓存写入也降 20%。在质量方面，“沟通风格改进”属于官方宣称与测试者主观评价，而非可量化的基准分数，其实际价值取决于每个人具体的长会话工作流程。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: Claude Opus 是 Anthropic 能力最强（此前也最贵）的模型档位；API 定价通常按每百万 token 计费，并对提示缓存（prompt cache）的读取与写入分别定价，缓存机制可以让重复使用的上下文以低得多的成本被复用。“为前沿技术减速（pacing the frontier）”是一种政策主张，与 pacingthefrontier.com 的公开信相关，它请求美国政府支持一项国际努力，开发必要的技术与治理工具，以刻意放慢前沿自动化 AI 的发展速度。2025 至 2026 年间，整个行业的 LLM API 价格持续下行，因此 Opus 级别的降价既被视为竞争手段，也被读作该实验室对自身发展路线的一种表态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pacingthefrontier.com/">Pacing the Frontier</a></li>
<li><a href="https://benchlm.ai/llm-pricing">LLM API Pricing Comparison &amp; Calculator (September 2026) | BenchLM.ai</a></li>
<li><a href="https://www.llm-prices.com/">LLM pricing calculator</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论帖（约 1165 分、792 条评论）意见明显分化：最高赞评论指出其中的讽刺意味——公告第一句还在提“为前沿技术减速”，其余篇幅却在用具体数字说明 Anthropic 完全没有减速；另一位评论者贴出完整价格对照表，并指出 Opus 5 是 OpenRouter 花费排行榜上最高的模型。也有人引用官方关于沟通风格改进的描述，认为这是最具实际意义的改动；还有用户反驳称，像 DeepSeek v4.1 这样更便宜的模型已经能以极低成本完成复杂的智能体任务。

**标签**: `#AI模型发布`, `#Claude`, `#LLM定价`, `#AI工具`, `#前沿AI政策`

---

<a id="item-3"></a>
## [openai-python v3.18.0 新增 GPT-6 Sol 与 Luna 模型标识符](https://github.com/openai/openai-python/releases/tag/v3.18.0) ⭐️ 8.0/10

2026 年 9 月 22 日，官方 openai-python SDK 发布 3.18.0 版本，唯一的特性变更是新增了两个新模型的 API 模型标识符——“GPT-6 Sol”和“Luna”（PR \#3935，提交 455ce1b）。发布说明仅有这一行内容，没有模型卡、基准测试、定价或废弃说明。 由于开发者必须先由官方客户端库识别模型的标识符字符串才能调用该模型，这类 SDK 版本更新历来是旗舰模型即将发布的最早公开信号之一。对于关注 AI 能力变化的人来说，这是来自 OpenAI 自有代码库的一手证据而非传言，也让 Python 开发者可以在正式发布前就开始搭建集成。 本次发布本身只提供了标识符字符串，因此开发者无法从发布说明中获知上下文窗口、定价、速率限制或与既有模型的能力差异。同日的外部报道显示，Sol 是推理能力更强的模型，而 Luna 是面向高并发、更便宜且更快的选项；两者都基于 Astra 引入的对齐工作，并相较各自的 GPT-5.6 对应型号有所提升——报道称在 OpenAI 自家基准测试中，GPT-6 Sol 的错误率约为 GPT-5.6 Sol 的一半。

github · openai-sdks\[bot\] · 9月22日 18:25

**背景**: openai-python 是封装 OpenAI REST API 的官方 Python 库，要求 Python 3.10 或更高版本，开发者需要向 API 请求中传入模型名称这样的标识符字符串来调用模型。OpenAI 惯于在正式公布模型之前或同期先在 SDK 中放出新的标识符，因此看似例行的版本号更新也会在开发者社区引发关注。GPT-5.6 是被 Sol 和 Luna 取代的上一代模型家族，而“Astra”是 OpenAI 用于指代这些新模型所基于的、聚焦对齐工作的模型项目名称。本条新闻未提供社区评论，因此此处不作讨论情绪总结。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://www.macrumors.com/2026/09/22/openai-gpt-6-sol-luna/">OpenAI&#x27;s New GPT - 6 Sol and Luna Models Bring Astra... - MacRumors</a></li>
<li><a href="https://github.com/openai/openai-python">GitHub - openai/ openai - python : The official Python library for the...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#AI模型发布`, `#开发者工具`, `#API更新`

---

<a id="item-4"></a>
## [Artificial Analysis 评测 Claude Opus 5.5：单任务成本减半](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

Artificial Analysis 发布了 Claude Opus 5.5 在“max”推理档位下的评测页面，结果显示其输出风格明显改善，单任务成本相比 Claude Opus 5 大约降低一半。该页面只是同一模型三个推理档位页面之一，另外还有“xhigh”与“medium”（默认档位）的独立评测页面。 在同等高推理强度下把单任务成本砍半，直接改变了智能体、编程助手和内容生成流水线的经济性，因为推理密集型任务正是账单增长最快的地方。这也让选型者能看到推理强度、延迟与花费之间更清晰的权衡曲线，而不是只盯一个跑分数字。 评测是按推理档位分别给出的，而不是一个统一数字；在 max 档位下模型可能消耗极长的 token 预算——有评论者称两次尝试“生成一只骑自行车的鹈鹕的 SVG”都在模型仍在推理时耗尽 128,000 token 预算。Anthropic 官方文档指出，在 Message Batches API 上 Opus 5.5 通过 beta 头可支持最多 30 万输出 token，最小可缓存提示长度为 512 token。

hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: Artificial Analysis 是一个独立评测平台，从质量、价格、输出速度和延迟等维度比较多款大语言模型，并为每个模型发布单独页面，许多开发者在选择 API 前会参考它。Claude Opus 5.5 这类现代推理模型提供可选的“推理强度”档位（例如 medium、high、xhigh、max），用更长的思考时间和更高的 token 消耗换取数学、编程、逻辑任务上更好的准确率，其中 medium 通常是默认值。Claude Opus 5.5 是 Anthropic 在 Opus 5 之后约两个月推出的后继模型；而“单任务成本”这一指标把 token 单价乘以模型完成一个任务实际消耗的 token 量，因此同时反映了模型的啰嗦程度与单价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model &amp; API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/reasoning-effort">Reasoning effort - LLM Parameter Guide - Vellum</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论总体对这次改进持欢迎态度：有人称赞 Opus 5.5 的输出风格和啰嗦程度相比 Opus 5 是巨大进步，并预测用户会迅速从旧版本迁移；也有人特别指出“同等高推理强度下单任务成本减半”这一点非常讨喜。Simon Willison 指出存在 max/xhigh/medium 三个独立页面，并提到在 max 档位下模型两次都在 SVG 生成提示上耗尽 128,000 token 预算；另有评论者提出更广泛的担忧：厂商的跑分很少在发布数周后重测，他称某竞品模型的实测表现已回落到与更弱的同门型号相当。

**标签**: `#Claude`, `#LLM benchmarks`, `#AI pricing`, `#creator tools`, `#model performance`

---

<a id="item-5"></a>
## [Claude Opus 5.5 与 GPT-6 Sol/Luna 发布，价格腰斩](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

2026 年 9 月 22 日，Anthropic 发布了 Claude Opus 5.5，约一小时后 OpenAI 发布了 GPT-6 Sol 与 GPT-6 Luna，而前一天还有 Grok 4.7 与小米 MiMo v2.6 Flash/Pro 登场。Simon Willison 指出，GPT-6 Sol 和 Luna 的价格大约只有各自 GPT-5.6 对应型号的一半，其中 GPT-6 Luna 的输入价格为每百万 token 0.10 美元、输出为每百万 token 0.50 美元。Claude Opus 5.5 同样迎来了降价。 对于基于这些 API 构建应用的开发者而言，在质量相当甚至更好的情况下价格减半，会直接改变模型选型与成本规划，让过去昂贵的能力可以在高并发场景下负担得起。这也标志着 OpenAI、Anthropic、xAI 以及小米等中国厂商之间的价格战正在加速，压缩了各家的利润空间，迫使厂商从比拼跑分转向比拼经济性。 Willison 提到 GPT-5.6 系列将在 11 月按计划涨价 25%，因此 GPT-6 实际上只有上一代促销价的一半；同时 GPT-5.6 Terra 与 GPT-6 Sol 价格相同，继续使用 Terra 的理由已不复存在。以 0.10/0.50 美元的价格计，GPT-6 Luna 是 OpenAI 有史以来最便宜的模型之一，仅被能力弱得多的 GPT-4.1 Nano 和 GPT-5 Nano 超越；不过这些看法属于早期一手体验，而非深入基准测试。

rss · Simon Willison · 9月22日 23:46

**背景**: 大语言模型 API 通常按每百万 token 计费，并对输入、缓存输入和输出分别定价，因此单价的适度下调在高并发应用中可能带来可观的成本节省。OpenAI 的 GPT-6 家族分为 Astra（旗舰）、Sol（中端，面向复杂编程与智能体工作流）和 Luna（低端，面向高并发、聚焦型任务），与 Anthropic 的 Claude 产品线（Opus 为最高档）形成对应。Willison 是知名开发者与写作者，长期跟踪模型发布，并用“鹈鹕 SVG”这类趣味测试来定性比较不同模型的输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://coursiv.io/blog/gpt-6-sol-luna">GPT - 6 Sol and Luna : Pricing, Benchmarks, Availability | Coursiv Blog</a></li>
<li><a href="https://kaelzhang.com/blog/ai-token-price-war-2026">AI Model Price War Heats Up: DeepSeek Cuts 75... | Kael Zhang</a></li>

</ul>
</details>

**标签**: `#AI模型发布`, `#Claude Opus`, `#OpenAI GPT-6`, `#价格战`, `#AI工具选型`

---

<a id="item-6"></a>
## [GPT-6 Astra 据称破解 2005 年悬而未决的 Enigma 密文](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 7.0/10

一名研究者据称借助 OpenAI 的 GPT-6 Astra 破解了一条约 2005 年以来一直未被解出的特定 Enigma 密文，相关文章在 Hacker News 上引发了 551 分、357 条评论的讨论。该密文以 &quot;BTTE UM ANGABE DES MARSQWEGES...&quot; 开头，大意是要求说明行军路线，并称己方在 Rosenow，要求立即以无线电回复。 这起事件成了检验&quot;AI 该拿多少功劳&quot;的现场案例——评论者指出 Astra 只是参与了两天的协作，协助编写 Python 与 C++ 的 Enigma 模拟器并提供思路。对于需要评估 AI 能力宣称的读者而言，它清楚展示了&quot;模型自己解出来的&quot;与&quot;人机分工&quot;之间的差距。 评论者指出这条密文格外难解的原因在于：它使用了与当天其他报文完全不同的密钥、原始转录存在错误，且左转子在字母 72 处发生换挡，从而破坏了标准的 crib 攻击。还有评论者声称另一竞品模型 Gemini 3.8 Flash 在约 45 分钟的无引导运行中一次性完成解密，说明 Astra 的贡献未必独一无二。

hackernews · sohkamyung · 9月22日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: Enigma 是德国在 1920 年代至二战期间使用的转子密码机，其早期破译由波兰数学家 Marian Rejewski、Henryk Zygalski 和 Jerzy Rozycki 完成，后来由 Bletchley Park 在 Alan Turing 的 Bombe 机器上进一步发展。&quot;Crib 攻击&quot;利用猜测的明文片段，并依赖对转子设置与换挡位置的假设，因此异常的转子换挡恰恰会让攻击失效。GPT-6 Astra 是 OpenAI 最新的模型，于 2026 年 9 月 3 日以限量预览形式发布，主打在计算机操作、编程、网络安全和科学领域的领先能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_GPT-6_Astra">OpenAI GPT-6 Astra</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma">Cryptanalysis of the Enigma - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: HN 讨论整体偏向怀疑而非欢呼：jtrn 认为诚实的标题应为&quot;研究者借助 Astra 的大力帮助破解了一条顽固的历史 Enigma 密文&quot;；tantalor 则质疑既然模型编写了 Python/C++ 模拟器并把搜索过程外包给程序，就很难说它&quot;完全靠自己&quot;完成。podgorniy 给出反例，称 Gemini 3.8 Flash 似乎能在约 45 分钟内无引导地解出同一密文，另有评论者贴出解密后的德语明文，并指出原始叙述具有误导性。

**标签**: `#AI能力评估`, `#大模型推理`, `#人类与AI协作`, `#AI炒作与批判性思维`, `#密码学`

---

<a id="item-7"></a>
## [WordPress 修复可致条件性 RCE 的未认证路径遍历漏洞](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 7.0/10

WordPress 发布了 7.1.2 版本，修复了一个未认证的路径遍历漏洞，该漏洞可能进一步导致条件性的远程代码执行（RCE）；同时官方将补丁回溯移植到了包括 4.7 在内的所有旧分支。 WordPress 驱动着互联网上极大比例的网站，其中包含大量创作者博客和小型企业站点，因此一个无需认证、还可能升级为代码执行的漏洞对庞大用户群来说属于亟待处理的远程可利用风险，尤其是约三分之一仍停留在非 7.x 分支的安装实例。 该安全公告附带了具体的修补提交，社区成员还指出，受影响的模板加载函数 locate\_template\(\) 早在九年前就有人在官方文档注释中提醒存在目录遍历风险，这强烈暗示用户可控的模板名参数一直未得到妥善校验。

hackernews · vntok · 9月22日 16:33 · [社区讨论](https://news.ycombinator.com/item?id=49803959)

**背景**: 路径遍历漏洞是指攻击者利用特制输入（例如 ../ 序列）访问应用程序本不应暴露的目录之外的服务器文件，其成因是代码直接用用户输入拼接文件路径而未做充分校验。远程代码执行（RCE）则意味着攻击者无需物理接触服务器即可远程运行自己的代码，因此一个能进一步串联到 RCE 的遍历漏洞，其危害远大于单纯的文件泄露。回溯移植（backport）是一种常见的维护做法，即把最新版本中的小型安全修复搬到仍在支持的旧版本上，这也是 WordPress 能够为 4.7 这样古老的分支提供补丁的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rot-ig.medium.com/path-traversal-vulnerability-explained-the-hidden-door-inside-web-applications-2f56474f9e75">Path Traversal Vulnerability Explained : The Hidden Door... | Medium</a></li>
<li><a href="https://www.wiz.io/academy/application-security/remote-code-execution-rce-attack">RCE meaning: Remote code execution attacks explained | Wiz</a></li>
<li><a href="https://en.wikipedia.org/wiki/Backporting">Backporting - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区认可官方将补丁回溯到 4.7 分支是出于善意，但也有人批评 WordPress 长期的安全记录，并指出约三分之一的安装实例并未运行较新的 7.x 分支。还有人分享了实际应对方式，例如一位开发者把网站迁移为静态托管的 Hugo 模板以摆脱 WordPress 的维护压力；另有人贴出九年前的官方文档注释，其中早已同时描述了该漏洞的性质与修复思路。

**标签**: `#WordPress`, `#网络安全`, `#漏洞修复`, `#开源软件`, `#自建站`

---

<a id="item-8"></a>
## [OpenAI 为 GPT-6 推出增强版提示缓存](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 7.0/10

OpenAI 宣布为 GPT-6 推出升级版提示缓存（prompt caching）系统，带来更高的缓存命中率，并新增诊断工具、显式缓存断点（explicit breakpoints）以及多项控制手段，用于降低延迟和推理成本。该版本还提供了监控仪表盘，让开发者可以观察缓存行为并排查缓存未命中（cache miss）的原因。 提示缓存直接影响开发者在规模化场景下最关心的两个指标——单位 token 成本和首 token 延迟，因此即便是渐进式改进，也会在高并发的生产负载中被放大。对于构建 AI 创作工具和智能体工作流的初创公司与团队来说，更优的缓存经济性可能显著改变单次调用的成本结构，使冗长且重复的系统提示词变得便宜得多。 此次更新引入显式断点，开发者可以精确标记哪些提示词前缀应被缓存，而不再完全依赖自动前缀匹配，同时配套诊断工具和仪表盘用于定位缓存未命中。有说法称类似的诊断工具有助于团队将命中率提升几个百分点、成本降低约 20%，但 OpenAI 并未提供独立的基准数据，而且缓存效果仍对 TTL（生存时间）以及在被缓存内容中嵌入时间戳等反模式非常敏感。

rss · OpenAI News · 9月22日 21:00

**背景**: 提示缓存是一种让 API 保存已处理过的提示词前缀的技术，后续请求只要复用同一前缀即可跳过重复处理，从而同时降低输入 token 成本与延迟；Anthropic 于 2024 年 8 月通过 Claude 推广了这一能力，如今 OpenAI、Google 等厂商都提供类似功能。各家在缓存触发方式上有所不同：Anthropic 采用显式缓存标记，而 OpenAI 过去更多依赖自动前缀检测；缓存写入通常按溢价计费（例如输入价格的 1.25 倍），缓存读取则享受折扣。缓存命中率——即成功复用缓存前缀的请求占比——是最关键的运营指标，而提示词前段的任何微小改动都可能让它归零。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/better-prompt-caching-for-gpt-6/">Better prompt caching for GPT-6 | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/prompt-caching">Prompt caching | OpenAI API</a></li>
<li><a href="https://openrouter.ai/docs/guides/best-practices/prompt-caching">Prompt Caching - Optimize AI Model Costs with Smart Caching</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#prompt caching`, `#OpenAI`, `#GPT-6`, `#cost optimization`

---