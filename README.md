### whisper_jetsonmom
##### 오린에서 해보기.
### 1. Creating your environment
``` bash
orin@orin-desktop:~$ python3 --version
```
```
 결과
 Python 3.10.12
```

``` bash

orin@orin-desktop:~$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
orin@orin-desktop:~$ bash Miniconda3-latest-Linux-aarch64.sh
orin@orin-desktop:~$ /home/orin/miniconda3/bin/conda init
orin@orin-desktop:~$ source ~/.bashrc
(base) orin@orin-desktop:~$ conda --version
```
#### conda 24.7.1
``` bash
(base) orin@orin-desktop:~$ conda create -n whisper_env python=3.10
(base) orin@orin-desktop:~$ conda activate whisper_env
(whisper_env) orin@orin-desktop:~$ pip install --upgrade pip
(whisper_env) orin@orin-desktop:~$ pip install whisper_live onnxruntime numpy

```
``` bash
mkdir whisper_project
cd whisper_project
conda create --name whisper_project python=3.10
conda activate whisper_project
conda install -c conda-forge ffmpeg 
```
![Screenshot from 2024-09-03 11-14-07](https://github.com/user-attachments/assets/bd77b30c-8832-4a72-85d1-8443fe5ee2a9)


``` bash
(whisper_project) orin@orin-desktop:~/whisper_project$ conda install -c conda-forge poetry  
```

![Screenshot from 2024-09-03 11-16-35](https://github.com/user-attachments/assets/29b3cef1-d53b-4cb8-98da-6efd1a64d5d9)

``` bash
(whisper_project) orin@orin-desktop:~/whisper_project$ poetry init
```
#### This command will guide you through creating your pyproject.toml config.        
                                                                                
#### Package name [whisper_project]: ?                                                
                                           
#### 깜박거리는 커저는 답을 기다리는 것임.

#### 기본적으로 [whisper_project]가 표시된 것은 현재 프로젝트 디렉토리의 이름입니다. 이 이름을 그대로 사용하려면 그냥 ENTER를 누르시면 됩니다. 
#### Poetry가 `pyproject.toml` 파일을 생성하기 위한 설정을 도와주고 있는 것입니다. `pyproject.toml` 파일은 Python 프로젝트의 메타데이터와 종속성(의존성) 정보를 포함하는 파일입니다. 이 과정에서 #### Poetry는 프로젝트의 기본 설정을 입력받고 있습니다.

#### 지금 보시는 메시지는 프로젝트의 이름을 입력하라는 것입니다. 커서가 깜박이는 것은 사용자가 입력할 내용을 기다리고 있다는 의미입니다.
```
선택 사항

1. **기본값 수락**:
   - 기본적으로 `[whisper_project]`가 표시된 것은 현재 프로젝트 디렉토리의 이름입니다. 이 이름을 그대로 사용하려면 그냥 `ENTER`를 누르시면 됩니다.
   
2. **새로운 이름 입력**:
   - 만약 프로젝트에 다른 이름을 지정하고 싶다면, 원하는 이름을 입력한 후 `ENTER`를 누르시면 됩니다.

다음 단계

이후에도 몇 가지 추가적인 질문이 나올 수 있습니다. 각 질문에 대해 다음과 같이 응답할 수 있습니다:

- **Version [0.1.0]:** 기본 버전 번호를 지정합니다. 그냥 `ENTER`를 눌러 기본값을 수락할 수 있습니다.
- **Description []:** 프로젝트에 대한 간단한 설명을 입력할 수 있습니다. 입력하지 않고 그냥 `ENTER`를 눌러도 됩니다.
- **Author [your_name <you@example.com>, n to skip]:** 작성자 정보를 입력할 수 있습니다. 기본값을 사용하려면 `ENTER`를 누르세요.

나는 Author [None, n to skip]:  Author [None, n to skip]:  jetsonmom <jmerrier0910@gmail.com>  

- **License []:** 프로젝트의 라이선스를 지정할 수 있습니다. 기본값으로 두려면 그냥 `ENTER`를 누르세요.
- **Would you like to define your main dependencies interactively? (yes/no) [yes]:** 프로젝트에 필요한 주요 의존성을 바로 입력할 것인지 묻습니다. `yes`를 선택하면 필요한 패키지를 바로 추가할 수 있습니다.
- **Would you like to define your development dependencies interactively? (yes/no) [yes]:** 개발 중에 필요한 의존성을 추가할 것인지 묻습니다. 보통 `no`를 선택하고 나중에 필요할 때 추가합니다.

모든 입력을 마치고 나면 `pyproject.toml` 파일이 생성되고, 이 파일을 통해 프로젝트의 종속성 관리와 환경 설정을 할 수 있게 됩니다.
```
![Screenshot from 2024-09-03 11-22-49](https://github.com/user-attachments/assets/886a0dbe-cc52-4486-ba8e-830236df30c1)

``` bash
Do you confirm generation? (yes/no) [yes]

(whisper_project) orin@orin-desktop:~/whisper_project$ 
```

###   2. Installing Whisper

#### poetry add openai-whisper

![Screenshot from 2024-09-03 11-24-49](https://github.com/user-attachments/assets/0454f6fc-2eae-4539-8328-9c115f3a0635)
```
이렇게 하면 pyproject.toml 파일이 생성되고, 프로젝트의 기본 설정이 완료됩니다. 이후에는 이 파일을 바탕으로 프로젝트의 종속성 관리 및 기타 설정을 할 수 있습니다.
```

### 3.Whisper 사용하기
```
이제 Whisper가 설치되었으므로, main.py 파일을 생성하고 Whisper를 Python 패키지로 가져온 후 사용하고자 하는 모델을 로드할 수 있습니다. Whisper에는 속도와 정확도 간의 균형을 제공하는 다섯 가지 모델 크기가 있습니다.

`get_transcribe` 함수로 오디오 파일의 전사를 얻을 수 있습니다.
이 함수는 두 가지 인수를 받습니다: 오디오 경로와 언어입니다.
`audio`는 환경 내 오디오 파일의 경로를 의미하며, `language`는 오디오 파일의 언어를 지정합니다.
Whisper가 오디오의 언어를 자동으로 인식할 수는 있지만, 시작부터 언어를 정의해주면 더 정확하게 동작할 수 있습니다.
이 예시에서는 다음 오디오 파일을 사용하여 전사를 얻겠습니다.

```

### `arecord` 명령어를 사용하여 오디오 녹음을 하고, Whisper 음성을 인식하는 작업

#### 3-1. **`arecord` 명령어 사용하기**

#### 먼저, `arecord` 명령어를 사용하여 오디오를 녹음한다.

``` bash
arecord -D hw:0,0 -f cd -t wav -d 10 1.wav
```

#### 이 명령어는 `hw:0,0`에 연결된 사운드 카드에서 10초 동안 CD 품질의 WAV 파일을 녹음하여 `1.wav`라는 파일로 저장합니다.
#### 이 녹음된 파일은 Whisper 음성 인식 엔진에서 사용될 수 있습니다.

### 3-2. **Whisper 사용하기**
```
- **Whisper**: Whisper는 OpenAI에서 만든 음성 인식 모델입니다.
 Whisper를 사용하여 한국어 음성 파일을 텍스트로 변환할 수 있습니다.
Whisper의 경우, 다양한 모델 크기(속도와 정확도에 따라 다름)를 선택할 수 있습니다.
```

### 3-3. **Whisper에서 음성 인식하기 (예시 코드)**

#### Python으로 Whisper를 사용하여 녹음한 파일을 인식하는 예시는 다음과 같습니다:
#### python  test_wav.py로 저장함

``` bash
import whisper

model = whisper.load_model("base")  # 사용하려는 모델 크기를 선택
result = model.transcribe("1.wav", language="ko")  # 한국어 음성 파일을 인식
print(result["text"])  # 인식된 텍스트 출력
```

``` bash
(whisper_project) orin@orin-desktop:~/whisper_project$ python3 test_wav1.py
```
```
실행 결과 에러남.

"/home/orin/.local/lib/python3.10/site-packages/numba/__init__.py", line 45, in _ensure_critical_deps
    raise ImportError(msg)
ImportError: Numba needs NumPy 2.0 or less. Got NumPy 2.1.
오류 메시지를 보면, Whisper 패키지가 사용하는 `numba` 라이브러리가 현재 설치된 `NumPy` 버전과 호환되지 않는다는 것을 알 수 있습니다. `Numba`는 `NumPy` 2.0 이하의 버전을 필요로 하지만, 현재 설치된 `NumPy` 버전은 2.1입니다.

### 해결 방법

1. **`NumPy` 버전 다운그레이드**

`NumPy`를 호환 가능한 버전으로 다운그레이드하여 문제를 해결할 수 있습니다. Whisper와 `numba`가 제대로 작동할 수 있도록 `NumPy` 버전을 2.0 이하로 변경해 보겠습니다:
```
``` bash
pip install numpy==1.24.3
```

``` 이 명령어는 `NumPy`의 버전을 1.24.3으로 다운그레이드합니다. 이 버전은 `numba`와 호환됩니다.

2. **`NumPy` 다운그레이드 후 Whisper 코드 다시 실행**

`NumPy` 버전을 다운그레이드한 후, 이전에 작성한 Python 스크립트를 다시 실행해 보세요:

- `NumPy`의 버전을 호환되는 버전으로 다운그레이드해야 합니다.
- 다운그레이드가 완료되면, Whisper를 사용하는 스크립트를 다시 실행하여 문제가 해결되었는지 확인합니다.

이 과정을 통해 Whisper와 `numba` 라이브러리의 호환성 문제를 해결할 수 있을 것입니다.
NumPy 버전을 2.0 이하로 변경해 보겠습니다:

```
``` bash
python3 test_wav.py
```

```
아 또 에러가 
(whisper_project) orin@orin-desktop:~/whisper_project$ pip install numpy==1.24.3 
Collecting numpy==1.24.3
  Downloading numpy-1.24.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (5.6 kB)
Downloading numpy-1.24.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 5.9 MB/s eta 0:00:00
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 2.1.0
    Uninstalling numpy-2.1.0:
      Successfully uninstalled numpy-2.1.0
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
ctranslate2 4.3.1 requires pyyaml<7,>=5.3, which is not installed.
onnxruntime 1.16.0 requires protobuf, which is not installed.
whisper-live 0.5.0 requires scipy, which is not installed.
현재 발생하는 오류는 여러 패키지 간의 종속성 충돌로 인해 발생하는 것입니다. 이를 해결하기 위해 누락된 모든 패키지를 한 번에 설치하는 방법을 사용할 수 있습니다.
```

``` bash
(whisper_project) orin@orin-desktop:~/whisper_project$ pip install scipy pyyaml protobuf
```
```
결과가 다음과 같읍니다.
protobuf-5.28.0-cp38-abi3-manylinux2014_aarch64.whl (316 kB)
Installing collected packages: scipy, protobuf
Successfully installed protobuf-5.28.0 scipy-1.14.1
```
```
실행 결과

내가 원하는 프로젝트 1
음성 파일을 텍스트로 바꿈.
```
![Screenshot from 2024-09-03 11-58-38](https://github.com/user-attachments/assets/1e24d79b-2c1b-40ba-b184-e6134950f58d)
```
#### 음성이 텍스트로 변환이 됩니다.
#### 일단 과정은 설치가 힘들지만 어렵지는 않군요.

















