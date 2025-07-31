# 使用轻量级基础镜像（如 alpine）
FROM alpine:latest

ARG TARGETPLATFORM=linux/amd64

# 设置工作目录
WORKDIR /app

COPY --chmod=755 tgs /app/tgs

# 直接运行二进制文件
ENTRYPOINT ["/app/tgs"]