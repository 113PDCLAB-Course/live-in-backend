# LiveIn Backend
ubuntu 18.04
python 3.6.9
python 2.7.17
mysql 14.14
apache 2.4.29

## Quick Start
### Requirement 
* docker 
* docker-compose 
* 填入重要資訊給 `./live_in_backend/.env`
```env
# PostgreSQL
POSTGRES_HOST= # 如果用 container，直接寫 container name 
POSTGRES_DB=live_in_backend
POSTGRES_USER= # superuser: postgres
POSTGRES_PASSWORD=
POSTGRES_PORT=5432

# Google API
GOOGLE_MAP_API_KEY=

# SECRET_KEY
SECRET_KEY=  # 任意填入， django 用於加密用
```
* 使用 `docker-compose --env-file ./live_in_backend/.env up -d ` 開啟
    * 如果兩個服務中有東西建立失敗，可用 `docker exec -it <container name> bash` 來見查
* **First start 則需要在加入兩個指令**
```
docker exec -it live_in_backend bash
# 進入 live_in_backend container 
live_in_backend# python manage.py migrate
live_in_backend# python manage.py loaddata
```

### 一點點簡單的 API TEST 文件
* get job 資料 `http://<localhost>:8000/api/jobs/?address=%E6%9D%B1%E5%9C%92%E8%A1%9728%E5%B7%B727%E8%99%9F%E5%9B%9B%E6%A8%93&district=6&min_salary=0`
  * 參數 `address`: 你的地址
  * 參數 `distinct`: 區域是 pk 值，紀錄在 json 文件
  * 參數 `min_salary`: 最低要求薪水
  * example: `http://<localhost>:8000/api/jobs/?address=%E6%9D%B1%E5%9C%92%E8%A1%9728%E5%B7%B727%E8%99%9F%E5%9B%9B%E6%A8%93&district=6&min_salary=0`
* post job 資料 `http://<localhost>:8000/api/jobs/`
  * 參數
    * url 網址
    * name 公司名稱
    * salary 薪水
    * tenure 需要滿足多少以上工作經驗
    * address 工作地址
    * distinct 區域
    * job_position 工作職稱
    * woring_hour 工作是日班還是夜班
    * benefit(optimal) 好處
  * example body:
```
{"url": "https://www.1111.com.tw/job/130452265", "name": "棉花田生機園地股份有限公司", "salary": 40000, "tenure": 0, "address": "台北市中正區忠孝西路一段66號22樓 ( 距離台北車站走路約 5 分鐘 )", "district": 6, "job_position": 3, "working_hour": 1, "benefit": [],  "coordinate": "25.02454,121.30551"}
```
