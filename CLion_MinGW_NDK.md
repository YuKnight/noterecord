


### 安装MinGW [CLion 增添 MinGW 环境](https://www.jianshu.com/p/f71b19b5545e)
* 下载MinGW, 选择使用离线安装包[MinGW-w64 - for 32 and 64 bit Windows](https://link.zhihu.com/?target=https%3A//sourceforge.net/projects/mingw-w64/files/Toolchains%2520targetting%2520Win64/Personal%2520Builds/mingw-builds/5.3.0/threads-posix/seh/)，选择32位版本安装，下载i686-posix-dwarf / i686-posix-sjlj  [MinGW-w64 - for 32 and 64 bit Windows](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/5.3.0/threads-posix/seh/)
* 下载安装CMake，[CMake下载地址](https://cmake.org/download/)，务必安装在不带中文路径的目录下  



>  * 操作系统接口协议:这个世界上只有两种操作系统，符合 posix 协议的，和 Windows 。如这个笑话所说的，如果你想要开发 Windows 程序，需要选择 win32 ，而开发 Linux、Unix、Mac OS 等其他操作系统下的程序，则需要选择 posix 。  
> * 异常处理模型（64位）:异常处理在开发中非常重要，你在开发的过程中，大部分的时间会耗在处理各种异常情况上。如果你之前选择了 64位，则这里有两个异常处理模型供你选择，seh 是新发明的，而 sjlj 则是古老的。seh 性能比较好，但不支持 32位。 sjlj 稳定性好，支持 32位  
> * 异常处理模型（32位）:选择了 32位 后，则可以用 dwarf 和 sjlj 两种异常处理模型。同样的，dwarf 的性能要优于 sjlj ，它不支持 64位 。  


### CLion配置NDK开发环境
* 配置Toolchains选项
1. 在默认的`MinGW(default)`先新建Toolchain,
2. `Name:` -> `Android`
3. `Environment` -> `MinGW` 选择安装MinGW的位置 `D:\Program Files (x86)\mingw-w64\i686-4.9.0-posix-dwarf-rt_v3-rev1\mingw32`
4. `CMake:` 选择`Android Sdk`目录中的CMake，位置为`Sdk\ndk\<version>\prebuilt\windows-x86_64\bin\make.exe`
5. `Make:` -> `Sdk\ndk\<version>\prebuilt\windows-x86_64\bin\make.exe`  
6. `C Compiler:` -> `Sdk\ndk\20.1.5948944\toolchains\llvm\prebuilt\windows-x86_64\bin\clang.exe`
7. `C++ Compiler:` -> `Sdk\ndk\20.1.5948944\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe`
8. `Debugger:` -> `Sdk\ndk\<version>\prebuilt\windows-x86_64\bin\gdb.exe`

* 配置CMake选项  
1. 菜单`Build,Execution,Deployment` -> `CMake` -> `CMake options:`中填写下列配置，CMake版本不同配置名称或有不同，参考[CMake官方文档](https://cmake.org/cmake/help/v3.12/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk)
```
-DCMAKE_TOOLCHAIN_FILE="D:\Android\Sdk\ndk\20.1.5948944\build\cmake\android.toolchain.cmake"
-DCMAKE_SYSTEM_NAME=Android
-DANDROID_ABI="armeabi-v7a"
-DCMAKE_ANDROID_NDK="D:\Android\Sdk\ndk\20.1.5948944"
-DCMAKE_SYSTEM_VERSION=16
-DCMAKE_C_FLAGS=""
-DCMAKE_CXX_FLAGS=""
-DCMAKE_ANDROID_NDK_TOOLCHAIN_VERSION=clang
```
2. `Name:`按个人喜好填写，此处配置为`Debug-Android`
3. `Build type:`按照是否版本选择`Debug`或者`Release`
4. `Toolchain:`选择`Toolchans`菜单中新增的那项`Android`












