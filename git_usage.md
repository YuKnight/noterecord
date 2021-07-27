
git clone -b jpbclib https://github.com/maerye/SM9.git



git clone 远程仓库地址 【默认克隆的是master分支，有可能不是想拉下来的分支】
已经克隆了master分支，想要到指定的分支，使用以下方法：
git branch -a                  先查看当前远端分支情况
git checkout origin/xxx   选择远端xxx分支（origin为远程仓库别名）
git branch xxx                 创建本地xxx分支
git checkout xxx              选择本地新创建的分支就可以了
－－－－－－－－－－－－－－－

2、多合一操作
直接指定clone某个分支即可：
git clone -b 远程分支名 远程仓库地址