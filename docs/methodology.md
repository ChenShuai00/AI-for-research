# 检索、热门口径与核验方法

[← 返回首页](../README.md) · [完整技能表](skills.md) · [来源记录](sources.md)

## 本次检索范围

检索日期为 **2026-10-07（北京时间）**。对象为公开的科研 **Agent Skills**：具有可访问的 `SKILL.md` 入口、可以由 AI Agent 加载的任务说明与资源。优先收录文献检索、研究设计、科研写作、统计、绘图、实验工程和成果整理；工具库、普通提示词、MCP 服务只有在配套真实 skill 时进入清单。

检索使用公开 Web 发现候选，再回到作者的 GitHub 仓库与具体技能文件核验。主要发现查询为：

| 查询 | 用途 |
| --- | --- |
| `GitHub scientific skills Claude Code K-Dense scientific skills` | 跨学科科研技能库 |
| `GitHub research skills academic paper writing agent skills 2026` | 写作与学术工作流 |
| `GitHub AI research skills Orchestra scientific skills` | AI 实验与研究工程 |

此外检查 Anthropic、Hugging Face 与 OpenAI 官方仓库。最终精选 **88 项 / 7 个来源仓库**；其中高关注来源 80 项，新兴学术工作流 8 项。当前清单提供多领域常用入口，未穷尽所有公开科研 skills。

## “热门”如何判断

| 指标 | 本清单采用的口径 | 解释限制 |
| --- | --- | --- |
| 社区关注 | 来源仓库累计 `stargazers_count >= 1,000` 为“高关注来源” | 不代表单项 skill 的使用量或效果 |
| 维护活动 | 核验日与 GitHub `pushed_at` 相差不超过 90 天，标为“近 90 天有推送” | 推送可能来自其他分支，不代表每项技能近期更新 |
| 新兴来源 | 当前不足 1,000 Star、但具备完整科研工作流的候选 | 单独放入新兴区，不计入热门来源 80 项 |
| 官方来源 | 作者组织为 Anthropic / Hugging Face / OpenAI | “官方”描述来源，不能代替质量评测 |
| 收录适配 | 有真实入口，用途与科研任务直接相关，依赖可识别 | 是人工精选判断，没有量化性能分数 |

仓库表按累计 Star 降序排列；技能表按科研流程分类。**本次没有采集最近 7/30 天的 Star 增量，也没有单项 skill 的安装量，因此不构成实时趋势榜或全球排名。** 高关注但较久未更新的项目仍可收录，并明确展示维护状态。

## 证据来源与流程

1. 使用 GitHub 仓库 REST 元数据读取 Star、Fork、`pushed_at`、默认分支和许可标记。
2. 使用提交 API 或 `git ls-remote ... refs/heads/main` 获取实际 commit SHA。目录 tree SHA 与提交 SHA 分开记录。
3. 在需要目录计数时读取完整递归 tree，检查 `truncated=false`。计数包含辅助子技能，不能直接当成独立顶层技能数量。
4. 阅读具体 `SKILL.md`，用中文重新概括用途与主要依赖；技能名采用 YAML frontmatter 的 `name`。
5. 统一读取固定 commit 的 raw 文件，核对 frontmatter 名称、HTTP 200 与原始字节 SHA256。本次 **88/88 通过**，结果保存在 [verification.json](../data/verification.json)。
6. 将审核后的条目写入 [skills.json](../data/skills.json)，通过生成脚本输出 Markdown 表格，检查重复条目、数量、固定链接、表格列数与本地链接。

可复核的来源数据在 [sources.json](../data/sources.json) 和各来源 snapshot 文件中。搜索摘要与博客用于发现候选；技能名称、功能与版本以作者仓库为依据。发生数量冲突时，优先使用实际目录与固定提交证据，并在 [来源记录](sources.md) 说明。

## 核验完成到哪一步

本次完成的是**来源和元数据核验**：仓库存在，所选文件可读取，名称与摘要对应，固定版本和哈希已记录。没有安装技能、运行训练或科研分析，也没有对论文质量或任务效果进行基准评测。

技能间的同名项可能来自不同作者，分别保留为 `repository + path` 唯一条目。依赖栏是阅读上游后的摘要；完整版本约束、API 访问权限与使用条件请查看对应 `SKILL.md`。引用库中的条目仍需回到真实论文或数据库核对。

## 后续维护

先运行 `python scripts/refresh_sources.py` 获取独立的新快照，再人工比较更名、移动、许可和维护状态变化。确认变更后更新精选数据与来源版本，重新生成 Markdown，并对固定链接进行核验。公共 API 达到配额时，保存失败信息并保留已有成功快照；可配置 `GITHUB_TOKEN` 或稍后重试。

日期为本次快照日期，不设置定时更新任务。重复核验不会自动证明 skill 执行正确。
