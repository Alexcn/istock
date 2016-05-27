# istock
istock 是一个抓取沪深股市的行情，并按照个人的喜好进行分析和整理的项目。集成了数据抓取、量化分析、以及制定相关的选股测略等相关的模块。深度分析股票涨跌的相关因素，找到一个合理的风险控制策略，保证稳定的盈利状态。但是股市的行情是会变化的，并不能保证一定会盈利。


### 依赖的第三方模块

- tushare
- pandas
- sqlalchemy
- PyYAML
- psycopg2

### 配置项目

请确保已经安装 PostgreSQL 数据库，并处于运行状态。如果没有数据库，也可以使用部分功能，不过无法持久化数据，无法对数据进行持续分析。以 *nix 系统为例：

- 取下项目代码

```shell
$ git clone https://github.com/itpubs/istock.git
```
- 配置数据库

```shell
$ cd istock/config
$ cp database_sample.yml database.yml  # 输入数据库名、用户名、端口号
```