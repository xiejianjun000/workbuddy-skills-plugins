# WorkBuddy Skills & Plugins (WorkBuddy 内置技能插件)

> WorkBuddy 19 个内置技能插件完整代码包 —— 含 SKILL.md、references、scripts 等全部文件（共 1399 个文件）

## 项目简介

本项目从 WorkBuddy（腾讯云 CodeBuddy）平台提取了 **19 个内置技能插件** 的完整代码，每个插件包含：

- **SKILL.md** — 技能定义文件（含 frontmatter 元数据和指令）
- **references/** — 参考文档和模板
- **scripts/** — 自动化脚本（如有）
- **其他资源** — 模板、配置、示例等

## 插件列表 (19 Plugins)

### 📊 数据分析 (Data & Analysis)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 1 | `data-analysis` | 析数数 | 58 | 数据分析专家技能 |
| 2 | `data` | 探数数 | 16 | 数据探索技能 |
| 3 | `finance-data` | 财数数 | 6 | 金融数据查询技能 |

### 💰 金融财务 (Finance & Financial)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 4 | `finance` | 记账账 | 13 | 记账/会计技能 |
| 5 | `financial-analysis` | 建模模 | 28 | 财务建模分析技能 |
| 6 | `equity-research` | 研股股 | 22 | 股票研究技能 |
| 7 | `investment-banking` | 投行行 | 16 | 投行业务技能 |
| 8 | `private-equity` | 募资资 | 11 | 私募股权技能 |
| 9 | `wealth-management` | 理财财 | 8 | 财富管理技能 |

### 🎨 产品设计 (Product & Design)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 10 | `product-management` | 产品通 | 13 | 产品管理技能 |
| 11 | `design-to-code` | 图变码 | 15 | 设计稿转代码技能 |

### 📢 营销增长 (Marketing)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 12 | `executing-marketing-campaigns` | 策动动 | 15 | 营销战役执行技能 |

### 📄 文档演示 (Document & Presentation)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 13 | `document-skills` | 理文文 | 253 | 文档处理技能（最大） |
| 14 | `ppt-implement` | 幻灯灯 | 718 | PPT 制作技能（文件最多） |

### 🌐 Web 开发 (Web Development)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 15 | `modern-webapp` | 速构构 | 118 | 现代 Web 应用开发技能 |
| 16 | `webapp-testing` | 端测测 | 3 | Web 应用测试技能 |
| 17 | `dockerfile-gen` | 容器器 | 2 | Dockerfile 生成技能 |

### 🎬 视频媒体 (Video & Media)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 18 | `remotion-video-generator` | 动画画 | 77 | Remotion 视频生成技能 |

### 💬 内部沟通 (Communication)

| # | 插件名 | 中文名 | 文件数 | 说明 |
|---|--------|--------|--------|------|
| 19 | `internal-comms` | 传令令 | 7 | 内部沟通协作技能 |

## 项目结构

```
workbuddy-skills-plugins/
├── README.md                              # 本文件
├── executing-marketing-campaigns/          # 营销战役执行 (15 files)
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
├── product-management/                     # 产品管理 (13 files)
├── design-to-code/                         # 设计转代码 (15 files)
├── data-analysis/                          # 数据分析 (58 files)
├── data/                                   # 数据探索 (16 files)
├── finance/                                # 财务记账 (13 files)
├── financial-analysis/                     # 财务建模 (28 files)
├── equity-research/                        # 股票研究 (22 files)
├── investment-banking/                     # 投行业务 (16 files)
├── private-equity/                         # 私募股权 (11 files)
├── wealth-management/                      # 财富管理 (8 files)
├── document-skills/                        # 文档处理 (253 files) ⭐
├── ppt-implement/                          # PPT制作 (718 files) ⭐⭐
├── modern-webapp/                          # 现代Web应用 (118 files)
├── finance-data/                           # 金融数据 (6 files)
├── dockerfile-gen/                         # Dockerfile生成 (2 files)
├── webapp-testing/                         # Web应用测试 (3 files)
├── internal-comms/                         # 内部沟通 (7 files)
└── remotion-video-generator/               # 视频生成 (77 files)
```

## 数据来源

- **源路径**: `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/`
- **manifest.json**: `~/.workbuddy/app/cache/experts/manifest.json` (WorkBuddy v1.0.0)
- 所有文件均为原始完整副本，未做任何修改

## 总计数据量

- **19 个技能插件**
- **1399 个文件**
- **9 大功能领域**

## 使用说明

### 查看某个插件的技能定义

```bash
# 查看 PPT 制作技能的定义
cat ppt-implement/SKILL.md

# 查看数据分析技能的参考文档
ls data-analysis/references/
```

### 在 WorkBuddy 中使用

这些插件已在 WorkBuddy 专家中心内置。进入 **专家 → 专家** 即可一键召唤对应技能。

## 相关项目

- [workbuddy-expert-teams](https://github.com/xiejianjun000/workbuddy-expert-teams) — 25 个专家团队完整代码包

## License

数据来源: WorkBuddy (CodeBuddy) by Tencent Cloud
Original Author: AI Expert Center (msitarzewski/agency-agents)
