#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = "/Users/mac/Android/pro/prometheus-android/app/release.keystore"
keyAlias = "your KeyAlias"
keystorePassword = "your KeystorePassword"
keyPassword = "your keyPassword"

#加固后的源文件路径（未重签名）
protectedSourceApkPath = "/Users/mac/downloads/app-release.encrypted.apk"

#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "/Users/mac/Library/Android/sdk/build-tools/25.0.2"

#输出文件目录
outputFilePath = "/Users/mac/downloads"

#channel文件路径
channelFilePath = "/Users/mac/Android/pro/prometheus-android/app/channel"