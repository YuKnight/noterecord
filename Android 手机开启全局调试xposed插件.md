### [Android 手机开启全局调试xposed插件](https://blog.csdn.net/spinchao/article/details/105419425)

* 手机开启全局调试ro.debuggable = 1 一般方法就是重刷boot.img ，大部分手机都比较困难。
还有就是命令临时修改，重启手机失效的。
还有magisk 刷的
今天给介绍一个xposed插件来实现 手机的全局调试

原理，反正是frame java层，管他什么hook就行。
再Zygote fork进程之前hook 修改runtimeFlags ，打开全局调试就可以。具体hook点查找思路，后续整理下发出来。

先说下，hook点为 frameworks/base/core/java/android/os/Process.java 的start方法，第五个参数处理下即可。
```java
public static final ProcessStartResult start(final String processClass,
                                  final String niceName,
                                  int uid, int gid, int[] gids,
                                  int runtimeFlags, int mountExternal,
                                  int targetSdkVersion,
                                  String seInfo,
                                  String abi,
                                  String instructionSet,
                                  String appDataDir,
                                  String invokeWith,
                                  String[] zygoteArgs) {
        return zygoteProcess.start(processClass, niceName, uid, gid, gids,
                    runtimeFlags, mountExternal, targetSdkVersion, seInfo,
                    abi, instructionSet, appDataDir, invokeWith, zygoteArgs);
    }
```
修改flag，打开当前进程的调试。
```java
if ((runtimeFlags & 1) == 0) {
            // 增加开启Android调试选项的标志
            flags |= 1;
        }
```

Xposed代码：
```java
package com.spc.xdebug;

import android.util.Log;
import android.os.Process;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.IXposedHookZygoteInit;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public class XDebugable implements IXposedHookLoadPackage, IXposedHookZygoteInit {

    private static final int DEBUG_ENABLE_DEBUGGER = 0x1;

    private XC_MethodHook debugAppsHook = new XC_MethodHook() {
        @Override
        protected void beforeHookedMethod(MethodHookParam param)
                throws Throwable {

            XposedBridge.log("-- beforeHookedMethod :" + param.args[1]);

            int id = 5;
            int flags = (Integer) param.args[id];
            // 修改类android.os.Process的start函数的第6个传入参数
            if ((flags & DEBUG_ENABLE_DEBUGGER) == 0) {
                // 增加开启Android调试选项的标志
                flags |= DEBUG_ENABLE_DEBUGGER;
            }
            param.args[id] = flags;

            if (BuildConfig.DEBUG) {
                XposedBridge.log("-- app debugable flags to 1 :" + param.args[1]);
            }
        }
    };

    @Override
    public void handleLoadPackage(final XC_LoadPackage.LoadPackageParam loadPackageParam) throws Throwable {

    }

    // 实现的接口IXposedHookZygoteInit的函数
    @Override
    public void initZygote(final IXposedHookZygoteInit.StartupParam startupParam) throws Throwable {

        // /frameworks/base/core/java/android/os/Process.java
        // Hook类android.os.Process的start函数
        Log.e("hook ", "initZygote");
        XposedBridge.hookAllMethods(Process.class, "start", debugAppsHook);
    }
}
```
注册下此类为xposed模块入口就可以了。









