# Phase 1: 問題分析モジュールのテスト
# Kaggle Notebook用

# GitHubからcloneした場合
import sys
sys.path.append('/kaggle/working/ai-mathematical-olympiad-progress-prize-3')

from problem_analyzer import create_analysis_prompt, parse_analysis_response, SAMPLE_PROBLEM
import pandas as pd

# 参考問題を読み込み
df = pd.read_csv('/kaggle/input/ai-mathematical-olympiad-progress-prize-3/reference.csv')

# 1問目で分析プロンプトを生成
problem_text = df.iloc[0]['problem']
prompt = create_analysis_prompt(problem_text)

print("=== 問題文 ===")
print(problem_text[:200] + "...")
print("\n=== 生成されたプロンプト（LLMに渡す） ===")
print(prompt)
