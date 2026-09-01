---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 28 条内容中筛选出 4 条重要资讯。

---

1. [谷歌从 Chrome 网上应用商店移除 Manifest V2 扩展，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [ChatGPT Work 技能参考：Playwright 浏览器自动化成亮点](#item-2) ⭐️ 7.0/10
3. [写作或是最安全的 AI 时代工作，读者反驳](#item-3) ⭐️ 7.0/10
4. [用低价值的晚间时间换取高价值的清晨时光](#item-4) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌从 Chrome 网上应用商店移除 Manifest V2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已开始从 Chrome 网上应用商店移除 Manifest V2 扩展，包括广受欢迎的广告拦截器 uBlock Origin。根据官方的 MV2 弃用时间表，升级到 Chrome 139 或更高版本的用户将无法再使用 MV2 扩展，从 2025 年 3 月 31 日起 MV2 已默认被禁用。 这一变化影响到数百万依赖 uBlock Origin 等扩展来拦截广告、保护隐私和抵御恶意广告的用户。它还引发了关于单一公司对互联网拥有单边控制的担忧，越来越多的用户转而推荐继续支持 MV2 过滤方式的 Firefox 等浏览器。 Manifest V3 引入了 declarativeNetRequest API，缺少 uBlock Origin 这类高效广告拦截器所依赖的动态 webRequestBlocking 能力。虽然存在功能较弱的替代品 uBlock Origin Lite，一些用户也尝试通过 Firefox、分叉版本或企业策略等方法绕行，但这些方案可能各有局限。

hackernews · twapi · 8月31日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 扩展的旧版框架；Google 设计 Manifest V3 是为了改善安全性、性能和隐私。但 MV3 也限制了扩展拦截网络请求的方式，因此被批评为对广告拦截器的打击。uBlock Origin 是一款免费、开源、跨平台的内容过滤扩展，而 Chrome 是使用最广泛的浏览器，这让 Google 对互联网拥有相当大的影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V 2 support timeline | Chrome for Developers</a></li>
<li><a href="https://factually.co/fact-checks/technology/manifest-v3-ad-blockers-ublock-origin-brave-firefox-2026-4d29ee">How Manifest V 3 Changed Ad Blockers: uBlock Origin, Br...</a></li>
<li><a href="https://ublockorigin.com/">uBlock Origin - Free, open-source ad blocker extension</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对谷歌的决定表示不满，许多人表示他们已经转用 Firefox。部分人认为广告拦截已成为安全问题，尤其是对不熟悉技术的用户而言；另一些人则对谷歌对互联网的控制表达更广泛的担忧，并建议使用分叉版本或其他浏览器。

**标签**: `#Chrome`, `#uBlock Origin`, `#ad blocking`, `#privacy`, `#browser`

---

<a id="item-2"></a>
## [ChatGPT Work 技能参考：Playwright 浏览器自动化成亮点](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 7.0/10

一个新参考网站整理了 ChatGPT Work 的技能与工具，其中一项基于 Playwright 的浏览器控制技能尤为突出，它让 ChatGPT 通过 Node.js REPL 操控浏览器，并会引导 AI 运行 \`nodeRepl.write\(await browser.documentation\(\)\)\` 获取详细使用说明。 它为开发者和高级用户提供了一份实用、立即可落地的 AI 网页自动化手册，减少使用 ChatGPT Work 时的试错成本。同时也表明 Playwright 这类浏览器自动化框架正成为智能体工作流的核心基础设施。 该控制浏览器技能通过 Node.js REPL 启动 Playwright 实例，并调用 \`browser.documentation\(\)\` 获取完整的浏览器用法说明。社区成员指出某些工具会拖慢任务并消耗大量 token，也有人质疑它与 OpenAI Codex 的差异。

hackernews · ijidak · 8月31日 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: Playwright 是微软开发的跨浏览器自动化库，支持 Chromium、Firefox 和 WebKit，常用于测试、脚本编写和 AI 智能体工作流。ChatGPT Work 技能是可复用、可分享的工作流，包含指令和代码，帮助 ChatGPT 更稳定地完成任务。这个参考站点就像是这类技能的实用目录，其中浏览器控制技能是把大语言模型与确定性自动化工具结合的典型示例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://playwright.dev/">Web automation and testing for apps, scripts, and AI agents | Playwright</a></li>
<li><a href="https://help.openai.com/en/articles/20001066-skills-in-chatgpt">Skills in ChatGPT | OpenAI Help Center</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 认为控制浏览器技能最有趣，并特别提到其自文档化的 \`browser.documentation\(\)\` 机制。其他人则提出实际应用中的注意事项，如 token 浪费和速度变慢，也有人询问它与 Codex 的区别，并建议改进长技能列表的界面显示。

**标签**: `#AI tools`, `#ChatGPT`, `#browser automation`, `#productivity`, `#workflows`

---

<a id="item-3"></a>
## [写作或是最安全的 AI 时代工作，读者反驳](http://muratbuffalo.blogspot.com/2026/08/the-safest-job-from-ai-may-be-writing.html) ⭐️ 7.0/10

一篇题为《最安全的工作也许就是写作》的博客文章认为，由于大语言模型缺乏意图，无法做出刻意的用词选择，人类作家仍将是安全的。评论区读者反驳说，即使最优秀的人类写作仍然更胜一筹，AI 仍在消灭入门级和日常写作岗位。 这场争论之所以重要，是因为它揭示了有意图的人类写作在质量上的优势，与大多数写作工作的市场经济学之间的差距。自由撰稿人、记者和内容从业者面临的未来是：AI 不会取代最优秀的作家，但会移除让新作家走向那个水平的职业阶梯。 文章的核心论点是，LLM 生成文本时缺乏意图：它们不会因为要刻意传达某种含义而选择每个词，而人类写作者会这样做。评论者指出，AI 已经在吸收新闻、翻译、技术写作和文案编辑等与文字相关的日常任务，而这些正是过去支撑有志写作者的入门级工作。

hackernews · ilreb · 8月31日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=49512856)

**背景**: 大语言模型（LLM）是基于深度神经网络构建的 AI 系统，通过从海量训练数据中预测下一个词来处理和生成类似人类的文本。它们没有目标或意识层面的意图，只是模拟推理，而非刻意试图传达特定含义。这篇博客文章正是将这种缺少意图的特点，作为人类写作难以被自动化的理由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/">Large Language Model (LLM) - GeeksforGeeks</a></li>
<li><a href="https://www.mesour.com/blog/en/does-ai-have-intentions/">Does AI Have Intentions ? | Matouš Němec</a></li>

</ul>
</details>

**社区讨论**: 评论区基本都在反驳这篇文章。&\#x27;matherial&\#x27; 认为问题在于经济层面：LLM 夺走了人们在成为知名作家之前赖以谋生的日常写作工作。&\#x27;muvlon&\#x27; 指出许多作家已经失业，而且机构不愿为文字质量的差异付费；&\#x27;dzonga&\#x27; 则认为作者把这个观点表达错了，但同意确实存在对能捕捉微妙之处的人类文章的需求。

**标签**: `#AI`, `#Writing`, `#Career`, `#Future of Work`, `#LLM`

---

<a id="item-4"></a>
## [用低价值的晚间时间换取高价值的清晨时光](https://twitter.com/JamesClear/status/tweet-2094417778014876127) ⭐️ 6.0/10

詹姆斯·克利尔在推文中请读者思考一天中哪些小时最有价值、哪些最没价值，并建议把夜晚的最后一小时换成清晨的第一小时，认为这对他是一笔非常划算的交易。 这个简单的自我反思问题能帮助人们识别浪费时间的习惯，并可能改善日常作息。它与关注生产力和习惯养成的广泛受众产生共鸣，强化了“时间安排上的小改变能带来显著回报”这一观念。 詹姆斯·克利尔提到他通常不在早上 5 点到 6 点间醒来，但醒来时很享受；而他晚上 10 点到 11 点常常被浪费掉。他把这称为一笔“高价值的交易”，并请其他人找出自己每天最高效和最低效的时段。

twitter · James Clear · 8月31日 13:31

**背景**: 詹姆斯·克利尔是一位著名的习惯与生产力作家，其代表作是《掌控习惯》（Atomic Habits）。他的推文常提供实用、可操作的自律建议，而这个问题鼓励读者用投入产出比的眼光审视自己的日常作息。

**标签**: `#productivity`, `#time management`, `#habits`, `#morning routine`, `#self-reflection`

---