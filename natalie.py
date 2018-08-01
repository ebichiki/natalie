import feedparser

#お笑いナタリーのURL
RSS_URL = "https://natalie.mu/owarai/feed/news"
natalie_dic = feedparser.parse(RSS_URL)

#お笑い芸人のリスト
artist = ["ナイツ","ジュニア","小峠"]
#タイトルを表示
print(natalie_dic.feed.title)
#記事のタイトルとリンクを表示
for entry in natalie_dic.entries:
    if any(s in entry.title for s in artist):
        title = entry.title
        link = entry.link
        print(link)
        print(title)