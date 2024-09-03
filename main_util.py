# main_util.py  오디오 파일 읽어서 필사 결과를 처리하는 유틸리티 코드
# chatgpt가 수정한 코드

import os
import logging
import whisper
from whisper.utils import get_writer

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Whisper 모델 로드
model = whisper.load_model('base',weights_only=True)  # torch.load에 weights_only=True를 설정하면 메모리 사용량을 줄이는 데 도움이 될 수 있습니다

def get_transcribe(audio_path: str, language: str = 'ko'):
    if not os.path.exists(audio_path):
        logging.error(f"The audio file {audio_path} does not exist.")
        return None
    try:
        return model.transcribe(audio=audio_path, language=language, verbose=True)
    except Exception as e:
        logging.error(f"Failed to transcribe the audio: {e}")
        return None

def save_file(results, output_dir='./output/', format='txt'):
    if results is None:
        logging.warning("No results to save.")
        return
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f'transcribe.{format}')
    try:
        writer = get_writer(format, output_dir)
        writer(results, output_file_path)
        logging.info(f"File saved successfully in {output_file_path}")
    except Exception as e:
        logging.error(f"Failed to save the file: {e}")

if __name__ == "__main__":
    audio_path = './input/test.wav'
    result = get_transcribe(audio_path)
    if result:
        print('-' * 50)
        print(result.get('text', ''))
        # 사용자가 지정할 수 있도록 경로와 포맷을 입력받게 수정
        output_dir = input("Enter the output directory (default './output/'): ") or './output/'
        formats = ['tsv', 'txt', 'srt']
        for format in formats:
            save_file(result, output_dir, format)


