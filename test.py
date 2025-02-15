print("Hello world")
# 到Terminal打git init, 將資料夾轉為git操控
# 打git status, 追蹤資料夾狀態, 紅字為untrack狀態
# 打git add . (add空格點),綠字為"詢問"把資料夾檔案變成一個版本
# 打git commit -m "add test py" 要多人協作
# Terminal的複製貼上不要用Ctrl+C/V,只需選取要的部分案右鍵,再按右鍵即可貼上
# 跑完上述流程,建立新版本
a = 1
b = 2
c = a+b
# 左邊的source control 裡的commit會顯示change的狀態,只需要按+就會自動修改存檔為新版本=modified
# 再source control的輸入欄輸入要置換的版本名稱,然後按commit自動存檔=committed
print(c)
# 若要將以修改版本退回未修改版本,指令git restore --staged <file name不須外框>
# 若要回去之前的版本,指令 git reset --hard(版本編碼) ->只看不改,後面會消失
# 若不要中間版本消失,不能修改,指令 git reflog ->查看所有版本編碼, 再次下指令 git reset --hard最新版
# 但若是回到之前版本並修改,原先的版本就強制消失
a = 3
b = 1
# 指定一些檔案永遠不要進到我的資料庫
# 新增檔案 .gitignore 並將不想要的檔案名稱打進去, 確認狀態git status
