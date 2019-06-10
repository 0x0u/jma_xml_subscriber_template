# jmx_subscriber_template

[![License](https://img.shields.io/badge/license-JMA-blue.svg)](https://www.jma.go.jp/jma/kishou/info/coment.html)

FlaskとGAE（GoogleAppEngine）を使って気象庁防災情報XML（以下JMX）を受信するためのサブスクライバテンプレートパッケージです。GAEでサブスクライバを運用するためのファイルがパッケージングされています。ここではテンプレートをクローンしてGAEへデプロイ、気象庁への登録申請までの手順を紹介します。

## 手順

### 1. パッケージをクローンする
githubからcloneします。

```
$ git clone https://github.com/0x0u/jmx_subscriber_template

$ cd jmx_subscriber_template
```        

中身は以下のようになっています。GAEにデプロイするために必要なファイル群です。

```
jmx_subscriber_template
    ├── app.yaml
    ├── main.py
    ├── requirements.txt
    ├── secret.yaml
    ├── .gitignore
    └── .gcloudignore
```

### 2. VERIFY_TOKENを設定する
送られてきたデータが真に気象庁からかどうかを判断するためのVERIFY_TOKENを設定します。jmx_subscriber_templateディレクトリ内でsecret.yamlのhogehoge部を自分で書き換えます。気象庁に登録申請する際に届け出るものと同じものを用意します。これはmain.pyのVERIFY_TOKENが拾います。環境変数は全てこのファイルに記述します。

```
env_variables:
  VERIFY_TOKEN: "hogehoge"
```

### 3. GAEにデプロイする  
gcloudコマンドを実行できるようにしておきましょう。以下のコマンドでデプロイします。

```
$ gcloud app deploy app.yaml
```

### 4. 申請する
[ユーザー登録について](http://xml.kishou.go.jp/open_trial/registration.html)に従い申請します。登録様式をダウンロードして、[2](https://github.com/0x0u/jmx_subscriber_template#2-verify_token%E3%82%92%E8%A8%AD%E5%AE%9A%E3%81%99%E3%82%8B)で設定したVERIFY_TOKENと3でデプロイしたサブスクライバのURL（https\://プロジェクトID.appspot.com/sub）、その他を記述してメールに添付して送信すれば申請完了です。 なりすましや、サーバーへの負荷対策のためにもVERIFY_TOKENとサブスクライバのURLは他人に知らせないように気をつけましょう。

下記に私が実際に申請した際の登録様式を少し改変して載せておきました。



登録様式例

```
【留意事項等チェックリスト】

　チェックした項目については、「□」を「■」に書き換えてください。

■　サーバメンテナンス等により、公開ＸＭＬ電文の掲載に遅延・停止が生じる
　　場合があることを理解し、承諾した。
■　利用者が公開ＸＭＬ電文を用いて行う一切の行為について気象庁は何ら責任を
　　負うものではないことを理解し、承諾した。
■　上記２項の他、「公開電文の利用上の留意事項等について」の
　　内容を全て確認の上、承諾した。
■　「気象庁防災情報XMLフォーマット運用指針」の
　　３．気象庁XMLの編集の項を確認の上、内容について承諾した。
■　subscriberを安定稼働するサーバーに配置し、Alert HUBからアクセス可能
　　（アクセス制御等の設定を含む）であること及びHUBから正しくフィードの
　　更新情報を受け取ることを確認した。

※登録完了後も一定期間毎にAlert HUBからsubscriberの存在確認が行われ、
　確認に失敗した場合は登録が削除される場合がありますので、
　subscriberが安定稼働するよう、お願いいたします。


【登録情報】

上記チェックリストの各項について確認、承諾の上、以下の通り登録を申し込みます。

[1]連絡先電子メールアドレス
hogehoge6@gmail.com

[2]subscriberのエンドポイントURL
https://hogehoge.appspot.com/sub

[3]verify.tokenの登録を希望する場合はtokenを記載
cdcdcdgdfasdf

[4]登録を希望するatomフィードの分類種別
　（選択した種別の「□」を「■」に書き換えてください。複数でも問題ありません。
　　具体的な情報の種類については「公開電文一覧」のページをご覧ください。）
　■　(1)定時 ：気象に関する情報のうち、天気概況など定時発表されるもの
　■　(2)随時 ：気象に関する情報のうち、警報・注意報など随時発表されるもの
　■　(3)地震火山 ：地震、火山に関する情報
　■　(4)その他 ：上記３種類のいずれにも属さないもの

[5]記入年月日
　平成31年1月23日
```

## 参考
* [気象庁防災情報XMLフォーマット形式電文の公開（PUSH型）](http://xml.kishou.go.jp/open_trial/index.html)

