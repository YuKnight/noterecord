使用Android SDK 创建一个模拟器  
以下命令皆在 `Android/Sdk/emulator` 目录下执行  

查看创建的模拟器  
`emulator -list-avds`  

启动模拟器  
`emulator -avd Nexus_4_API_18`  

以代理的方式启动  
`emulator -avd Nexus_4_API_18 -http-proxy http://192.168.51.206:8888/`  

查看相关路径 配置信息  
`emulator @Nexus_4_API_18 -verbose`  

启动  
`emulator -avd Nexus_4_API_18 -kernel kernel-qemu`  

# Charles 抓包
 1. 安装并破解  
  https://www.codetd.com/article/8057017  
 2. 在PC上面添加charles证书  
  `Help` -> `SSL Proxying` -> `Install Charles Root Certificate`  
 3. 在弹出的对话框中点击安装证书  
  勾选 `将所有证书放入下列存储`  选择 `受信任的根证书颁发机构`
 4. 代理设置  
  `Proxy` -> `Proxy Settings...` -> `Proxies` -> `Enable transparent HTTP Proxying`
 5. 手机安装charles证书  
   手机浏览器访问 chls.pro/ssl 安装证书
 6. 打开模拟器中的设置  
  `More...` -> `Mobile networks` -> `Access Point Names`
    * 修改以下设置  
      > APNs 新建  
      > Name : fd APN  
      > APN  : epc.tmobile.com  
      > Proxy: 192.168.51.206 -- charles上的ip地址  
      > Port : 8888 -- charles 的代理端口  
      > MMSC : http://mms.msg.eng.t-mobile.com/mms/wapenc
 7. 设置好后并保存， 在 APNs 选项页面选择新建的那个 `fd APN`  

#### 多级列表
- 1.1 AA
  - 1.1.1 BB
    - 1.1.1.1 CC
        - 1.1.1.1.1 DD
        - 1.1.1.1.2 EE 
    - 1.1.1.2 CCD
    - 1.1.1.3 CCE
  - 1.1.2 BBC
- 2.1 AB