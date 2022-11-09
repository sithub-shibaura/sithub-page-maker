# sithub-page-maker

## 目次
- [sithub-page-maker](#sithub-page-maker)
  - [目次](#目次)
  - [About](#about)
  - [How to use this?](#how-to-use-this)
    - [Windows10/11](#windows1011)
    - [Linux](#linux)
    - [Python版](#python版)
  - [Help](#help)
  - [for Developer](#for-developer)

## About
このソフトウェアは、WEBサイト「[SIThub for WEB](https://sithub.info/)」へ記事やコンテンツの作成・投稿や編集を行うためのソフトウェアです。  
現在は開発中のため使用することはできません。  
今後、以下の環境で使用することができるようになる予定です。  
- Download版
  - Windows10
  - Windows11
  - Linux
    - Ubuntu 22.04
    - Linux Mint 21
    - Fedora 36
  
- Python版
  - Python3.10.5

- HTML(JavaScript)ファイル
  - Google Chrome 最新版
  - Mozilla Firefox 最新版

## How to use this?
Python環境がある場合は、Python版が最も簡単です。OSにも依存しません。
### Windows10/11
1. [releaseページ](https://github.com/sithub-shibaura/sithub-page-maker/releases)から、最新版のsithub-page-maker-○.○.○-installer.exeをダウンロードします。
2. 実行します。**管理者権限は必要ありません。**
3. 生成したsithub-page-makerフォルダ内のsithub-page-maker.exeを実行することで、起動することができます。
4. 作業中、ログインを求められる場合があります。必要に応じてSIThubアカウントを利用してログインしてください。(予め[ここで](https://sithub.info/account/signup.php)アカウントを作成している必要があります。)
5. アンインストールは、インストール時に生成したフォルダを削除するだけです。

### Linux
1. [releaseページ](https://github.com/sithub-shibaura/sithub-page-maker/releases)から、最新版のsithub-page-maker-○.○.○.debまたは.rpmをダウンロードします。ダウンロードする際、各々のパッケージ管理ツールに合わせた拡張子を選択してください。  
2. インストール/実行します。
   - (.debの場合)
     1. ファイルをダウンロードされたディレクトリまで移動します。
     2. このコマンドを実行します。：```$ sudo dpkg -i sithub-page-maker-〇.〇.○.deb```※ファイル名はダウンロードされたファイル名に合わせてください。
     3. ```$ sithub-page-maker```をターミナル上で実行することで、使用することができます。
   - (.rpmの場合)
     1. ファイルをダウンロードされたディレクトリまで移動します。
     2. このコマンドを実行します。：```$ sudo rpm -ivh sithub-page-maker-〇.〇.○.rpm```※ファイル名はダウンロードされたファイル名に合わせてください。
     3. ```$ sithub-page-maker```をターミナル上で実行することで、使用することができます。
3. 作業中、ログインを求められる場合があります。必要に応じてSIThubアカウントを利用してログインしてください。(予め[ここで](https://sithub.info/account/signup.php)アカウントを作成している必要があります。)
4. アンインストールは、dpkgまたはrpmコマンドから可能です。

### Python版
1. [releaseページ](https://github.com/sithub-shibaura/sithub-page-maker/releases)から、最新版のsource.zipをダウンロードします。
2. 適当な場所で展開します。
3. 解凍されたディレクトリに移動し、コマンドライン上で```$ pip install -r requirements.txt```を実行します。必要に応じて、venv等の仮想環境で実行してください。
4. その後、そのまま```python3 main.py```、のようにmain.pyを実行することで、起動することができます。

## Help
詳細の使い方やヘルプ等のドキュメントは、[こちら](https://sithub-shibaura.github.io/sithub-page-maker/)。/docsフォルダ内のindex.mdからも確認することができます。

## for Developer
このプロジェクトでは、複数のライブラリを使用しています。requirements.txtから使用されているライブラリを確認することができます。  