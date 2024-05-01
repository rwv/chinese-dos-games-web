#!/bin/bash 

echo "[$(date)] 默认不存在游戏，需要手动执行命令下载，数据目录：/app/static/games/bin"
echo "[$(date)] 执行内部容器命令：python3 /app/static/games/download_data.py"
echo "[$(date)] 注意最好将数据卷挂载到主机"
echo ""
echo "[$(date)] 可以使用 Docker / Docker Compose / Kubernetes 执行命令："
echo "[$(date)] 使用 Docker: docker exec -it <container_id> python3 /app/static/games/download_data.py"
echo "[$(date)] 使用 Docker Compose: docker-compose exec <service_name> python3 /app/static/games/download_data.py"
echo "[$(date)] 使用 Kubernetes: kubectl exec -it <pod_name> python3 /app/static/games/download_data.py"
echo ""

# python3 app.py
gunicorn -w 5 -b 0.0.0.0:5000 app:app
