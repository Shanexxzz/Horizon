---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 13 条内容中筛选出 1 条重要资讯。

---

1. [Strata 在单张 RTX 4090 上运行 125B Qwen 3.8 Flash Next](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata 在单张 RTX 4090 上运行 125B Qwen 3.8 Flash Next](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata 的 GitHub 项目声称能在单张消费级 RTX 4090 上运行 125B 参数的 Qwen3.8-Flash-Next 多模态 MoE 模型，并有用户报告自己在本地实测到约 124 tokens/秒。该消息在 Hacker News 上引发 607 分、282 条评论的热议，其中包括一项独立的 50 张图片视觉基准测试：Strata 的中位定位误差约 155 像素，而在 llama.cpp 上运行完全相同的 GGUF 权重仅约 46 像素。 如果这一说法站得住脚，125B 级别的模型就能在约 1600 美元的消费级显卡上本地运行，而不必依赖约 1 美元/小时租用的数据中心 GPU，这将显著降低个人开发者进行私密、离线推理的门槛。但低于 4-bit 的量化是否会造成明显精度损失仍存争议，因此&quot;能跑起来&quot;未必等于&quot;真正好用&quot;，实际价值取决于速度优势能否经得起检验。 Strata 是专门针对 Qwen3.8-Flash-Next 的运行时，而非通用推理引擎；该模型本身是 Qwen4 架构的稀疏 MoE 多模态推理预览版，原生上下文长度达 262,144 token。124 tok/s 的实测环境为 RTX 4090 搭配 128GB DDR5 和 Ryzen 7950X3D，而社区基准显示，在使用相同权重的情况下，其视觉任务表现相较 llama.cpp 出现可测量的下降。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: MoE（混合专家）模型每个 token 只激活一部分参数，因此 125B 规模的模型理论上所需的显存和算力远低于其参数总量所暗示的水平。量化则通过用更少的比特（常见为 4-bit）存储权重进一步压缩占用，让大模型塞进有限的显存，代价是输出质量下降；GGUF 是 llama.cpp 生态中本地推理最主流的量化格式。Strata 属于针对特定模型家族优化的替代运行时，而非通用推理引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://www.local-llm.net/learn/quantization-explained/">Understanding LLM Quantization : GGUF, GPTQ, AWQ... | local- llm .net</a></li>

</ul>
</details>

**社区讨论**: 讨论整体呈现&quot;既兴奋又怀疑&quot;的氛围：snehesht 证实自己在 4090 上确实跑到了 124 tok/s；a11r 对低于 4-bit 的量化持保留态度，并分享自己在约 1 美元/小时租用的 RTX Pro 6000 上用 4-bit 处理高难度但边界清晰的编码任务的经验。Jackson\_\_ 提供了最有力的反证：在 50 张图片的基准中，相同权重下 Strata 的中位定位误差（154.8 像素）是 llama.cpp（46.5 像素）的三倍多；AntiRush 则称赞 ds4 的 Q4 量化在 RTX 6000 Pro 上解码可达 255 tok/s 并支持 4 路并发；jacquesm 提醒说铺天盖地的 Strata 链接可能炒作多于实质。

**标签**: `#local-llm-inference`, `#quantization`, `#consumer-gpu`, `#ai-tools`, `#hn-discussion`

---