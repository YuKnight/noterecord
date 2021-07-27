

## fiddler查看IP地址
打开fiddler, 快捷键Ctrl+R  或者  菜单->Rules->Customize Rules…，然后在CustomRules.js文件里Ctrl+F查找字符串：static function Main()，然后添加一行代码即可显示IP，代码如下：
```js
FiddlerObject.UI.lvSessions.AddBoundColumn("Server IP", 120, "X-HostIP");  
```
添加完成后，重启下fiddler，就可以显示出请求的服务器ip。

完整js代码如下：
```js
// The Main() function runs everytime your FiddlerScript compiles
static function Main() {
    var today: Date = new Date();
    FiddlerObject.StatusText = " CustomRules.js was loaded at: " + today;

    // Uncomment to add a "Server" column containing the response "Server" header, if present
    // UI.lvSessions.AddBoundColumn("Server", 50, "@response.server");

    // Uncomment to add a global hotkey (Win+G) that invokes the ExecAction method below...
    // UI.RegisterCustomHotkey(HotkeyModifiers.Windows, Keys.G, "screenshot"); 
    FiddlerObject.UI.lvSessions.AddBoundColumn("ServerIP",120,"X-HostIP");
}
```




## Fiddler添加查看响应时间
打开fiddler, 快捷键Ctrl+R  或者  菜单->Rules->Customize Rules…，在`class Handlers{`里面添加
```js
function BeginRequestTime(oS: Session)
{
    if (oS.Timers != null)
    {
        return oS.Timers.ClientBeginRequest.ToString();
    }
    return String.Empty;
}

public static BindUIColumn("Time Taken")
function CalcTimingCol(oS: Session){
    var sResult = String.Empty;
    if ((oS.Timers.ServerDoneResponse > oS.Timers.ClientDoneRequest))
    {
    sResult = (oS.Timers.ServerDoneResponse - oS.Timers.ClientDoneRequest).ToString();
    }
    return sResult;
}
```
添加完成后，重启下fiddler，就可以显示。



## Fiddler抓包 WebSocket 数据
### [利用fiddler抓取websockt包](https://www.cnblogs.com/jinjiangongzuoshi/p/5061892.html)  

打开Fiddler，点开菜单栏的Rules，选择Customize Rules...
这时会打开CustomRules.js文件，在class Handlers中加入以下代码
```js
static function OnWebSocketMessage(oMsg: WebSocketMessage) {
    // Log Message to the LOG tab
    FiddlerApplication.Log.LogString(oMsg.ToString());
}
```
保存后就可以在Fiddler右边栏的Log标签里，看到WebSocket的数据包。
到了这里，还有一个情况要说明，就算是有工具可以抓到WebSocket中的包，看到的也不一定是明文。这个要看传输的水是什么，如果是普通水那谁都可以分析；但如果是水银，那这个分析水的设备很可能就显示乱码了。 所以也就有同学明明使用了可以抓WebSocket包的程序，却抓出来的是乱码。那是因为别人传输的是二进制数据流（比如AMF包），而不是JSON之类的对人类可读的明文。



### [Fiddler抓包和修改WebSocket数据，支持wss](https://www.cnblogs.com/xiangyuecn/p/10618982.html)  

#### 修改WebSocket数据
在`Fiddler`界面中并未找到修改`WebSocket`数据的地方，搜索也没找到多少直接的资料信息，不过写怎么打印`WebSocket`数据日志的倒蛮多（`Fiddler 4.5`开始已没有这个必要了）。另外看到一篇`利用fiddler core api 拦截修改 websocket 数据`的。两个综合一下就大功告成了。

在`Fiddler`菜单`Rules > Customize Rules`中实现`Handlers`类的`OnWebSocketMessage`方法，此方法可以得到`WebSocket`收发的数据，而且可以修改。另：`Fildder`主界面中`FildderScript`也可以直接修改脚本代码。

`Fiddler`采用的`JScript.Net`语法，这个语法不熟？没关系，我也不熟，但对`JavaScript`和`C#`任意一个熟就行了。

`Classic ASP` 用户可能对`JScript`和它的好基友`VBScript`比较熟，这两个除了写`ASP`外，`Windows`上的`vbs` `js`脚本代码也是主力使用方向。

简单点，把`JScript`当做`IE 6`来写就ojbk了，绝对的原味，反正下面的例子里面js代码居多。参考文章结尾的测试代码，不要在意那些拼音或者缩写的奇丑变量名。
```js
class Handlers
{
	//实现此方法，拦截处理数据
	static function OnWebSocketMessage(oMsg: WebSocketMessage) {
		var arr=oMsg.PayloadAsBytes();
		var bs=Utilities.ByteArrayToString(arr);
		var txt=bytesToViewText(arr);//此文本为英文，可读的文本信息，不可读的乱码、中文都过滤掉了
		var newTxt="";
		
		//假设的修改场景，只要收发的数据中包含了 test edit: 就干它
		var edit=false;
		if(txt.indexOf("test edit:")+1){
			var nbs=bs;
			var m1=/(test edit:)(.*)/.exec(txt)||[];
			nbs=nbs.Replace(strToHex(m1[0]||""),strToHex(m1[1]+(oMsg.IsOutbound?"send":"onmessage")+" change:"+m1[2]));
			
			edit=true;
			oMsg.SetPayload(hexToBytes(nbs));
			
			newTxt=bytesToViewText(oMsg.PayloadAsBytes());
		}
		
		//并未直接提供获取SessionID的方法，应该是没有公开
		var all=oMsg.ToString();
		var m1=/#(\d+)/.exec(all)||[];
		var sessionID=m1[1]||-1;
		
		FiddlerApplication.Log.LogString(
			sessionID+":["+oMsg.ID+"]"
			+"["+(oMsg.IsOutbound?"出":"入")+"]"
			+"["+(edit?"改:"+newTxt:"")+"]"
			+txt+"\n");
	}
	
	//以下为一些功能函数
	static function bytesToViewText(arr:byte[]){
		var s="";
		for(var i=0;i<arr.length;i++){
			if(arr[i]>=32 && arr[i]<=126){
				s+=String.fromCharCode(arr[i]);
			}
		}
		return s;
	}
	static function strToHex(str:String){
		var byts=new byte[str.Length];
		for(var i=0;i<str.Length;i++){
			byts[i]=(byte)(str.charCodeAt(i));
		}
		return Utilities.ByteArrayToString(byts);
	}
	static function hexToBytes(hexString:String)
	{
		hexString = hexString.Replace(" ", "");
		var length = hexString.Length / 2;
		var hexChars = hexString.ToCharArray();
		var d = new byte[length];
		for (var i = 0; i < length; i++)
		{
			var pos = i * 2;
			d[i] = (byte)(charToByte(hexChars[pos]) << 4 | charToByte(hexChars[pos + 1]));
		}
		return d;
	}
	static function charToByte(c:String)
	{
		return "0123456789ABCDEF".indexOf(c);
	}

.......
```


### Fiddler使用特定证书解密https
[Changing Fiddler root certificate to successfully decrypt HTTPS](https://stackoverflow.com/questions/26616621/changing-fiddler-root-certificate-to-successfully-decrypt-https)  
* Is there a way to change the Fiddler's root certificate. I want it for a scenario when the client app uses certificate pinning and I have access to the keystore, whose certificate is being trusted by the client app.  

I think you're asking `"Can I change the certificate Fiddler uses for a particular site"` rather than the `root certificate`, which is used for all sites.

Yes, if you really do have the private key for the certificate, you can configure Fiddler to use it. Inside Fiddler's Rules > Customize Rules > OnBoot function, you can call either:
```js
CertMaker.StoreCert("example.com", certMyCert);
```
or
```js
CertMaker.StoreCert("example.com", "C:\\temp\\cert.pfx", "TopSecretPassword");
```
The first call requires that your X509Certificate2 variable (`certMyCert` in this case) refer to a certificate that is already installed in your computer's Certificate Manager (`certmgr.msc`), so its private key can be found, while the second allows you to specify a PFX file from disk.



[Attaching client certificates](http://www.fiddlerbook.com/fiddler/help/httpsclientcerts.asp)  






