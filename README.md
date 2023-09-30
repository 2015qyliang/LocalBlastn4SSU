# LocalBlastn4SSU
Run blast fastly based on local SILVA database

If cite, please use url: **https://github.com/2015qyliang/LocalBlastn4SSU**

[点击可下载新版本](https://github.com/2015qyliang/LocalBlastn4SSU/archive/refs/tags/V2.0.tar.gz)

### 2023年7月

根据EzBioCloud的网站2023年7月份更新的新数据库，重新作数据库并更新简化操作。

### 2021年7月30日

EzBioCloud的网站最近更新了网站架构，提高了反爬虫的灵敏度。

因此为实现16S rDNA一代测序结果本地批量比对，改善数据库的选择策略，一边倒地倾向[Silva数据库](https://www.arb-silva.de/)，所处理的版本是[release_138](https://www.arb-silva.de/fileadmin/silva_databases/release_138/Exports/SILVA_138_SSURef_NR99_tax_silva.fasta.gz)。

### 2021年5月24日

在传统微生物资源挖掘过程中, 需要对大量的分离菌株进行鉴定. 通过在线提交序列获取初步鉴定信息已经不能满足日益繁多的一代测序结果的解决现状. 

故, 将分类鉴定中常使用的EzBioCloud在线数据库进行本地化, 提供可批量快速进行序列比对并获得初步分类信息的分析流程, 该流程与本地化NCBI数据库具有更高的可行性操作.

该流程可主要应对两种情况:

- -1> 一代测序结果直接序列比对获取初步的分类学信息;
- -2> 可对正反向测序或者克隆序列进行序列拼装.

**流程主要依赖 python (>3.5) 进行搭建, 须配置 biopython 分析包**
