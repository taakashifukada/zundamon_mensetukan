import os
import json
import requests

class VoiceFileGenerator:
    def __init__(self, list_of_strings, output_dir="voice_files"):
        self.list_of_strings = list_of_strings
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_voice_files(self):
        for text in self.list_of_strings:
            audio_file = f"{self.output_dir}/{text}.wav"
            if not os.path.exists(audio_file):
                self.text_to_voice(text)

    def text_to_voice(self, text):
        # 音声合成処理
        # audio_query (音声合成用のクエリを作成するAPI)
        res1 = requests.post("http://localhost:50021/audio_query",
                            params={"text": text, "speaker": 1})
        # synthesis (音声合成するAPI)
        res2 = requests.post("http://localhost:50021/synthesis",
                            params={"speaker": 1},
                            data=json.dumps(res1.json()))
        # wavファイルに書き込み
        audio_file = f"{self.output_dir}/{text}.wav"
        with open(audio_file, mode="wb") as f:
            f.write(res2.content)

