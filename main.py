import easygui as eg
import webbrowser


def main():
    show_info = '请按以下规则输入：\n\n普通部分：\n\t1.条目空间：直接输入条目名称\n\t2.随机条目：不输入\n\t3.查询子页面：p:[页面名称]\n\t4.链入页面:l:[页面名称]' \
                '\n\t5.重定向至本页面的页面：r:[页面名称]' \
                '\n\n用户页部分：\n\t1.用户页：输入u:[用户名称]或者user:[用户名称]\n\t2.用户讨论：ut:[用户名称]\n\t3.用户贡献：uc:[用户名称]\n\t4.用户组：ug:[用户名称]'
    info = eg.enterbox(show_info, '输入', image='./show.png')
    if not info:
        url = 'https://zh.wikipedia.org/wiki/Special:随机页面/'
    elif info[:2] == 'uc':
        url = 'https://zh.wikipedia.org/wiki/Special:用户贡献/' + info[3:]
    elif info[:2] == 'ug':
        url = 'https://zh.wikipedia.org/wiki/Special:用户权限/' + info[3:]
    elif info[:1] == 'p':
        url = 'https://zh.wikipedia.org/wiki/Special:前缀索引/' + info[2:]
    elif info[:1] == 'l':
        url = 'https://zh.wikipedia.org/wiki/Special:链入页面/' + info[2:]
    elif info[:1] == 'r':
        url = 'https://zh.wikipedia.org/w/index.php?title=Special:链入页面/' + info[2:] + '&hidelinks=1&hidetrans=1'
    else:
        url = 'https://zh.wikipedia.org/wiki/' + info

    webbrowser.open(url)


if __name__ == '__main__':
    main()
