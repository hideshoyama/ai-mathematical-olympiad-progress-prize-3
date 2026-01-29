# AI Mathematical Olympiad - Progress Prize 3

## 戦略: ゴール指向の逆算推論（Backward Chaining）

- [x] プロジェクト方針・コンセプト策定
    - [x] 実装計画の作成 (`implementation_plan.md`)

---

## Phase 1: 問題分析モジュール
- [/] LLMプロンプト設計: 問題文からGoal/Given/分野を抽出 (`problem_analyzer.py`)
- [ ] サンプル問題でのプロンプトテスト

## Phase 2: 逆算推論モジュール
- [ ] ゴール→サブゴール分解ロジックの設計
- [ ] 再帰的展開のプロンプト設計
- [ ] サンプル問題での動作確認

## Phase 3: 計画実行モジュール
- [ ] Pythonコード生成プロンプトの設計
- [ ] 安全なコード実行環境（sandbox）の実装
- [ ] エラー時の再試行（Reflexion）ロジック

## Phase 4: 検証・統合
- [ ] AIME過去問での評価
- [ ] Kaggle Notebook形式への統合
- [ ] 最終提出

---

## 環境セットアップ（未完了）
- [x] ワークスペース作成
- [ ] データダウンロード（手動）
- [ ] ベースモデル選定・取得
