
### gdbserver和gdb所在位置：  
* gdbserver  
    Android\Sdk\ndk\20.1.5948944\prebuilt\android-arm\gdbserver\gdbserver  
* gdb   
    Android\Sdk\ndk\20.1.5948944\prebuilt\windows-x86_64\bin\gdb.exe  
### 调试步骤 
1. 把gadbserver推入到手机中  
    `adb push Android\Sdk\ndk\20.1.5948944\prebuilt\android-arm\gdbserver\gdbserver /data/local/tmp`  

2. 给予gdbserver执行权限
    ```sh
    root@hammerhead:/data/local/tmp # chmod 777 gdbserver
    ```
3. 打开待调试app, 查找待调试app的 `pid`
    * 查找包名
        ```sh
        root@hammerhead:/data/local/tmp # dumpsys activity activities |grep mFo
        ```
        或者
        ```sh
        root@hammerhead:/data/local/tmp # dumpsys activity top | grep TASK
        ```
    * 获取进程`pid`
        ```sh
        root@hammerhead:/data/local/tmp # ps|grep com.game.XXX
        u0_a409   30704 324   1260456 218392 sys_epoll_ b6d1a894 S com.game.XXX
        u0_a409   31208 324   953548 94176 sys_epoll_ b6d1a894 S com.game.XXX:pushcore
        ```


4. root权限使用gdbserver挂接，其中12345为调试端口号，需要进行转发到pc中，30704即为待调试app的pid
    ```sh
    root@hammerhead:/data/local/tmp # ./gdbserver :12345 --attach 30704
    ```

即以上步骤为
```sh
root@hammerhead:/data/local/tmp # chmod 777 gdbserver
root@hammerhead:/data/local/tmp # dumpsys activity activities |grep mFo
root@hammerhead:/data/local/tmp # dumpsys activity top | grep TASK
root@hammerhead:/data/local/tmp # ps|grep com.game.XXX
u0_a409   30704 324   1260456 218392 sys_epoll_ b6d1a894 S com.game.XXX
u0_a409   31208 324   953548 94176 sys_epoll_ b6d1a894 S com.game.XXX:pushcore
root@hammerhead:/data/local/tmp # ./gdbserver :1991 --attach 30704
```




5. 执行端口转发
    ```sh
    adb forward tcp:12345 tcp:12345
    ```
    `adb forward tcp:<本地机器的网络端口号> tcp:<模拟器或是真机的网络端口号>`  
    > 例: adb [-d|-e|-s ] forward tcp:6100 tcp:7100   
    > 表示把本机的6100端口号与模拟器的7100端口建立起相关，当模拟器或真机向自己的7100端口发送了数据，那们我们可以在本机的6100端口读取其发送的内容  
    查看已转发的端口 `adb forward --list`

6. 进入gdb目录中执行gdb  
`cd Android\Sdk\ndk-bundle\prebuilt\windows-x86_64\bin`  
`[Android\Sdk\ndk\20.1.5948944\prebuilt\windows-x86_64\bin]$ gdb`  

7. 挂接gdbserver  
`(gdb) target remote :12345`  
挂接完毕后可以看到读取到的so的信息
8. 让app继续运行  
`(gdb) c`  

## 相关资料 
[解决Android加固多进程ptrace反调试的思路整理](https://www.cnblogs.com/csnd/p/11800658.html)  
[GDB在线调试Android Framework Native C/C++代码](https://blog.csdn.net/songjinshi/article/details/53020629)  
[Android常见App加固厂商脱壳方法的整理](https://www.cnblogs.com/csnd/p/11800662.html)  
脱壳：  
gdb gcore法  
`.gdbserver :1234 –attach pid`  
`adb forward tcp:1234 tcp:1234`  
`.gdb`  
`(gdb) target remote :1234`  
`(gdb) gcore`  


