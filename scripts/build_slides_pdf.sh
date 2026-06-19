#!/usr/bin/env bash
set -euo pipefail

npx @marp-team/marp-cli training/slides.md --pdf --output training/slides.pdf
echo "PDF generado en training/slides.pdf"
