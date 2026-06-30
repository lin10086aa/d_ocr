# 01 · 需求 / 活 PRD 〔本项目活记忆 · AI 维护〕

> **作用**:这是本项目唯一的需求文档。所有新功能、缺陷、技术债都追加到这里,不要另起多个 PRD 文件。
> **更新时机**:每次有新需求、需求变更、验收标准变化时更新。

---

## 1. 需求来源

| 类型 | 来源 | 进入方式 |
|---|---|---|
| 功能需求 Feature | 用户 | 写成用户故事 |
| 缺陷 Bug | 测试 / 线上日志 / 用户反馈 | 写复现步骤和期望结果 |
| 技术债 Tech Debt | 开发 / Review / CI/CD 故障 | 写影响和修复目标 |

---

## 2. Issue 生命周期

| 阶段 | 状态 | 动作 |
|---|---|---|
| 提出 | Open | 写清场景、目标、验收标准 |
| 排期 | Backlog / Todo | 决定优先级和负责人 |
| 开发 | In Progress | 从 main 开 feature 分支 |
| 评审 | In Review | 提 PR,等待 CI 和 Review |
| 合并 | Done | PR 合并 main,自动关闭 Issue |
| 验收 | Verified | 按验收标准确认 |

**追踪规则**:分支名带 Issue 号,PR 描述写 `closes #<编号>`。

---

## 3. 用户故事模板

```text
### US-<编号> <一句话标题> · 状态: Backlog
作为 <角色>,
我想要 <能力>,
以便 <价值>。

验收标准:
- AC1: Given <前提>,When <动作>,Then <可验证结果>。
- AC2: <补充标准>

技术备注:
- <可选:约束、边界、风险>
```

---

## 4. 需求清单

### US-1 初始化项目工程化与 CI/CD · 状态: Backlog

作为 **项目开发者**,
我想要 项目具备基础工程结构、测试、CI 与 CD,
以便 后续每次开发都能自动检查并自动部署。

验收标准:
- AC1: 从 `main` 开 feature 分支完成初始化,不直接 push main。
- AC2: PR 触发 CI,至少包含格式检查、静态检查、单元测试、构建检查。
- AC3: CI 全绿后合并 main。
- AC4: 合并 main 自动触发 CD,部署后健康检查通过。
- AC5: 完成后更新 `standards/PROGRESS.md`。

---

### US-2 PDF 文件上传 · 状态: Backlog

作为 **普通用户**,
我想要 在浏览器中打开一个页面,选择并上传一个或多个 PDF 文件,
以便 将 PDF 内容提交给 OCR 服务进行处理。

验收标准:
- AC1: Given 用户打开前端页面,When 页面加载完成,Then 显示文件上传区域(支持拖拽或点击选择)。
- AC2: Given 用户选择了 1 个 PDF 文件(<20MB),When 点击上传,Then 文件成功上传至后端,返回上传成功状态。
- AC3: Given 用户选择了 3 个 PDF 文件,When 点击上传,Then 3 个文件全部成功上传,后端逐一接收。
- AC4: Given 用户选择了非 PDF 文件(如 .txt),When 点击上传,Then 前端给出友好错误提示"仅支持 PDF 文件"。
- AC5: Given 用户选择了超过 50MB 的 PDF 文件,When 点击上传,Then 给出文件过大提示。

技术备注:
- 前端:文件类型校验(.pdf)、大小校验(建议单文件 ≤ 50MB)、上传进度提示。
- 后端:接收 multipart/form-data,存储到临时目录,返回文件 ID 列表。

---

### US-3 OCR 识别与 Markdown 输出 · 状态: Backlog

作为 **普通用户**,
我想要 上传 PDF 后,系统自动使用 PP-StructureV3 进行 OCR 识别,并将结果转换为 Markdown 格式,
以便 我能直接获得结构化、可编辑的文字内容。

验收标准:
- AC1: Given 一个文字型 PDF(含文本层),When 系统处理,Then 输出保留段落结构的 Markdown 文本。
- AC2: Given 一个扫描型 PDF(纯图片,无文本层),When 系统处理,Then 输出 OCR 识别后的 Markdown 文本。
- AC3: Given 一个含表格的 PDF,When 系统处理,Then 输出中包含 Markdown 表格格式。
- AC4: Given 一个含图片区域(非文字)的 PDF,When 系统处理,Then 图片区域被标注或跳过,不产生乱码。
- AC5: Given 一个混合排版的 PDF(文字+表格+图片),When 系统处理,Then 输出 Markdown 保留原版面阅读顺序。
- AC6: Given 上传的 PDF 为空(0 页),When 系统处理,Then 返回明确提示"PDF 无有效页面"。

技术备注:
- 使用 PP-StructureV3 的版面分析(layout) + 文字识别(OCR) + 表格识别(table)能力。
- PDF 需先将每页渲染为图片(RGB),再送入 PP-StructureV3。
- 结果合成 Markdown:标题、段落、表格、列表等结构。
- OCR 模型首次运行时自动下载(约需 500MB~1GB),Docker build 时可预下载。

---

### US-4 结果查看与下载 · 状态: Backlog

作为 **普通用户**,
我想要 在 OCR 处理完成后,能在页面上查看 Markdown 结果并下载,
以便 我可以复制使用或离线保存。

验收标准:
- AC1: Given OCR 处理完成,When 用户打开结果页,Then 显示渲染后的 Markdown 预览。
- AC2: Given 结果页显示,When 用户点击"下载"按钮,Then 浏览器下载 `.md` 文件。
- AC3: Given 同时上传了多个 PDF,When 全部处理完成,Then 每个 PDF 对应一个独立的结果页/下载。
- AC4: Given OCR 处理失败(如 PDF 损坏),When 用户查看,Then 显示友好错误信息"处理失败:xxx",不显示空白页。

技术备注:
- Markdown 预览可使用 marked.js 或类似库在前端渲染。
- 下载文件名建议为原 PDF 文件名 + `.md`。

---

### US-5 Docker 部署 · 状态: Backlog

作为 **运维人员**,
我想要 通过 Docker 一键构建和启动整个应用(前端+后端+OCR),
以便 在任何支持 Docker 的服务器上快速部署,无需手动配置 Python 环境和 OCR 依赖。

验收标准:
- AC1: Given 已安装 Docker 的服务器,When 执行 `docker build -t d_ocr . && docker run -p 8000:8000 d_ocr`,Then 服务启动成功。
- AC2: Given 容器启动后,When 访问 `http://localhost:8000`,Then 显示前端上传页面。
- AC3: Given 容器运行中,When 访问 `http://localhost:8000/health`,Then 返回 `{"status":"ok"}`。
- AC4: Given 容器运行中,When 上传 PDF 并触发 OCR,Then 正常完成识别并返回结果。
- AC5: Given Docker 镜像,When 首次启动,Then OCR 模型自动可用(预下载或自动下载),无需人工介入。

技术备注:
- Dockerfile 基于 Python 3.11 slim 镜像。
- OCR 依赖(PaddlePaddle + PP-StructureV3)较大,镜像可能 3~5GB。
- 使用多阶段构建尽量减小镜像体积。
- 可选 docker-compose.yml 简化启动命令。

---

### US-6 处理状态实时反馈 · 状态: Backlog

作为 **普通用户**,
我想要 在上传 PDF 后看到处理进度(排队中/处理中/已完成/失败),
以便 我知道当前状态,不用盲目等待。

验收标准:
- AC1: Given 用户上传 PDF,When 上传成功,Then 页面显示"排队中"状态。
- AC2: Given PDF 进入 OCR 处理,When 后端开始处理,Then 页面更新为"处理中"。
- AC3: Given OCR 处理完成,When 结果生成,Then 页面更新为"已完成"并可查看结果。
- AC4: Given OCR 处理失败,When 错误发生,Then 页面更新为"失败"并显示错误原因。

技术备注:
- 可使用轮询(polling)或 Server-Sent Events(SSE)实现状态更新。
- 初期建议用轮询(简单可靠),后续可升级 SSE/WebSocket。

---

## 5. 非功能需求

- **安全**:密钥只进 Secrets,不进 Git。上传文件临时存储,处理完成后定期清理。
- **可维护**:一需求一小 PR,避免大爆炸式提交。
- **可测试**:核心逻辑(OCR 调用封装、PDF 转图片、Markdown 合成)必须有单元测试。
- **可部署**:部署后必须有健康检查(`/health`)。
- **性能**:单个 PDF(10 页内)OCR 处理时间 < 60 秒(取决于 CPU 和 PDF 复杂度)。
- **兼容性**:支持 PDF 1.4~2.0 格式;支持中英文混合识别。
- **可靠性**:OCR 服务异常时返回明确错误,不静默失败;上传文件处理完自动清理临时文件。
