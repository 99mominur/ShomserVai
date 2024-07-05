# ShomserVai - An AI Chat Assistant

ShomserVai is an AI Chat Assistant that can be used to response your questions. ShomserVai is developed upon pai-001-chatbot-framework by Baidu, a leading Chinese technology company. 


## Features

- AI Chat Assistant
- Previous conversation history
- Registration
- login
- Logout

## Screenshot

![Example Image](https://github.com/your-username/your-repository/blob/main/images/example.png)
![Example Image](https://github.com/your-username/your-repository/blob/main/images/example.png)
![Example Image](https://github.com/your-username/your-repository/blob/main/images/example.png)

## Installation

- Install requirements.txt using `pip install -r requirements.txt`
- Change in settings.py:
    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShomserVai_db',
        "USER": "your mysql username",
        "PASSWORD": "your password",
        "HOST": "localhost",
        "PORT": 3306,
        
    }
}

 - Run `python manage.py makemigrations`
 - Run `python manage.py migrate`
 - Get an free API-KEY from [here](https://discord.gg/pawan) in `Bot` Channel and change `Openai.api_key` in `views.py` of `Bot App` using `/key` command 

```python
    openai.api_key = "Your API Key"
```
 - For first time use you have to use `/resetip` in `Bot App`, Beacause its free for one ip address.
 Bassically we are doing reverse proxy.
 - Now run `python manage.py runserver` on `manage.py` directory of `ShomserVai` Project.
 - Open `http://127.0.0.1:8000/` in your browser.
 - Enjoy!

## Usage

It's very easy to use. Just ask some questions to ShomserVai and it will answer you.


