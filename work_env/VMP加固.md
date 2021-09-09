

# 虚拟机用户密码跟超级管理员密码都是用户名

# 环境依赖
1. android-ndk-r12b-linux-x86_64.zip
2. jdk-8u11-linux-x64.tar.gz
3. 路径：/mis/android/
    1. reinforce目录是一期加固
    2. reinforce2是动态加载和抽取
    3. reinforce4是vmp的某一个老版本，针对dex的，不是最新版。调用方式见目录中的README.md。目录中包含一个隐藏目录`.resource`，`libxvmp.so`和`libcapstone.so`
    4. 最新的VMP位于：`/home/muge/桌面/temp/VMP/LASTVMP`
        1. VMP编译出的so位于：VMP/bin/resource 目录下
        2. 调用接口：`LASTVMP/VMP/VMP/src/kendy/VmpControl.java`
        3. ndk编译命令(`history | grep ndk-build`)：`export PATH=$PATH:/mis/android/reinforce4/android-ndk-r12b/ndk-build` `ndk-build APP_ABI=all`
4. 命令行调用方式为：接口调用为：`VMP/src/kendy/vmp/VmpControl/reInforce`



```
// https://www.cnblogs.com/williamjie/p/10649121.html
由于jdk的版本问题导致在windows上编译打包好的jar包放在linux服务器上运行的时候出现一点小异常，所以决定在linux上进行一次项目编译，这有两个选择
1.在相同的linux环境下安装linux版的eclipse 进行编译
2.在linux用javac命令行进行编译
3.用maven,ant等项目管理工具
经试验，使用方法1确实解决了我遇到的问题，但是太麻烦。
这里记录一下第二种方法，第三种方法。。我也不会使用。

目录结构是这样的：
├── lib
└── src
    ├── com
    │   └── xxx
    └── org
        └── json

lib下面有依赖的库
src下面是源文件

用javac编译的步骤：
1.先找出所有需要编译的java文件并保存到文件列表到javaFiles.txt
find src -name \*.java >javaFiles.txt
2.使用javac进行编译，因为源代码依赖lib里面的库，所以需要指定classpath参数
javac -d bin -cp .:./lib/*  @.javaFiles.txt
-d指定输出目录  -cp指定classpath为当前目录和lib目录下面所有的库文件   @后面指定需要编译的文件列表

3.使用jar进行打包
先进入class文件的目录
cd bin
jar -cp  xxx.jar  com  org   这样就把class文件打包成jar包了
```


# 编译方式
1. C/C++代码使用ndk进行编译
2. java代码直接使用java命令行编译成class之后打包即可，即可以不用依赖于eclipse。



# VMP 目录结构分析
1. `VMP/vmp/jni`为`libxvmp.so`的源码。
2. `VMP/native`为`libAntiHelp.so`的源码。
3. `VMP/src`为最终编译出jar的源码
4. `VMP/libs`为依赖的java依赖库，其中`VMP/libs/kendy-commons.jar`可能是自己编写的库文件，没有找到相应源码。
5. `bin/resource`目录下的`libs`目录中存放经过源码编译出来的各个架构的so文件，`linux` `mac` `windows`分别为各个操作系统下需要用到的工具(`aapt`和`upx`)和库(`capstone`版本可能为`capstone-4.0.2-win64`)，其中`upx`只能在`mac`和`linux`下使用。


https://vault.centos.org/7.7.1908/isos/x86_64/
https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html


[centos7老版本镜像官方下载地址](http://vault.centos.org/)
[CentOS-7-x86_64-DVD-1908.iso](https://vault.centos.org/7.7.1908/isos/x86_64/)
# centos VMware安装
1. `[CentOS-7-x86_64-DVD-1908.iso](https://vault.centos.org/7.7.1908/isos/x86_64/CentOS-7-x86_64-DVD-1908.iso)` SHA256: `9BBA3DA2876CB9FCF6C28FB636BCBD01832FE6D84CD7445FA58E44E569B3B4FE`，可能是 7.7.1908 版本，http://mirrors.sohu.com/centos/7.7.1908/isos/x86_64/
2. VMware中`文件` -> `新建虚拟机(N)...` 
3. 选择`自定义(高级)(C)`
4. 硬件兼容性默认即可(`Workstation 15.x` 即直接点击下一步)。
5. 选择系统镜像文件路径
6. 输入虚拟机名称`VMPDeploy`，选择虚拟机存放位置路径`F:\jiaguVM\VMPDeploy`
7. 选择处理器数量: 1 ，每个处理器的内核数量: 2。
8. 内存分配4G(4096)
9. `网络连接`选择默认配置即可(`使用网络地址转换(NAT)(E)`)。
10. `I/O控制器类型`选择默认配置即可(`SCSI控制器:`->`LSI Logic(L) 推荐`)。
11. `虚拟磁盘类型`选择默认配置即可(`SCSI(S) (推荐)`)。
12. `磁盘`选择默认即可(`创建新虚拟磁盘(V)`)。
13. 磁盘大小设置为`120.0`，即120G，可以根据自己需要设置磁盘最大大小。`将虚拟磁盘拆分成多个文件(M)`默认选项选这个，不用改。
14. `磁盘文件(F)`默认即可(`VMPDeploy.vmdk`)。
15. `创建后开启此虚拟机(P)`默认是勾选的。点击完成。
16. 等待VMward处理完成后进入系统配置界面

# centos安装配置 [VMware安装Centos7桌面版超详细图文过程](https://blog.csdn.net/qq_39722988/article/details/90548280)
1. 进入界面，语言选择`English` `English(United States)`，**建议选择英文，有些IDE出现中文符号会有问题**。
2. 点击`SOFTWARE`下面`SOFTWARE SELECTION`中`Base Environment`选`GNOME Desktop`，`Add-Ons for Selected Environment`中勾选`Legacy X Window System Compatibility`
3. 点击`SYSTEM`下面`INSTALLATION DESTINATION`选项。进入后直接点击`Done`返回即可进行安装。
4. `Begain Installation`
5. `ROOT PASSWORD`中`Root Passowrd:` 321 `Confirm:` 321
6. `USER CREATION`中`Create USER` `User name:Nesun` `Password:321`  `Confirm password:321`  默认勾选`Require a password to use this account`
7. 等待安装完成`Reboot`








[JDK8各版本下载](https://www.oracle.com/cn/java/technologies/javase/javase8-archive-downloads.html)

# 安装JDK
## tar.gz安装
[Centos7安装JDK(tar.gz版)](https://blog.csdn.net/qq_31484941/article/details/78987085)

1. 查找需要卸载的OpenJDK:
```sh
[root@localhost /]# rpm -qa | grep java
javapackages-tools-3.4.1-6.el7_0.noarch
python-javapackages-3.4.1-6.el7_0.noarch
java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64
tzdata-java-2015a-1.el7.noarch
java-1.7.0-openjdk-headless-1.7.0.75-2.5.4.2.el7_0.x86_64
```

```sh
[Nesun@localhost tools]$ rpm -qa | grep java
java-1.8.0-openjdk-headless-1.8.0.222.b03-1.el7.x86_64
java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64
tzdata-java-2019b-1.el7.noarch
java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
python-javapackages-3.4.1-11.el7.noarch
javapackages-tools-3.4.1-11.el7.noarch
java-1.8.0-openjdk-1.8.0.222.b03-1.el7.x86_64
[Nesun@localhost tools]$ java -version
openjdk version "1.8.0_222-ea"
OpenJDK Runtime Environment (build 1.8.0_222-ea-b03)
OpenJDK 64-Bit Server VM (build 25.222-b03, mixed mode)

[Nesun@localhost tools]$ su
Password: 
[root@localhost tools]# rpm -qa | grep java
java-1.8.0-openjdk-headless-1.8.0.222.b03-1.el7.x86_64
java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64
tzdata-java-2019b-1.el7.noarch
java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
python-javapackages-3.4.1-11.el7.noarch
[root@localhost tools]# rpm -e --nodeps java-1.8.0-openjdk-headless-1.8.0.222.b03-1.el7.x86_64
[root@localhost tools]# rpm -e --nodeps java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64
[root@localhost tools]# rpm -e --nodeps tzdata-java-2019b-1.el7.noarch
[root@localhost tools]# rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
[root@localhost tools]# rpm -e --nodeps python-javapackages-3.4.1-11.el7.noarch
[root@localhost tools]# 
```

2. 依次卸载
`rpm -e --nodeps javapackages-tools-3.4.1-6.el7_0.noarch`
`rpm -e --nodeps python-javapackages-3.4.1-6.el7_0.noarch`
`rpm -e --nodeps java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64`
`rpm -e --nodeps tzdata-java-2015a-1.el7.noarch`
`rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.75-2.5.4.2.el7_0.x86_64`

3. 查看是否已删除干净：
`rpm -qa | grep java`

4. 将JDK安装包 jdk-7u79-linux-x64.tar.gz 上传到 /usr/local/java 下解压：
`tar -zxvf jdk-7u75-linux-x64.tar.gz`
`tar -zxvf jdk-7u75-linux-x64.tar.gz -C /usr/local/java`

5. 配置JDK, 编辑 /etc/profile 文件，尾部添加如下 
```sh
export JAVA_HOME=/usr/local/jdk1.7.0_79
export JRE_HOME=/$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
```


```sh
export JAVA_HOME=/root/java/jdk1.8.0_241      （路径和版本不能错，要和自己的一致）
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

6. 重新加载/etc/profile：
`source /etc/profile`

7. 检查JDK是否安装成功：
`java -version`



## rmp安装
`rpm -ivh /usr/java/jdk-8u112-linux-x64.rpm`






`win7 旗舰版SP1`下`VMware 15.0.0 build-10134415`(`VMware-workstation-full-15.0.0-10134415`)安装`centos 7.7.1908`


# 关闭防火墙
重启网络：`service network restart`
若本机使用xshell工具连接centos7，还要关闭防火墙，命令如下:
`systemctl stop firewalld  # 临时关闭防火墙`
`systemctl disable firewalld  # 禁止防火墙开机启动`
查看防火墙状态:
```sh
[root@localhost knight]# firewall-cmd --state
not running
[root@localhost knight]# service firewalld status
Redirecting to /bin/systemctl status firewalld.service
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since 二 2021-09-07 19:56:44 CST; 15min ago
     Docs: man:firewalld(1)
  Process: 887 ExecStart=/usr/sbin/firewalld --nofork --nopid $FIREWALLD_ARGS (code=exited, status=0/SUCCESS)
 Main PID: 887 (code=exited, status=0/SUCCESS)

9月 08 02:36:00 localhost.localdomain systemd[1]: Starting firewalld - dynamic fir....
9月 08 02:36:05 localhost.localdomain systemd[1]: Started firewalld - dynamic fire....
9月 07 19:56:43 localhost.localdomain systemd[1]: Stopping firewalld - dynamic fir....
9月 07 19:56:44 localhost.localdomain systemd[1]: Stopped firewalld - dynamic fire....
Hint: Some lines were ellipsized, use -l to show in full.
[root@localhost knight]# systemctl status firewalld.service
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since 二 2021-09-07 19:56:44 CST; 15min ago
     Docs: man:firewalld(1)
  Process: 887 ExecStart=/usr/sbin/firewalld --nofork --nopid $FIREWALLD_ARGS (code=exited, status=0/SUCCESS)
 Main PID: 887 (code=exited, status=0/SUCCESS)

9月 08 02:36:00 localhost.localdomain systemd[1]: Starting firewalld - dynamic fir....
9月 08 02:36:05 localhost.localdomain systemd[1]: Started firewalld - dynamic fire....
9月 07 19:56:43 localhost.localdomain systemd[1]: Stopping firewalld - dynamic fir....
9月 07 19:56:44 localhost.localdomain systemd[1]: Stopped firewalld - dynamic fire....
Hint: Some lines were ellipsized, use -l to show in full.
[root@localhost knight]# 
```




# 配置网络
```sh
[knight@localhost ~]$ su
密码：
[root@localhost knight]# ls -al /etc/sysconfig/network-scripts/
总用量 260
drwxr-xr-x. 2 root root  4096 9月   8 2021 .
drwxr-xr-x. 6 root root  4096 9月   8 2021 ..
-rw-r--r--. 1 root root   279 9月   8 2021 ifcfg-ens33
-rw-r--r--. 1 root root   254 3月  29 2019 ifcfg-lo
lrwxrwxrwx. 1 root root    24 9月   8 2021 ifdown -> ../../../usr/sbin/ifdown
-rwxr-xr-x. 1 root root   654 3月  29 2019 ifdown-bnep
-rwxr-xr-x. 1 root root  6532 3月  29 2019 ifdown-eth
-rwxr-xr-x. 1 root root  6190 8月   9 2019 ifdown-ib
-rwxr-xr-x. 1 root root   781 3月  29 2019 ifdown-ippp
-rwxr-xr-x. 1 root root  4540 3月  29 2019 ifdown-ipv6
lrwxrwxrwx. 1 root root    11 9月   8 2021 ifdown-isdn -> ifdown-ippp
-rwxr-xr-x. 1 root root  2130 3月  29 2019 ifdown-post
-rwxr-xr-x. 1 root root  1068 3月  29 2019 ifdown-ppp
-rwxr-xr-x. 1 root root   870 3月  29 2019 ifdown-routes
-rwxr-xr-x. 1 root root  1456 3月  29 2019 ifdown-sit
-rwxr-xr-x. 1 root root  1621 3月  18 2017 ifdown-Team
-rwxr-xr-x. 1 root root  1556 3月  18 2017 ifdown-TeamPort
-rwxr-xr-x. 1 root root  1462 3月  29 2019 ifdown-tunnel
lrwxrwxrwx. 1 root root    22 9月   8 2021 ifup -> ../../../usr/sbin/ifup
-rwxr-xr-x. 1 root root 12415 3月  29 2019 ifup-aliases
-rwxr-xr-x. 1 root root   910 3月  29 2019 ifup-bnep
-rwxr-xr-x. 1 root root 13475 3月  29 2019 ifup-eth
-rwxr-xr-x. 1 root root 10114 8月   9 2019 ifup-ib
-rwxr-xr-x. 1 root root 12075 3月  29 2019 ifup-ippp
-rwxr-xr-x. 1 root root 11893 3月  29 2019 ifup-ipv6
lrwxrwxrwx. 1 root root     9 9月   8 2021 ifup-isdn -> ifup-ippp
-rwxr-xr-x. 1 root root   650 3月  29 2019 ifup-plip
-rwxr-xr-x. 1 root root  1064 3月  29 2019 ifup-plusb
-rwxr-xr-x. 1 root root  4997 3月  29 2019 ifup-post
-rwxr-xr-x. 1 root root  4154 3月  29 2019 ifup-ppp
-rwxr-xr-x. 1 root root  2001 3月  29 2019 ifup-routes
-rwxr-xr-x. 1 root root  3303 3月  29 2019 ifup-sit
-rwxr-xr-x. 1 root root  1755 3月  18 2017 ifup-Team
-rwxr-xr-x. 1 root root  1876 3月  18 2017 ifup-TeamPort
-rwxr-xr-x. 1 root root  2711 3月  29 2019 ifup-tunnel
-rwxr-xr-x. 1 root root  1836 3月  29 2019 ifup-wireless
-rwxr-xr-x. 1 root root  5419 3月  29 2019 init.ipv6-global
-rw-r--r--. 1 root root 20671 3月  29 2019 network-functions
-rw-r--r--. 1 root root 31027 3月  29 2019 network-functions-ipv6
[root@localhost knight]# ls /etc/sysconfig/network-scripts/
ifcfg-ens33  ifdown-isdn      ifup          ifup-plip      ifup-tunnel
ifcfg-lo     ifdown-post      ifup-aliases  ifup-plusb     ifup-wireless
ifdown       ifdown-ppp       ifup-bnep     ifup-post      init.ipv6-global
ifdown-bnep  ifdown-routes    ifup-eth      ifup-ppp       network-functions
ifdown-eth   ifdown-sit       ifup-ib       ifup-routes    network-functions-ipv6
ifdown-ib    ifdown-Team      ifup-ippp     ifup-sit
ifdown-ippp  ifdown-TeamPort  ifup-ipv6     ifup-Team
ifdown-ipv6  ifdown-tunnel    ifup-isdn     ifup-TeamPort
[root@localhost knight]# ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::34a3:3c18:203b:1e88  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:78:bd:41  txqueuelen 1000  (Ethernet)
        RX packets 936  bytes 65282 (63.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 203  bytes 19765 (19.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 496  bytes 43088 (42.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 496  bytes 43088 (42.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:7b:7c:a0  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[root@localhost knight]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:78:bd:41 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::34a3:3c18:203b:1e88/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever
4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
    link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
[root@localhost knight]# ls /etc/sysconfig/network-scripts/
ifcfg-ens33  ifdown-isdn      ifup          ifup-plip      ifup-tunnel
ifcfg-lo     ifdown-post      ifup-aliases  ifup-plusb     ifup-wireless
ifdown       ifdown-ppp       ifup-bnep     ifup-post      init.ipv6-global
ifdown-bnep  ifdown-routes    ifup-eth      ifup-ppp       network-functions
ifdown-eth   ifdown-sit       ifup-ib       ifup-routes    network-functions-ipv6
ifdown-ib    ifdown-Team      ifup-ippp     ifup-sit
ifdown-ippp  ifdown-TeamPort  ifup-ipv6     ifup-Team
ifdown-ipv6  ifdown-tunnel    ifup-isdn     ifup-TeamPort
[root@localhost knight]# vi /etc/sysconfig/network-scripts/ifcfg-ens33 
[root@localhost knight]# systemctl restart network
[root@localhost knight]# ping www.baidu.com
PING www.a.shifen.com (220.181.38.149) 56(84) bytes of data.
^C
--- www.a.shifen.com ping statistics ---
8 packets transmitted, 0 received, 100% packet loss, time 6999ms

[root@localhost knight]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:78:bd:41 brd ff:ff:ff:ff:ff:ff
    inet 192.168.80.142/24 brd 192.168.80.255 scope global noprefixroute dynamic ens33
       valid_lft 1782sec preferred_lft 1782sec
    inet6 fe80::34a3:3c18:203b:1e88/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever
4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
    link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
[root@localhost knight]# ping 192.168.51.206
PING 192.168.51.206 (192.168.51.206) 56(84) bytes of data.
64 bytes from 192.168.51.206: icmp_seq=1 ttl=128 time=0.609 ms
64 bytes from 192.168.51.206: icmp_seq=2 ttl=128 time=1.08 ms
64 bytes from 192.168.51.206: icmp_seq=3 ttl=128 time=1.07 ms
64 bytes from 192.168.51.206: icmp_seq=4 ttl=128 time=1.27 ms
^C
--- 192.168.51.206 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 0.609/1.013/1.277/0.248 ms
[root@localhost knight]# 
[root@localhost knight]# vi /etc/sysconfig/network-scripts/ifcfg-ens33 
[root@localhost knight]# 
[root@localhost knight]# systemctl restart network
[root@localhost knight]# 
[root@localhost knight]# vi /etc/sysconfig/network-scripts/ifcfg-ens33 
[root@localhost knight]# 
[root@localhost knight]# systemctl restart network
[root@localhost knight]# 
```
其中，需要把`/etc/sysconfig/network-scripts/ifcfg-ens33`中`ONBOOT=no`修改为`ONBOOT=yes`，重启服务`systemctl restart network`即可让firefox联网。

1. 使用ip addr查看当前的ip地址（命令ifconfig查看也可）
    ```sh
    [root@localhost knight]# ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
        valid_lft forever preferred_lft forever
    2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 00:0c:29:78:bd:41 brd ff:ff:ff:ff:ff:ff
        inet6 fe80::34a3:3c18:203b:1e88/64 scope link noprefixroute 
        valid_lft forever preferred_lft forever
    3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
        link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
        inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
        valid_lft forever preferred_lft forever
    4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
        link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
    [root@localhost knight]# ifconfig
    ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet6 fe80::34a3:3c18:203b:1e88  prefixlen 64  scopeid 0x20<link>
            ether 00:0c:29:78:bd:41  txqueuelen 1000  (Ethernet)
            RX packets 936  bytes 65282 (63.7 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 203  bytes 19765 (19.3 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 496  bytes 43088 (42.0 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 496  bytes 43088 (42.0 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
            inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
            ether 52:54:00:7b:7c:a0  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    ```
    可知网卡ens33并没有相应的inet属性即没有IP地址，也就无法通过IP地址连接虚拟机。  
    centos获取IP地址的方式有两种：一是动态获取IP，二是设置静态IP


2. 使用命令ls /etc/sysconfig/network-scripts/查看ens33对应的文件名
    ```sh
    [root@localhost knight]# ls /etc/sysconfig/network-scripts/
    ifcfg-ens33  ifdown-isdn      ifup          ifup-plip      ifup-tunnel
    ifcfg-lo     ifdown-post      ifup-aliases  ifup-plusb     ifup-wireless
    ifdown       ifdown-ppp       ifup-bnep     ifup-post      init.ipv6-global
    ifdown-bnep  ifdown-routes    ifup-eth      ifup-ppp       network-functions
    ifdown-eth   ifdown-sit       ifup-ib       ifup-routes    network-functions-ipv6
    ifdown-ib    ifdown-Team      ifup-ippp     ifup-sit
    ifdown-ippp  ifdown-TeamPort  ifup-ipv6     ifup-Team
    ifdown-ipv6  ifdown-tunnel    ifup-isdn     ifup-TeamPort
    ```
3. 使用命令`vi /etc/sysconfig/network-scripts/ifcfg-ens33`打开并编辑文件内容（按下字母i进入编辑状态，按下esc退回到查看状态，按下:wq保存并退出文件内容回到命令行）
    > 从上图可知，centos7 默认是使用动态获取IP的方式且是不启动网卡的（BOOTPROTO=dhcp，ONBOOT=no），若要配置动态IP则只需将ONBOOT=no更改为ONBOOT=yes后重启网络即可；
    若要设置静态IP则需将BOOTPROTO=dhcp，ONBOOT=no更改为BOOTPROTO=static，ONBOOT=yes，并在后面添加上要设置的静态IP地址及DNS地址：
    IPADDR=静态IP地址
    NETMASK=255.255.255.0
    GATEWAY=IP地址所在网关地址
    DNS1=119.29.29.29
    DNS2=8.8.8.8（其中DNS1和DNS2都是网上找的免费DNS服务器）

4. 使用命令`systemctl restart network`重启网络
5. 检查是否设置成功
    ```sh
    [root@localhost knight]# ifconfig
    ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.80.142  netmask 255.255.255.0  broadcast 192.168.80.255
            inet6 fe80::34a3:3c18:203b:1e88  prefixlen 64  scopeid 0x20<link>
            ether 00:0c:29:78:bd:41  txqueuelen 1000  (Ethernet)
            RX packets 9459  bytes 8596664 (8.1 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 5316  bytes 672628 (656.8 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 1408  bytes 124848 (121.9 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 1408  bytes 124848 (121.9 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
            inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
            ether 52:54:00:7b:7c:a0  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    [root@localhost knight]# 
    [root@localhost knight]# ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
        valid_lft forever preferred_lft forever
    2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 00:0c:29:78:bd:41 brd ff:ff:ff:ff:ff:ff
        inet 192.168.80.142/24 brd 192.168.80.255 scope global noprefixroute dynamic ens33
        valid_lft 1282sec preferred_lft 1282sec
        inet6 fe80::34a3:3c18:203b:1e88/64 scope link noprefixroute 
        valid_lft forever preferred_lft forever
    3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
        link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
        inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
        valid_lft forever preferred_lft forever
    4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
        link/ether 52:54:00:7b:7c:a0 brd ff:ff:ff:ff:ff:ff
    [root@localhost knight]# 
    ```



使用命令rpm -aq | grep kernel-headers查看kernel-headers是否安装成功
使用命令rpm -ql kernel-headers-3.10.0-957.21.2.el7.x86_64|less查看安装目录，因安装目录太多故后面加less方便翻页查看







# 如果虚拟机里面有网络问题，可以尝试还原默认设置，（使用NAT-DHCP模式）`编辑(E)` -> `虚拟网络编辑器(N)...` -> `更改设置` -> `还原默认设置`。还原之后进入虚拟机，编辑`/etc/sysconfig/network-scripts/ifcfg-ens33` 还原设置，并修改`ONBOOT=no` 为 `ONBOOT=yes`即可

```sh
[root@localhost knight]# cat /etc/sysconfig/network-scripts/ifcfg-ens33 
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=cd0e95c2-9efa-4283-ae59-e2c95b229cc7
DEVICE=ens33
ONBOOT=yes
[root@localhost knight]# 
```


# 另一个原因[CentOS 7 在vmware中的网络设置详细介绍](https://www.jb51.net/article/98641.htm) 没有在`/etc/resolv.conf`添加配置导致????



安装编译环境:`yum -y install perl gcc gcc-c++ make cmake kernel kernel-headers kernel-devel net-tools`以避免后期网络问题









# 安装JDK[CentOS 7 安装 JAVA环境（JDK 1.8）](https://www.cnblogs.com/stulzq/p/9286878.html)  

## JDK下载
1. 打开url选择jdk1.8下载：http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
2. wget下载：`wget http://download.oracle.com/otn-pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz?AuthParam=1531155951_4e06a4d17c6c1dbfb8440352e19dd2ae`
3. 下载以后通过命令检查安装包大小是否符合
```sh
[root@localhost knight]# ls -lht /mnt/share/deploytools/jdk-8u121-linux-x64.tar.gz 
-rwxrwxrwx. 1 root root 175M 9月   1 16:57 /mnt/share/deploytools/jdk-8u121-linux-x64.tar.gz
```

## [查找需要卸载的OpenJDK](https://blog.csdn.net/qq_31484941/article/details/78987085)  

```sh
[root@localhost knight]# rpm -qa | grep java
tzdata-java-2019b-1.el7.noarch
python-javapackages-3.4.1-11.el7.noarch
javapackages-tools-3.4.1-11.el7.noarch
java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64
java-1.8.0-openjdk-1.8.0.222.b03-1.el7.x86_64
java-1.8.0-openjdk-headless-1.8.0.222.b03-1.el7.x86_64
java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
[root@localhost knight]# rpm -e --nodeps tzdata-java-2019b-1.el7.noarch
[root@localhost knight]# rpm -e --nodeps python-javapackages-3.4.1-11.el7.noarch
[root@localhost knight]# rpm -e --nodeps javapackages-tools-3.4.1-11.el7.noarch
[root@localhost knight]# rpm -ql java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64 # 查看安装目录，便于后续选择java安装目录
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/bin/policytool
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/lib/amd64/libjavagtk.so
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/lib/amd64/libjsoundalsa.so
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/lib/amd64/libpulse-java.so
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/lib/amd64/libsplashscreen.so
/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64/jre/lib/amd64/xawt/libmawt.so
/usr/share/applications/java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64-policytool.desktop
/usr/share/icons/hicolor/16x16/apps/java-1.7.0.png
/usr/share/icons/hicolor/24x24/apps/java-1.7.0.png
/usr/share/icons/hicolor/32x32/apps/java-1.7.0.png
/usr/share/icons/hicolor/48x48/apps/java-1.7.0.png
/usr/share/man/man1/policytool-java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64.1.gz
[root@localhost knight]# rpm -e --nodeps java-1.7.0-openjdk-1.7.0.221-2.6.18.1.el7.x86_64
[root@localhost knight]# rpm -e --nodeps java-1.8.0-openjdk-1.8.0.222.b03-1.el7.x86_64
[root@localhost knight]# rpm -e --nodeps java-1.8.0-openjdk-headless-1.8.0.222.b03-1.el7.x86_64
[root@localhost knight]# rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
[root@localhost knight]# rpm -qa | grep java # 确认是否删除干净
[root@localhost knight]# 
[root@localhost knight]# 

```



## 安装
1. 创建安装目录`mkdir /usr/local/java/`
    ```sh
    [root@localhost knight]# ls -al /usr/local/java
    ls: 无法访问/usr/local/java: 没有那个文件或目录
    ```
1. 解压至安装目录`tar -zxvf jdk-8u171-linux-x64.tar.gz -C /usr/local/java/`
## 设置环境变量
1. 打开文件`vim /etc/profile`
在末尾添加
    ```
    export JAVA_HOME=/usr/local/java/jdk1.8.0_171
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
    export PATH=${JAVA_HOME}/bin:$PATH
    ```
2. 使环境变量生效`source /etc/profile`
3. 添加软链接`ln -s /usr/local/java/jdk1.8.0_171/bin/java /usr/bin/java`
4. 检查`java -version`



```sh
[root@localhost knight]# ls -al /usr/local/java
ls: 无法访问/usr/local/java: 没有那个文件或目录
[root@localhost knight]# mkdir /usr/local/java
[root@localhost knight]# tar -zxvf /mnt/share/deploytools/jdk-8u121-linux-x64.tar.gz -C /usr/local/java/
```

编辑`vi /etc/profile`并在文件末尾添加
```sh
export JAVA_HOME=/usr/local/java/jdk1.8.0_121
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:${JAVA_HOME}/jre/lib/rt.jar
export PATH=$PATH:$JAVA_HOME/bin
```
使环境变量生效`source /etc/profile`
```sh
[root@localhost knight]# source /etc/profile
[root@localhost knight]# java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
[root@localhost knight]# javac -version
javac 1.8.0_121
[root@localhost knight]# 
```













# 编译so ndk版本为：android-ndk-r12b-linux-x86_64.zip 
1. 配置好NDK环境后，进入目录`cd VMP/native/`进行编译`ndk-build APP_ABI=armeabi,armeabi-v7a,arm64-v8a`
2. `cd VMP/vmp/`进行编译`ndk-build`





使用最新版的eclipse编译，选择jdk8进行编译，
`Window` -> `Preferences` -> `Installed JREs` -> `Add` 选择JDK安装的路径`/usr/local/java/jdk1.8.0_121`
右键项目`Properties` -> `Java Compiler` -> `Complier compliance level` 选择`1.8`
[Eclipse IDE for Java Developers - Linux ](https://mirrors.tuna.tsinghua.edu.cn/eclipse/technology/epp/downloads/release/2021-06/R/eclipse-java-2021-06-R-linux-gtk-x86_64.tar.gz)  
[Eclipse IDE for Java Developers - Windows ](https://mirrors.tuna.tsinghua.edu.cn/eclipse/technology/epp/downloads/release/2021-06/R/eclipse-java-2021-06-R-win32-x86_64.zip)  









