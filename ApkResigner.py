#!/usr/bin/python  
#-*-coding:utf-8-*-

import os
import sys
import config
import platform


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


#当前脚本文件所在目录
parentPath = curFileDir() + getBackslash()

#config
libPath = parentPath + "lib" + getBackslash()
buildToolsPath =  config.sdkBuildToolPath + getBackslash()
checkAndroidV2SignaturePath = libPath + "CheckAndroidV2Signature.jar"
walleChannelWritterPath = libPath + "walle-cli-all.jar"
outputFilePath = parentPath + "channels"
channelFilePath = parentPath +"channel"
keystorePath = config.keystorePath
keyAlias = config.keyAlias
keystorePassword = config.keystorePassword
keyPassword = config.keyPassword
protectedSourceApkPath = parentPath + config.protectedSourceApkName

zipalignedApkPath = protectedSourceApkPath[0 : -4] + "_aligned.apk"
signedApkPath = zipalignedApkPath[0 : -4] + "_signed.apk"

#创建文件夹
try:
	os.makedirs(outputFilePath)
	pass
except Exception:
	pass


#对齐
zipalignShell = buildToolsPath + "zipalign -v 4 " + protectedSourceApkPath + " " + zipalignedApkPath
os.system(zipalignShell)

#签名
signShell = buildToolsPath + "apksigner sign --ks "+ keystorePath + " --ks-key-alias " + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" + keyPassword + " --out " + signedApkPath + " " + zipalignedApkPath
os.system(signShell)

#检查V2签名是否正确
checkV2Shell = "java -jar " + checkAndroidV2SignaturePath + " " + signedApkPath;
os.system(checkV2Shell)

#写入渠道
writeChannelShell = "java -jar " + walleChannelWritterPath + " batch -f " + channelFilePath + " " + signedApkPath + " " + outputFilePath
os.system(writeChannelShell)

print "\n**** Finish! Please Check the 'Channels' Folder in your root Floder ! ****\n"



