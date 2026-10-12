---
layout: default
title: "Horizon Summary: 2026-10-12 (ZH)"
date: 2026-10-12
lang: zh
---

> 从 30 条内容中筛选出 4 条重要资讯。

---

1. [陶哲轩发布“数学 2.0”：AI 让数学走向人机协作](#item-1) ⭐️ 8.0/10
2. [Karpathy：关于 LLM 能力的认知鸿沟正在扩大](#item-2) ⭐️ 7.0/10
3. [Passkey 是陷阱？远程认证与设备锁定遭质疑](#item-3) ⭐️ 7.0/10
4. [AI 代理消耗 5000 亿 token 反编译一款第一人称射击游戏](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [陶哲轩发布“数学 2.0”：AI 让数学走向人机协作](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf) ⭐️ 8.0/10

陶哲轩（Terence Tao）发布了题为“Math 2.0”的演讲幻灯片（标注日期为 2026 年 10 月，在加州理工学院发表），他在其中提出：AI 能够自动求解公开问题，这终结了“证明稀缺”的时代，并提出未来的“数学 2.0”应当用 AI 工具来维系数学共同体本身以及数学理解的价值。他配套的博客文章把当下描述为过度强调由 AI 求解问题，而忽视了构建连贯理论体系。 当一位菲尔兹奖得主把 AI 重新定义为真正的合作者而非工具时，这标志着数学家选择问题、培养学生、撰写经费申请的方式，以及资助方评判研究价值的标准都将发生范式转变。这一论断的影响远超数学领域，适用于任何“AI 能比人类更快地产出合格成果、但人类来不及建立理解”的专业领域。 该材料是幻灯片加博客文章，而非经过同行评审的论文；其中有一页关于 AI 研发抗癌药物的内容，批评者认为这超出了陶哲轩的专业范围。陶哲轩的核心比喻是“公开问题是灯塔，而不是目的地”——它们应指向理论“代码库”需要扩展的方向；他还认为当前的数学 AI 不是“好公民”，因为它只针对单个问题做优化，而不为共享理论做出优雅、可复用的贡献。

hackernews · Anon84 · 10月11日 13:16 · [社区讨论](https://news.ycombinator.com/item?id=50043026)

**背景**: 数学传统上依靠研究者个人证明定理，并通过期刊和同行评审来传播，陶哲轩把这一流程称为“数学 1.0”。过去几年里，能够辅助甚至自主产出数学证明的 AI 系统开始解决长期悬而未决的公开问题，这让研究者既兴奋，也让人担心人类产出的证明会变得泛滥而廉价。陶哲轩是加州大学洛杉矶分校的菲尔兹奖得主，也是关于 AI 如何改变科研实践最受关注的评论者之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/10/10/math-2-0/">Math 2.0 | What&#x27;s new</a></li>
<li><a href="https://officechai.com/ai/terence-tao-math-2-0/">Terence Tao Says &#x27;Math 2.0&#x27; Must Move Past Problem-Solving in ...</a></li>
<li><a href="https://community.openai.com/t/terence-tao-on-math-2-0-and-the-need-for-a-holistic-approach/1404266">Terence Tao on &quot;Math 2.0&quot; and the need for a holistic ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论异常深入，且以质疑为主。从事药物研发的 dekhn 强烈反驳陶哲轩关于抗癌药物的那一页，指出许多药物在机理模型极不完整的情况下依然有效；另一位评论者则提到，连全身麻醉的作用机制都尚未完全弄清。也有人描述 AI 解决自己研究多年的问题所带来的情感与经济冲击：有评论者称，同事得知 OpenAI 的输出为他们长期未解的问题画上句号，不得不彻底重写刚刚提交的经费申请；thomasahle 则用软件来解读陶哲轩——纯数学是在维护一套高质量的“理论代码库”，而当前的 AI 还不是这个代码库的“好公民”。

**标签**: `#AI collaboration`, `#future of knowledge work`, `#mathematics`, `#expertise and automation`, `#AI in research`

---

<a id="item-2"></a>
## [Karpathy：关于 LLM 能力的认知鸿沟正在扩大](https://twitter.com/karpathy/status/2109361546505966046) ⭐️ 7.0/10

Andrej Karpathy 在 X 上发帖指出，人们对大语言模型真实能力的共识正在瓦解，业内人士与普通公众之间的认知差距越拉越大。这一观点在 Hacker News 上引发了约 250 分、404 条评论的讨论，用户们争论 agentic AI 究竟有没有给普通人带来真实可见的收益。 这场争论凸显出正在扩大的技术采用与技能分层：一小部分人从 agentic 编程和推理工具中获得了巨大的生产力提升，而大多数人几乎感受不到日常生活有什么变化，因此对相关宣传持怀疑态度。对于围绕 AI 做产品或培养人才的人来说，结论是：能力主张如今必须针对不同真实用户群体分别评估，而不是套用单一叙事。 有评论者反驳了“即便是最顶尖的 0.2% 也认为智能体能替代数周工作量”的说法，指出为了可维护性、未来的 token 成本、性能优化以及模型可能悄悄犯下的错误，人工审查 LLM 生成的代码仍然必不可少。也有人指出，大部分公众对 agentic LLM 并没有具体的使用场景，因此在能力能对应到他们已经在做的任务之前，“能力”对他们而言毫无意义。

hackernews · albertzeyer · 10月11日 20:20 · [社区讨论](https://news.ycombinator.com/item?id=50047422)

**背景**: 大语言模型（LLM）是在海量文本语料上训练的神经网络，能够生成、总结、翻译和分析语言，支撑着 ChatGPT、Claude、Gemini、DeepSeek 等聊天机器人。Agentic AI 指的是超越了单纯问答的系统：它们会规划、调用工具，并以一定自主性为达成目标而采取行动。Karpathy 是 AI 研究者，曾任职于特斯拉和 OpenAI，是谈论 LLM 实际能力时最受关注的发声者之一，因此他的表述往往能设定整个讨论的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is agentic AI? - IBM</a></li>

</ul>
</details>

**社区讨论**: 整体情绪以怀疑和重视实证为主。一条高赞评论列举了汽车、洗碗机、晚点的火车、油价、房租等日常开销，认为 AI 对普通人几乎没有带来任何改善；另一条评论则质疑“顶尖从业者都认同智能体能替代数周工作量”这一前提，强调代码审查与长期维护的重要性；还有人对公众究竟该拿这些模型“做什么”提出疑问。也有较为反思性的评论认为，真正的转折点可能是人形机器人，而非编程智能体。

**标签**: `#AI能力认知差`, `#LLM`, `#创作者经济`, `#技术采用`, `#生产力工具`

---

<a id="item-3"></a>
## [Passkey 是陷阱？远程认证与设备锁定遭质疑](https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them) ⭐️ 7.0/10

一篇题为《Passkeys are a trap》的 Substack 文章认为，passkey 可能因远程认证（remote attestation）、设备锁定以及凭据可移植性下降而变成陷阱，该文在 Hacker News 上引发了 275 分、151 条评论的讨论。争论的核心是：网站是否可能在注册环节强制要求经过认证的 passkey，从而限制用户只能使用特定设备或认证器。 Apple、Google 和 Microsoft 正大力推广泛 passkey 作为密码的替代方案，因此任何设计缺陷都会影响数以亿计的普通用户，而不只是安全专家。如果认证成为强制要求，用户可能失去备份、导出或迁移自己凭据的能力，账号访问权实质上会被少数几家平台厂商掌握。 评论者强调，认证只能在凭据注册时被要求，无法在登录时追溯性强制，而且当网站请求认证时浏览器会弹出权限提示，因此拒绝的用户只是注册失败，而不会被悄悄追踪。文章本身也承认认证有其正当用途，例如拦截诈骗者伪造的 passkey 应用；其补充说明还指出 passkey 与域名绑定，因此能抵御中间人钓鱼攻击。

hackernews · laurex · 10月11日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=50048312)

**背景**: Passkey 本质上是 WebAuthn 凭据，这是 W3C 制定的标准（基于 FIDO/CTAP 协议），用公钥数字签名代替共享密码来验证用户身份。最常见的认证器是内置于操作系统的平台认证器，如 Apple Keychain、Windows Hello 和 Android，它们通常会在设备间同步凭据；漫游认证器则包括 USB/NFC 硬件安全密钥。远程认证（remote attestation）是另一套机制，一方需要向远程方证明其硬件与软件栈值得信任，这一理念源自可信计算（Trusted Computing）和 TPM 芯片，Richard Stallman 等批评者称之为「背叛式计算」，因为该硬件不仅为用户提供保护，也被用来防范用户本人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Passkeys">Passkeys</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_attestation">Remote attestation</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/confidential-computing/attestation-solutions">Attestation Types and Scenarios | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向认同该批评，但充满技术性补充：agwa 指出认证只能在注册时进行，且浏览器会通过权限提示告知用户，他怀疑 Netflix 或 Twitter 目前并不会拒绝未认证的 passkey。bmitch3020 主张可移植性与离线备份，认为手机指纹不如密码管理器中的长密码可靠；MathMonkeyMan 则指出认证确实有正当用途，可防范伪造的 passkey 应用。danpalmer 点出文章最后一条脚注的讽刺之处：作者承认 passkey 与域名绑定、能抵御中间人攻击，这可能是其最强的安全特性，却未在正文中提及。

**标签**: `#passkeys`, `#authentication`, `#digital privacy`, `#security`, `#platform lock-in`

---

<a id="item-4"></a>
## [AI 代理消耗 5000 亿 token 反编译一款第一人称射击游戏](https://momo5502.com/posts/2026-10-09-game-decompilation/) ⭐️ 7.0/10

工程师 momo5502 发布了一篇详细博文，介绍如何用 AI 代理驱动大约 5000 亿 token 的大模型算力，对一款商业第一人称射击游戏进行字节级匹配（byte-matching）反编译——重建出能够编译回原始二进制文件的源代码。该文登上了 Hacker News 首页（163 分、113 条评论），但作者提到此前两篇相关文章已被删除，并且出于商标原因他无法公开游戏名称。 它用一个真正困难的反向工程任务，具体而大规模地展示了代理式编码循环（agentic coding loop）目前能做什么、不能做什么，而不是又一篇关于 AI 编程的观点文章。讨论还把话题从工具层面推进到算力成本、知识产权与法律风险，并引出一种更宏观的判断：专有软件或许不得不转向云端，才能在 AI 辅助复制面前保住护城河。 最引人注目的是约 5000 亿「Luna 等价」token 的消耗，而作者本人也承认这基本上是个娱乐性质的副业实验；加上成果领域狭窄且受商标限制，它作为基准的可迁移性有限。由于目标是字节级匹配（编译结果与原始二进制完全一致），这套流程远比追求「功能等价」的反编译昂贵，而评论者认为后者可以快得多。

hackernews · davikr · 10月11日 02:02 · [社区讨论](https://news.ycombinator.com/item?id=50039092)

**背景**: 反编译是指从已编译的二进制文件中还原出可读源代码（如 C 或 C++），传统上靠人工或 IDA、Ghidra 等工具完成；而字节级匹配反编译是更严格的目标：重建出的代码重新编译后必须与原二进制完全一致。所谓 token 是大语言模型处理文本的基本单位，因此 token 数量实际上衡量了模型做了多少工作。这里的 AI「代理」指的是把大模型放进一个带工具和测试框架的循环里——包括提示、改文件、构建、验证等步骤——而不是一次性生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.06095">[2604.06095] LLM4CodeRE: Generative AI for Code Decompilation ...</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://microsoft.github.io/Workshop-Interact-with-OpenAI-models/tokenization/">Tokenization | Learn how to interact with OpenAI models</a></li>

</ul>
</details>

**社区讨论**: 讨论整体情绪是赞叹与质疑并存。一位评论者算了一笔环境账：约 5000 亿 Luna token 大致相当于 15 次旧金山—伦敦往返航班，或一个普通美国人约 15 个月的碳排放，并质疑一个永远无法广泛分享的成果意义何在；另一位则提出一个有趣的法律问题：即便代码不能分享，系统的 Lean/TLA+ 行为规范是否可以公开。有开发者提出更快的替代方案：让 Agent A 编写语义等价（而非字节匹配）的代码并同时写测试，交给测试框架验证；还有人认为专有软件终将迁往云端，因为如今任何本地程序都可能被「vibe 复制」，或被两个 AI 以净室方式逆向重写。

**标签**: `#AI agents`, `#code decompilation`, `#agentic workflows`, `#compute cost`, `#software IP`

---