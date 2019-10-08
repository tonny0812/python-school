## 使用无头浏览器和Selenium自动化测试工具+python

#### phantomjs 已停止维护，selenium最新版已不支持

#### HeadLess FirxFox 需要下载[geckodirver](https://github.com/mozilla/geckodriver/releases)

需要配置环境变量
或者在selenium中指定路径
```python
from selenium import webdriver
driver = webdriver.Firefox(executable_path='D:\geckodriver_win32\geckodriver.exe')
driver.set_page_load_timeout(50)
driver.get(root_url)
```

#### HeadLess Chrome 需要下载[chromedriver](http://npm.taobao.org/mirrors/chromedriver/)