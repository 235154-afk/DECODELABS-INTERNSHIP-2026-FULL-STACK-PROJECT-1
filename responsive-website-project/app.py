from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent


def _to_data_uri(file_path: Path) -> str:
    suffix = file_path.suffix.lower()
    mime_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }
    mime = mime_map.get(suffix, "application/octet-stream")
    encoded = base64.b64encode(file_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def build_embedded_site() -> str:
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "styles" / "main.css").read_text(encoding="utf-8")
    js = (ROOT / "scripts" / "main.js").read_text(encoding="utf-8")

    index_html = index_html.replace(
        '<link rel="stylesheet" href="styles/main.css">',
        f"<style>\n{css}\n</style>",
    )
    index_html = index_html.replace(
        '<script src="scripts/main.js"></script>',
        f"<script>\n{js}\n</script>",
    )

    logo_path = ROOT / "assets" / "logo.jpeg"
    if logo_path.exists():
        index_html = index_html.replace(
            'src="assets/logo.jpeg"', f'src="{_to_data_uri(logo_path)}"'
        )

    return index_html


st.set_page_config(
    page_title="Muhammad Talal Tariq | Internship Project 1",
    layout="wide",
    initial_sidebar_state="collapsed",
)

site_html = build_embedded_site()
components.html(site_html, height=3200, scrolling=True)
