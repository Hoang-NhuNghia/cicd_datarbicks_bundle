#!/bin/bash

# 環境変数からSSH秘密鍵を取得
echo "$SSH_PRIVATE_KEY" > /tmp/id_rsa
chmod 600 /tmp/id_rsa

# SSHコマンドの設定
export GIT_SSH_COMMAND='ssh -i /tmp/id_rsa -o StrictHostKeyChecking=no'

# GitHubリポジトリからパッケージをインストール
pip install "git+ssh://git@github.com/aucnet-dev/dx-data-analytics-functions.git@develop#egg=databricks_lake_utils&subdirectory=databricks_utils/"

# 一時ファイルのクリーンアップ
rm /tmp/id_rsa