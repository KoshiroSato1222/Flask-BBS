from server import db
from server import Article
# DBを作成する
db.create_all()

# サンプルデータを作成する
sample = Article(username="花子", email="hanako@gmail.com", post="ダイエットについて質問です。・・・")

# サンプルデータをDBに挿入する
db.session.add(sample)
db.session.commit()

# データを表示する
print(Article.query.all())