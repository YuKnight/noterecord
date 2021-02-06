

## [hexo](https://hexo.io/docs/asset-folders "asset-folders")
* 依赖nodejs  
  `npm -v`  

* 安装  
  `npm install -g hexo-cli`  

* 进入准备存放博客的目录，输入下面命令初始化我们自己的网站  
 `hexo init Blog`

* 进入`Blog`目录，接着输入`npm install`安装必备的组件  

* 修改`Blog`目录下配置文件`_config.yml`打开资源管理配置项，以后每次新建博客都会产生一个目录存放资源文件，否则默认没有存放资源文件的目录  
    ```
    _config.yml
    post_asset_folder: true
    ```
* 输入`hexo s`查看生成的网站，如果要指定端口则用`hexo s -p 9000`  

* 创建新的blog `hexo new post "First Blog"`

* 在`Blog\source\_posts\First-Blog.md`写入资源引用 `{% asset_img 1.png This is an example image %}` 并在`Blog\source\_posts\First-Blog`目录中存放引用的图片`1.png`  

* 使用`hexo g`生成网页   
* `hexo s`打开网页`http://localhost:4000`进行本地预览  

```sh
E:\GitHub>hexo init Blog
(node:10528) ExperimentalWarning: The fs.promises API is experimental
INFO  Cloning hexo-starter https://github.com/hexojs/hexo-starter.git
INFO  Install dependencies
added 188 packages from 443 contributors and audited 194 packages in 47.167s
found 0 vulnerabilities

INFO  Start blogging with Hexo!

E:\GitHub>cd Blog

E:\GitHub\Blog>npm install
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.3.1 (node_modules\fse
vents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@
2.3.1: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"}
)

added 5 packages from 1 contributor and audited 194 packages in 3.834s
found 0 vulnerabilities


E:\GitHub\Blog>hexo s
(node:22376) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
INFO  Bye!
终止批处理操作吗(Y/N)? y

E:\GitHub\Blog>hexo s --help
(node:23520) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
Usage: hexo server

Description:
Start the server and watch for file changes.

Options:
  -i, --ip            Override the default server IP. Bind to all IP address by
default.
  -l, --log [format]  Enable logger. Override log format.
  -o, --open          Immediately open the server url in your default web browse
r.
  -p, --port          Override the default port.
  -s, --static        Only serve static files.


E:\GitHub\Blog>hexo s -p 9000
(node:5716) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
INFO  Start processing
INFO  Hexo is running at http://localhost:9000 . Press Ctrl+C to stop.
INFO  Farewell
终止批处理操作吗(Y/N)? y


E:\GitHub\Blog>hexo new post "First Blog"
(node:33160) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
INFO  Created: E:\GitHub\Blog\source\_posts\First-Blog.md

E:\GitHub\Blog>hexo g
(node:22120) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
INFO  Start processing
INFO  Files loaded in 189 ms
INFO  Generated: archives/index.html
INFO  Generated: archives/2021/index.html
INFO  Generated: 2021/01/30/First-Blog/index.html
INFO  Generated: archives/2021/01/index.html
INFO  Generated: index.html
INFO  Generated: 2021/01/30/First-Blog/1.png
INFO  6 files generated in 42 ms

E:\GitHub\Blog>hexo s
(node:26840) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
INFO  Farewell
终止批处理操作吗(Y/N)? y
```

其中`First-Blog.md`中的内容为：
```
---
title: First Blog
date: 2021-01-30 16:58:35
tags:
---
{% asset_img 1.png This is an example image %}
```

windows下的CMD命令tree可以很方便的得到文件夹目录树
```
tree [drive][path] [/F] [/A]
#/f 显示所有目录及目录下的所有文件，省略时，只显示目录，不显示目录下的文件
#/a 使用ASCII字符，而不使用扩展字符
```

```sh
[E:\GitHub\Blog]$ tree /F > tree.txt
```

`Blog`目录结构为：
```
├─Blog  
   ├─node_modules
   ├─public
   ├─scaffolds
   ├─source
   │  └─_posts
   │      ├─First-Blog
   │      │   └─1.png
   │      ├─First-Blog.md
   │      └─hello-world.md
   ├─themes
   ├─.gitignore
   ├─_config.landscape.yml
   ├─_config.yml
   ├─db.json
   ├─package.json
   └─package-lock.json
```