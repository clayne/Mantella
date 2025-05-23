# Mantella <a href="https://www.nexusmods.com/skyrimspecialedition/mods/98631" target="_blank" style="padding-right: 8px;"><img src="./img/nexus_mods_link.png" alt="Mantella Skyrim Nexus Mods link" width="auto" height="28"/></a><a href="https://www.nexusmods.com/fallout4/mods/79747" target="_blank"><img src="./img/nexus_mods_fallout4_link.png" alt="Mantella Fallout 4 Nexus Mods link" width="auto" height="28"/></a>

<img src="./img/mantella_logo_github.png" align="right" alt="Mantella logo" width="150" height="auto">

> Bring Skyrim and Fallout 4 NPCs to life with AI

Mantella is a Skyrim and Fallout 4 mod which allows you to naturally speak to NPCs using speech-to-text ([Moonshine](https://github.com/usefulsensors/moonshine) / [Whisper](https://github.com/openai/whisper)), LLMs, and text-to-speech ([Piper](https://github.com/rhasspy/piper) / [xVASynth](https://github.com/DanRuta/xVA-Synth) / [XTTS](https://www.nexusmods.com/skyrimspecialedition/mods/113445)).  

Click below or [here](https://youtu.be/FLmbd48r2Wo?si=QLe2_E1CogpxlaS1) to see the full trailer:

<a href="https://youtu.be/FLmbd48r2Wo?si=QLe2_E1CogpxlaS1
" target="_blank"><img src="./img/mantella_trailer.gif"
alt="Mantella trailer link" width="auto" height="220"/></a>

For more details, see [here](https://art-from-the-machine.github.io/Mantella/index.html).

# Contribute
The source code for Mantella is included in this repo. Please note that this development version of Mantella is prone to error and is not recommended for general use. See [here](https://www.nexusmods.com/skyrimspecialedition/mods/98631) for the latest stable release.

Here are the quick steps to get set up:

1. Clone the repo to your machine
2. Create a virtual environment via `py -3.11 -m venv MantellaEnv` in your console (Mantella requires Python 3.11)
3. Start the environment in your console (`.\MantellaEnv\Scripts\Activate`)
4. Install the required packages via `pip install -r requirements.txt`
5. Create a file called `GPT_SECRET_KEY.txt` and paste your secret key in this file
6. Set up your paths / any other required settings in the `config.ini`
7. Run Mantella via `main.py` in the parent directory

If you have any trouble in getting the repo set up, please reach out on [Discord](https://discord.gg/Q4BJAdtGUE)!

Related repos:
- Mantella Spell (Skyrim): [https://github.com/art-from-the-machine/Mantella-Spell](https://github.com/art-from-the-machine/Mantella-Spell)
- Mantella Gun (Fallout 4): [https://github.com/YetAnotherModder/Fallout-4-VR-Mantella-Mod](https://github.com/YetAnotherModder/Fallout-4-Mantella-Mod)
- Mantella Gun (Fallout 4 VR): [https://github.com/YetAnotherModder/Fallout-4-VR-Mantella-Mod](https://github.com/YetAnotherModder/Fallout-4-VR-Mantella-Mod)

Updates made on one repo are often intertwined with the other, so it is best to ensure you have the latest versions of each when developing.

The source files for the [Mantella docs](https://art-from-the-machine.github.io/Mantella) are stored in the [gh-pages branch](https://github.com/art-from-the-machine/Mantella/tree/gh-pages).

# Attributions
Mantella uses material from the "[Skyrim: Characters](https://elderscrolls.fandom.com/wiki/Category:Skyrim:_Characters)" articles on the [Elder Scrolls wiki](https://elderscrolls.fandom.com/wiki/The_Elder_Scrolls_Wiki) at [Fandom](https://www.fandom.com/) and is licensed under the [Creative Commons Attribution-Share Alike License](https://creativecommons.org/licenses/by-sa/3.0/).
