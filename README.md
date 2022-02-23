<h1> # Discord Hype Man Bot </h1>

Assign the Hype Man Bot a discordID# that hypes up the call that he joins.

<h1> ## Installation </h1>

Use git to clone this repository [git]

```bash
git clone https://github.com/Nathanrowe32/Discord-Bot-API.git
```

 Deploy a discord bot on a server through the [Discord Developer Portal] (https://discord.com/login?redirect_to=%2Fdevelopers/).
 
 While logged into the DDP follow Applications>'HYPEBOT">BOT> then copy the Token.
 
 Paste the token in constants.py.
 
 Place the hype man recipient's discord ID in targetID in constants.py.
 ```python
 targetID = DeWayne#4674
 ```
 
 Deploy on server by main.py.

<h1> ## Usage </h1>

```python
# prints "`Yo yo yo " + callers + ", i'm " + targetID + "'s hype bot! :D`"
!HypeBot()

# joins the caller's voice channel
!join()

# bot will leave any voice channel
!leave()

# bot will join caller's channel
!raid()

# list of commands will display in caller's chat.
!commands()

!
```

<h2> # Additional notes </h2>
Feel free to pull and play around, I really made this because it was fun experimenting with discord bot functionality.
Also shake some rust off the Python skills.

