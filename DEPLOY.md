# oTree Render Deployment Guide

このプロジェクトをRenderにデプロイするためのガイドです。

## 必要なファイル

以下のファイルがRenderデプロイ用に準備されています：

- `Procfile` - Render用のプロセス定義
- `requirements.txt` - Python依存関係
- `render.yaml` - Render用の設定ファイル（オプション）

## デプロイ手順

### 1. Renderアカウントの準備
1. [Render](https://render.com)でアカウントを作成
2. GitHubリポジトリと連携

### 2. 環境変数の設定
Renderダッシュボードで以下の環境変数を設定：

```
SECRET_KEY=your-secret-key-here
OTREE_ADMIN_PASSWORD=your-admin-password
LANGUAGE_CODE=en
REAL_WORLD_CURRENCY_CODE=USD
USE_POINTS=true
```

### 3. データベースの設定
- Render PostgreSQLサービスを作成
- `DATABASE_URL`環境変数を設定

### 4. デプロイ
1. 新しいWebサービスを作成
2. リポジトリを選択
3. 設定：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `otree prodserver1of2`
   - Environment: `Python 3`

### 5. Workerサービスの追加
1. 新しいBackground Workerを作成
2. 設定：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `otree prodserver2of2`

## 注意事項

- 無料プランでは制限があります
- データベースは定期的にリセットされる可能性があります
- 本番環境では適切なセキュリティ設定を行ってください

## トラブルシューティング

### ポートエラー
Renderは自動的にポートを設定するため、`settings.py`でポート設定を確認してください。

### データベース接続エラー
`DATABASE_URL`環境変数が正しく設定されているか確認してください。

### 静的ファイルエラー
`whitenoise`がrequirements.txtに含まれていることを確認してください。
