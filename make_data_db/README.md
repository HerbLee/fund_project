## 构建基金数据库

### 数据来源

目前数据来源为新浪财经

#### docker

```buildoutcfg
# 建立数据库

docker run -p 3306:3306 --name herb_fund_db -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7


```