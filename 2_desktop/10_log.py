# import logging

# # logging.basicConfig(level= logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# logging.basicConfig(level= logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < warning < error < critical 
# logging.debug("아 이거 누가 짠거야~~")
# logging.info(" 자동화 수행 준비")
# logging.warning(" 이스크립트는 오래 되었습니다. 실행에 문제 있습니다")
# logging.error("에러발생.. 에러코드는 ....")
# logging.critical("복구불가능한 심한문제 발생....")
from datetime import datetime
import logging
# 시간 [로그레벨] 메세지   형태로 로그작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
#로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
stHandler = logging.StreamHandler()
stHandler.setFormatter(logFormatter)
logger.addHandler(stHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m$d%H%M%S.log")
flHandler = logging.FileHandler(filename, encoding="utf-8")
flHandler.setFormatter(logFormatter)
logger.addHandler(flHandler)

logging.error(" 에러발생...")
logging.debug("이거 누가 짠거야")