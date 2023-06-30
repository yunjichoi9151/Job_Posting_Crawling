from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# WebDriver 인스턴스 생성
driver = webdriver.Chrome()

# 네이버 인재영입 페이지 접속
print('\n[NAVER]\n')
naver_url = 'https://recruit.navercorp.com/rcrt/list.do?subJobCdArr=1010001%2C1010002%2C1010003%2C1010004%2C1010005%2C1010006%2C1010007%2C1010008%2C1010020%2C1020001%2C1030001%2C1030002%2C1040001%2C1050001%2C1050002%2C1060001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=&sw=&subJobCdData=1010001&subJobCdData=1010002&subJobCdData=1010003&subJobCdData=1010004&subJobCdData=1010005&subJobCdData=1010006&subJobCdData=1010007&subJobCdData=1010008&subJobCdData=1010020&subJobCdData=1020001&subJobCdData=1030001&subJobCdData=1030002&subJobCdData=1040001&subJobCdData=1050001&subJobCdData=1050002&subJobCdData=1060001'
driver.get(naver_url)
naver_num = 1

# 네이버 채용공고 리스트 가져오기
naver_job_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'card_list')]")))

# 네이버 채용공고 각각 가져오기
naver_job_elements = naver_job_list.find_elements(By.XPATH, ".//li[contains(@class, 'card_item')]")

# 각 채용공고 출력
for naver_job_element in naver_job_elements:
    # 채용공고 제목
    naver_job_title_element = naver_job_element.find_element(By.XPATH, ".//h4[@class='card_title']")
    naver_job_title = naver_job_title_element.text
    naver_job_info_element = driver.find_element(By.CLASS_NAME, 'card_info')
    # 모집 부서
    naver_job_department_element = naver_job_info_element.find_element(By.XPATH, ".//dt[text()='모집 부서']")
    naver_job_department_dd = naver_job_department_element.find_element(By.XPATH, "following-sibling::dd[@class='info_text']")
    naver_job_department = naver_job_department_dd.text.strip()

    # 모집 분야
    naver_job_field_element = naver_job_info_element.find_element(By.XPATH, ".//dt[text()='모집 분야']")
    naver_job_field_dd = naver_job_field_element.find_element(By.XPATH, "following-sibling::dd[@class='info_text']")
    naver_job_field = naver_job_field_dd.text.strip()

    # 모집 경력
    naver_job_career_element = naver_job_info_element.find_element(By.XPATH, ".//dt[text()='모집 경력']")
    naver_job_career_dd = naver_job_career_element.find_element(By.XPATH, "following-sibling::dd[@class='info_text']")
    naver_job_career = naver_job_career_dd.text.strip()

    # 근로 조건
    naver_job_employment_element = naver_job_info_element.find_element(By.XPATH, ".//dt[text()='근로 조건']")
    naver_job_employment_dd = naver_job_employment_element.find_element(By.XPATH, "following-sibling::dd[@class='info_text']")
    naver_job_employment = naver_job_employment_dd.text.strip()

    # 모집 기간
    naver_job_recruitment_element = naver_job_info_element.find_element(By.XPATH, ".//dt[text()='모집 기간']")
    naver_job_recruitment_dd = naver_job_recruitment_element.find_element(By.XPATH, "following-sibling::dd[@class='info_text']")
    naver_job_recruitment_period = naver_job_recruitment_dd.text.strip()
    # 출력
    print(naver_num, '. ', naver_job_title, sep='')
    print(' ' * (int)(len(str(naver_num)) + 1), '[', naver_job_department, '|', naver_job_recruitment_period, '|', naver_job_field, '|', naver_job_career, '|', naver_job_employment, ']')
    naver_num += 1
time.sleep(3)

# 카카오 인재영입 페이지 접속
print('\n[kakao]\n')
kakao_url = 'https://careers.kakao.com/jobs'
driver.get(kakao_url)
kakao_num = 1

# 카카오 채용공고 리스트 가져오기
kakao_job_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'list_jobs')))

# 카카오 채용공고 각각 가져오기
kakao_job_elements = kakao_job_list.find_elements(By.TAG_NAME, 'li')

# 각 채용공고 출력
for kakao_job_element in kakao_job_elements:
    # 채용공고 제목
    kakao_job_title_element = kakao_job_element.find_element(By.CLASS_NAME, 'tit_jobs')
    kakao_job_title = kakao_job_title_element.text
    # 채용공고 영입마감일
    kakao_endtime_element = kakao_job_element.find_element(By.XPATH, './/dt[@class="screen_out"][text()="영입마감일"]')
    kakao_endtime = kakao_endtime_element.find_element(By.XPATH, './following-sibling::dd').text
    # 채용공고 회사정보
    kakao_company_element = kakao_job_element.find_element(By.XPATH, './/dt[@class="screen_out"][text()="회사정보"]')
    kakao_company = kakao_company_element.find_element(By.XPATH, './following-sibling::dd').text
    # 채용공고 직원유형
    kakao_type_element = kakao_job_element.find_element(By.XPATH, './/dt[@class="screen_out"][text()="직원유형"]')
    kakao_type = kakao_type_element.find_element(By.XPATH, './following-sibling::dd').text
    # 출력
    print(kakao_num, '. ', kakao_job_title, sep='')
    print('   [ ', kakao_company, ' | ', kakao_type, ' | ', kakao_endtime, ' ]', sep='')
    kakao_num += 1
time.sleep(3)

# LG 인재영입 페이지 접속
print('\n[LG]\n')
url = 'https://careers.lg.com/app/job/RetrieveJobNotices.rpi'
driver.get(url)
LG_num = 1

# LG 분야 버튼 클릭
wait = WebDriverWait(driver, 10)
field_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="lnb"]/div[1]/ul/li[2]/div[1]/button')))
field_button.click()
time.sleep(3)

# LG IT서비스 버튼 클릭
it_service_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="lnb"]/div[1]/ul/li[2]/div[2]/div/ul/li[7]/a')))
it_service_button.click()
time.sleep(3)

# LG 채용공고 리스트 가져오기
LG_job_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jobNoticesList"]/div')))

# LG 채용공고 각각 가져오기
LG_job_elements = LG_job_list.find_elements(By.XPATH, './/div[contains(@id, "scroll_")]')

# 각 채용공고 출력
for LG_job_element in LG_job_elements:
    # 채용공고 제목
    LG_job_title_element = LG_job_element.find_element(By.XPATH, './/ul[@class="adListTitle"]/li/a')
    LG_job_title = LG_job_title_element.text
    # 채용공고 상세정보(회사, 경력여부, 분야, 마감일)
    adListInfo_elements = LG_job_element.find_elements(By.XPATH, './/ul[@class="adListInfo"]/li')
    LG_job_info = []
    for element in adListInfo_elements:
        LG_job_info.append(element.text.strip())
    # 출력
    print(LG_num, '. ', LG_job_title, ' [', LG_job_info[0][0:-16], ']', sep='')
    print(' ' * (int)(len(str(LG_num)) + 2), '[ ', LG_job_info[1], ' | ', LG_job_info[2], ' | ', LG_job_info[3], ' | ', LG_job_info[0][-16:], ' ]', sep='')
    LG_num += 1

# 현대오토에버 채용정보 페이지 접속
print('\n[현대오토에버]\n')
url = 'https://hyundai-autoever.recruiter.co.kr/app/jobnotice/list'
driver.get(url)
AutoEver_num = 1

# 현대오토에버 신입채용 버튼 클릭
wait = WebDriverWait(driver, 10)
filed_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divTabList"]/ul/li[2]/a')))
filed_button.click()
time.sleep(3)

# 현대오토에버 채용공고 리스트 가져오기
AutoEver_job_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='divJobnoticeList']/ul")))

# 현대오토에버 채용공고 각각 가져오기
AutoEver_job_elements = AutoEver_job_list.find_elements(By.XPATH, ".//li")

# 각 채용공고 출력
for AutoEver_job_element in AutoEver_job_elements:
    # 채용공고 제목
    AutoEver_title_element = AutoEver_job_element.find_element(By.XPATH, ".//h2[@class='list-bbs-title']/span[@class='list-bbs-notice-name']/a")
    AutoEver_title = AutoEver_title_element.text
    # 채용공고 접수기간
    AutoEver_date_element = AutoEver_job_element.find_element(By.XPATH, ".//span[@class='list-bbs-date']")
    AutoEver_date = AutoEver_date_element.text
    # 채용공고 상태
    AutoEver_status_element = AutoEver_job_element.find_element(By.XPATH, ".//div[@class='list-bbs-status']/span")
    AutoEver_status = AutoEver_status_element.text
    # 출력
    print(AutoEver_num, '. ', AutoEver_title, sep='')
    print(' ' * (int)(len(str(AutoEver_num)) + 2), '[ ', AutoEver_status, ' | ', AutoEver_date, ' ]', sep='')
    AutoEver_num += 1
# WebDriver 종료
driver.quit()