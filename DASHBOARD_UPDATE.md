# ダッシュボード更新手順

## 構成の概要

```
GitHub（コード管理）→ Apps Script（ホスティング）→ ダッシュボード
Google Sheets（データ）→ Apps Script（毎アクセス時に読み込み）
```

- **データ更新**（日次自動）：Python パイプラインが自動実行、作業不要
- **画面更新**（手動）：下記の手順で実施

---

## データだけ更新したい場合

タスクスケジューラーが自動実行するため、**作業不要**です。
手動で即時反映したい場合は `SEO_AIO週次レポート実行.bat` を実行してください。

---

## 画面レイアウト・機能を更新したい場合

### 事前に必要なもの

- このリポジトリへのGitHubアクセス権
- Python 3.x（ローカルに導入済み）
- Apps Script プロジェクトへのアクセス権（yogibo.inc アカウント）

---

### 手順

#### 1. GitHub でコードを編集

`index.html` を直接編集するか、ブランチを切ってPRを作成します。

```
編集対象: index.html
```

> **注意**: データは埋め込まれていません。`GA4_DATA`、`ARTICLE_TRAFFIC_DATA`、`SEO_DATA` 等の定数はプレースホルダーになっています。ローカルでの動作確認はできません。

#### 2. Apps Script エディタに貼り付け

1. 以下のURLを **@yogibo.inc アカウント** で開く

   ```
   https://script.google.com
   ```

2. プロジェクト「**Yogibo SEO AIO Dashboard v4**」を開く

3. 左側のファイル一覧から `index.html` を選択

4. GitHub の `index.html` の内容を **全選択（Ctrl+A）→ 貼り付け（Ctrl+V）**

5. **保存（Ctrl+S）**

#### 4. 再デプロイ

1. 右上「**デプロイ**」→「**デプロイを管理**」をクリック

2. 鉛筆アイコン（編集）をクリック

3. バージョン：「**新しいバージョン**」を選択

4. 「**デプロイ**」をクリック

5. 完了。URLは変わりません

---

## Apps Script プロジェクト情報

| 項目 | 内容 |
|---|---|
| データ書き込み（Writer） | Yogibo SEO AIO Dashboard v4 writer |
| ダッシュボード表示 | Yogibo SEO AIO Dashboard v4 |
| ダッシュボードURL | yogibo.inc アカウントの config.py を参照 |
| データ格納先 | Google Sheets（スプレッドシートID: 1b8WO8X9KsMvdBvka0vfiX9p6wzh_eiu4GNRjRs3PoMQ） |

---

## トラブルシューティング

| 症状 | 原因 | 対処 |
|---|---|---|
| 画面が真っ白 | JS エラー | ブラウザの開発者ツール（F12）でエラーを確認 |
| データが古い | Sheets 未更新 | `SEO_AIO週次レポート実行.bat` を実行 |
| アクセスできない | yogibo.inc 以外のアカウント | yogibo.inc アカウントでログインし直す |
| 「doGet が見つからない」 | 誤ったコードが貼られている | `apps_script_dashboard.gs` の内容を Code.gs に貼り直す |
