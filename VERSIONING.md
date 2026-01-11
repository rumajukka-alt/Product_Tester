# Versioning

This project keeps the authoritative version in the top-level `VERSION` file.

Purpose:
- Ensure the UI (from `Assets/branding.json`) and other places using the version show the same value.

Behavior:
- `Assets/branding.py` will read the top-level `VERSION` file and, if it differs
  from `Assets/branding.json`, update `branding.json` on disk so the two stay
  consistent.
- You can also run the provided helper script to sync files explicitly:

```bash
python tools/sync_version.py
```

Workflow when bumping a version:
1. Update `VERSION` with the new version string (e.g. `1.2.3`).
2. Run `python tools/sync_version.py` (or start the app once; `branding.py` will update the file automatically).
3. Commit the updated `VERSION` and `Assets/branding.json` together.

Notes:
- The helper script and runtime update will overwrite `Assets/branding.json`'s `version` field to match `VERSION`.
- After updating files, commit changes so the repository reflects the new version.
