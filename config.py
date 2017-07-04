#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = "/Users/mac/Android/pro/prometheus-android/app/release.keystore"
keyAlias = "your KeyAlias"
keystorePassword = "your KeystorePassword"
keyPassword = "your keyPassword"

#加固后的源文件名（未重签名）
protectedSourceApkName = "app-release.encrypted.apk"

#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "/Users/mac/Library/Android/sdk/build-tools/25.0.2"