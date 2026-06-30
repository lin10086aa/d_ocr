# PROGRESS · d_ocr / PDF 图转文字 〔本项目活记忆 · 状态机〕

> **作用**:这是项目的"存档点"。任意 AI、任意重启会话,读它即可知道当前做到哪、下一步做什么、踩过什么坑。
> **更新时机**:每完成一个有意义步骤、每次会话结束前。
> **格式要求**:时间倒序,最新在上;短、准、可接力。

---

## 当前状态 (最后更新: 2026-06-30 · by AI)

- **阶段**:`初始化` — 对应 06 六步流程第 ① 步:建仓 + 配 Secrets
- **上一步完成**:已填写 `00-project-context.md` 和 `01-requirements.md`,初始化本 PROGRESS.md。
- **下一步 (TODO 第一条)**:
  1. **人类确认**:审阅 `00`/`01`/`PROGRESS` 三个文件,确认需求无误后进入第 ① 步。
  2. 第 ① 步:创建 GitHub 仓库 → 配置 Secrets → 推送初始工程骨架。
- **阻塞项**:等待人类确认三个 standards 文件。

---

## 待办清单 (TODO,按优先级)

### 阶段 0: 项目初始化(当前)

- [ ] **人类确认 standards 目录内容** ← 当前卡点
- [ ] 第①步:创建 GitHub 仓库(`d_ocr`),推送最小引导提交(.gitignore/README)
- [ ] 第①步:提示人类配置 GitHub Secrets(`SSH_PRIVATE_KEY`/`SSH_HOST`/`SSH_USER`)

### 阶段 1: 工程骨架 + CI/CD(US-1)

- [ ] 第②步:从 `main` 开 feature 分支 `feature/1-project-init`
- [ ] 搭建 Python 项目骨架:`backend/`、`tests/`、`requirements.txt`、`requirements-dev.txt`
- [ ] 配置 ruff(pyproject.toml)
- [ ] 编写 FastAPI 最小应用(`/health` 端点)
- [ ] 编写 Dockerfile + docker-compose.yml
- [ ] 编写 CI workflow(`.github/workflows/ci.yml`)
- [ ] 编写 CD workflow(`.github/workflows/cd.yml`)
- [ ] 编写健康检查测试
- [ ] 第④步:本地 CI 自检(ruff + pytest + 覆盖率)
- [ ] 第⑤步:推送分支、创建 PR、等 CI 全绿
- [ ] 第⑥步:人工合并后验证 CD 部署 + `/health`

### 阶段 2: OCR 核心能力(US-3)

- [ ] 第②步:从 `main` 开 feature 分支 `feature/3-ocr-engine`
- [ ] 封装 PP-StructureV3 调用:PDF → 图片 → OCR → 结构化结果
- [ ] 实现 Markdown 合成:段落/标题/表格/列表
- [ ] 编写 OCR 核心逻辑单元测试
- [ ] 第④步:本地 CI 自检
- [ ] 第⑤步:推送分支、创建 PR、等 CI 全绿

### 阶段 3: 文件上传 API(US-2)

- [ ] 第②步:从 `main` 开 feature 分支 `feature/2-file-upload`
- [ ] 实现上传 API:multipart/form-data 接收、文件校验、临时存储
- [ ] 实现文件类型和大小校验
- [ ] 编写上传 API 测试
- [ ] 第④~⑤步:CI 自检 + PR

### 阶段 4: 前端页面(US-2 + US-4 + US-6)

- [ ] 第②步:从 `main` 开 feature 分支 `feature/4-frontend`
- [ ] 实现上传页面:拖拽/点击上传、文件类型校验、进度提示
- [ ] 实现结果页:Markdown 预览 + 下载按钮
- [ ] 实现状态轮询:排队中/处理中/已完成/失败
- [ ] 编写前端集成测试
- [ ] 第④~⑤步:CI 自检 + PR

### 阶段 5: Docker 部署完善(US-5)

- [ ] 第②步:从 `main` 开 feature 分支 `feature/5-docker-finalize`
- [ ] Dockerfile 多阶段构建优化
- [ ] OCR 模型预下载集成到 Docker build
- [ ] 端到端验证:docker run → 上传 PDF → OCR → 下载 Markdown
- [ ] 第④~⑤步:CI 自检 + PR

---

## 关键决策记录 (ADR)

| 日期 | 决策 | 理由 |
|---|---|---|
| 2026-06-30 | OCR 引擎选用 PP-StructureV3(PaddleOCR) | 用户明确要求;支持版面分析+文字识别+表格识别;开源、可本地部署 |
| 2026-06-30 | 后端框架选用 FastAPI | 异步支持好、自带文件上传处理、OpenAPI 文档、Python 生态匹配 |
| 2026-06-30 | 前端初期用 FastAPI 内置静态文件 + 纯 HTML/JS | 降低初始复杂度;不引入独立前端构建工具链;后续可升级为独立前端 |
| 2026-06-30 | 部署方式为 Docker | 用户明确要求;统一环境、避免 OCR 依赖(PaddlePaddle)手动安装痛苦 |
| 2026-06-30 | 数据库暂不引入 | 初期无用户系统/持久化需求;文件上传临时存储、处理完即清理;后续按需引入 |

---

## 已知坑 (GOTCHAS)

- *暂无*(项目刚启动,待开发中积累)

---

## 里程碑 (DONE)

- [ ] *暂无*(项目刚启动)
