#!/bin/sh
set -e


gftools qa -f ../fonts/vf/Rubik[wght].ttf  -gfb --fontbakery --diffenator -o ../fonts/vf/out_roman

gftools qa -f ../fonts/vf/Rubik-Italic[wght].ttf  -gfb --fontbakery --diffenator -o ../fonts/vf/out_italic
