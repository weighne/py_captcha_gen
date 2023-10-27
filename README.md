# py_captcha_gen
Generate simple captcha images using python

### Prerequisites
* [Captcha](https://pypi.org/project/captcha/)

```
pip install captcha
```

### Usage
Running the script will randomly generate a two word phrase, using the [diceware word list](https://goblinehole.com/diceware_clean.txt), which will then be used to create a captcha image (via the [captcha library](https://github.com/lepture/captcha)). This 500x70 PNG will be dumped into the same directory as the script and named using the randomly generated words.
