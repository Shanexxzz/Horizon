---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 22 条内容中筛选出 8 条重要资讯。

---

1. [复杂系统如何失效：1998 年经典论述](#item-1) ⭐️ 9.0/10
2. [用 agent.md 文件提升 LLM 辅助编程的代码质量](#item-2) ⭐️ 8.0/10
3. [高级工程师分享发现关键问题的实用方法](#item-3) ⭐️ 7.0/10
4. [AI 智能体中的 Harness 是什么？](#item-4) ⭐️ 7.0/10
5. [做中学胜过看视频：对可汗学院式教学的批评](#item-5) ⭐️ 7.0/10
6. [关于邪教、骗局与阴谋的非虚构书单精选](#item-6) ⭐️ 7.0/10
7. [数据丢失致 17 万非营利组织数据全无，微软云可靠性遭质疑](#item-7) ⭐️ 7.0/10
8. [Anthropic 最佳 AI 模型难获用户青睐，更便宜工具走红](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [复杂系统如何失效：1998 年经典论述](https://how.complexsystems.fail/) ⭐️ 9.0/10

Richard Cook 于 1998 年撰写的《复杂系统如何失效》一文再次被广泛讨论。文章指出，复杂系统必然会发生故障，而安全性是通过韧性和适应来实现的，并非靠消除风险或寻找根本原因。 这篇文章至今仍是安全工程、韧性思维和系统思维的基础性文献，影响着医疗、航空和软件等行业。其中反直觉的观点挑战了传统的根本原因分析，并持续影响着混沌工程等现代实践。 Cook 强调，事故是由多种因素共同作用导致的常规事件，而非单一根本原因引发的。他还指出，无故障运行需要通过实际经历故障来积累经验，而且事后偏差会让过去的事故看起来比实际更可预测。

hackernews · shortcrct · 8月23日 15:13 · [社区讨论](https://news.ycombinator.com/item?id=49409473)

**背景**: Richard Cook 是一位医生兼安全研究人员，以研究复杂系统中的人与组织因素而闻名。这篇 1998 年首次发表的文章已成为韧性工程领域的关键文献。它描述了医院、电网和交通网络等系统天然具有危险性，而安全性正是源于系统内操作人员的持续适应。

**社区讨论**: 评论者普遍表示强烈认同，并补充了实践视角。有人指出，在复杂系统上进行根本原因分析是徒劳的；也有人将文章与混沌工程联系起来，认为主动制造故障有助于建立更好的防御体系。还有人推荐了 John Gall 的相关著作，并指出了原文中可能存在的拼写错误。

**标签**: `#complex systems`, `#mental models`, `#resilience`, `#safety engineering`, `#systems thinking`

---

<a id="item-2"></a>
## [用 agent.md 文件提升 LLM 辅助编程的代码质量](https://fabiensanglard.net/agent.md/index.html) ⭐️ 8.0/10

Fabien Sanglard 发布了他的个人 agent.md 文件，这是一套供 LLM 遵循的指令，编码工具会在会话开始时自动加载该文件。他表示，这个文件显著提升了代码质量，使其接近他手工编写的水平。 随着越来越多的开发者依赖 LLM 辅助编程，像这样具体且可共享的指导文件有助于提高一致性并减少重复修正。这也反映了 AGENTS.md 这一开放格式日益普及，正成为在各类工具中引导编码 Agent 的标准方式。 该 agent.md 文件包含代码风格规则，例如始终使用大括号、函数名保持简短，以及解释性指南，如添加简洁的注释并使用 ASCII 图来描述完整系统。作者指出，在使用 agent.md 之前，他必须在每个新会话中重复相同的指令，这非常繁琐。

hackernews · ibobev · 8月23日 17:59 · [社区讨论](https://news.ycombinator.com/item?id=49410932)

**背景**: AGENTS.md 是一种用于引导编码 Agent 的简单开放格式，常被描述为“给 Agent 的 README”。Cursor、Claude Code 和 GitHub Copilot 等现代编码工具会在每次 LLM API 调用时发送该文件，使其成为存放项目特定指令和偏好的稳定位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fabiensanglard.net/agent.md/index.html">My agent.md to improve LLM-assisted code quality</a></li>
<li><a href="https://github.com/agentsmd/agents.md">GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for ...</a></li>
<li><a href="https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/">How to teach your coding agent with AGENTS.md</a></li>

</ul>
</details>

**社区讨论**: 评论者建议，许多规则，例如始终使用大括号或保持函数名简短，应该通过 linting 强制执行，而不仅仅是依赖 LLM 指令。有人质疑 agents.md 文件的价值，也有人分享了自己的版本，其中包括一条“收敛规则”，要求每个任务最终要么成功、要么取得有意义的进展。一位评论者警告说，过于臃肿的 agent.md 文件会增加上下文消耗，并建议让 Agent 先思考需要做什么，再选择适用哪些规则。

**标签**: `#LLM`, `#coding`, `#AI tools`, `#code quality`, `#productivity`

---

<a id="item-3"></a>
## [高级工程师分享发现关键问题的实用方法](https://lalitm.com/post/find-problems-staff-engineer/) ⭐️ 7.0/10

一位高级工程师在 lalitm.com 上发表了基于经验的文章《高级工程师如何发现要解决的问题》，介绍了在大型公司中识别有影响力问题的常用方法。该文章引发了社区的热烈讨论，获得了 202 个点赞和 73 条评论。 这篇文章之所以重要，是因为它涉及高级工程师一项核心却很少被系统总结的能力：判断哪些问题值得投入精力和影响力。它也引发了对行业更广泛趋势的关注——在日益自上而下的管理环境中，工程师是否正在失去自下而上的自主权。 作者明确指出，自己的经验主要来自大型公司中具有高度自下而上自主权的基础设施和开发者工具团队。他提醒说，在更加自上而下的环境中，采用这些方法的空间可能本来就较为有限。

hackernews · vanpra · 8月23日 19:23 · [社区讨论](https://news.ycombinator.com/item?id=49411643)

**背景**: 高级工程师（staff engineer）是资深的技术个人贡献者，通常需要在没有直接管理权力的情况下发挥技术领导力并推动影响力。他们工作中的一个关键部分是识别哪些问题具有战略重要性并值得解决，而不是简单地执行任务。这篇文章为这一发现问题的方法提供了实用框架，同时承认组织环境在很大程度上决定了工程师真正拥有的自主空间。

**社区讨论**: 评论者就工程师实际拥有多少自主权展开了辩论：有人质疑行业趋势是否正在走向更自上而下的控制，而一位来自初创公司的评论者表示问题从来不会稀缺，真正的挑战是优先级排序。还有人认为大型科技公司存在过多闲散工程师，导致会议和文档等浪费性工作；另有人提醒，会问‘如何发现问题’的人可能尚未准备好承担真正的高级工程师角色。

**标签**: `#career`, `#engineering`, `#problem-solving`, `#staff-engineer`, `#leadership`

---

<a id="item-4"></a>
## [AI 智能体中的 Harness 是什么？](https://earendil.com/posts/what-is-a-harness/) ⭐️ 7.0/10

这篇文章用&\#x27;底盘-引擎-燃料-汽车&\#x27;的比喻，解释了 AI 智能体系统中&\#x27;harness&\#x27;（护栏/支架）的含义，并将其与底层模型区分开来。文章认为，harness 是模型周围的软件基础设施，它把原始 LLM 变成可工作的智能体。 随着 AI 智能体从演示走向生产，理解 harness 对于构建可靠、实用的智能体应用至关重要。这篇文章提供了一个经久耐用的心智模型，评论区分享的真实经验和陷阱对开发者有直接参考价值。 这个类比中：harness=底盘，模型=引擎，token=燃料，智能体=汽车。评论者还讨论了 harness 的实际功能，例如为智能体构建内部 CLI、跨模态/模型/提供商的&\#x27;交接（handoff）&\#x27;难题，以及 Pi 的扩展系统。

hackernews · tosh · 8月23日 14:24 · [社区讨论](https://news.ycombinator.com/item?id=49409092)

**背景**: Agent harness（智能体护栏/支架）是围绕大型语言模型的软件基础设施，负责管理工具调用、记忆、状态持久化、执行环境和反馈循环。由于 LLM 本身是无状态的，正是 harness 使其能够与外部世界交互并完成多步骤任务。一个流行的简写是&\#x27;智能体=模型+harness&\#x27;，harness 常被比作引擎周围的脚手架或底盘。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/concepts/harness">Agent Harness | Microsoft Learn</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>

</ul>
</details>

**社区讨论**: 评论区的整体情绪很热情：有评论者称 harness 是&\#x27;下一个前沿&\#x27;，一旦 LLM 基础设施标准化，harness 将成为真正的价值提供者，并称赞 Pi 的扩展系统。另一些人分享了实际实现经验，例如内部 CLI 对智能体很有价值、skills 常常过于局限于作者自身功能，还有人询问 CLI、Web 界面、团队成员、模态和模型/提供商之间的&\#x27;交接（handoff）&\#x27;方案。作者也指出，这篇文章本来是面向非极客读者，并补充了&\#x27;底盘-引擎-燃料-汽车&\#x27;的类比。

**标签**: `#AI Agents`, `#LLM Tooling`, `#Mental Models`, `#Agent Architecture`, `#Developer Experience`

---

<a id="item-5"></a>
## [做中学胜过看视频：对可汗学院式教学的批评](https://punyamishra.com/2026/04/16/why-sal-khant-on-learning-by-making-but-teaching-by-telling/) ⭐️ 7.0/10

Punya Mishra 发表博文，批评可汗学院以视频为先的教学模式，认为“做中学”（constructionism）优于被动观看教学视频。该文在 Hacker News 上引发了 76 条评论的讨论，围绕翻转课堂、反馈机制和主动学习展开。 这场辩论触及教育科技的核心问题：视频讲授和动手建构，哪种方式更能促进深层理解。它对设计课程的教师、为孩子选择学习工具的家长，以及像可汗学院这样的教育科技平台的评估都具有重要意义。 文章指出，现场教学能在学生困惑时提供即时反馈，而视频无法做到这一点；不过评论者也提到，视频会受益于全球观众对内容的纠错。还有评论将这种方法与哈佛物理学家 Eric Mazur 开创的“翻转课堂”联系起来，一位用户称赞可汗学院会推导公式而非仅仅呈现公式。

hackernews · the-mitr · 8月23日 15:59 · [社区讨论](https://news.ycombinator.com/item?id=49409862)

**背景**: 被动学习（如观看讲座视频）以教师为中心，而主动学习则通过提问、练习和反馈让学生参与进来。Seymour Papert 提出的建构主义（constructionism）理论认为，当人们在现实世界中制作有形的物品时学习效果最好，它建立在让·皮亚杰的建构主义（constructivism）观点之上。翻转课堂是一种混合式学习策略，把讲座放到课后，把课堂时间用于解决问题，这种模式通常与主动学习联系在一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flipped_classroom">Flipped classroom - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Constructionism_%28learning_theory%29">Constructionism (learning theory)</a></li>
<li><a href="https://bokcenter.harvard.edu/flipped-classrooms">Flipped Classrooms | The Derek Bok Center for Teaching and ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大体认同文章的核心论点，但认为对可汗学院的描述不够公允，指出视频可以作为深入理解的脚手架，并受益于全球性的反馈机制。还有人提到翻转课堂已被广泛接受；一位可汗学院的资深用户则称赞该平台通过推导公式来教学，而非让学生死记硬背。

**标签**: `#education`, `#learning`, `#khan-academy`, `#active-learning`, `#personal-growth`

---

<a id="item-6"></a>
## [关于邪教、骗局与阴谋的非虚构书单精选](https://bookdna.com/best-books/nonfiction-about-cults-scams-and-schemes) ⭐️ 7.0/10

BookDNA 发布了一份关于邪教、骗局与阴谋的非虚构类书籍精选书单。社区评论补充了几本明显缺失的重要著作，例如 Steven Hassan 的《Combating Cult Mind Control》以及 Bridget Read 在 2025 年出版的关于 MLM（多层次传销）的《Little Bosses Everywhere》。 这篇文章的评分为 7.0/10，被认为虽非开创性，但在互动和讨论质量上表现良好。评论者指出，从资深爱好者的角度看这份书单略显稀疏，并补充了 Howdunit 系列、《Spying In Guru Land》和《Life 102》等书目。

hackernews · bwb · 8月23日 13:51 · [社区讨论](https://news.ycombinator.com/item?id=49408858)

**背景**: 关于邪教、骗局和阴谋的非虚构类书籍通常探讨心理操控、高控制团体、欺诈和欺骗性体系。这类书籍在关注批判性思维、想理解人们如何被招募、控制及利用的读者中很受欢迎。

**社区讨论**: 评论者总体上认可这一主题，但从资深爱好者的角度批评书单不够完整。重要推荐包括 Steven Hassan 的《Combating Cult Mind Control》作为首要读物、Bridget Read 2025 年关于 MLM 的《Little Bosses Everywhere》、针对个人骗局的 Howdunit 系列，以及《Spying In Guru Land》和《Life 102》等区域性或有针对性的纪实作品。

**标签**: `#books`, `#cults`, `#scams`, `#critical-thinking`, `#psychology`

---

<a id="item-7"></a>
## [数据丢失致 17 万非营利组织数据全无，微软云可靠性遭质疑](https://slate.com/technology/2026/08/microsoft-software-nonprofit-data-delete.html) ⭐️ 7.0/10

一起数据丢失事件已导致超过 17 万家非营利组织的所有数据被清除。该事件引发公众对微软云存储可靠性以及云端数据管理整体风险的审视。 这一事件凸显了在缺乏适当备份策略的情况下依赖云服务商进行数据保留的巨大风险。受影响机构数量庞大，许多非营利组织可能缺乏恢复数据的技术资源，这或将促使各机构重新审视云端存储与灾难恢复方案。 微软的保留政策规定，在账户过期或终止后，客户数据将在 180 天内被删除。根据共享责任模型，备份数据的责任在客户一方，这使得缺乏准备的非营利组织可能没有任何恢复手段。

hackernews · tchalla · 8月23日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=49411395)

**背景**: 云存储服务遵循共享责任模型：服务商负责基础设施安全，而客户需自行保护数据。Microsoft 365 会在订阅终止后自动删除客户数据，通常最大保留期为 180 天。许多小型组织，尤其是非营利组织，可能没有完善的数据备份策略（如不可变备份），因而面临永久性数据丢失的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/compliance/assurance/assurance-data-retention-deletion-and-destruction-overview">Data retention, deletion, and destruction in Microsoft 365 - Microsoft Service Assurance | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility">Shared responsibility in the cloud - Microsoft Azure | Microsoft Learn</a></li>
<li><a href="https://www.ibm.com/think/topics/immutable-backups">What are immutable backups? - IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者大多批评微软，有人称其&quot;不严肃&quot;，是&quot;一个极不严肃行业的先锋&quot;。还有人分享了个人数据丢失经历，并指出官方过渡警告邮件未被垃圾邮件过滤器拦截。一位评论者还告诫不要使用 SSD 进行归档，反映出对云存储短暂性的广泛担忧。

**标签**: `#data loss`, `#cloud computing`, `#Microsoft`, `#risk management`, `#backup`

---

<a id="item-8"></a>
## [Anthropic 最佳 AI 模型难获用户青睐，更便宜工具走红](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

Anthropic 在 2026 年 7 月的年化收入达到 650 亿美元，高于 5 月的 470 亿美元，并向投资者表示预计第三季度将实现盈利。然而，Ramp 的账单数据显示，其最新旗舰模型 Fable 5 仅占 Anthropic 模型支出的 8.0%，而较旧且更便宜的 Opus 4.8 占比高达 28.0%。 这些数据揭示了营收增长与最先进（且可能最昂贵）AI 模型采用率之间的显著差距。如果企业继续偏好更便宜、较旧的模型，整个 AI 行业的定价和模型设计策略可能会转向成本效益导向。 Anthropic 拥有 6,000 个年消费 10 万美元及以上的客户，而 OpenAI 的年化收入在季度至今增长 35%后已超过 400 亿美元。基于 7 万家公司账单数据的 Ramp AI 指数显示，Opus 4.8 以 28%的 Anthropic 支出占比领先，Sonnet 4.6 为 8.3%，Fable 5 为 8.0%，而刚发布的 Opus 5 仅占 3.5%。

rss · Simon Willison · 8月23日 20:24

**背景**: 年化收入是一种运行率估算，将当前月度收入外推至全年，常用于追踪 Anthropic 和 OpenAI 这类快速增长的非上市公司。Ramp AI 指数通过分析超过 7 万家使用 Ramp 企业信用卡和账单支付平台的公司的账单数据，衡量真实的 AI 采用和支出水平。像 OpenAI 这样的机构已在 2026 年 7 月发布 GPT-5.6 新模型系列以刺激需求。Anthropic 的 Claude 模型分为 Opus、Sonnet、Haiku 等层级，而 Fable 似乎是其最新旗舰系列；文章指出 Fable 的高成本使其受欢迎程度降低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#revenue`, `#AI adoption`

---