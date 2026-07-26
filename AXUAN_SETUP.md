# 阿轩的 Horizon 配置说明

这个 fork 已经按“成长号内容选题雷达”完成基础配置：

- 每天北京时间 07:00 由 GitHub Actions 自动运行。
- 只生成中文日报。
- 信息分为“成长与认知、内容与增长、AI 与工具”三组。
- 每日最多保留 20 条，AI 评分低于 6.5 的内容会被过滤。
- 默认采集公开 RSS、Hacker News、Reddit、GitHub 和 OSS Insight。
- 日报发布到 GitHub Pages。

## 必需密钥

只需先配置一个：

| GitHub Secret | 用途 | 是否必需 |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | 新闻评分、过滤、补充背景和生成中文日报 | 必需 |

请不要把密钥写进 `.env` 后提交，也不要发到 Issue、README 或公开聊天记录。

### 配置方法 A：GitHub 网页

1. 打开仓库的 **Settings → Secrets and variables → Actions**。
2. 点击 **New repository secret**。
3. Name 填 `DEEPSEEK_API_KEY`。
4. Secret 填 DeepSeek 控制台生成的 API Key。

### 配置方法 B：GitHub CLI

在本机终端运行：

```powershell
gh secret set DEEPSEEK_API_KEY -R Shanexxzz/Horizon
```

命令会提示你粘贴密钥，输入内容不会写进仓库。

## 可选配置

| GitHub Secret | 何时需要 |
| --- | --- |
| `APIFY_TOKEN` | 要开启 Twitter/X 账号采集时 |
| `HORIZON_WEBHOOK_URL` | 要把日报推送到飞书、钉钉、Slack 或 Discord 时 |

GitHub Actions 自带 `GITHUB_TOKEN`，线上运行无需另外提供个人 GitHub Token。

## 第一次运行

配置 `DEEPSEEK_API_KEY` 后：

1. 打开仓库 **Actions**。
2. 进入 **Daily Horizon Summary**。
3. 点击 **Run workflow**。
4. 等待任务完成后，检查 GitHub Pages 日报。

如果要调整信息源，编辑 `data/config.github.json`；不要把密钥写进这个文件。
