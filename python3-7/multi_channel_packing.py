import io
import os
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 注意以下信息需要自己根据具体情况配置
signKeyPath = ".\\sign_key_store.jks"
keyAlias = "alias"
ksPass = "123456"
keyPass = '123456'
wallePath = ".\\walle-cli-all.jar"
config_channel_path = ".\\channel_config_demo.json"
jiagu360_home = ""  # 360加固主目录http://jiagu.360.cn/#/global/help/164


def deal_protected_apk_dir():
    path_name = os.path.split(protectedApkPath)
    # 加固后的apk文件所在的目录
    global protectedApkDir
    protectedApkDir = path_name[0] + os.path.sep
    # 加固apk的文件名称(不包含后缀名)
    global protectedApkName
    protectedApkName = path_name[1][:path_name[1].rindex(".")]


def sign_apk():
    # 签名，注意需要将build-tools路径配置到环境变量中（例如：E:\Develop_Software\Android\sdk\build-tools\27.0.2）
    global signedApkPath
    signedApkPath = protectedApkDir + protectedApkName + "_signed.apk"
    sign_shell = "apksigner sign -ks " + signKeyPath + " -ks-key-alias " + keyAlias + " -ks-pass pass:" + \
                 ksPass + " -key-pass pass:" + keyPass + ' -out ' + signedApkPath + " " + protectedApkPath
    print(sign_shell)
    os.system(sign_shell)


# 删除某个路径下的所有文件
def delete_dir(path):
    if os.path.exists(path):
        file_list = os.listdir(path)
        for file in file_list:
            if os.path.isfile(file):
                os.remove(file)


# 创建目录（如果没有就创建，如果有就删除里面的文件）
def create_dir(path):
    if os.path.exists(path):
        delete_dir(path)
    else:
        os.mkdir(path)


# 注入渠道信息
def inject_channel_info(config_json_path, channel_path):
    walle_shell = "java -jar " + wallePath + " batch2 -f " + config_json_path + " " + signedApkPath + " " + channel_path
    print(walle_shell)
    os.system(walle_shell)


# 生成渠道包
def market_channels():
    channel_path = protectedApkDir + "market_channels"
    create_dir(channel_path)
    inject_channel_info(config_channel_path, channel_path)


def packing():
    deal_protected_apk_dir()
    if not has_signed:
        sign_apk()
    else:
        global signedApkPath
        signedApkPath = protectedApkPath

    market_channels()
    tkinter.messagebox.showwarning('提示', '打包完成')


protectedApkPath = ""


def explore_apk_file():
    global protectedApkPath
    file_path = tkinter.filedialog.askopenfilename()
    if file_path != '':
        protectedApkPath = file_path
        apkPath.set(protectedApkPath)


def begin_packing():
    global protectedApkPath
    if protectedApkPath == '' or not protectedApkPath.endswith(".apk"):
        tkinter.messagebox.showwarning('提示', '请选择正确的 apk 文件')
        return
    if has_protected or has_signed == TRUE:
        packing()
        return
    deal_protected_apk_dir()
    jiagu_shell = "java -jar " + path360.get() + "\\jiagu.jar -jiagu " + protectedApkPath + " " + protectedApkDir
    os.system(jiagu_shell)
    file_list = os.listdir(protectedApkDir)
    find = FALSE
    for file in file_list:
        if file.endswith(".apk") and protectedApkName in file and 'jiagu' in file:
            protectedApkPath = os.path.join(protectedApkDir, file)
            find = TRUE
    if not find:
        tkinter.messagebox.showwarning('警告', '未找到加固后的apk文件')
        return
    packing()


has_protected = FALSE
has_signed = FALSE


def if_protected():
    global has_protected
    has_protected = not has_protected


def if_signed():
    global has_signed
    has_signed = not has_signed


windowW = 500
windowH = 300

root = tkinter.Tk()
root.title("多渠道打包")
root.geometry(str(windowW) + "x" + str(windowH))

# 360加固的主目录
label360 = Label(root, text="360加固的主目录：")
label360.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
path360 = StringVar()
path360Edit = Entry(root, textvariable=path360)
path360.set("H:\工作\\360加固\\360jiagubao_windows_64\\jiagu")
path360Edit.pack(fill=X)

protected = Checkbutton(
    root, text="已经加固（选中则跳过加固步骤）",
    command=if_protected)
protected.pack()

signed = Checkbutton(
    root, text="已经加固并且签名（选中则跳过加固以及签名步骤）",
    command=if_signed)
signed.pack()

apk_type = StringVar()
apk_type.set("请选择符合条件的 apk 文件：")
l1 = Label(root, textvariable=apk_type)
l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

apkPath = StringVar()
apkPath.set("选择apk文件")
editPathBtn = Button(root, textvariable=apkPath, command=explore_apk_file)
editPathBtn.pack()

beginPack = Button(root, text="开始打包", command=begin_packing)
beginPack.pack()

# 屏幕分辨率
scrnW = root.winfo_screenwidth()
scrnH = root.winfo_screenheight()

root.withdraw()  # 隐藏
# 移到屏幕外，避免闪烁
root.geometry('+%d+%d' % (scrnW + 100, scrnH + 100))

# 部件布局完成
root.update()  # 刷新
root.deiconify()  # 显示，使窗口尺寸属性可用

left = (scrnW - root.winfo_width()) // 2
top = (scrnH - root.winfo_height()) // 2 - 50

root.geometry("+%d+%d" % (left, top))
root.mainloop()
