import os
import platform


def clearTestReportFile(remove_dir, removeType):
    """
    根据修改时间，清楚除最近10条外的测试报告
    :param remove_dir: 清楚目录多余的测试报告
    :removeType: 删除的文件类型
    :return:
    """
    removeType = '.' + removeType
    html_list = []
    removeList = []
    file_list = os.listdir(remove_dir)
    cSlash = getSlash()
    # 将指定目录下所有文件根据修改时间进行排序，最近修改在最后一位
    # os.get.getatime(file)返回文件的最后修改时间
    # os.path.isdire(file) 判断file 是否为路径， 返回true， false
    file_list.sort(key=lambda fn: os.path.getatime(remove_dir + cSlash + fn) if not os.path.isdir(remove_dir + cSlash + fn) else 0)

    # print(file_list)
    # 判断文件列表中文件是否是html格式，是加入html_list
    for file in file_list:
        fileName, extension = os.path.splitext(file)
        if extension == removeType:
            html_list.append(file)


    # 根据需求保留目录下存放最近10条
    if len(html_list) > 10:
        removeNumber = len(html_list) - 10
        print('removeNumber:'+str(removeNumber))
        for i in range(removeNumber):
            removeList.append(html_list[i])
            # print(len(removeList))
        for removeL in removeList:
            if os.path.exists(os.path.join(remove_dir, removeL)):
                os.remove(os.path.join(remove_dir, removeL))


def platformSystem():
    """
    判断当前使用系统
    :return: 系统的自符串
    mac = 'Darwin'
    windows= 'Window'
    linux = 'Linux'
    """
    if platform.system() == 'Darwin':
        return 'mac'
    elif platform.system() == 'Windows':
        return 'windows'
    else:
        return 'others'


def getSlash():
    """
    通过当前系统来判断使用何种斜杠
    :return:
    """
    cSystem = platformSystem()
    if cSystem == 'mac':
        return '/'
    else:
        return '\\'



