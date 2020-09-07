## Description
Simple [anti-captcha.com](https://anti-captcha.com) compatable API (createTask/getTaskResult) to solve the Amazon's text captcha for free.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install amazoncaptcha-api

```bash
pip3 install amazoncaptcha-api
```
or
```bash
git clone https://github.com/melehin/amazoncaptcha-api
cd amazoncaptcha-api
pip3 install .
```

## Run

### Under flask development server (bind local ip)
```bash
python3 -m amazoncaptcha_api
```

### Under supervisor and gunicorn (bind external ip)
Put this snippet to */etc/supervisor/conf.d/amazoncaptcha_api.conf*
```script
[program:amazoncaptcha_api]
directory=/tmp/
command=gunicorn amazoncaptcha_api:app -b 0.0.0.0:5000
autostart=true
autorestart=true
stderr_logfile=/var/log/amazoncaptcha_api.err.log
stdout_logfile=/var/log/amazoncaptcha_api.out.log
```
And run

```bash
supervisorctl reload
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)