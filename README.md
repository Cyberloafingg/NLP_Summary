## 运行环境：
   - CPU：Intel® Xeon® E5-2680 v4 CPU，主频2.4GHz
   - GPU：NVIDIA® Tesla® P40 24G（12TFLOPS 单精度浮点计算，47INT8 TOPS）
   - 内存：DDR4，2666MT/s。
   - 操作系统：Linux Ubuntu 18.04 LTS
   - CUDA 11.2
## 所需安装包
```angular2html
pip install -r requirements.txt
```
## 运行说明
1. 新建path/to/data文件夹,将数据集放在data文件夹下[数据集连接](https://www.datafountain.cn/competitions/536/datasets)
2. 新建path/to/model文件夹，用于保存模型，将训练好的第一个PEGASUS模型[百度网盘（链接）](https://pan.baidu.com/s/1vhIM_xKbXCyYnAfT5cn9Tw?pwd=0000 )保存在model文件夹的checkpoints1文件夹下，作为迭代生成所使用的模型
3. 运行DataPreprocessing.ipynb笔记本，生成预处理数据将在processed文件夹中
4. 运行train.ipynb笔记本，训练模型
5. 运行GenerateResult.py，生成摘要
6. 运行AfterProcess.ipynb，进行后处理
7. 将result.csv提交到竞赛官网进行评测

## 下载链接
[工程代码](https://github.com/Cyberloafingg/NLP_Summary.git)

[模型链接](https://pan.baidu.com/s/1vhIM_xKbXCyYnAfT5cn9Tw?pwd=0000 )

