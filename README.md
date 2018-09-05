# ProtectedApkResignerForWalle
一步解决应用加固导致[Walle](https://github.com/Meituan-Dianping/walle)渠道信息失效的自动化脚本，自动生成渠道包

----------
# 用法：

- 按照config.py文件中的注释改成自己项目配置
- 将已经加固好的包【未签名的包，请不要使用加固客户端签名工具】放到脚本工具根目录下，即app-release.encrypted.apk
- 各种渠道的定义是在channel这个文件中，请根据项目情况修改
- 运行命令 `python ApkResigner.py`,即可自动生成所有渠道包。
----------

# python3.7 windows环境下图形界面打包(运行截图如下)
在multi_channel_packing.py文件中配置相应的信息：
```python
# 注意以下信息需要自己根据具体情况配置
signKeyPath = ".\\sign_key_store.jks"
keyAlias = "alias"
ksPass = "123456"
keyPass = '123456'
wallePath = ".\\walle-cli-all.jar"
config_channel_path = ".\\channel_config_demo.json"
jiagu360_home = "H:\工作\\360加固\\360jiagubao_windows_64\\jiagu"  # 360加固主目录，配置文档见：http://jiagu.360.cn/#/global/help/164
# apk_signer_home的主目录,一般是在android SDK的build-tools目录下，例如: E:\\Develop_Software\\Android\\sdk\\build-tools\\28.0.2
apk_signer_home = ""
```
双击run.vbs即可运行
![python3.7 windows环境下图形界面打包(运行截图如下)](https://github.com/heqinghqocsh/ProtectedApkResignerForWalle/blob/master/screenshot/main_frame.png)


# 运行注意事项：
[！！必看！！](https://github.com/Jay-Goo/ProtectedApkResignerForWalle/wiki/Run-Attentions)

# Wiki
更多用法和常见问题讨论请参看[wiki](https://github.com/Jay-Goo/ProtectedApkResignerForWalle/wiki)

----------
# 支持平台：（需要python环境）
- Windows (Test)
- Mac OS (Test)
- Linux

注意：python2.x版本正常，python3.x待测试
----------
# 问题讨论
[讨论传送门>>>](https://github.com/Meituan-Dianping/walle/wiki/360%E5%8A%A0%E5%9B%BA%E5%A4%B1%E6%95%88%EF%BC%9F)


----------
# 感谢
[支持Android7.0 Signature V2 Scheme 多渠道打包，并解决类似360加固后获取不到渠道信息 - 渠道统计失败的问题](%E6%94%AF%E6%8C%81Android7.0%20Signature%20V2%20Scheme%20%E5%A4%9A%E6%B8%A0%E9%81%93%E6%89%93%E5%8C%85%EF%BC%8C%E5%B9%B6%E8%A7%A3%E5%86%B3%E7%B1%BB%E4%BC%BC360%E5%8A%A0%E5%9B%BA%E5%90%8E%E8%8E%B7%E5%8F%96%E4%B8%8D%E5%88%B0%E6%B8%A0%E9%81%93%E4%BF%A1%E6%81%AF%20-%20%E6%B8%A0%E9%81%93%E7%BB%9F%E8%AE%A1%E5%A4%B1%E8%B4%A5%E7%9A%84%E9%97%AE%E9%A2%98)


