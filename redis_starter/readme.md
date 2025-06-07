#  Redis
## 应用场景
- 缓存系统
- 计数器
- 消息队列系统
- 排行榜
- 社交网络
- 实时系统

## 安装、环境搭建

## 核心配置文件

`/etc/redis/redis.conf`

- 绑定ip
  - `bind 127.0.0.1 -::1`
- 端口
  - `port 6379`
- 守护进程方式
  - `daemonize yes`
- 备份数据文件
  - `dbfilename dump.rdb`
- 数据文件存储路径
  - `dir /var/lib/redis`
- 日志文件
  - `logfile /var/log/redis/redis-server.log`
- pid文件
  - `pidfile /run/redis/redis-server.pid`
- 数据库:默认16个
  - `databases 16`

## 服务器端和客户端命令

### 服务端命令

- 启动服务
  - 最简启动
- > redis-server
  - 启动参数
- > redis-server
  - 配置文件
- > redis-server /etc/redis/redis.conf


>  service redis-server start
- 关闭服务
>  service redis-server stop

### 客户端命令

- 客户端连接
> redis-cli -h 127.0.0.1 -p 6379

- 客户端返回类值
  - 状态回复 `ping`
  - 错误回复 `hget hello field`
  - 整数回复 `incr hello`
  - 字符串回复 `get hello`
  - 多行字符串回复 `mget hello world`


## Redis数据类型(5)

- String
  - set key value
  - get key
- List
  - lpush carlist
  - llen carlist
  - lrange carlist 0 3
- Hash
  - hget
  - hset field value
- Set
  - sadd myset a b c d
- zet

## 通用命令

### 通用命令
- keys
- dbsize
- exsists key
- del key [key,...]
- expire key seconds
- type key

## Redis 发布与订阅
- Pub/Sub

