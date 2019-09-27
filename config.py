#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = "epost_keys.keystore"
keyAlias = "ePost"
keystorePassword = "cxyapp"
keyPassword = "cnpost"

#加固后的源文件名（未重签名）
protectedSourceApkName = "epost_encrypted.apk"
#加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = "app/build/outputs"
#渠道包输出路径，默认在此文件夹Channels目录下
channelsOutputFilePath = "app/build/outputs/channels/"
#指定的渠道列表配置，如有配置，则它的优先级高于channelFilePath，channelFilePath将会失效。渠道名间用英文逗号分隔。如"meituan,meituan2,meituan3"
channelList = ""
#渠道名配置文件路径，默认在此文件夹根目录
channelFilePath = "app/channel/"
#额外信息配置文件（绝对路径，例如/Users/mac/Desktop/walle360/config.json）
#配置信息示例参看https://github.com/Meituan-Dianping/walle/blob/master/app/config.json
extraChannelFilePath = ""
#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "/home/ciUser/apps/android_sdk/build-tools/28.0.3"
