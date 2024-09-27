# Frequent-Pattern-Mining
频繁模式挖掘（Frequent Pattern Mining），采用了Apriori算法和FP-growth算法，目前实现了窗口图形化操作
> 点开dist文件夹下的p.exe文件可以直接食用，不会~~release~~

> data_mini_create 可以生成数据集，用于测试

# code

## apriori_1：v.1.1.0923
第一个版本实现了四个功能：1.按照频繁项集次序输出2.按照支持度次序输出3.输出极大频繁项集4.输出支持度前k项集

## apriori_2：v.1.2.0927
第二个版本，优化了四个按键实现的冗余代码，将四个功能封装成一个函数，同时加入了剪枝操作优化代码，优化了效率。

要求几乎都完成了：![img00](https://github.com/lvlebin2876587146/picx-images-hosting/raw/master/image.73twuhnqvg.webp)
