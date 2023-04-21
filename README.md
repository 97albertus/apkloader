# APK Loader
### APK Loader - скрипт для преобразования ссылки на страницу приложения в Play Market в прямую ссылку на загрузку APK-файла.

Требования:
* Python 3.8+
* Chrome Web Browser

Установка необходимых библиотек:
```
pip -r requirements.txt
```
Использование:
Программа принимает ссылку на страницу приложение в Play Store
```https://play.google.com/store/apps/details?id=com.twitter.android```
Ответ
```
{
  "result_link": "https://download.apkcombo.com/com.twitter.android/Twitter_9.85.0-release.0_apkcombo.com.apk?ecp=Y29tLnR3aXR0ZXIuYW5kcm9pZC85Ljg1LjAtcmVsZWFzZS4wLzI5ODUwMDAwLmUwZDlkYWE5MjJlMjg2MjUxNWFjMGE3MzZhNjE2YzUyZTgxNmNmN2EuYXBr&iat=1682058320&sig=64e9800ac5a3776fdddb68e1bff334ad&size=113351794&from=cf&version=latest&lang=ru&fp=5ef5ae05034550c2cae08371d140c129&ip=188.18.236.147"
}
```

### Каталог
* main.py - основная функция
* app.py - готовое веб-приложение на Flask, включает main.py
* chromedriver - веб драйвер для работы Selenium
* templates/index.html - html интрефейс для веб-приложения
