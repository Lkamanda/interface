import os


def clearTestReportFile(html_dir):
    """
    根据修改时间，清楚除最近10条外的测试报告
    :param html_dir: 清楚目录多余的测试报告
    :return:
    """
    html_list = []
    removeList = []
    file_list = os.listdir(html_dir)
    # 将指定目录下所有文件根据修改时间进行排序，最近修改在最后一位
    # os.get.getatime(file)返回文件的最后修改时间
    # os.path.isdire(file) 判断file 是否为路径， 返回true， false
    file_list.sort(key=lambda fn: os.path.getatime(html_dir + "\\" + fn) if not os.path.isdir(html_dir + "\\" + fn) else 0)

    # 判断文件列表中文件是否是html格式，是加入html_list
    for file in file_list:
        fileName, extension = os.path.splitext(file)
        if extension == '.html':
            html_list.append(file)

    # 根据需求保留目录下存放最近10条
    if len(html_list) > 10:
        removeNumber = len(html_list) - 10
        print('removeNumber:'+str(removeNumber))
        for i in range(removeNumber):
            removeList.append(html_list[i])
            # print(len(removeList))
        for removeL in removeList:
            if os.path.exists(os.path.join(html_dir, removeL)):
                os.remove(os.path.join(html_dir, removeL))
