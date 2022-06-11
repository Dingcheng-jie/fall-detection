1、创建环境：
conda create -n falldetection python=3.7.0
conda create cudatoolkit=10.0
conda create cudnn=7.6

2、安装需求库
pip install -r requirements.txt

3、整理数据集，成如下结构
![图片](https://user-images.githubusercontent.com/82815279/173191506-3a7d4c1c-241d-4fdf-9a33-9315e3bf35dc.png)


4、划分训练集、验证集
python split_train_val.py –xml_path dataset1/Annotations –txt_path datasets1/ImageSets/Main
 
5、接下来准备labels，把数据集格式转换成yolo_txt格式，即将每个xml标注提取bbox信息为txt格式（这种数据集格式成为yolo_txt格式），每个图像对应一个txt文件，文件每一行为一个目标的信息，包括class, x_center, y_center, width, height格式。
python voc_label.py
运行后会生成如下labels文件夹和三个包含数据集的txt文件，其中labels中为不同图像的标注文件，train.txt等txt文件为划分后图像所在位置的绝对路径，如train.txt就含有所有训练集图像的绝对路径。
 
6、配置yaml文件
在yolov5目录下的data文件夹下新建一个falldown.yaml文件，用来存放训练集和验证集的划分文件（train.txt和val.txt），这两个文件是通过运行voc_label.py代码生成的，然后是目标的类别数目和具体类别列表，falldown.yaml内容如下
 
7、选择一个需要运行的预训练模型，修改模型配置（将类别数量nc改成跌倒数据集的）
 
8、训练模型
python train.py --img 640 --batch 64 --epoch 10 --data data/falldown.yaml --cfg models/yolov5l.yaml --weights weights/yolov5l.pt --device '0'
 
9、模型预测
python test.py --weights runs/train/exp/weights/best.pt --source testdata/test --device 0 --save-txt
