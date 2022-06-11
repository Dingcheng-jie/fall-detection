import os
# 把错误图片的数字依次删除。jpg/xml文件后，再次运行Paddlex的切分数据集命令
#在模型训练时会出现报错，可以看到那些图片识别shape会报错
file_name = "Fall_dataset/images/fall_392.jpg"
if os.path.exists(file_name):
    os.remove(file_name)
    print('成功删除文件:', file_name)
else:
    print('未找到此文件:', file_name)

file_name = "Fall_dataset//Annotations/fall_392.xml"
if os.path.exists(file_name):
    os.remove(file_name)
    print('成功删除文件:', file_name)
else:
    print('未找到此文件:', file_name)