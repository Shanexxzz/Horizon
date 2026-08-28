---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 39 条内容中筛选出 12 条重要资讯。

---

1. [Cloudflare 通过优化 1.1.1.1 DNS 缓存节省 100TB 内存](#item-1) ⭐️ 8.0/10
2. [小语言模型走向主流，关注点从尖端 AI 转向高效本地部署](#item-2) ⭐️ 8.0/10
3. [开源维护者怒斥：为刷简历而提交的 AI 生成 PR 泛滥](#item-3) ⭐️ 8.0/10
4. [谷歌发布 Gemini 3.5 Transcribe 人工智能语音转文字模型](#item-4) ⭐️ 8.0/10
5. [ChatGPT 结合批判性思维训练提升学生原创性](#item-5) ⭐️ 8.0/10
6. [Gemini Omni 1.1 Flash 新增视频创作控制，赋能开发者](#item-6) ⭐️ 8.0/10
7. [谷歌 DeepMind 率先试点双盲 AI 评测](#item-7) ⭐️ 8.0/10
8. [研究者通过 ZIP 压缩包提示注入攻破 Claude Code Auto Mode](#item-8) ⭐️ 8.0/10
9. [乔布斯流放岁月：法纳姆街播客深度解读](#item-9) ⭐️ 7.0/10
10. [Buffer 发布 2026 年 11 款最佳社媒分析与报告工具](#item-10) ⭐️ 6.0/10
11. [Wondering Canvas 支持并行视觉 ChatGPT 对话](#item-11) ⭐️ 6.0/10
12. [IQ Routing：基于轨迹的 LLM 路由削减智能体成本](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Cloudflare 通过优化 1.1.1.1 DNS 缓存节省 100TB 内存](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare 发布了一篇博文，讲述了他们如何将 1.1.1.1 公共 DNS 解析器的内存占用减少 100 TB。这些节省源于对缓存数据结构和内存分配进行的系统性底层优化。 这个案例表明，在大规模基础设施中进行内存优化可以带来巨大的成本和性能收益。它也凸显了系统编程技能的重要性，即使在以 Rust 这样的内存安全语言构建的现代环境中依然如此。 这些优化涉及多种技术，例如消除记录数据的单独分配、缩小每个条目的开销以及更积极地复用内存。一些评论者指出，将多个独立列表合并为一个列表的做法可能会在一定程度上削弱 Rust 的安全保证。

hackernews · TangerineDream · 8月27日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=49468083)

**背景**: 1.1.1.1 是 Cloudflare 的公共 DNS 解析器，负责将人类易读的域名转换为 IP 地址。为了处理海量查询，解析器会缓存 DNS 响应，而部署在全球数据中心时，这种缓存会消耗巨大的内存。优化此类缓存已成为大规模互联网基础设施的核心关注点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/1.1.1.1">1.1.1.1 - Wikipedia</a></li>
<li><a href="https://developers.cloudflare.com/1.1.1.1/">1.1.1.1 (DNS Resolver) · Cloudflare 1.1.1.1 docs</a></li>
<li><a href="https://www.akamai.com/glossary/what-is-dns-caching">What Is DNS Caching ? | How Does DNS Caching Work ? | Akamai</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上对这项工程工作表示赞赏，尽管有些人认为这些技术相当常规。一位评论者分享了自己通过单次 malloc 将黑名单内存从 237 MB 降至 9.5 MB 的经验，其他人讨论了结构体对齐，还有少数人担心这些优化会对 Rust 的安全保证产生影响。

**标签**: `#systems programming`, `#memory optimization`, `#DNS`, `#Cloudflare`, `#engineering`

---

<a id="item-2"></a>
## [小语言模型走向主流，关注点从尖端 AI 转向高效本地部署](https://calv.info/small-models-have-arrived) ⭐️ 8.0/10

文章认为，小语言模型的能力已足以胜任许多现实应用，并预测对“快速/便宜/够用”模型的需求将上升。这标志着关注点正从尖端规模系统转向高效、本地的部署。 这一转变可能通过降低成本、提升隐私保护以及支持消费端和创作者经济中的设备端产品，使 AI 更加普及。它也为初创公司或产品开发者创造了机会，他们现在无需依赖前沿实验室就能使用能力足够的模型。 小语言模型通常参数低于 100 亿，可以在笔记本电脑、手机或本地服务器上运行，提供更低延迟和更紧凑的部署边界。但与前沿模型相比，它们可能缺乏广泛的世界知识；前沿模型通常经过数万亿参数训练，以支持推理和多模态任务。

hackernews · tosh · 8月27日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49466917)

**背景**: 前沿 AI 指的是在推理、多模态理解和自主任务上推动边界的大规模通用模型，通常以数十亿或数万亿参数训练。相比之下，本地 AI 意味着完全在自己的硬件上运行模型，从而保证数据隐私、零 API 成本以及离线可用性。文章认为，小模型的成熟是通向实用、面向特定应用 AI 的关键一步，而非一味追求越来越大的通用系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agneya.medium.com/small-language-models-are-winning-db22c3fbf062">Small Language Models Are Winning | by Agneya Pathare | Medium</a></li>
<li><a href="https://www.local-llm.net/learn/what-is-local-ai/">What Is Local AI? The Complete Guide to Running AI on Your ...</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了乐观且细致的观点：有人提到早期使用 7B 本地模型进行代码生成的实验，也有人讨论了为什么消费级 AI 公司稀少，并与前沿实验室进行对比。还有人将工作模式与 Paul Graham 的“制造者日程”进行比较，并推测大参数规模与其说是用于推理，不如说是用于储存世界知识。

**标签**: `#AI`, `#small language models`, `#productivity`, `#creator economy`, `#technology trends`

---

<a id="item-3"></a>
## [开源维护者怒斥：为刷简历而提交的 AI 生成 PR 泛滥](https://neilalexander.dev/2026/06/30/flooding-contributions) ⭐️ 8.0/10

Neil Alexander 于 2026 年 6 月 30 日发布文章，批评大量仅为充实简历而提交的 AI 生成 PR。社区讨论探索了检测、处理并重新思考此类贡献的方法。 这凸显了开源领域日益严重的信任问题：低质量 AI 贡献加重了维护者负担，并贬低了真正贡献的价值。这影响到维护者、贡献者以及围绕贡献指标和审核的平台政策。 评论者称每周收到约五个低质量 AI 生成 PR，有时这些 PR 忽略了仓库中的 AGENTS.md 文件。提出的解决方案包括使用 AI 进行自动筛选、让平台单独统计或标注此类 PR，以及建立跨项目的贡献者声誉分。

hackernews · signa11 · 8月28日 03:49 · [社区讨论](https://news.ycombinator.com/item?id=49474143)

**背景**: 在开源开发中，拉取请求（PR）允许外部贡献者提出代码更改，由维护者审查并合并。AI 编程助手能快速生成看似合理但肤浅的修改，导致低质量贡献大量涌入。文章认为这种行为破坏了开源的信任基础，并浪费了维护者的时间。

**社区讨论**: 评论大多表示认同，有人建议维护者用 AI 来过滤 AI 生成的 PR。也有人认为平台应以不同方式统计或展示这些 PR，还有评论者指出 AI 侵蚀信任，可能阻碍未来的开源发布，进而对新人不公平。

**标签**: `#AI ethics`, `#open source`, `#maintainer experience`, `#content quality`, `#developer culture`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.5 Transcribe 人工智能语音转文字模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.5 Transcribe，一款新的人工智能语音转文字模型。该模型将为 Gboard 的 Rambler 功能提供支持，并陆续集成到 Chrome 等谷歌产品中，提供更智能的转录体验。 该发布对创作者工作流和 AI 工具意义重大，可能重塑转录和实时翻译服务。早期测试表明它在准确性上领先，可能对 Soniox 和 Eleven Labs 等竞争对手构成压力。 社区测试显示 Gemini 3.5 Transcribe 在准确性上超越其他模型，但延迟较明显，这对实时语音转文字应用至关重要。该模型还支持函数调用，可委派图像生成等任务，并已通过 Gemini API 开放。

hackernews · k9294 · 8月27日 18:03 · [社区讨论](https://news.ycombinator.com/item?id=49468818)

**背景**: 语音转文字（STT）模型将语音音频转换为书面文本，是语音助手、字幕和翻译工具的基础。Gemini 3.5 Transcribe 属于谷歌的 Gemini 系列，利用大语言模型技术处理多语言转录和翻译，与传统声学模型有所区别。它的竞品包括 Soniox STT v5、Voxtral Mini 3b 和 Eleven Labs 等专用 STT 服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Introducing Gemini 3.5 Transcribe - The Keyword</a></li>
<li><a href="https://deepmind.google/models/gemini-audio/ai-transcription/">Gemini Audio – AI transcription — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/google-announces-gemini-3-5-transcribe-for-ai-powered-speech-to-text/">Google announces Gemini 3.5 Transcribe for AI-powered speech ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：Fliptalk 的一位测试者认为在实时翻译场景下 Soniox STT v5 的延迟更优，但认可 Gemini 3.5 的准确性；另一位用户更偏好 Voxtral Mini 3b 用于本地及行业专业场景；还有 Pixel 11 Pro 用户不喜欢模型会“简化”精确措辞。另有一位开发者指出关于函数调用的文档令人困惑。

**标签**: `#AI`, `#speech-to-text`, `#Gemini`, `#transcription`, `#creator tools`

---

<a id="item-5"></a>
## [ChatGPT 结合批判性思维训练提升学生原创性](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training) ⭐️ 8.0/10

一项针对 1000 多名学生的随机研究发现，将 ChatGPT 的使用与批判性思维训练相结合，能显著提高学生在真实大学作业中的原创性和表现。 这项基于证据的对照研究为在教育中整合 AI 工具同时不损害学习效果提供了一个可信的范例。它为教育者和政策制定者关于如何平衡 AI 应用与培养人类思维能力的持续争论提供了参考。 该研究采用真实大学作业而非合成测试，并同时衡量了原创性和表现。结果表明，教学设计——特别是批判性思维训练——是发挥 ChatGPT 教育益处的关键。

rss · OpenAI News · 8月27日 09:00

**背景**: ChatGPT 是一种大型语言模型，可以生成文本、回答问题并协助完成各种任务。批判性思维指分析、评估和构建合理论证的能力。该研究考察了接受过此类技能专门训练的学生是否能更有效地将 ChatGPT 用于复杂的学术任务。

**标签**: `#AI education`, `#critical thinking`, `#ChatGPT`, `#research`, `#learning`

---

<a id="item-6"></a>
## [Gemini Omni 1.1 Flash 新增视频创作控制，赋能开发者](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/) ⭐️ 8.0/10

Google DeepMind 发布了 Gemini Omni 1.1 Flash，该模型于 2026 年 8 月 27 日通过 Gemini API 推出，带来一系列创作控制和生成式视频能力。它支持 40 秒场景扩展、首尾帧控制，以约三分之一成本生成 360p 草稿，并可输出最高 4K 分辨率且带音频的视频。 此次发布让开发者对 AI 生成的视频拥有更强的控制力，可通过自然语言工作流进行精确编辑、扩展和放大。它使高质量视频生成更易用、更经济，直接惠及 AI 工具用户和内容创作者。 主要功能包括 40 秒场景扩展、首尾帧控制、每秒 0.03 美元的 360p 草稿并支持放大至 4K，以及带同步音频的输出。该模型已集成到 Adobe Firefly，并可在 Comfy 上使用，单节点即可支持文生视频、图生视频、参考生视频、视频编辑和场景扩展。

rss · Google DeepMind · 8月27日 16:11

**背景**: Gemini Omni 是谷歌的多模态 AI 模型系列，支持多种输入和输出模态，包括视频。Flash 版本优先考虑速度和效率，适用于实时或近实时应用。生成式视频模型通常将文本或图像转换为视频，而增加帧锚定和低成本草稿等控制功能，则扩展了其在专业创作者和开发者中的实用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/">Build with Gemini Omni 1 . 1 Flash</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash">Gemini Omni Flash | Gemini API | Google AI for Developers</a></li>
<li><a href="https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026">Gemini Omni 1.1 Flash: 40s Extensions, $0.03/s Drafts (Aug ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#Google DeepMind`, `#Developer Tools`, `#Model Release`

---

<a id="item-7"></a>
## [谷歌 DeepMind 率先试点双盲 AI 评测](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) ⭐️ 8.0/10

谷歌 DeepMind 宣布，正在试点全球首个针对专有前沿 AI 模型的双盲评测。评测被密封在加密“盒子”中，模型开发者与评测方都无法看到对方的数据。 这是 AI 透明性和信任度方面一项重要的方法论突破。若被广泛采用，双盲评测可能成为评估前沿模型的新标准，减少“刷基准”的动机，并为监管机构和用户提供更可靠的性能信号。 该系统利用加密安全区实现双向盲测，模型提供方和评测方都看不到对方的数据。该试点源于研究显示“基准攻击”问题紧迫，曾有前沿实验室在 Chatbot-Arena 上测试了 27 个私有模型变体，只发布最高分的那一个。

rss · Google DeepMind · 8月27日 12:59

**背景**: 传统 AI 基准测试可能被“钻空子”，因为模型可能在测试数据上训练或调优，这被称为基准污染或基准攻击。双盲方法借鉴自临床试验，通过确保模型开发方和基准评测方都不知道对方的输入来防止此类问题。这次试点用基于硬件的加密安全区将这一理念应用于前沿 AI 模型，向着更可信的 AI 评测标准迈出一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/">Piloting the world&#x27;s first double-blind AI evaluations</a></li>
<li><a href="https://www.explainx.ai/blog/google-deepmind-double-blind-ai-evaluation-benchmark-contamination-august-2026">DeepMind Double-Blind AI Evaluation: How It Works (2026 ...</a></li>
<li><a href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/piloting-the-worlds-first-double-blind-ai-evaluations/double-blind-evaluations-technical-report.pdf">Double Blind Evals: Resolving the Dual Confidentiality ...</a></li>

</ul>
</details>

**标签**: `#AI evaluation`, `#double-blind methodology`, `#AI safety`, `#Google DeepMind`, `#research standards`

---

<a id="item-8"></a>
## [研究者通过 ZIP 压缩包提示注入攻破 Claude Code Auto Mode](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

安全研究员 Johann Rehberger 展示了一种提示注入攻击，约 80%的情况下能绕过 Claude Code 的 auto mode 保护。该攻击诱导 Claude Code 下载并解压 zip 压缩包，然后在导入 base64 时执行被劫持的本地 struct.py 文件。 此事意义重大，因为 Anthropic 最近将 auto mode 设为 Claude Code Pro、Max 和 Team 计划的默认模式，并宣称其非常安全。该漏洞表明，即使内置安全防护的 AI 代理也可能被攻破，因此任何运行无人值守编码代理的人都必须采用沙箱和网络限制。 该攻击利用 Python 的模块搜索路径：压缩包内含恶意 struct.py，作为标准库 base64 模块的依赖被导入。在数次运行中，auto mode 甚至阻止了 Claude 自行终止恶意进程的清理命令，使安全机制本身成为失败的一环。

rss · Simon Willison · 8月27日 22:50

**背景**: 提示注入是一类攻击，攻击者将恶意指令隐藏在输入内容（如网页或文件）中，诱使大语言模型执行非预期行为。Auto mode 是 Claude Code 的一种权限模式，通过分类器自动批准或阻止操作，Anthropic 已将其设为许多计划的默认模式。Python 解释器导入模块时会先搜索当前目录，因此这类基于 zip 压缩包的攻击可以把恶意模块放在会被正常 import 加载的位置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode-default-in-claude-code">Auto mode is now the default in Claude Code for Pro, Max, and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://github.com/echo-devim/pyjacktrick">GitHub - echo-devim/pyjacktrick: Python module hijacking POC · GitHub</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#AI security`, `#Claude Code`, `#coding agents`, `#vulnerability`

---

<a id="item-9"></a>
## [乔布斯流放岁月：法纳姆街播客深度解读](https://fs.blog/knowledge-project-podcast/geoffrey-cain/) ⭐️ 7.0/10

法纳姆街（Farnam Street）的知识项目播客于 9 月 1 日发布了一期节目，深入探讨史蒂夫·乔布斯在 1985 年被逐出苹果公司至 1990 年代末回归之间那段鲜为人知的故事。该期节目邀请到杰弗里·凯恩（Geoffrey Cain）作为嘉宾，会员在公开释出前可提前收听。 这期节目之所以重要，是因为它审视了乔布斯生命中塑造其后来成功的关键时期，为听众提供了关于韧性、领导力和创造力的宝贵启示。对于关注个人成长的受众来说，它带来了超越普通科技新闻的深度洞察。 该节目属于法纳姆街知识项目播客系列，嘉宾为杰弗里·凯恩。内容聚焦于 1985 年乔布斯被迫离开苹果到 1990 年代末重返公司之间的岁月，这段经历在主流叙事中常常被一笔带过。

rss · Farnam Street · 8月27日 09:50

**背景**: 史蒂夫·乔布斯于 1976 年联合创立了苹果公司，并于 1985 年被迫离开这家自己一手创立的公司。在“流放”期间，他创办了计算机公司 NeXT，并从卢卡斯影业收购了皮克斯（Pixar），后者后来制作了热门动画电影《玩具总动员》。1997 年，苹果收购了 NeXT，乔布斯因此回归并出任临时 CEO，随后带领公司推出了 iMac、iPhone 和 iPad 等划时代产品，取得了历史性成功。

**标签**: `#Steve Jobs`, `#leadership`, `#personal growth`, `#resilience`, `#creativity`

---

<a id="item-10"></a>
## [Buffer 发布 2026 年 11 款最佳社媒分析与报告工具](https://buffer.com/resources/best-social-media-analytics-tools/) ⭐️ 6.0/10

Buffer 发布了 2026 年 11 款最佳社交媒体分析与报告工具的盘点文章，旨在帮助创作者将多个平台的指标汇总在一起。 这份清单对于需要在统一面板中跟踪多个平台表现的内容创作者和营销人员来说很有用，有助于改进内容策略和提高效率。它也反映出创作者经济中对整合分析工具日益增长的需求。 提供的文章片段并未列出这 11 款工具，也没有包含详细对比。该文面向同时管理多个平台的创作者，强调指标整合与解读。

rss · Buffer · 8月27日 10:00

**标签**: `#social media analytics`, `#creator economy`, `#content strategy`, `#productivity`, `#tools`

---

<a id="item-11"></a>
## [Wondering Canvas 支持并行视觉 ChatGPT 对话](https://www.producthunt.com/products/wondering-2) ⭐️ 6.0/10

Wondering 推出了 Canvas，这是其用户研究平台的一项新功能，允许在数字画布上并行运行多个视觉 ChatGPT 对话。这使 AI 交互超越了简单的聊天窗口，进入可视化、可编辑的工作空间。 这对 AI 生产力很重要，因为它让研究人员和知识工作者可以并行探索复杂主题，而不是顺序进行，从而节省时间并更好地比较想法。这也反映了 AI 工具采用基于画布的界面而非传统仅聊天布局的行业趋势。 该工具在 Product Hunt 上获得了 6.0/10 的评分，评论指出它有趣但并非开创性，且缺乏证据支持。它被定位为视觉学习和研究平台，而非通用 ChatGPT 客户端，缺乏社区讨论意味着其实际验证尚未得到评估。

rss · Product Hunt · 8月27日 06:40

**背景**: Visual ChatGPT 于 2023 年 3 月推出，是一个将 ChatGPT 与各种视觉基础模型连接的系统，使用户能够发送和接收图像，并通过自然语言执行复杂的视觉编辑或问答任务。像 Wondering Canvas 这样的基于画布的 AI 工具进一步将这一概念扩展，允许用户在数字画布上空间排列多个对话或任务，从而促进并行探索和更好的视觉思想组织。这种方法是更广泛的趋势的一部分，即从线性聊天界面转向更灵活、可编辑的 AI 工作空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stork.ai/en/wondering-canvas">Wondering Canvas Review (2026) | Stork.AI</a></li>
<li><a href="https://toolwise.ai/news/wondering-canvas-ai-research-tool-launch">User Research Tool Adds AI Canvas Workspace | ToolWise</a></li>
<li><a href="https://arxiv.org/abs/2303.04671">[2303.04671] Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#productivity`, `#visual-chatgpt`, `#parallel-processing`, `#tool`

---

<a id="item-12"></a>
## [IQ Routing：基于轨迹的 LLM 路由削减智能体成本](https://www.producthunt.com/products/iq-routing) ⭐️ 6.0/10

IQ Routing 是一个新推出的即插即用 LLM 网关，它会对请求进行分类、提供缓存服务，并将请求路由到达到质量门槛的最便宜模型，旨在降低智能体成本。该产品已在 Product Hunt 上线，并声称在自身流量上可减少 40%至 80%的开支，且可在 30 秒内完成部署。 对于精通 AI 工具的创作者和运行 LLM 智能体的企业来说，这解决了一个关键痛点：在保持输出质量的同时优化成本。其轨迹感知方法不同于传统的按调用路由，可能影响整个行业优化智能体工作流的方式。 该工具的独特见解是：智能体是一个轨迹，而非独立调用的流，因此它对样板步骤使用便宜模型，对关键步骤使用更强模型。它是一个即插即用网关，并且存在开源替代方案（如 UIUC 的 LLMRouter）可供比较。

rss · Product Hunt · 8月27日 06:54

**背景**: LLM 路由是一种根据复杂度、成本和质量等因素将每个请求发送到最合适模型的技术。传统路由会独立地为每次调用做决策，而轨迹感知路由会考虑智能体工作流中整个调用序列。这种区别很重要，因为智能体循环通常包含许多不需要顶级模型的常规调用，因此整体路由可以在不牺牲任务完成质量的情况下带来显著的成本节约。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.producthunt.com/products/iq-routing">IQ Routing: Trajectory-aware LLM routing that cuts agent cost | Product Hunt</a></li>
<li><a href="https://iq-routing.com/">Route Every LLM Call to the Cheapest Model | IQ Routing</a></li>
<li><a href="https://launly.com/products/iq-routing">IQ Routing — Trajectory-aware LLM routing that cuts agent ...</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#LLM routing`, `#cost optimization`, `#productivity`, `#creator economy`

---