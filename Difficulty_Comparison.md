<p align="center">
  <a href="https://github.com/PycraftDeveloper" target="_blank" rel="noreferrer"><img src="https://github.com/PycraftDeveloper/Pycraft/assets/81379254/66cf677f-b4c9-4ee3-b487-69243f01ba34" alt="my banner"></a>
</p>

Pycraft is an OpenGL, open world, video game made entirely with Python. This project is a game to shed some light on OpenGL programming in Python as it is a seldom touched area of Python's vast amount of uses. Feel free to give this project a run, and message us if you have any feedback! <br />
Made with Python 3 64-bit and Microsoft Visual Studio Code.

[![](https://img.shields.io/badge/python-3.10-blue.svg)](www.python.org/downloads/release/python-3100) [![](https://img.shields.io/badge/python-3.9-blue.svg)](www.python.org/downloads/release/python-390) [![](https://img.shields.io/badge/python-3.8-blue.svg)](www.python.org/downloads/release/python-380) [![](https://img.shields.io/badge/python-3.7-blue.svg)](www.python.org/downloads/release/python-370) <br />
![](https://img.shields.io/github/license/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/stars/PycraftDeveloper/Pycraft) ![GitHub all releases](https://img.shields.io/github/downloads/PycraftDeveloper/Pycraft/total) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/PycraftDeveloper/Pycraft) ![GitHub repo size](https://img.shields.io/github/repo-size/PycraftDeveloper/Pycraft)

## Game Difficulty in Pycraft

In versions of Pycraft newer than pycraft v9.5.5, a new concept of difficulty has been added to the game. There are two different difficulties:

* Normal mode: In this version, all game mechanics are at their default values and behaviours. This makes it easier than hard mode, but is still designed to be challenging enough to keep the player interested as they progress.
* Hard mode: In this game mode, some values and game mechanics are changed to make Pycraft harder to play, but they are not intended to make the game impossible to play or frustrating, they are designed to challenge more experienced players.

When choosing a game mode in Pycraft, which is done when the user first creates that game, the difficulty cannot be adjusted later down the line through Pycraft, however there are work arounds by modifying the ``game.json`` file - not that we would tell you how to do do this. There are no rules in Pycraft that would prevent you from doing this, and it shouldnt also cause any game breaking behaviours - however because it isn't strictly a feature, there is no guarrantee of this.

## A Comparison Between Normal and Hard Mode

Here is a comprehensive list of all the changes that will (or have) been added to Pycraft to diofferentiate the two different difficulties. This list may be changed at any time, and lists the intended behaviour in normal mode and how that differs in hard mode, and also looks at wether the feature in question has been added to Pycraft yet (corresponding to the version of the game this file belongs to).

|Normal mode game mechanic|Hard mode game mechanic|Currently implimented in Pycraft|
|---|---|---|
|The player starts with 4 hearts by default|The player starts with 3 hearts by default|❌|
|The player is allowed 3 saves and 3 auto-saves, therefore a total of 6 saves can be made|In hard mode, that is reduced by 1 for both saves and auto-saves, meaning that only a total of 4 saves can be made|❌|
|Combat oriented entities (COEs) have 8, 16, 32, 64, 128, 256 and 512 health|Combat oriented entities (COEs) have 16, 32, 64, 128, 256, 512 and 1024 health|❌|
|Combat oriented entities (COEs) do not regenerate health|Combat oriented entities (COEs) do regenerate health after 2.5 minutes of inactivity|❌|
|Combat oriented entities (COEs) do not have a probability of spawning with potion effects|Combat oriented entities (COEs) have a small probability of spawning with potion effects, with the probability increasing based on base health. Additionally, top level COEs with 1024 base health, have a very small probability of spawning with two potion effects, or one stronger effect|❌|
|Loot from chests has a normally distributed probability|Loot from chests has a normally distributed probability with a slight skew towards lower value items|❌|
|You can get up to 3 different items from the same chest|You can get up to 4 different items from the same chest, although the probability is very small|❌|
|The loot from chests is as normal|The loot from chests is more likely to be a higher value, when a higher value item is drawn|❌|
|There is no change in the mechanics of bosses specifically, however other changed game mechanics do still apply|There is no change in the mechanics of bosses specifically, however other changed game mechanics do still apply|❌|
|The range of being noticed by a Combat oriented entity (COE) is less than in hard mode|The range of being noticed by a Combat oriented entity (COE) is less than in hard mode|❌|
