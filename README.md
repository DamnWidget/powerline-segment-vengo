## Powerline extension for VenGO environments

Just a simple segment extension to add VenGO environments to powerline

### Install
Install using pip:
`pip install git+https://github.com/DamnWidget/powerline-segment-vengo.git`

### Configure

Add to your shell theme a new section containing:

```json
{
	"function": "powerlinevengo.segments.vengo.vengoenv",
    "priority": 50
},
```

Add to your `.config/powerline/colorschemes/default.json`:

```json
"vengoenv":                  { "fg": "white", "bg": "darkcyan", "attrs": [] },
```
