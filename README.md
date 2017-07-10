# Rubik Fonts

The Rubik Fonts project was initiated as part of the [Chrome CubeLab](https://www.chrome.com/cubelab) project.

Rubik is a 5 weight Roman + Italic family. 
Rubik Mono One is paired with Rubik One, a proportionally spaced variation of the design.

Rubik supports the Latin, Cyrillic and Hebrew scripts. 
The Latin and Cyrillic were designed by Philipp Hubert and Sebastian Fischer at [Hubert Fischer](http://hubertfischer.com).

The Hebrew was initially designed by Philipp and Sebastian, and then revised by type designer and Hebrew native reader Meir Sadan to adjust proportions, spacing and other design details. 

Cyrillic was initially designed by Philipp and Sebastian, and then revised and expanded by Cyreal Fonts Team (Alexei Vanyashin and Nikita Kanarev). Exising glyphs were improved, and glyph set was expanded to GF Cyrillic Plus.


#### License

Licensed under the SIL Open Font License (v1.1)

#### Hebrew Revision, 2015

The Hebrew revision project was undertaken in 2015 and included:

1. Adjusting glyph outlines with better bezier handle positions and points placed at extremes, and minor adjustments to the glyphs in accordance to Hebrew type design conventions.
2. Where necessary completing missing glyphs such as Geresh (׳), Gershayim (״), Maqaf (־), Sheqel (₪), vowel marks (nikkud)*. Biblical cantillations were not be added or supported at this time.
3. Font metrics were updated, with a focus on metrics rather than kerning pairs (which were kept to a bare minimum.
4. The Glyphs editor and ttfautohint were used to add appropriate OpenType features for Hebrew vowel points (nikkud) positioning and TrueType hinting.
5. The fonts were reviewed by Philipp and Sebastian and merged back into the original Rubik project.

Meir also contributed to the [github.com/impallari/Font-Testing-Page](https://github.com/impallari/Font-Testing-Page) project with [Hebrew test specimens](http://www.impallari.com/testing/index-hebrew.php) for examining the fonts and testing them for errors.

#### Cyrillic Revision and Expansion, 2016. Version 2.000

The Cyrillic revision was undertaken in 2016 and included:

1. Improving existing Cyrillic glyphs, and further glyph set expansion to GF Cyrillic Plus.
2. Cyrillic font metrics were revised.
3. The fonts were reviewed by Philipp and Sebastian. 
4. Existing source files were ported to Glyphs App, and made compatible. Existing hinting was removed, and fonts were ttfautohinted in Glyphs App. 

#### Source Files v.2.001
In January 2017 all the source files have moved to `.glyphs` format.

Hebrew uses a different interpolation gain than Latin for better interscript coherency. To accomodate these differences `Local Interpolation` parameter has been applied to the Hebrew range in the sources files.


Style | Hebrew scheme | Latin scheme | Local Interpolation for Hebrew
--- | --- | --- | ---
Light (Master) | 200 | 60 | - 
Regular | 300 | 90 | 86
Medium | 450 | 125 | 126.5
Bold | 600 | 160 | 166
Black (Master) | 800 | 220 | - 


#### Source Files v2.100
In June 2017 the .ttfs are now manually hinted using [VTT](https://www.microsoft.com/en-us/Typography/vtt.aspx). To build the manually hinted fonts, follow the Generating hinted ttfs instructions.


#### Generating hinted ttfs
```
# fontTools is the only required dependency.

$ cd sources
$ python generate_hinted_ttfs.py
```
