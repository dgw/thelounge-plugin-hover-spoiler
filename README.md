# thelounge-plugin-hover-spoiler
Simple plugin for The Lounge that adds CSS to reveal spoilers (same fg &amp; bg color) on hover

## History
Based on my (apparently popular) Gist: https://gist.github.com/dgw/3aac59b4103b5ea8f4ca6e0b0f18d27b

## Development
`gencss.py` is used to generate the CSS file:

```bash
python3 gencss.py > hover-spoiler.css
```

Test strings to paste in chat come from `genteststr.py`.
