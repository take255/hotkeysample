# hotkeysample
Blenderのスクリプトエディタに読み込んで使う用のサンプルです。

使い方：
hotkeysample.pyをスクリプトエディタに読み込む。
実行ボタンを押す。

サンプルではshift + alt + W　で　頂点マージが実行されます。

ただコピペするだけだとシーンをあけるたびに設定が消えてしまうので、読み込まれた状態でデフォルトシーンとして保存すると毎回使えるようになります。
その場合Text > registerにチェックを入れておけば毎回自動実行されるのですが、セキュリティに問題があると注意されます。

運用するにはアドオンにするのが一番いいのですが、ちょっとしたコマンドをホットキーに登録したいだけなのにアドオンをつくるのは、そこまでやらないとダメなの？っていう気にはなりますね。

