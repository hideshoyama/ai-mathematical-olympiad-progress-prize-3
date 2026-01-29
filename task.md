# AI Mathematical Olympiad - Progress Prize 3

## 戦略: ゴール指向の逆算推論（Backward Chaining）

- [x] プロジェクト方針・コンセプト策定
    - [x] 実装計画の作成 (`implementation_plan.md`)

---

## Phase 1: 問題分析・分類
- [x] 分類・ゴール抽出プロンプト設計 (`EDA.ipynb`に実装)
- [/] サンプル問題での分野判別テスト

## Phase 2: 分野別RAG構築 & 逆算推論
- [/] 幾何学公式ライブラリの構築（公式集 + 適用条件）
- [ ] 整数論公式ライブラリの構築
- [ ] 問題例ライブラリの構築（LLM学習用）
- [ ] 逆算プロンプトの調整（RAG連携）

## Phase 3: 計画実行・Reflexion
- [ ] Pythonコード生成プロンプトの調整
- [ ] 安全な実行環境（sandbox）の強化
- [ ] エラー時の再試行（Reflexion）ロジックの実装

## Phase 4: 検証・統合
- [ ] AIME問題での評価
- [ ] Few-shot vs RAG の比較検証
- [ ] Kaggle提出用パイプラインの作成

---

## 環境セットアップ（未完了）
- [x] ワークスペース作成
- [ ] データダウンロード（手動）
- [ ] ベースモデル選定・取得
