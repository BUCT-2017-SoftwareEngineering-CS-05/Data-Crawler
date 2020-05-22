from scrapy import cmdline
name = 'info88'
cmd = 'scrapy crawl {0}{1}'.format(name, '')
cmdline.execute(cmd.split())