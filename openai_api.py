import openai
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# OpenAI APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# APIキーが正しく読み込まれているか確認（デバッグ用）
if not openai.api_key:
    print("Error: OPENAI_API_KEYが設定されていません。'.env'ファイルを確認してください。")
else:
    print("APIキーが設定されました。")

try:
    # OpenAI APIへのリクエスト
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # または "gpt-4" に変更して試してください
        messages=[
            {"role": "system", "content": "あなたは勤勉な大人です。"},
            {"role": "user", "content": "今日のIT関連のニュースについて一つ教えてください。"}
        ]
    )

    # レスポンスの内容を表示
    print(response.choices[0].message.content)

except openai.error.OpenAIError as e:
    print(f"Error: {e}")
