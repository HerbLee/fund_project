sudo docker run -p 3309:3306 --name onehaven_db -e MYSQL_ROOT_PASSWORD='123' -d mysql:5.7  --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci
sudo docker run -itd --name redis-onehaven -p 6379:6379 redis