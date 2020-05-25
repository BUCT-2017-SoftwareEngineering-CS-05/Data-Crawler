from scrapy import cmdline

for i in range(90):
    name = 'info' + str(i)
    cmd = 'scrapy crawl {0}{1}'.format(name, '')
    try:
        cmdline.execute(cmd.split())
    except:
        pass
