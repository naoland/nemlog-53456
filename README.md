[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/naoland/nemlog-53456)

# 簡単プログラミング！XEMの現在価格をLINEに通知しよう（Python編）

## はじめに

さて、今回はPython言語を使ってXEMの現在価格を取得し、その内容をLINEに通知してみたいと思います。

LINEに通知するための準備は[前回の記事](https://nemlog.nem.social/blog/53471)をご覧ください。

今回はccxtのような取引所関連ライブラリは使用せず、一般的なHTTPリクエスト関連の処理を記述します。
`Requests`というHTTP向けのPythonライブラリを使用します。

流れとしては、

- LINE Notifyで、アクセストークンを発行する（前回の記事ですで完了済み）
- LINEのアクセストークンが有効かどうか確認する。無効だった場合は終了
- XEMの現在価格を取得する
- XEMの現在価格をLINEに通知する

「XEMの現在価格を取得するコード」は今まで`JavaScript`を使って記述してきましたが、やることは同じです。

トークンを直接コードに埋め込まないでください。

## 前提条件

[LINEに通知するための準備](#links)までの作業が終わっているのが前提です。

![トークンの取得](./images/reg-complete.png)

## コードの説明

コード全体は次のようになります。

```python
```


## まとめ



今回採用したPythonは現在非常に人気のあるプログラミング言語ですので、軽く使えるようになっておくとよいでしょう。

## 関連情報へのリンク
<a id="links"></a>

- [LINEに通知するための準備](https://nemlog.nem.social/blog/53471)
- [現物公開API — Zaif api document v2.0.0 ドキュメント](https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html)
- [LINE Notify API Document](https://notify-bot.line.me/doc/ja/)  
上記ドキュメントの「通知系」の箇所をご覧ください。
