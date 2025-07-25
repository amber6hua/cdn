# 使用轻量级基础镜像（如 alpine）
FROM alpine:latest

# 设置工作目录
WORKDIR /app

# 复制二进制文件
COPY tgs /app/tgs

# 设置可执行权限
RUN chmod +x /app/tgs

# 暴露端口（可选，实际运行时仍需 -p 参数映射）
EXPOSE 7856/tcp

# 直接运行二进制文件
ENTRYPOINT ["/app/tgs"]