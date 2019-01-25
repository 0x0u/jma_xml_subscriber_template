# jmx_subscriber_template

[![License](https://img.shields.io/badge/license-JMA-blue.svg)](https://www.jma.go.jp/jma/kishou/info/coment.html)

FlaskとGAE（GoogleAppEngine）を使って気象庁防災情報XML（以下JMX）を受信するためのサブスクライバのテンプレートパッケージです。GAEでサブスクライバを運用するためのファイルがパッケージングされています。ここではテンプレートをクローンしてGAEへデプロイ、気象庁への登録申請までの手順を紹介します。

## 手順

#### 1. パッケージをクローンする
gitからcloneします。

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

#### 2. VERIFY_TOKENを設定する
jmx_subscriber_templateディレクトリ内でsecret.yamlのhogehoge部を自分で書き換えます。気象庁に登録申請する際に届け出るものと同じものを用意します。main.pyのVERIFY_TOKENが拾います。環境変数は全てこのファイルに記述します。

```
env_variables:
  VERIFY_TOKEN: "hogehoge"
```

#### 3. GAEにデプロイする  
GAEとgcloudコマンドが実行できるようにしておくのが前提条件です。以下のコマンドでデプロイします。

```
$ gcloud app deploy app.yaml
```

#### 4. 申請する
[ユーザー登録について](http://xml.kishou.go.jp/open_trial/registration.html)に従い申請します。登録様式をダウンロードして、2で設定したVERIFY_TOKENと3でデプロイしたサブスクライバURL（https\://プロジェクトID.appspot.com/sub）、その他を記述してメールに添付して送信すれば申請完了です。


## 参考
* [気象庁防災情報XMLフォーマット形式電文の公開（PUSH型）](http://xml.kishou.go.jp/open_trial/index.html)
