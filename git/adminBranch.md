#  分支管理流程
## 从远程仓库克隆代码
    git clone https://github.com/rainstar100/mindmap.git
## 查看并创建分支
    git branch
    git branch linearRegression
## 切换分支
    git switch linearRegression
## 修改分支
    xxx
## 暂存更改和提交
    git add .
    git commit -m ""
## 合并分支
    git switch main
    git merge linearRegression
## 推送到远程仓库
    git remote -v  
    git push origin main