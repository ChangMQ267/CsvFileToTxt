import os.path
import csv


def importCSV(pathSaveFile,pathCsvFile,file):
    suffix = os.path.splitext(file)[1]
    ModelName = os.path.splitext(file)[0]
    HOME = pathSaveFile
    filePath = pathCsvFile+file
    strNeed = '**需求\n'
    strError = '**缺陷\n'
    strNode = '**子任务\n'
    if suffix == '':
        print("请选择文件！！！")
    elif suffix != '.csv':
        print("文件类型不是CSV文件，请选择CSV文件")
    else:
        with open(filePath, encoding='utf-8') as fileCSV:
            reader = csv.reader(fileCSV)
            for row in reader:
                types = row[0]
                id = row[1]

                if types == '需求':
                    about = row[3]
                    if about == '':
                        about = row[4]
                    needRow = '    * ' + id + ' ' + about
                    strNeed = strNeed+needRow+'\n'
                elif types == '缺陷':
                    about = row[3]
                    if about == '':
                        about = row[4]
                    needRow = '    * ' + id + ' ' + about
                    strError =  strError+needRow+'\n'
                elif types == '子任务':
                    about = row[4]
                    needRow = '    * ' + id + ' ' + about
                    strNode = strNode + needRow+'\n'

            if strNeed != '**需求\n':
                file = open(HOME+ModelName+'-需求.txt',mode='a+',encoding='GBK')
                file.writelines(strNeed)
                file.close()
            if strError != '**缺陷\n':
                file = open(HOME+ModelName + '-缺陷.txt', mode='a+', encoding='GBK')
                file.writelines(strError)
                file.close()
            if strNode != '**子任务\n':
                file = open(HOME+ModelName + '-子任务.txt', mode='a+', encoding='GBK')
                file.writelines(strNode)
                file.close()

if __name__ == '__main__':

    print("#################For ChangMQ267 V1.0.0#####################")
    print("#  导出.csv文件前请选择按照关键词升序                       #\n"+
          "#  请格式化.csv文件名称，例如’RealtimeService-V1.0.5.csv‘ #\n"+
          "##########################################################")

    pathSaveFile = '.\恒生文档\\'
    pathCsvFile = pathSaveFile +'csv\\'
    try:
        os.makedirs(pathCsvFile)
    except:
        print("文件夹已存在，请清空文件夹下文件。")

    true = input("请将所有CSV文件放置在 程序目录/恒生文档/csv 目录下\n确认请输入Y：")
    if true == 'Y' or true == 'y':
        for root, ds, fs in os.walk(pathCsvFile):
            for file in fs:
                importCSV(pathSaveFile,pathCsvFile,file)
        print("转化完成，欢迎使用！！！")
    else:
        print("程序结束，欢迎使用！！！")
