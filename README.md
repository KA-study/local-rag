# Local RAG System
本プロジェクトは、ローカル環境で動作するRAGシステムの実装です。
PDFなどのローカルデータを取り込み、ベクトル検索を通じてLLMに文脈を与える構成を想定しています。

## 1.目的
- ローカルデータ（PDF等）を対象にした検索システムの構築
- 複雑なプログラムの構造理解
- 責務の分離を感覚的につかむ
- 適切な名前付けをできるようになる

## 2.できること
- PDFファイルの読み込み、embeddingし、VectorStoreに保存
- ユーザー入力を用いてVectorStore探索
- 以上を用いてLLMと接続

## 3.使用方法
- 指定の（後述）ディレクトリにPDFファイルを保存
- 当アプリケーションを起動
- sessionを選択し、チャット開始

## 4.設計方針

### 4.1.差し替え可能設計
以下のコンポーネントは差し替え可能にする想定
- LLM（モデル切り替え）
- Embeddingモデル
- VectorDB
- PDF loader（pypdf/pdfplumber等）

### 4.2.例や構造

## 5.設計詳細
このプログラムの詳細については以下をご覧ください

- [アーキテクチャ](docs/architecture.md)
- [依存関係](docs/dependency.md)
- [処理フロー](docs/sequence.md)
- [テスト方式](docs/testing.md)

