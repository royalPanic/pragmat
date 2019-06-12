# CommDev.py Documentation

# Commands:
## Prefix = `>`
## Utility Commands:
### Hit or Miss
>I guess I never miss, huh?

This is our bot's variant of a `ping` command, and it's simply used to prompt a response from the bot to check if it is online.
#### Usage `>hitormiss`

### Repeat
Another impractical ping variant, this simple command repeats whatever is passed as an argument. Since the bot is written in Python, it requires quotes for multi-word strings.
```
>repeat helloworld
>>> helloworld
-----------------------
>repeat hello world
>>> hello
-----------------------
>repeat "hello world"
>>> hello world
```
#### Usage `>repeat {str}`
