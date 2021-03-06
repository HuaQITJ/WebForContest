# 开发环境

## github账号

+ 每次commit之前要把Front_end下面的node_modules删除(体积太大)

+ 每个人有一个以名字首字母小写命名的分支

```shell
git clone             #


```





## 项目结构

前端：

```sh
npm install
npm run serve
```

后端：

flask框架





# 网站介绍





```mermaid
graph TB
D1[企业]--> C1[企业主界面]
F{两个按钮}-->|多主播搜索|E[多个主播搜索]

D[主播]-->G[主播主界面]
F{两个按钮}-->|单主播搜索|X[单主播搜索]

X1(搜索框)-->T(套餐页面)
E1(搜索框)-->T(套餐页面)

subgraph 主页面
A[网页功能]-->B[免费试用]
A[网页功能]-->C{登录注册}
A[网页功能]-->D0[网页介绍]
C{登录注册}-->|选择主播|D[主播]
C{登录注册}-->|选择企业|D1[企 业]


end
subgraph 企业主界面
C1[企业主界面]-->F{两个按钮}
end

subgraph 多主播搜索页面
E[多个主播搜索]---E1(搜索框)
end
subgraph 主播主界面
G[主播主界面]---Q{企业搜索}
end

subgraph 单主播搜索页面
X[单主播搜索]---X1(搜索框)
end

subgraph 套餐页面
T(套餐页面)-->Show(显示决策方案)
end

```

## 主页面

+ 介绍

+ + 免费试用
  + 登录\注册

  

## 企业主界面

+ 主播搜索
  + 方案一：热门搜索关键词
  + 方案二：固定的类别

+ 右上角功能 
  + 升级续费
  + 我的权限
  + 我的收藏
  + 个人消息
  + 退出

## 主播主界面

### 相关功能

**提供一个搜索框**

+ 主播主动可以联系企业进行合作

+ 右侧栏

  + 付费服务

    + 向平台申请做广告

  + 我的权限

    + 自主设计广告权限

  + 我的收藏

  + 个人消息

  + 退出

    






## 单主播搜索页面

### 相关功能

+ 排序

  + 综合排序

  + 流量排序

  + 薪酬排序

  + 信用排序

+ 筛选条件
  + 合作薪酬

  + 直播时段

  + 直播平台

  + 流量口

## 多主播搜索页面

### 相关功能

+ 筛选条件
  + 预算选择
  + 产品类型选择
  + 期望销售数量

## 决策方案提供页面

+ 主播数据

+ 方案分析

+ 粉丝画像

+ 套餐对比

  




# 数据库设计

## 主播数据

```mermaid
graph LR

S[主播]---Na((姓名))
S[主播]---Age((年龄))
S[主播]---P((评论数))
S[主播]---Po((带货能力评价))
S[主播]---Fan((粉丝数))
S[主播]---G((关注数量))
S[主播]---T((带货类型))



En[企业]--- |多对多|Mid{合约}
En[企业]---EnName((企业名))
En[企业]---ENa((企业编号))
Mid{合约}---|多对多|S[主播]



Date((合约时长))---Mid{合约}
Mon((合约薪水))---Mid{合约}
Time((合约日期))---Mid{合约}

```



# 数据抓取

# 数学建模

