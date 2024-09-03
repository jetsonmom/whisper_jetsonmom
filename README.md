### whisper_jetsonmom
##### 오린에서 해보기.
### 1. Creating your environment
``` bash
orin@orin-desktop:~$ python3 --version
```
# 결과
# Python 3.10.12
``` bash

orin@orin-desktop:~$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
orin@orin-desktop:~$ bash Miniconda3-latest-Linux-aarch64.sh
orin@orin-desktop:~$ /home/orin/miniconda3/bin/conda init
orin@orin-desktop:~$ source ~/.bashrc
(base) orin@orin-desktop:~$ conda --version
```
# conda 24.7.1
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
####This command will guide you through creating your pyproject.toml config.        
                                                                                
####Package name [whisper_project]: ?                                                
                                           
#### 깜박거리는 커저는 답을 기다리는 것임.

#### 기본적으로 [whisper_project]가 표시된 것은 현재 프로젝트 디렉토리의 이름입니다. 이 이름을 그대로 사용하려면 그냥 ENTER를 누르시면 됩니다. 
#### Poetry가 `pyproject.toml` 파일을 생성하기 위한 설정을 도와주고 있는 것입니다. `pyproject.toml` 파일은 Python 프로젝트의 메타데이터와 종속성(의존성) 정보를 포함하는 파일입니다. 이 과정에서 #### Poetry는 프로젝트의 기본 설정을 입력받고 있습니다.

#### 지금 보시는 메시지는 프로젝트의 이름을 입력하라는 것입니다. 커서가 깜박이는 것은 사용자가 입력할 내용을 기다리고 있다는 의미입니다.
```
### 선택 사항

1. **기본값 수락**:
   - 기본적으로 `[whisper_project]`가 표시된 것은 현재 프로젝트 디렉토리의 이름입니다. 이 이름을 그대로 사용하려면 그냥 `ENTER`를 누르시면 됩니다.
   
2. **새로운 이름 입력**:
   - 만약 프로젝트에 다른 이름을 지정하고 싶다면, 원하는 이름을 입력한 후 `ENTER`를 누르시면 됩니다.

### 다음 단계

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

