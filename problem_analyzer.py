"""
問題分析モジュール (Problem Analysis Module)
Phase 1: 問題文からGoal/Given/分野を抽出する

このモジュールはLLMを使って数学問題を構造化データに変換します。
"""

# 問題分析用プロンプトテンプレート
PROBLEM_ANALYSIS_PROMPT = """
あなたは数学オリンピックの問題を分析する専門家です。
以下の数学問題を分析し、JSON形式で構造化してください。

## 問題文
{problem}

## 出力形式（JSON）
```json
{{
    "goal": "最終的に求めるもの（例: 面積、個数、余り、最大値など）",
    "goal_type": "integer" または "expression",
    "given": [
        "与えられた条件1",
        "与えられた条件2",
        ...
    ],
    "field": "algebra" | "geometry" | "number_theory" | "combinatorics" | "mixed",
    "key_concepts": ["使用する可能性のある定理や概念"],
    "difficulty_indicators": ["問題の難易度を示す要素"]
}}
```

## 分析のポイント
1. **goal**: 問題が最終的に何を求めているかを明確に
2. **given**: 問題で与えられている条件を全てリストアップ
3. **field**: 問題の数学的分野を判定
4. **key_concepts**: 解法に使えそうな定理・公式・テクニック

JSONのみを出力してください。説明は不要です。
"""


def create_analysis_prompt(problem_text: str) -> str:
    """問題文から分析プロンプトを生成"""
    return PROBLEM_ANALYSIS_PROMPT.format(problem=problem_text)


def parse_analysis_response(response: str) -> dict:
    """LLMの応答からJSONを抽出してパース"""
    import json
    import re
    
    # ```json ... ``` ブロックを抽出
    json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
    else:
        # ブロックがない場合は全体をJSONとして試行
        json_str = response.strip()
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {e}", "raw": response}


# テスト用サンプル問題
SAMPLE_PROBLEM = """
Let $ABC$ be an acute-angled triangle with integer side lengths and $AB<AC$. 
Points $D$ and $E$ lie on segments $BC$ and $AC$, respectively, such that $AD=AE=AB$. 
Line $DE$ intersects $AB$ at $X$. Circles $BXD$ and $CED$ intersect for the second time at $Y \\neq D$. 
Suppose that $Y$ lies on line $AD$. There is a unique such triangle with minimal perimeter. 
This triangle has side lengths $a=BC$, $b=CA$, and $c=AB$. 
Find the remainder when $abc$ is divided by $10^{5}$.
"""


if __name__ == "__main__":
    # テスト実行例
    prompt = create_analysis_prompt(SAMPLE_PROBLEM)
    print("=== 生成されたプロンプト ===")
    print(prompt)
    print("\n=== 次のステップ ===")
    print("このプロンプトをLLM（Gemma, DeepSeek等）に渡して分析結果を取得します。")
