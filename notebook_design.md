# EDA.ipynb 設計書

## 1. 概要

### 1.1 目的
Kaggle「AI Mathematical Olympiad - Progress Prize 3」に向けた学習・開発用Notebookを構築する。

### 1.2 設計方針
- **ゴール指向の逆算推論（Backward Chaining）** アプローチを採用
- 従来の「多数決（Self-Consistency）」方式とは異なり、問題構造を分析してから解く
- 学習教材としても使えるよう、各セクションに解説を含める

### 1.3 ファイル構成
```
ai-mathematical-olympiad-progress-prize-3/
├── EDA.ipynb              ← メインNotebook（本設計書の対象）
├── problem_analyzer.py    ← Phase 1 モジュール（既存）
├── test_phase1.py         ← テストスクリプト（既存）
├── implementation_plan.md ← 実装計画
├── task.md                ← タスク管理
└── (その他既存ファイル)
```

---

## 2. Notebook構成（セクション詳細）

### セクション0: セットアップ

**目的**: Kaggle環境でのデータ読み込みと基本設定

**内容**:
```python
import pandas as pd
import numpy as np
import json
import re

DATA_PATH = '/kaggle/input/ai-mathematical-olympiad-progress-prize-3/'
df = pd.read_csv(DATA_PATH + 'reference.csv')
```

**出力**: 問題データの概要（問題数、カラム構成）

---

### セクション1: Phase 1 - 問題分析モジュール

**目的**: 問題文を構造化データに変換する

**入力**: 問題文（自然言語 + LaTeX数式）

**出力**: JSON形式の構造化データ
```json
{
    "goal": "求めるもの（例: abcを10^5で割った余り）",
    "goal_expression": "数式表現",
    "given": ["条件1", "条件2", ...],
    "field": "geometry | algebra | number_theory | combinatorics | mixed",
    "key_concepts": ["使用する可能性のある定理・概念"]
}
```

**実装内容**:
1. `PROBLEM_ANALYSIS_PROMPT` - LLMに渡すプロンプトテンプレート
2. `create_analysis_prompt(problem_text)` - プロンプト生成関数
3. `parse_analysis_response(response)` - LLM応答のJSONパーサー

**テスト**: reference.csvの1問目でプロンプト生成を確認

---

### セクション2: Phase 2 - 逆算推論モジュール

**目的**: ゴールから逆算してサブゴールを分解する

**入力**: Phase 1の分析結果（JSON）

**出力**: 解法計画（JSON）
```json
{
    "goal": "最終ゴール",
    "subgoals": [
        {"step": 1, "description": "...", "requires": ["..."]}
    ],
    "execution_order": ["ステップ3", "ステップ2", "ステップ1"]
}
```

**実装内容**:
1. `BACKWARD_REASONING_PROMPT` - 逆算推論プロンプト
2. LLM呼び出し関数（TODO）

**現状**: プロンプトテンプレートのみ。LLM統合は未実装。

---

### セクション3: Phase 3 - 計画実行モジュール

**目的**: 解法計画をPythonコードに変換し、実行する

**入力**: Phase 2の解法計画（JSON）

**出力**: 計算結果（整数）

**実装内容**:
1. `CODE_GENERATION_PROMPT` - コード生成プロンプト
2. `execute_code_safely(code, timeout)` - サンドボックス実行関数

**安全対策**:
- タイムアウト設定（デフォルト30秒）
- 一時ファイルでの実行
- エラーハンドリング

---

### セクション4: Phase 4 - 検証・提出

**目的**: 正答率の計測と提出形式への変換

**実装内容**:
1. `evaluate_on_reference(solve_fn, df)` - reference.csvでの評価
2. Kaggle評価API形式への対応（TODO）

---

## 3. 依存関係

### 必須ライブラリ
- pandas
- numpy
- json（標準）
- re（標準）
- subprocess（標準）

### LLMモデル（未決定）
- 候補: Gemma-2-9B / DeepSeek-Math-7B / Qwen-2.5-Math
- Kaggle環境での量子化が必要（4-bit推奨）

---

## 4. 今後の作業

| 項目 | ステータス | 備考 |
|------|----------|------|
| セクション0: セットアップ | ✅ 完了 | |
| セクション1: Phase 1 | ✅ 完了 | プロンプト・パーサー実装済み |
| セクション2: Phase 2 | ⚠️ テンプレートのみ | LLM統合が必要 |
| セクション3: Phase 3 | ⚠️ テンプレートのみ | LLM統合が必要 |
| セクション4: Phase 4 | ⚠️ テンプレートのみ | 評価関数のみ |
| LLMモデル選定・統合 | ❌ 未着手 | 次の主要作業 |

---

## 5. 承認事項

この設計でNotebookを構築してよいか、ご確認ください。

- [ ] 設計承認
- [ ] LLMモデルの選定（Gemma / DeepSeek / Qwen / その他）
- [ ] 追加要件があれば記載
