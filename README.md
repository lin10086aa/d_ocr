# d_ocr - PDF 图转文字

将 PDF(含扫描件、图片型 PDF)通过 PP-StructureV3 OCR 转为 Markdown 文字。

## 快速开始

```bash
# 构建镜像
docker build -t d_ocr .

# 启动服务
docker run -p 8000:8000 d_ocr

# 打开浏览器
# http://localhost:8000
```

## 技术栈

- Python 3.11 + FastAPI
- PP-StructureV3 (PaddleOCR)
- Docker

## 项目状态

🚧 开发中 — 见 [standards/PROGRESS.md](standards/PROGRESS.md)
