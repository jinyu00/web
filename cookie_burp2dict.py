cookie = '''kDapH_auth=77c1pn6JRrGqWtVZHBCyAYPSffKvjWVOoaUMR09bhuEGurI8BEBF2Fo0traseEObyHPI4W230hpj_9oRMJiZ5WIKiAeDhKAdSI7NENSF71WkcphNOD211cbXqrlf4jG1IZaO_rQO_c57e00hl_YzlhA; kDapH__userid=68c8BHE75BlmNHA7zzoZhX7Zz_W_jgMwRCvctn4f; kDapH__username=cbcbR9zX-jGpef0iUYWgM47zpaAjehAo3UeKjShzsvw; kDapH__groupid=294dSoWgFZfo2eSj9Y8ZQDdh-X9pkPLv98hAv7bJ; kDapH__nickname=8893kAl9RBgTX5tXGzspnKriXuipkFiB7z7Jf2qiBU0; PHPSESSID=p9sa5v3ig3d0877h3d8glnkau0'''
import re
cookies = {}
ay = cookie.split(";")
for i in ay:
	tp = i.split("=")
	cookies[tp[0]] = tp[1]
print type(cookies)
for k,v in cookies.items():
	print "%s -> %s" %(k,v)

