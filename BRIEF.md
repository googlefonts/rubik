## Fixing Rubik's Hebrew Character Set

The Rubik fonts are originally designed by Philipp Hubert and Sebastian Fischer at http://hubertfischer.com as part of the https://www.chrome.com/cubelab project.

Rubik is a 5 weight Roman + Italic family.

This project takes Rubik's original Hebrew designs and tries to improve proportions, spacing and design details related to correct Hebrew type design standards. The Hebrew fork of the project is designed and maintained by Meir Sadan @meirsadan.

1. Clean up glyph outlines (i.e. correct beziers and position points at extremes) and make minor adjustments to the glyphs in accordance to Hebrew type design conventions, keeping with the limited schedule set forth.
2. If necessary, complete missing glyphs such as Geresh (׳), Gershayim (״), Maqaf (־), Sheqel (₪), vowel marks (nikkud)*. Biblical cantillations will not be added nor supported.
3. Correct font metrics, focusing mainly on global font spacing (kerning pairs, if any, will be kept to a bare minimum).
4. Use Glyphs and ttfautohint to add the appropriate OpenType features for Hebrew vowel points (nikkud) positioning and TrueType hinting.
5. The font will be offered to merge back to the original Rubik project, but may also be released as "Rubik Hebrew".
6. Contribute online specimens for examining the fonts and to test them for errors to the https://github.com/impallari/Font-Testing-Page project.

