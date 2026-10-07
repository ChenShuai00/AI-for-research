# 贡献指南

欢迎推荐科研 Agent Skills、纠正名称或修复链接。请提供作者仓库与具体 `SKILL.md`，并说明它能解决哪个科研任务。

## 新条目的最低信息

| 字段 | 要求 |
| --- | --- |
| 技能名称 | 与上游 YAML frontmatter `name` 一致 |
| 来源 | 规范的 `owner/repo` 与真实 `SKILL.md` 路径 |
| 中文用途 | 用自己的话概括，不复制大段上游内容 |
| 分类 | 文献、选题、写作、数据、绘图、训练、评估、计算、学科或文档 |
| 依赖 | Python/工具、API、账户、GPU 或宿主条件 |
| 版本 | 本次核验的 commit SHA 与日期 |
| 关注度 | 仓库 Star 与查询日期；不足 1,000 Star 放入新兴区 |
| 许可 | 仓库或单项许可链接；没有明确许可时如实标注 |

普通工具库、未附 skill 的 MCP 服务和仅有营销页面的条目暂不收录。已有技能效果测评可以作为补充证据，需提供任务、模型、输入和基线。

## 更新流程

1. 修改相应的 `data/*_candidates.json` 与来源 snapshot，必要时更新人工分类。
2. 运行 `python scripts/assemble_catalog.py` 整合输入；`data/skills.json` 与 `data/sources.json` 为发布快照。
3. 运行 `python scripts/verify_catalog.py --online` 核验固定版本链接、名称与哈希。
4. 运行 `python scripts/build_catalog.py` 生成首页、完整技能表与来源记录，再运行 `python scripts/verify_catalog.py` 检查发布文件。
5. 更新 `CHANGELOG.md`；数量或筛选规则变化时同步修改 `docs/methodology.md`。

`refresh_sources.py` 只产生供比较的新快照，不自动改写人工精选列表。链接失效时，保留变更原因；更名或同名技能通过来源仓库区分。

表格由脚本生成，建议从数据输入更新。不得把来源读取成功写成技能执行成功，也不得用仓库 Star 代替单项技能的效果证据。
