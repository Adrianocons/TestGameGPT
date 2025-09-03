# TestGameGPT

This repository contains a simple roguelite, turn-based strategy prototype inspired by *The Battle of Polytopia*.
It features a small playable demo where you steer a unit on a procedurally generated map.

For Windows-specific setup instructions, see [WINDOWS_SETUP.md](WINDOWS_SETUP.md).

## Running

Interactive demo (requires pygame):

```bash
python -m polythorogue.gui
```

Use the arrow keys to move your unit. Reach the village tile to win and avoid the roaming enemy. Press `R` to restart after the game ends.

## Testing

Run the test suite with:

```bash
pytest
```
