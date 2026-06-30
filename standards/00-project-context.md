# 00 · 项目上下文 〔本项目活记忆 · AI 维护〕

> **作用**:这是项目的"身份档案"。AI 接管项目时先读这里,了解项目目标、技术栈、目录、部署取值。
> **更新时机**:架构、技术栈、目录结构、端口、部署目录、重要约束变化时更新。

---

## 1. 项目是什么

- **项目名称**:`d_ocr` / PDF 图转文字
- **一句话目标**:用户通过前端页面上传一个或多个 PDF,后端使用 PP-StructureV3 进行 OCR 识别,输出 Markdown 格式文字结果。
- **使用者/受益者**:需要从 PDF 文档(含扫描件、图片型 PDF)中提取结构化文字内容的用户。
- **核心功能**:
  - 前端页面支持上传一个或多个 PDF 文件
  - 后端接收 PDF,调用 PP-StructureV3 进行版面分析 + OCR 识别
  - 将识别结果转换为 Markdown 格式输出
  - 用户可在前端查看/下载 Markdown 结果
  - 支持 Docker 一键部署
- **输入/数据**:用户上传的 PDF 文件(可能含扫描图片、文字图片);不上传至第三方服务,本地处理;OCR 模型文件较大,不进 Git,通过 Docker 镜像或启动脚本下载。

## 2. 技术栈

| 层 | 选型 | 理由 |
|---|---|---|
| 语言/运行时 | Python 3.11 | PP-StructureV3(PaddleOCR)生态基于 Python,生态成熟 |
| Web/API 框架 | FastAPI | 异步支持好、自带 OpenAPI 文档、文件上传处理方便 |
| 前端 | 内嵌于 FastAPI(静态 HTML/JS) 或 独立轻量前端(如 Vue/React 单页) | 先以 FastAPI 内置静态文件 + 纯 HTML/JS 实现,降低复杂度 |
| OCR 引擎 | PP-StructureV3(PaddleOCR) | 用户指定,支持版面分析+文字识别+表格识别,输出可转 Markdown |
| 测试 | pytest + pytest-cov | Python 标准测试方案 |
| 格式/静态检查 | ruff(format + check) | 快、All-in-one |
| 打包/运行 | Docker + docker-compose | 用户要求 Docker 部署,统一环境 |
| CI/CD | GitHub Actions | 通用、可视化、适合教学与团队协作 |

## 3. 目录地图

```text
d_ocr/
├── standards/                  # AI 项目记忆与通用规范
│   ├── README.md
│   ├── 00-project-context.md
│   ├── 01-requirements.md
│   ├── PROGRESS.md
│   ├── 02-coding-standards.md
│   ├── 03-testing-standards.md
│   ├── 04-git-workflow.md
│   ├── 05-cicd-standards.md
│   ├── 06-ai-collab-protocol.md
│   └── templates/
├── backend/                    # FastAPI 后端源码
│   ├── main.py                 # 应用入口
│   ├── api/                    # 路由/接口
│   ├── ocr/                    # OCR 核心逻辑(PP-StructureV3 封装)
│   ├── models/                 # 数据模型(Pydantic)
│   └── utils/                  # 工具函数(文件处理等)
├── frontend/                   # 前端静态资源(如独立)
│   └── static/                 # HTML/CSS/JS
├── tests/                      # 测试
│   ├── test_api/               # API 测试
│   └── test_ocr/               # OCR 逻辑测试
├── requirements.txt            # 生产运行依赖
├── requirements-dev.txt        # 本地/CI 检查依赖
├── Dockerfile                  # Docker 镜像构建
├── docker-compose.yml          # 可选,编排多服务
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
└── README.md
```

> 新增目录前先更新本节,避免项目越做越散。

## 4. 质量门槛

| 类型 | 本项目标准 |
|---|---|
| 格式检查 | `ruff format --check .` |
| 静态检查 | `ruff check .` |
| 单元测试 | `pytest` |
| 覆盖率 | `>=80%`(核心逻辑) |
| 构建 | `docker build` 成功 |
| 业务/模型指标 | OCR 识别准确率(选取标准样本集人工评估);接口成功率 >= 99% |
| 接口健康检查 | `/health` 返回 200 |

## 5. 不变约束

- 密钥、密码、私钥、Token **绝不写进代码或文档**,只进 GitHub Secrets / 环境变量。
- 大文件、数据集、模型产物不进 Git(PaddleOCR 模型通过 pip 安装后在运行时自动下载,或 Docker build 时预下载)。
- `main` 分支受保护,日常开发必须走 feature 分支 + PR。
- CI 红灯不合并。
- PDF 文件仅本地处理,不上传至第三方 OCR 服务。

## 6. 部署/CI 占位符取值

> `guides/` 和 workflow 里的通用占位符,在本项目里的真实值只写这里。

| 占位符 | 本项目取值 | 说明 |
|---|---|---|
| `<APP>` | `d_ocr` | 应用名/镜像名/容器名 |
| `<DEPLOY_DIR>` | `/opt/d_ocr` | 服务器部署目录 |
| `<PORT>` | `8000` | 服务主机端口(容器内固定 8000) |
| `<PORT_MAX>` | `8010` | 主机端口回退上限 |
| `<PYVER>` | `3.11` | Python 版本 |
| `<HEALTHCHECK>` | `/health` | 健康检查地址 |
| `<SSH_USER>` | `root` 或 `deploy` | 部署用户(待定) |
| `<SSH_HOST>` | `<服务器公网 IP 或域名>` | 部署目标 |
