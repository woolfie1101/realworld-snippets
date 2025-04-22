# Tableau 사용자 역할 일괄 변경 스크립트

이 스크립트는 Tableau 서버의 사용자 역할을 일괄적으로 변경하기 위한 도구입니다.

## 기능

- 특정 조건에 맞는 사용자의 역할을 일괄 변경
- 테스트 모드 지원 (10명 제한)
- 변경 대상 사용자 미리보기 기능
- CSV 파일로 결과 저장
- 상세한 로깅 지원

## 사전 요구사항

- Python 3.10 이상
- tableauserverclient 라이브러리
- 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 설정

1. `config.py` 파일에 서버 접속 정보를 설정합니다:
```python
config = {
    'my_env': {
        'server': '서버주소',
        'username': '사용자이름',
        'password': '비밀번호'
    }
}
```

## 사용 방법

### 1. 변경 대상 사용자 미리보기 (신규 기능)

테스트 모드에서 변경될 처음 10명의 사용자 목록을 미리 확인할 수 있습니다:
```bash
python update_user_roles.py --preview
```
- 로그에 10명의 상세 정보가 표시됩니다
- `test_users_preview_[날짜시간].csv` 파일로도 저장됩니다
- 미리보기를 통해 변경 대상을 확인한 후 실제 변경을 진행할 수 있습니다

### 2. 전체 대상 사용자 확인

모든 변경 대상 사용자 목록을 확인:
```bash
python update_user_roles.py
```

### 3. 테스트 모드로 역할 변경

처음 10명의 사용자만 역할 변경 (테스트 목적):
```bash
python update_user_roles.py --update --role Explorer --test
```

### 4. 전체 사용자 역할 변경

모든 대상 사용자의 역할 변경:
```bash
python update_user_roles.py --update --role Explorer
```

## 역할 종류

사용 가능한 역할:
- Viewer
- Explorer
- ExplorerCanPublish
- Creator

## 로그 확인

- 모든 작업 내역은 `role_check_[날짜시간].log` 파일에 저장됩니다
- 변경된 사용자 목록은 CSV 파일로도 저장됩니다

## 주의사항

1. 역할 변경 전에 반드시 미리보기 기능으로 대상자를 확인하세요
2. 테스트 모드로 먼저 실행해보는 것을 권장합니다
3. 변경 작업은 되돌릴 수 없으니 신중하게 진행하세요

## 문제 해결

오류가 발생하는 경우:
1. 로그 파일을 확인하세요
2. 서버 연결 정보가 올바른지 확인하세요
3. 필요한 라이브러리가 모두 설치되어 있는지 확인하세요 