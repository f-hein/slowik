# Słowik 
(eng. nightingale)


Fun side-project just to play with Yandex translator API. Why Yandex? because it's easier to obtain API key from them than from Google.

### So, what's the point of this? ###
The idea was to create a small program to check how translator changes the input after a specific number of translations. All you 
have to do is to run a program and feed a word or a phrase into the system! It will then translate it a bunch of times and will return you 
translated stuff. Fun thing - you'll see every translation which happened along the way (with input/output languages)!
(ie. pl->de, de->ru, ru->gb) and at the end it will translate it back to the input language. 

### How to use it? ### 
**0.** You obtain API key from Yandex Translate (https://tech.yandex.com/translate/), create api_key.py and create
a variable inside named api_key which will hold you API key value preceded by '?key='. Example:
> api_key = "?key=your_key_goes_here"

**1.** Run main_functionality.py

**2.** Follow the instructions.

**3.** ???

**4.** Profit!

Hope y'all like it :)
