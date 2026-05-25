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
program_files/
├── chat/             
│   └──history.py     # チャット履歴管理 
├── config.py         # 設定値管理
├── data/             # 永続データ
│   ├── chroma/       # ベクトルDB保存領域
│   ├── pdf/          # 入力PDF
│   └── sqlite/       # ログ・履歴等
├── embedding/        
│   └──embedder.py    # Embedding処理
├── llm/              
│   └──client.py      # LLMクライアント
├── pdf/              # PDF処理モジュール群
│   ├── loader / chunker / factory
│   ├── base.py       # 抽象化（差し替え前提）
│   └── _types.py     # 内部型定義
├── rag/
│   └── pipeline.py   # RAG全体パイプライン
├── vectorstore/
│   └── chroma_store.py
├── utils/
│   └── logger.py
├── schemas.py        # 共通スキーマ
└── main.py           # エントリポイント

## 4.設計方針

### 4.1.差し替え可能設計
以下のコンポーネントは差し替え可能にする想定
- LLM（モデル切り替え）
- Embeddingモデル
- VectorDB
- PDF loader（pypdf/pdfplumber等）

### 4.2.例や構造
- pdf/: 知識ベース取り込み処理
- embedding/: 数値化層
- vectorstore/: 検索層
- rag/: 統合パイプライン層
- llm/: 生成層
- main.py: アプリケーション層
















