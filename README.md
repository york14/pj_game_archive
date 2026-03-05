# pj_game_archive

個人のゲーム検証・考察をシンプルにアーカイブするプロジェクト。

> **Note**: このREADMEはAI・人間の作業者向けの内部ドキュメントです。
> GitHubリポジトリページに表示されるREADMEは `.github/README.md` です。

## ディレクトリ構造

```
pj_game_archive/
├── .github/
│   └── README.md            ← GitHub表示用README
├── docs/                    ← 公開コンテンツ（GitHub Pages対象）
│   ├── _config.yml          ← Jekyll設定（テーマ・Sitemap等）
│   ├── index.md             ← トップページ（目次）
│   ├── google*.html         ← Google Search Console 所有権確認ファイル
│   ├── ake/                 ← Arknights: Endfield
│   ├── ff14/                ← Final Fantasy XIV
│   └── general/             ← ゲーム横断・汎用
├── foundation/              ← 非公開：プロジェクト運営ドキュメント
├── _private/                ← 非公開：検証用生データ・下書き
│   ├── drafts/              ← 下書き・メモ
│   └── raw_data/            ← 検証用の生データ
├── .gitignore               ← _private/ を除外
└── README.md                ← 本ファイル（AI・作業者向け）
```

## 方針
- **docs/**: GitHub Pages公開対象。事実重視、シンプル、Markdownのみ
- **foundation/**: 作業用ドキュメント（非公開）
- **_private/**: 下書き・検証データ（.gitignoreで除外）
- 記事は「書きたくなったとき」に追加。定期義務なし

## SEO設定
- **Sitemap**: `jekyll-sitemap` プラグインで自動生成（`_config.yml`）
- **Google Search Console**: `docs/google10abfcac54aa5cc5.html` で所有権確認
