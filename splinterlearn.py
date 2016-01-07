from splinter import Browser

# with Browser() as br:
#    br.visit('http://www.baidu.com/')
br = Browser();
br.visit('http://www.baidu.com/')
br.fill("wd", "haha")
bt = br.find_by_id(u"su")
bt.click()
br.quit()
