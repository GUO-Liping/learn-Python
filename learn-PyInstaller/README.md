---

typora-root-url: myFigures
---

# PyInstaller打包教程（Windows，PyQt5）

**本文旨在总结PyInstaller在Windows系统下对Python 3程序打包为可执行程序.exe的一般步骤。打包过程中拟解决以下问题：**

**Step 1: 如何通过最简单的方式通过PyInstaller打包.exe文件？**

**Step 2: PyInstaller打包.exe文件过程中用到的参数有哪些？分别是什么含义？**

**Step 3: 如何精简打包后.exe文件的大小？在巨人的肩膀上再进一步**

## 1 如何通过最简单的方式通过PyInstaller打包.exe文件？

### 1.1 安装测试 pyinstaller

#### 1.1.1 pip 安装 pyinstaller库

(1) 管理员方式打开命令提示符-cmd

国内用户建议采用

(2) 默认pip安装

```shell
pip install pyinstaller
```

(3) 采用清华大学镜像源安装

```shell
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

(4) 采用阿里云镜像源安装

```shell
pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple/
```

(5) 采用网易镜像源安装

```shell
pip install pyinstaller -i https://mirrors.163.com/pypi/simple/
```

#### 1.1.2 测试是否安装成功

cmd下输入

```shell
pip list

PyInstaller				3.6 or later
```

表示安装成功，可以使用。

### 1.2 PyInstaller打包第一个程序

#### 1.2.1 写一个简单numpy计算程序

myFirstExe.py

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import os
# 将numpy数组中对大于平均值的值求余弦，对小于平均值的数求正弦，最后返回

def func_compute(para_d):
	mean_value = np.mean(para_d)
	para_d_after = np.empty_like(para_d)
	for i in range(len(para_d)):
		if para_d[i] > mean_value:
			para_d_after[i] = np.cos(para_d[i])
		elif para_d[i] < mean_value:
			para_d_after[i] = np.sin(para_d[i])
		else:
			para_d_after[i] = para_d[i]
	return para_d_after


if __name__ == '__main__':
	test_array = np.array([-np.pi/4, 0, np.pi/4])
	test_array_after = func_compute(test_array)
	print('test_array = ', test_array)
	print('test_array_after = ', test_array_after)
	os.system("pause")  # 不要执行完立即关闭窗口

```

#### 1.2.2 最简单打包

(1) 将命令提示符cmd目录切换至当前myFirstExe.py目录下

首先，找到文件目录

![](/../README.assets/path.jpg)

接着，鼠标点击文件路径，删除路径，输入cmd

![](/../README.assets/cmd_path.jpg)

按Enter进入cmd，即为当先路径

![](/../README.assets/cmd_open.jpg)

(2) 开始最简单打包

![](/../README.assets/command1.jpg)

(3) 打包成功

![](/../README.assets/success1.jpg)

(4) 找到exe可执行文件

默认是打包成一堆文件，都在dist目录下，生成了myFirstExe文件夹

![](/../README.assets/dist_path.jpg)

打开怎么样

![](/../README.assets/exe_open.jpg)

再看看打包完成后的文件夹大小

![](/../README.assets/tooLarge.jpg)

什么？？？！！！几行代码打包完582M？？？显然无法接受这么大的exe文件，试想一下随便写的复杂点不得几个G，要知道MATLAB安装包也不过几个G，人家啥功能？我啥功能？

怎么办？看来对pyinstaller了解不够，唯有继续学习，顺便再来一碗鸡汤 The zen of python: Now is better than never. 

来到第二个问题...

## 2 PyInstaller打包.exe文件过程中用到的参数有哪些？分别是什么含义？

### 2.1 pyinstaller参数及含义

来自帮助文档...不得不说帮助文档（英文版）依然是深夜程序猿独自苦苦探索pyinstaller的明灯...这里附上网址膜拜http://www.pyinstaller.org，附件里也传了最新版帮助文档的pdf。

pyinstaller -h可以调出所有的参数说明，这里给出常用的参数及其含义

### 本教程cmd在当前目录打开（需打包的myFirstExe.py目录！）

命令1：

```python
pyinstaller -h          # 查看pyinstaller所有命令参数
```

命令2：

```python
pyinstaller myFirstExe.py          #最简单打包，生成包含exe的一个文件夹，文件夹名称为dist
```

命令3：

```python
pyinstaller -D myFirstExe.py          # 等同于--onedir，默认打包exe，与命令2功能一致
```

命令:4：

```python
pyinstaller -F myFirstExe.py          # 等同于--onefile，打包为单个exe文件，在文件夹dist下
```

命令5：

```shell
pyinstaller -i myLOGO.ico myFirstExe.py          # 打包为exe文件附带图标myLOGO.ico
```

开始打包exe

```shell
D:\Program Files\GitHub\myFirstExe>pyinstaller -F -i myLogo.ico myFirstExe.py
```

打包完成，图标正常显示，问题不大，不过还是200多兆。

![](/../README.assets/icoExe.jpg)

命令6：

```python
pyinstaller -w myFirstExe.py          # 等同于--windowed，--noconsole打包成功后运行exe将不会显示命令行黑窗口（Windows）
```

命令7：

```python
pyinstaller -d all myFirstExe.py          # 等同于--debug，产生debug版本的可执行文件，当打包文件报错时，一定要加上这个命令，然后在cmd命令行中输入myFirstExe.exe，来显示报错原因。-d all为调试参数，可选all：包含所有可调试的部分
```

命令8：

```python
pyinstaller --clean myFirstExe.py          # 打包前将清理原有打包产生的临时文件
```

......

命令还有这些：

```python
usage: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--add-data <SRC;DEST or SRC:DEST>]
                   [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                   [--hidden-import MODULENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--key KEY] [-d {all,imports,bootloader,noarchive}] [-s]
                   [--noupx] [--upx-exclude FILE] [-c] [-w]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns>]
                   [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                   [--win-no-prefer-redirects]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--runtime-tmpdir PATH] [--bootloader-ignore-signals]
                   [--distpath DIR] [--workpath WORKPATH] [-y]
                   [--upx-dir UPX_DIR] [-a] [--clean] [--log-level LEVEL]
                   scriptname [scriptname ...]
```

### 2.2 使用说明

2.1节中所有pyinstaller参数可以混合、多次使用，比如：

```python
pyinstaller --clean --noupx -F -w -d all -i myICON.ico myFirstExe2.py myFirstExe1.py
```

所有原则上说，通过上述命令，可以解决打包的绝大多数问题，只有特别特别特殊的情形必须通过编辑myFirstExe.spec文件来执行打包，哪几种特殊情形呢？官网给出了解释，以下四种情形：

```
• When you want to bundle data files with the app.需要给exe绑定额外数据
• When you want to include run-time libraries (.dll or .so files) that PyInstaller does not know about from
any other source.需要打包时执行额外批处理文件.dll等
• When you want to add Python run-time options to the executable.需要打包时执行其他操作等
• When you want to create a multiprogram bundle with merged common modules.当要创建一个包含合并的模块的多个程序包时。
```

值得说明的是，spec文件编辑的意义在于使得命令行输入的一长串参数以结构化的方式清晰的展现在你眼前，尤其对于你的参数很多很多时，这一点尤为重要。

## 3 如何精简打包后.exe文件的大小？在巨人的肩膀上再进一步

重头戏来了，我想打包的是一个PyQt5+numpy实现的计算及可视化界面，矩阵计算部分通过numpy实现，数据展示与实时可视化通过PyQt5实现，大约有2000行代码吧。好了，正常打包下来，不出所料696M，嗯，很符合对Pyinstaller的预期，毕竟自己啥也没搞清楚，一个exe文件就被制造出来了，真的棒...

不得不承认，就这样扔给别人一个几百兆的软件，要么你真的特别NB，要么...要么自己心里很虚...接下来我们看几种亲测有效的打包方法，最终这个696M的软件终于被打包成46M，可能还有进步的空间，但可以接受了

### 3.1 精准调用第三方库，采用from numpy import sin, cos等等，试一下（失败）

#### (1)重写调用

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from numpy import empty_like, mean, cos, sin, array, pi
from os import system
# 将numpy数组中对大于平均值的值求余弦，对小于平均值的数求正弦，最后返回

def func_compute(para_d):
	mean_value = mean(para_d)
	para_d_after = empty_like(para_d)
	for i in range(len(para_d)):
		if para_d[i] > mean_value:
			para_d_after[i] = cos(para_d[i])
		elif para_d[i] < mean_value:
			para_d_after[i] = sin(para_d[i])
		else:
			para_d_after[i] = para_d[i]
	return para_d_after


if __name__ == '__main__':
	test_array = array([-pi/4, 0, pi/4])
	test_array_after = func_compute(test_array)
	print('test_array = ', test_array)
	print('test_array_after = ', test_array_after)
	system("pause")  # 不要执行完立即关闭窗口

```

#### (2) 再次打包-cmd

```python
pyinstaller myFirstExe.py
```

#### (3) 再次查看打包exe大小

![exe_open2](/../README.assets/exe_open2.jpg)

582M，完全没有变呢，说明这种说法可能不太靠谱！![cry](/../README.assets/cry.png)

### 3.2 打包成单个exe文件

没错，你没看错，就是加一个参数“-F”，不开玩笑，就是这个方法，相当于打包成exe后，将python运行环境，临时文件等通通压缩为一个exe文件，压缩后文件比起 "-D" 要小差不多一半，当然这会影响打开后的运行速度，毕竟打开后后台还需要再次解压建立python运行环境再执行脚本。

```python
D:\Program Files\GitHub\myFirstExe>pyinstaller -F myFirstExe.py
```

加 -F 就行了，转眼打包成功，看下多大呢

![](/../README.assets/singleExe.jpg)

减小了一半！200M的样子了，没想到打包成单个exe文件，包的大小竟然显著减小。

### 3.3 排除不必要的第三方库

```python
pyinstaller --exclude-module scipy myFirstExe.py
```

### 3.4 使用Pipenv 创建打包python虚拟环境

(1) 安装 Pipenv

```python
pip install pipenv         
```

(2) 新建文件夹作为虚拟环境，然后该目录下打开cmd命令窗口:

```python
pipenv install --python 3.6
```

(3) 在命令行下进入虚拟环境

```python
pipenv shell
```

(4) 虚拟环境下安装 Pyinstaller 和.py程序引用的第三方库

```python
pip install pyinstaller
pip install pyqt5
pip install numpy
```

不过网上也有人这样（见参考文献，不过我没成功）：

```python
pipenv install pyinstaller
pipenv install pyqt5
pipenv install numpy
```

(5) 查看虚拟环境中安装的python第三方库

```python
pip list

(python_env-3JXKqTB9) D:\Program Files\GitHub\python_env>pip list
Package        Version
-------------- ---------
altgraph       0.17
future         0.18.2
numpy          1.18.1
pefile         2019.4.18
pip            20.0.2
PyInstaller    3.6
pypiwin32      223
PyQt5          5.14.1
PyQt5-sip      12.7.1
pywin32        227
pywin32-ctypes 0.2.0
setuptools     44.0.0
wheel          0.34.2
```

将自己需要打包的py文件通通放到虚拟环境目录下，然后当前目录打开cmd，激活虚拟环境进打包

```python
pipenv shell
```

打包结束后文件大小大大降低，由原来的696M降为145，还能再小吗？当然可以，是时候请出upx这一神器了，目前国内对pyinstaller结合upx打包的研究可谓鲜有报道，在本人阅读pyinstaller帮助文档的时候，UPX赫然在列，于是乎，经过一番摸索。。。终于有了本文。。。再次感谢详尽的帮助文档。当然还有GitHub。。。

### 3.5 UPX神器在pyinstaller中的正确应用

Version 1

```shell
pyinstaller --clean --noupx --debug all -D -w -i myLOGO.ico part_to_run.py part_to_compute.py part_to_UI.py
```

Version 2


3.5.1 将第三方库setuptools版本降为44.0.0

```python
pip install setuptools==44.0.0
```

3.5.2 安装pywin32

```python
pip install pywin32
(python_env-3JXKqTB9) D:\Program Files\GitHub\python_env>pyinstaller myFirstExe.py
```

## 3.6 Pyinstaller终极操作—利用.spec文件打包
### 3.6.1 生成.spec文件

```python
pyi-makespec -D -w -i myLOGO.ico name.py
```
```python
pipenv shell
pyinstaller --clean setup.spec
```
生成spec文件时只能使用如下命令:

```python
• --upx-dir=
• --distpath=
• --workpath=
• --noconfirm
• --ascii
• --clean
```

### 3.6.2 命令选项

```cmd
-h, --help show this help message and exit
-v, --version Show program version info and exit.
--distpath DIR Where to put the bundled app (default: ./dist)
--workpathWORKPATH Where to put all the temporary work files, .log, .pyz and etc. (default:
./build)
-y, --noconfirm Replace output directory (default: SPECPATH/dist/SPECNAME) without asking
for confirmation
--upx-dir UPX_DIR Path to UPX utility (default: search the execution path)
-a, --ascii Do not include unicode encoding support (default: included if available)
--clean Clean PyInstaller cache and remove temporary files before building.
--log-level LEVEL Amount of detail in build-time console messages. LEVEL may be one of
TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO).
```

### 3.6.3 生成内容选项
```cmd
-D, --onedir Create a one-folder bundle containing an executable (default)
-F, --onefile Create a one-file bundled executable.
--specpath DIR Folder to store the generated spec file (default: current directory)
-n NAME, --name NAME Name to assign to the bundled app and spec file (default: first script’s
basename)
```

### 3.6.4 附件选项
```cmd
--add-data <SRC;DEST or SRC:DEST> Additional non-binary files or folders to be added to the
executable. The path separator is platform specific, os.pathsep (which is ;
on Windows and : on most unix systems) is used. This option can be used
multiple times.
--add-binary <SRC;DEST or SRC:DEST> Additional binary files to be added to the executable. See
the --add-data option for more details. This option can be used multiple
times.
-p DIR, --paths DIR A path to search for imports (like using PYTHONPATH). Multiple paths are
allowed, separated by ‘:’, or use this option multiple times
--hidden-import MODULENAME, --hiddenimport MODULENAME Name an import not visible
in the code of the script(s). This option can be used multiple times.
--additional-hooks-dir HOOKSPATH An additional path to search for hooks. This option can be
used multiple times.

--runtime-hook RUNTIME_HOOKS Path to a custom runtime hook file. A runtime hook is code
that is bundled with the executable and is executed before any other code or module
to set up special features of the runtime environment. This option can be used
multiple times.
--exclude-module EXCLUDES Optional module or package (the Python name, not the path name)
that will be ignored (as though it was not found). This option can be used multiple
times.
--key KEY The key used to encrypt Python bytecode.


```

### 3.6.5 生成模式选项

```cmd
-d <all,imports,bootloader,noarchive>, --debug <all,imports,bootloader,noarchive> Provide assistance
with debugging a frozen application. This argument may be provided
multiple times to select several of the following options.
• all: All three of the following options.
• imports: specify the -v option to the underlying Python interpreter, causing
it to print a message each time a module is initialized, showing the place
(filename or built-in module) from which it is loaded. See https://docs.
python.org/3/using/cmdline.html#id4.
• bootloader: tell the bootloader to issue progress messages while initializing
and starting the bundled app. Used to diagnose problems with missing
imports.
• noarchive: instead of storing all frozen Python source files as an archive
inside the resulting executable, store them as files in the resulting output
directory.
-s, --strip Apply a symbol-table strip to the executable and shared libs (not recommended
for Windows)
--noupx Do not use UPX even if it is available (works differently between Windows and
*nix)
--upx-exclude FILE Prevent a binary from being compressed when using upx. This is typically used
if upx corrupts certain binaries during compression. FILE is the filename of the
binary without path. This option can be used multiple times.
```

### 3.6.6 windows & Linux特殊选项

```cmd
-c, --console, --nowindowed Open a console window for standard i/o (default). On Windows this
option will have no effect if the first script is a ‘.pyw’ file.
-w, --windowed, --noconsole Windows and Mac OS X: do not provide a console window for standard
i/o. On Mac OS X this also triggers building an OS X .app bundle. On Windows
this option will be set if the first script is a ‘.pyw’ file. This option is ignored in
*NIX systems.
-i <FILE.ico or FILE.exe,ID or FILE.icns>, --icon <FILE.ico or FILE.exe,ID or FILE.icns>
FILE.ico: apply that icon to a Windows executable. FILE.exe,ID, extract the
icon with ID from an exe. FILE.icns: apply the icon to the .app bundle on Mac
OS X
```

### 3.6.7 windows特殊选项

```cmd
--version-file FILE add a version resource from FILE to the exe
-m <FILE or XML>, --manifest <FILE or XML> add manifest FILE or XML to the exe
-r RESOURCE, --resource RESOURCE Add or update a resource to a Windows executable. The
RESOURCE is one to four items, FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE
can be a data file or an exe/dll. For data files, at least TYPE and NAME must be
specified. LANGUAGE defaults to 0 or may be specified as wildcard * to update
all resources of the given TYPE and NAME. For exe/dll files, all resources from
FILE will be added/updated to the final executable if TYPE, NAME and LANGUAGE
are omitted or specified as wildcard *.This option can be used multiple
times.
--uac-admin Using this option creates a Manifest which will request elevation upon application
restart.
--uac-uiaccess Using this option allows an elevated application to work with Remote Desktop.
```



## 参考文献

### 1. GitHub用户

### https://jdhao.github.io/2019/10/14/python_script_to_exe/

### 2. 简书用户

### https://www.jianshu.com/p/a4339550d7c1

### 3. CSDN用户

### https://blog.csdn.net/frostime/article/details/90523062

### 4. CSDN用户

### https://blog.csdn.net/Victor_zero/article/details/8095

### 5. 博客园用户

### https://www.cnblogs.com/valorchang/p/11358541.html



