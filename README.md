# pj_game_archive

個人のゲーム検証・考察をシンプルにアーカイブするプロジェクト。

## ディレクトリ構造

```
pj_game_archive/
├── docs/                    ← 公開コンテンツ（GitHub Pages対象）
│   ├── index.md             ← トップページ（目次）
│   ├── ake/                 ← Arknights: Endfield
│   ├── ff14/                ← Final Fantasy XIV
│   └── general/             ← ゲーム横断・汎用
├── foundation/              ← 非公開：プロジェクト運営ドキュメント
├── _private/                ← 非公開：検証用生データ・下書き
│   ├── drafts/              ← 下書き・メモ
│   └── raw_data/            ← 検証用の生データ
├── _config.yml              ← Jekyll設定
├── .gitignore               ← _private/ を除外
└── README.md                ← リポジトリ説明（非公開前提のメモ）
```

## 方針
- **docs/**: GitHub Pages公開対象。事実重視、シンプル、Markdownのみ
- **foundation/**: 作業用ドキュメント（非公開）
- **_private/**: 下書き・検証データ（.gitignoreで除外可能）
- 記事は「書きたくなったとき」に追加。定期義務なし
