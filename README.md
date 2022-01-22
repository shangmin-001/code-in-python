# tool-in-python

python 版本 python3

## 生成依赖包工具 
1. 安装` pip3 install pipreqs`
2. 生成 `pipreqs ./ --encoding=utf8`
3. 安装 `pip3 install -r requriements.txt`
  > IOError: [Errno 2] No such file or directory: 'requirements.txt' 
  > Solution 1: create the requirements file first `pip freeze > requirements.txt`
  > Solution 2: find requirements.txt path `find -name "requirements.txt"` && `find . -regex '.*requirements.txt$' //on theroot directory of your terminal`
