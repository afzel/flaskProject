#flask-client-server
Клиент-серверное взаимодействие под  flask и  linux.<br>
## Запуск сервера :
```bash
$ python app.py
 * Running on http://127.0.0.1:5000/
```
<br><br>
 
## Запуск клиента
 Чтобы получать текущую утилизацию cpu в % нам необходимо  выполнить  скрипт:
 ```bash
 awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' \
<(grep 'cpu ' /proc/stat) <(sleep 10;grep 'cpu ' /proc/stat)
```
Далее настраиваем Cron чтобы периодически выполнять скрипт
```bash
 $ crontab -e

```
Cron выражение на каждые 10 секунд
 ```bash
* * * * * /home/adminr/kor/script.sh
* * * * * sleep 10; /home/adminr/kor/script.sh
* * * * * sleep 20; /home/adminr/kor/script.sh
* * * * * sleep 30; /home/adminr/kor/script.sh
* * * * * sleep 40; /home/adminr/kor/script.sh
* * * * * sleep 40; /home/adminr/kor/script.sh
```
Теперь полученные данные отправим через curl на сервер
 ```bash
 curl -X POST -H "Content-Type: application/json" -d '@script.sh' 127.0.0.1:5000/cpu
```
 
 ![](https://github.com//afzel/flaskProject/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png) 
 
 Powered by [salohov](https://salohov.website).
