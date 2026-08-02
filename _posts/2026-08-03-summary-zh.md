---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 20 条内容中筛选出 3 条重要资讯。

---

1. [卡帕西的 3D《指环王》演示引发 AI 基准测试之争](#item-1) ⭐️ 8.0/10
2. [欧盟年龄验证项目强制要求硬件绑定证明](#item-2) ⭐️ 7.0/10
3. [美国 AI 企业联名公开信呼吁支持开放权重模型](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [卡帕西的 3D《指环王》演示引发 AI 基准测试之争](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

安德烈·卡帕西在推文中表示，他给 Anthropic 的 Claude Opus 5 提供了《指环王》的第一段以及约 10 美元、100 万 token 的预算，模型花了大约两小时编写了 5500 行 three.js 代码，以程序化方式在 3D 中渲染了故事。他说 AI 正‘开始离开’诸如‘创建一个骑自行车的鹈鹕 SVG’这类简单提示词的领域。 这标志着 AI 能力评估方式的转变，从简单的图像生成提示转向需要理解物理世界的复杂、多步骤创意编程。它也重新引发了关于粗糙的 3D 输出是否是有意义的基准，或者仅仅是模型对 three.js 过拟合的证据的争论。 输出被描述为‘有点粗糙但有趣’，整个过程大约需要两小时的自主工作。这些代码程序化生成场景，而不是使用预先构建的资源，卡帕西将其作为 LLM 更通用基准的一个例子。

hackernews · delichon · 8月2日 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: 大型语言模型通常用诸如‘创建一个骑自行车的鹈鹕 SVG’这样的简单提示来测试，但卡帕西认为这类测试正在过时。研究人员最近引入了 PhysBench 和 PAI-Bench 等基准，用于评估模型在视频生成和理解任务中对物理世界的理解。卡帕西的演示将这个想法扩展到通过代码进行程序化 3D 场景生成，并以一段著名的文学描述作为输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xcancel.com/karpathy/status/2083749667410727319">Andrej Karpathy (@karpathy): &quot;We&#x27;re starting to leave the territory where you&#x27;d test an LLM by e.g. &quot;create an svg of pelican on a bicycle&quot;. As one idea to generalize it, I was interested what Opus 5 would do if I gave it the first paragraph of the Lord of the Rings, a 1M token budget (~$10) and asked for three js render of it. Opus went off for ~2 hours and wrote 5500 lines of code that (procedurally) rendered the story. It&#x27;s kind of janky but fun. But it&#x27;s a bit mindboggling that the LLM has to place and</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/08/60861644/andrej-karpathy-says-ai-has-moved-beyond-simple-prompts-after-claude-opus-builds-3d-lord-of-the-rings-world">Andrej Karpathy Says AI Has Moved Beyond Simple Prompts After Claude Opus Builds 3D Lord of the Rings Wor - Benzinga</a></li>
<li><a href="https://arxiv.org/abs/2501.16411v2">[2501.16411v2] PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人同意粗糙的输出正是关键所在，因为它为未来的进展创建了一个定性基准；另一些人则怀疑 Anthropic 的模型是专门针对编写 three.js 代码训练的，因此不那么能代表通用理解。还有评论者担心，接触 AI 内容降低了人们对质量的期望，让一个‘粗糙的鹈鹕’看起来像是已经解决的问题。另一个人分享了使用 LLM 构建 3D DeLorean 动画的实践经验，认为有趣但需要大量调优。

**标签**: `#AI`, `#benchmarks`, `#3D`, `#LLM`, `#Karpathy`

---

<a id="item-2"></a>
## [欧盟年龄验证项目强制要求硬件绑定证明](https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/) ⭐️ 7.0/10

欧盟委员会已推出一款强制要求硬件绑定证明的年龄验证应用，用户需通过带有硬件支持的密钥的移动应用验证年龄。这改变了此前纯粹依赖零知识证明（ZKP）来保护隐私的方案。 这一决定引发了重大的隐私和数字主权担忧，因为年龄验证被绑定到谷歌和苹果等硬件厂商，可能使用户被跟踪和关联。这也带来了反竞争的问题，并可能实际上将 Linux 桌面用户排除在外。 硬件绑定证明使用由硬件制造商根 CA 认证的设备专属密钥；与基于 ZKP 的系统不同，它可能会暴露硬件标识符，由中间人将其转换为临时证书。Linux 桌面用户需要另备一台移动设备才能使用该系统，而且该应用据称是临时性的，欧盟后续计划推出更广泛的数字钱包。

hackernews · RobotToaster · 8月2日 20:44 · [社区讨论](https://news.ycombinator.com/item?id=49148128)

**背景**: 年龄验证是为了防止未成年人访问成人内容的一项监管要求，通常由欧盟《数字服务法》等法律强制规定。欧盟的年龄验证蓝图原本围绕零知识证明（ZKP）设计，以在不泄露身份的情况下证明年龄；然而，实际实施现在强制要求硬件绑定证明，将验证与可信平台模块和应用商店证明服务绑定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ageverification.dev/">EU Age Verification Blueprint — the dedicated technical portal</a></li>
<li><a href="https://eutechloop.com/the-eus-age-verification/">The EU &#x27;s age verification app launched: technically ready, legally...</a></li>
<li><a href="https://stealthcloud.ai/glossary/attestation/">Attestation (Cryptographic) | Definition &amp; Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者担心硬件绑定证明方法会暴露硬件 ID，并允许中间方协作勾结，同时批评欧盟强制依赖 Google/Apple 账户既是主权问题也是反竞争问题。还有人指出，Linux 用户需要另备一台非 Linux 设备，这削弱了系统的可及性。

**标签**: `#digital identity`, `#privacy`, `#EU policy`, `#age verification`, `#hardware attestation`

---

<a id="item-3"></a>
## [美国 AI 企业联名公开信呼吁支持开放权重模型](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

2026 年 7 月下旬，微软牵头组织了一封由 235 家 AI 相关企业（包括 NVIDIA、亚马逊和 OpenAI）联署的公开信，呼吁美国政策制定者支持开放权重模型。数天后，另一封名为《Pacing the Frontier》的公开信获 1324 名前沿 AI 企业员工签署，呼吁国际社会共同治理、审慎把握 AI 发展的节奏。 这标志着 AI 行业对美国政府可能限制开放权重模型的强烈反对，可能影响 AI 监管方向。OpenAI/微软与 Anthropic 之间的立场分歧，凸显了关于开放与封闭 AI 安全策略日益激烈的争论。 微软的公开信明确为“蒸馏”（用其他模型的输出训练模型）辩护，敦促政策制定者不要将其与盗用混为一谈。Anthropic 未在信上签名，其 CEO Dario Amodei 呼吁打击“工业规模的蒸馏操作”，但同时坚称公司从未主张全面禁止开放权重。《Pacing the Frontier》的签署者包括 OpenAI、Anthropic 和 SSI 的研究人员，他们担心自动化 AI 研究会加速 AI 进展。

rss · Simon Willison · 8月2日 04:16

**背景**: 开放权重模型会公开训练后的参数，使任何人都能在自己的硬件上运行或微调；但与开源模型不同，它们可能不包含训练数据或完整代码。美国政府此前曾因安全顾虑暂停对某款 Claude 模型的访问，引发业界对可能出台限制措施的担忧。这些公开信是“开放权重与封闭模型哪个更安全、更符合美国利益”这一长期争论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.busch-labs.at/resources/glossary/open-weight-model">Open - weight Model - Definition | UX Research Glossary</a></li>
<li><a href="https://www.fierce-network.com/content/open-weight-ai-vs-open-source-ai-whats-difference">Open-weight AI vs. open-source AI: What’s the difference?</a></li>
<li><a href="https://telnyx.com/resources/open-weight-models">Open Weight Models What They Are and How to Use Them</a></li>

</ul>
</details>

**社区讨论**: 没有提供关于此新闻的社区评论。

**标签**: `#AI`, `#Open Source`, `#Policy`, `#Industry`, `#News`

---