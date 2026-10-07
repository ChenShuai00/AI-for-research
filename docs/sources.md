# 来源记录与版本快照

核验日期：**2026-10-07（北京时间）**。

[← 返回首页](../README.md) · [完整技能表](skills.md) · [检索方法](methodology.md)

## 当前收录来源

| 仓库 | Star / Fork | 许可口径 | 宿主与依赖 | 维护状态 |
| --- | --- | --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 180,017 / 21,294 | 混合许可；本次 4 项为专有许可 | Claude 官方；其他宿主需适配 | 近 90 天有推送 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47,872 / 4,322 | MIT | 兼容 Agent Skills 的宿主 | 近 90 天有推送 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 13,327 / 941 | MIT | Claude Code / Codex 等，按上游安装器 | 超过 90 天未推送 |
| [huggingface/skills](https://github.com/huggingface/skills) | 11,145 / 762 | Apache-2.0；检查单项条款 | 多种 Agent Skills 宿主；部分依赖 HF 账户 | 近 90 天有推送 |
| [openai/plugins](https://github.com/openai/plugins) | 7,335 / 952 | 检查各插件条款；API 未提供总许可 | Codex；部分技能需要插件与连接器 | 近 90 天有推送 |
| [VincenzoImp/academic-research-skills](https://github.com/VincenzoImp/academic-research-skills) | 3 / 0 | MIT | Agent Skills；需适配项目目录与 MCP | 近 90 天有推送 |
| [jjfroehlich/agent-skills-for-academic-research](https://github.com/jjfroehlich/agent-skills-for-academic-research) | 1 / 1 | MIT | Agent Skills；效果仍待评估 | 近 90 天有推送 |

## 固定版本

| 仓库 | 提交版本 | 最近推送 UTC | 核验时间 UTC | 来源 |
| --- | --- | --- | --- | --- |
| AN | [`683bc88e56f3`](https://github.com/anthropics/skills/commit/683bc88e56f3e09ba94f7055977f3d3aa499f202) | 2026-10-05T13:46:45Z | 2026-10-07T15:13:15.974Z | [GitHub API](https://api.github.com/repos/anthropics/skills) |
| KD | [`92ace75ac21e`](https://github.com/K-Dense-AI/scientific-agent-skills/commit/92ace75ac21efe19a620434e0ca4e356081fe807) | 2026-10-05T09:39:11Z | 2026-10-07T15:10:53.7695347Z | [GitHub API](https://api.github.com/repos/K-Dense-AI/scientific-agent-skills) |
| OR | [`773a52944ba4`](https://github.com/Orchestra-Research/AI-Research-SKILLs/commit/773a52944ba4747a18bd4ae9ade53fff041adcbc) | 2026-06-16T01:36:46Z | 2026-10-07T15:13:49Z | [GitHub API](https://api.github.com/repos/Orchestra-Research/AI-Research-SKILLs) |
| HF | [`ca0325bb20b2`](https://github.com/huggingface/skills/commit/ca0325bb20b2d0a1b2efa893670c4c72f79e707b) | 2026-10-01T12:33:22Z | 2026-10-07T15:13:56.922Z | [GitHub API](https://api.github.com/repos/huggingface/skills) |
| OA | [`5fd93af4cd0c`](https://github.com/openai/plugins/commit/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f) | 2026-09-28T17:08:10Z | 2026-10-07T15:13:15.972Z | [GitHub API](https://api.github.com/repos/openai/plugins) |
| VA | [`28a4f18e43ae`](https://github.com/VincenzoImp/academic-research-skills/commit/28a4f18e43ae5c086357c4a1e1412b0a96c74703) | 2026-08-25T11:40:01Z | 2026-10-07T15:13:56.922Z | [GitHub API](https://api.github.com/repos/VincenzoImp/academic-research-skills) |
| JA | [`9b1b256e9905`](https://github.com/jjfroehlich/agent-skills-for-academic-research/commit/9b1b256e99055006725fe4c6b8f90d301ceef7b0) | 2026-08-28T21:22:58Z | 2026-10-07T15:13:56.922Z | [GitHub API](https://api.github.com/repos/jjfroehlich/agent-skills-for-academic-research) |

## 本次发现的版本差异

- **K-Dense 更名**：当前规范仓库为 `K-Dense-AI/scientific-agent-skills`，技能位于 `skills/<name>/SKILL.md`。本次完整目录实测 177 个；旧搜索缓存中的 165/166 数字不用于当前清单。[官方 README](https://github.com/K-Dense-AI/scientific-agent-skills)
- **Orchestra 计数差异**：固定提交 README 第 20 行称 98，第 381 行仍称 87；完整目录实测 98，未截断。本清单采用目录证据。[固定版本 README](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/README.md#L381)
- **Orchestra 维护状态**：最近推送为 2026-06-16，距本次核验已超过 90 天，表中明确标出。累计关注度较高并不能证明近期维护活跃。[官方仓库](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- **OpenAI 来源迁移**：`openai/skills` README 已声明 deprecated，转向 `openai/plugins`；旧库当前 27,919 Star 只记入排除记录。[弃用说明](https://github.com/openai/skills)
- **文档技能许可**：K-Dense 2.72.0 移除了 vendored `docx/pdf/pptx/xlsx`，这四项本清单直接链接 Anthropic 来源，其 frontmatter 声明 Proprietary。[K-Dense 发布说明](https://github.com/K-Dense-AI/scientific-agent-skills#whats-new-in-2720)

## 快照文件

[sources.json](../data/sources.json) 保存 Star、Fork、最近推送、版本与排除记录。[verification.json](../data/verification.json) 保存所有精选技能的固定版本访问核验。

目录计数包含递归发现的全部 `SKILL.md`，例如 OpenAI 插件可能包含内嵌技能，HF 也有辅助子技能；本清单的 88 行是人工精选，不等同于各库目录数之和。
