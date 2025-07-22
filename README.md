# 🐾BearATM

BearATM는 Python으로 구현된 Simple ATM(현금자동입출금기)입니다.<br>
카드 입력, PIN 인증, 계좌 선택, 입출금, 잔액조회 등 ATM의 핵심 기능을 Layered Architecture로 설계, 구현하였습니다.

## 주요 기능

- **카드 등록 및 검증**: 카드 번호로 등록 여부 확인, 등록되지 않은 카드 예외 처리
- **PIN 인증**: 카드 PIN 입력 및 검증 (틀릴 경우 예외 발생)
- **계좌 관리**: 카드에 여러 계좌 연결 및 계좌 선택
- **입금/출금**: 계좌에 대한 입금, 출금 기능 (잔액 부족, 비정상 금액에 대한 예외 처리)
- **잔액 조회**: 계좌별 잔액 확인
- **단위 테스트**: 각 기능에 대한 단위 테스트 구현
- **통합 테스트**: 카드 삽입 → PIN 인증 → 계좌 선택 → 입금/출금 등 실제 ATM 사용 시나리오 테스트 코드 포함

## 설치 및 실행 방법, 코드 구조

1. **Github clone**
    ```bash
    git clone https://github.com/shosae/ATM/
    ```
2. **가상환경 설정, 실행 및 pytest 설치**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install pytest
    ```
3. **테스트 실행**
    ```bash
    cd app
    python -m pytest
    ```

4. **코드 구조**
    ```
    app/
      ├── controller/       # ATMController: 외부 API의 접점. 요청/응답 처리
      ├── service/          # ATMService: 핵심 비즈니스 로직 처리
      ├── repository/       # ATMRepository: 데이터 영속성 관리
      ├── domain/           # Card, Account: 도메인 비즈니스 규칙을 담은 객체
      ├── exceptions/       # 커스텀 예외 정의
      ├── tests/            # pytest 테스트 코드
      ├── error_handler     # API 예외 처리 데코레이터
      └── exception_handler # 예외별 에러 응답 생성

    ```
