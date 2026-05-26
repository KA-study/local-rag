# Local RAG System
本プロジェクトは、ローカル環境で動作するRAGシステムの実装です。
PDFなどのローカルデータを取り込み、ベクトル検索を通じてLLMに文脈を与える構成を想定しています。

## 1.目的
- ローカルデータ（PDF等）を対象にした検索システムの構築
- 複雑なプログラムの構造理解
- 責務の分離を感覚的につかむ
- 適切な名前付けをできるようになる

## 2.システム構成
PDF -> Chunking -> Embedding -> VectorStore(chroma)
まで考えている。

## 3.ディレクトリ構成
```
├── README.md
├── developer_note
│   └── mermaid-diagram.png
├── docs
│   ├── commite_rule.md
│   ├── decisions.md
│   └── dev_log.md
├── program_files
│   ├── active
│   │   ├── chat
│   │   │   └── history.py              # チャット履歴管理
│   │   └── query
│   │       ├── generator.py            # クエリ生成
│   │       ├── pipeline.py             # 検索パイプライン
│   │       ├── prompt_builder.py       # プロンプト構築
│   │       └── retriever.py            # 検索・取得処理
│   ├── passive
│   │   └── ingest
│   │       ├── embedding
│   │       │   └── embedder.py         # 埋め込み生成
│   │       └── pdf
│   │           ├── _types.py           # 内部型定義
│   │           ├── base.py             # 抽象PDFローダ
│   │           ├── chunker.py          # チャンク分割
│   │           ├── factory.py          # ローダ生成
│   │           └── loader.py           # PDF読み込み
│   ├── shared
│   │   ├── config.py                   # 設定管理
│   │   ├── llm
│   │   │   └── client.py               # LLMクライアント
│   │   ├── schemas.py                 # 共通スキーマ
│   │   ├── utils
│   │   │   └── logger.py              # ログ機能
│   │   └── vectorstore
│   │       └── chroma_store.py        # ChromaDB操作
│   ├── data
│   │   ├── chroma                     # ベクトルDB永続化
│   │   ├── pdf                        # 入力PDF
│   │   └── sqlite                     # 履歴・ログ保存
│   └── main.py                        # エントリポイント
└── requirements.txt
```

## 4.設計方針

### 4.1.差し替え可能設計
以下のコンポーネントは差し替え可能にする想定
- LLM（モデル切り替え）
- Embeddingモデル
- VectorDB
- PDF loader（pypdf/pdfplumber等）

### 4.2.例や構造