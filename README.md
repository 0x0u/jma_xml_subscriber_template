# jma_xml_subscriber_template
FlaskとGAE(GoogleAppEngine)を使って気象庁XMLを受信するためのサブスクライバテンプレートです。以下の手順に従ってデプロイから気象庁への登録申請をします。

## 手順

#### 1. サブスクライバ用のコードを取得する
gitからcloneします。

```
git clone https://github.com/0x0u/jma_xml_subscriber_template.git
cd jma_xml_subscriber_template
```        

中身は以下の様になっています。今回紹介したソースコード（main.py）とGAEにデプロイするために必要なファイル群です。

```
jma_xml_subscriber_template
    ├── app.yaml(GAE設定ファイル)
    ├── main.py
    ├──requirements.txt(インストールが必要な外部モジュール)
    ├──.gcloudignore(GAPにデプロイする際に除外するファイルを指定するためファイル)
    └──.gitignore
```

#### 2. VERIFY_TOKENを設定する
jma_xml_subscriber_templateディレクトリ内でsecret.yamlを作成しhogehoge部を自分で書き換えます。これはGAEにデプロイする際に使うファイルで環境変数を指定します。main.pyのVERIFY_TOKENが取得します。

```
VERIFY_TOKEN: "hogehoge"
```

#### 3. GAEにデプロイする  
GAEとgcloudコマンドが実行できるようにしておくのが前提条件です。以下のコマンドでデプロイします。

```
gcloud app deploy app.yaml
```

#### 4. 申請する
[ユーザー登録について](http://xml.kishou.go.jp/open_trial/registration.html)に従い申請します。`登録様式`をダウンロードして、2で設定したVERIFY_TOKENと3でデプロイしたサブスクライバURL(https://プロジェクトID.appspot.com/sub)、その他を記述してメールに添付して送信すれば申請完了です。


## 参考
* [コンテンツ
トップページ
更新情報
技術資料
情報の取得方法(PUSH型)
情報の取得方法(PULL型)
参考資料集
気象庁防災情報XMLフォーマット形式電文の公開（PUSH型）](http://xml.kishou.go.jp/open_trial/index.html)
