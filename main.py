# main.py  test.wav 파일을 텍스트로 만들어주는 코드
import whisper
model = whisper.load_model('base')

def get_transcribe(audio: str, language: str = 'ko'):
    return model.transcribe(audio=audio, language=language, verbose=True)

if __name__ == "__main__":
    result = get_transcribe(audio='/home/orin/whisper_project/input/test.wav')

    print('-'*50)
    print(result.get('text', ''))
