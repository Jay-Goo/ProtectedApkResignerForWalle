#!/usr/bin/python  
#-*-coding:utf-8-*-

# /**
#  * ================================================
#  * 作    者：JayGoo
#  * 版    本：1.0.1
#  * 更新日期：2017/12/29
#  * 邮    箱: 1015121748@qq.com
#  * ================================================
#  */

import os
import sys
import config
import platform
import shutil

#获取脚本文件的当前路径
def curFileDir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，
     #如果是脚本文件，则返回的是脚本的目录，
     #如果是编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

#判断当前系统
def isWindows():
  sysstr = platform.system()
  if("Windows" in sysstr):
    return 1
  else:
    return 0

#兼容不同系统的路径分隔符
def getBackslash():
	if(isWindows() == 1):
		return "\\"
	else:
		return "/"


# 清空临时资源
def cleanTempResource():
  try:
    os.remove(zipalignedApkPath)
    os.remove(signedApkPath)
    pass
  except Exception:
    pass
 
 # 清空渠道信息
def cleanChannelsFiles():
  try:
    os.makedirs(channelsOutputFilePath)
    pass
  except Exception:
    pass

# 创建Channels输出文件夹
def createChannelsDir():
  try:
    os.makedirs(channelsOutputFilePath)
    pass
  except Exception:
    pass

# 检查自定义路径，并作替换
def checkCustomPath():
  if len(config.protectedSourceApkDirPath) > 0:
    protectedSourceApkPath = config.protectedSourceApkDirPath + getBackslash() + config.protectedSourceApkName

  if len(config.channelsOutputFilePath) > 0:
    channelsOutputFilePath = config.channelsOutputFilePath

  if len(config.channelFilePath) > 0:
    channelFilePath = config.channelFilePath


    
#当前脚本文件所在目录
parentPath = curFileDir() + getBackslash()

#config
libPath = parentPath + "lib" + getBackslash()
buildToolsPath =  config.sdkBuildToolPath + getBackslash()
checkAndroidV2SignaturePath = libPath + "CheckAndroidV2Signature.jar"
walleChannelWritterPath = libPath + "walle-cli-all.jar"
keystorePath = config.keystorePath
keyAlias = config.keyAlias
keystorePassword = config.keystorePassword
keyPassword = config.keyPassword
channelsOutputFilePath = parentPath + "channels"
channelFilePath = parentPath +"channel"
protectedSourceApkPath = parentPath + config.protectedSourceApkName

# 检查自定义路径，并作替换
checkCustomPath()

zipalignedApkPath = protectedSourceApkPath[0 : -4] + "_aligned.apk"
signedApkPath = zipalignedApkPath[0 : -4] + "_signed.apk"

# 创建Channels输出文件夹
createChannelsDir()

#清空Channels输出文件夹
cleanChannelsFiles()


#对齐
zipalignShell = buildToolsPath + "zipalign -v 4 " + protectedSourceApkPath + " " + zipalignedApkPath
os.system(zipalignShell)

#签名
signShell = buildToolsPath + "apksigner sign --ks "+ keystorePath + " --ks-key-alias " + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" + keyPassword + " --out " + signedApkPath + " " + zipalignedApkPath
os.system(signShell)
print(signShell)

#检查V2签名是否正确
checkV2Shell = "java -jar " + checkAndroidV2SignaturePath + " " + signedApkPath;
os.system(checkV2Shell)

#写入渠道
writeChannelShell = "java -jar " + walleChannelWritterPath + " batch -f " + channelFilePath + " " + signedApkPath + " " + channelsOutputFilePath
os.system(writeChannelShell)

cleanTempResource()

print "\n**** =============================TASK FINISHED=================================== ****\n"
print "\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   Please check channels in the path   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n"
print "\n"+channelsOutputFilePath+"\n"
print "\n**** =============================TASK FINISHED=================================== ****\n"


