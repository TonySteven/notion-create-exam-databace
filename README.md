# 和学在线作业题库整理到notion数据库

![](https://tva1.sinaimg.cn/large/e6c9d24ely1h46gwh86roj21id0u0wmu.jpg)

## 简介

> 时间: 2022/07/13 项目版本
>
> 和学在线作业题库整理到notion数据库

### 内容简介

```

需求背景

死记硬背的交给计算机,把更多时间放在自己感兴趣的事情上.

1. 建立notion数据库, 考试根据数据库找题即可.

设计思路

1. 解析和学在线后台系统的作业历史接口获取Json数据

2. 解析Json数据库,通过notion_API建立notion数据库.

3. 考试时直接通过notion数据库找题即可.

```

### 使用文档

---

#### 1. 直接用建好的notion数据库 (山师的同学们可以复用并持续更新)

[notion考试题库](https://genesisorgcn.notion.site/f406642b43ba49ff99844e621608f8d3?v=35e6eb4671e34683825a47cc2e050cc3)

#### 2. 通过项目搭建自己notion数据库 (其他学校的同学)

##### 2.1 环境准备

###### 2.1.1 申请notion_API (参考最后项目实现文档)

###### 2.1.2 pull下main分支代码后,通过requirements.txt还原Python环境(记得新建项目环境)

```shell
pip install -r requirements.txt
```

![](https://tva1.sinaimg.cn/large/e6c9d24ely1h46hhe5xqej21c80u0416.jpg)

##### 2.2 使用

##### 2.2.0 查看本地按照redis布隆过滤器环境文档,并安装本地按照redis布隆过滤器环境.

##### 2.2.1 获取Json数据并放入origin_json_data文件夹 (参考最后项目实现文档)

##### 2.2.2 获取Json数据 (参考最后项目实现文档)

##### 2.2.3 analysis.py的两处替换

![](https://tva1.sinaimg.cn/large/e6c9d24ely1h46htnbjilj20yp0u0gol.jpg)

![](https://tva1.sinaimg.cn/large/e6c9d24ely1h46hut8dvvj20u00wvq6f.jpg)

##### 2.2.4 analysis.py运行即可

---

### 项目文档

- [项目逐步实现文档 - notion](https://genesisorg.notion.site/Json-API-notion-0e28fa9199ce4ea681b823239c235d2b)
