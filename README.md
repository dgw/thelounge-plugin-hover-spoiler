# thelounge-plugin-hover-spoiler

Simple plugin for [The Lounge](https://thelounge.chat/) that adds CSS to
reveal spoilers (same fg & bg color) on hover

## Installation

- If you installed thelounge via npm/yarn:

   `thelounge install thelounge-plugin-hover-spoiler`

- If you installed thelounge via source:

   `node index.js install thelounge-plugin-hover-spoiler`

- If you are a user on someone else's thelounge server:

   Copy [the plugin's CSS](hover-spoiler.css) into your
   [user styles](https://thelounge.chat/docs/guides/custom-css)

## Usage

Styles are added to all clients automatically. Open clients will need to be
refreshed after installation, but The Lounge need not be restarted.

## Development

`gencss.py` is used to generate the CSS file:

```bash
python3 gencss.py > hover-spoiler.css
```

Test strings to paste in chat come from `genteststr.py`.

### Dev install

At the time of writing, The Lounge doesn't offer a way to install packages
from source without npm; it must be done manually.

The easiest way is installing `thelounge` locally and adding this plugin as a
new package in the `$THELOUNGE_HOME/packages` directory. For that you need a
`package.json` file in that `packages` dir that looks like this:

```json
{
    "private": true,
    "description": "Packages for The Lounge. All packages in node_modules directory will be automatically loaded.",
    "dependencies": {
        "thelounge-plugin-hover-spoiler": "1.0.1"
     }
}
```

The important thing here is the package name. You need to create a folder with
that name in the `node_modules` subdirectory, and place this plugin's files
(`package.json`, `index.js`, and generated `hover-spoiler.css`) inside.
Copying and pasting will work, but hardlinking or symlinking the files from
the project into the packages folder is recommended for any serious
development work. For example:

```
ln package.json /path/to/THELOUNGE_HOME/packages/node_modules/thelounge-plugin-hover-spoiler/package.json
ln index.js /path/to/THELOUNGE_HOME/packages/node_modules/thelounge-plugin-hover-spoiler/index.js
ln hover-spoiler.css /path/to/THELOUNGE_HOME/packages/node_modules/thelounge-plugin-hover-spoiler/hover-spoiler.css
```

You can then just edit the files in the local git repository folder. Changes
will be picked up any time The Lounge is restarted.

## History

I started this in a gist in November 2020:
https://gist.github.com/dgw/3aac59b4103b5ea8f4ca6e0b0f18d27b

In December 2022, I got wind that questions about this kind of spoiler tagging
were becoming quite frequent, and the link to my gist was being pasted a lot.
It seemed like it'd be nice if the CSS was available as a plugin. Fortunately
The Lounge's package API had progressed to the point of allowing such
functionality, and this plugin was born.
