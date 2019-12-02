# docker-test
node集成docker 

## Dockerfile

```
FROM node:12
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . . 
EXPOSE 8080
CMD [ "node", "index.js" ]
```

## 打包

```
docker build -t 名称 .
```

## 运行

```
docker run -p 外部端口:docker端口 -d docker包
```

https://juejin.im/post/5d8440ebe51d4561eb0b2751