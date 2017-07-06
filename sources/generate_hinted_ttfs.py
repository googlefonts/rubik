from fontTools.ttLib import TTFont, newTable
import os


def get_fonts(path):
    fonts = {}
    for f in os.listdir(path):
        if f.endswith('ttf'):
            font_path = os.path.join(path, f)
            font = TTFont(font_path)
            fonts[f] = font
    return fonts


def transfer_glyfs(from_font, to_font):
    glyphs = to_font['glyf'].keys()

    for glyph in glyphs:
        print 'Transferring %s' % glyph
        to_font['glyf'][glyph] = from_font['glyf'][glyph]


def main():
    hinted_dir = 'hinted_ttfs'
    unhinted_dir = os.path.join('..', 'fonts', 'ttf')

    hinted_fonts = get_fonts(hinted_dir)
    unhinted_fonts = get_fonts(unhinted_dir)

    shared_fonts = set(hinted_fonts.keys()) & set(unhinted_fonts.keys())
    for name in shared_fonts:

        shipped_font_path = os.path.join(unhinted_dir, name)
        transfer_glyfs(hinted_fonts[name],
                       unhinted_fonts[name])
        
        unhinted_fonts[name]['cvt '] = hinted_fonts[name]['cvt ']
        unhinted_fonts[name]['fpgm'] = hinted_fonts[name]['fpgm']
        unhinted_fonts[name]['prep'] = hinted_fonts[name]['prep']
        unhinted_fonts[name]['gasp'] = hinted_fonts[name]['gasp']


        unhinted_fonts[name]['TSI0'] = hinted_fonts[name]['TSI0']
        unhinted_fonts[name]['TSI1'] = hinted_fonts[name]['TSI1']
        unhinted_fonts[name]['TSI2'] = hinted_fonts[name]['TSI2']
        unhinted_fonts[name]['TSI3'] = hinted_fonts[name]['TSI3']
        
        os.remove(shipped_font_path)
        unhinted_fonts[name].save(shipped_font_path)
    

    print 'done'

if __name__ == '__main__':
    main()
