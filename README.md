### Run your server

There are two ways to run your server:

#### Option 1: Using `uvx` directly from git repository (recommended)

```bash
# Install the server directly from the repository
uvx --refresh --from git+https://github.com/kartaview/mcp-karta-view/
```

This method is recommended as it:
- Doesn't require cloning the repository manually
- Automatically updates when the source changes with the `--refresh` flag
- Simplifies the installation process

#### Option 2: Using `uv` with local files

If you've already cloned the repository:

```bash
# Navigate to the directory
cd path/to/mcp-karta-view

# Run the server
uv run mcp-karta-view
```

#### Option 3:
```
{
  "mcpServers": {
    ...
    "kartaview": {
      "command": "uvx",
      "args": [
        "--refresh",
        "--from",
        "git+ssh://git@github.com/kartaview/mcp-karta-view/mcp-karta-view.git",
        "mcp-karta-view"
      ]
    }
    ...
  }
}

```

### Cursor 

This project has a basic `.cursorrules` - It will be most effective if you let the cursor agent run `uvx`.