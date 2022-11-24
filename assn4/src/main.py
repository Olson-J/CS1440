#!/usr/bin/env python3

#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  

import sys
import FractalFactory
import ImagePainter
import FractalParser
import PaletteFactory


def main():
    """
    if no arguments given, run program with default values
        create a fractal and palette object
    if only filename given, use default palette
        create a fractal and palette object
    if both arguments given, run program with them
        create a fractal and palette object
    call imagePainter to create image
    """
    if len(sys.argv) == 1:  # no filename given, defaults
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        fracConstruct = FractalFactory.FractalFactory(dictionary)
        fractal = fracConstruct.factory()

        paletteClass = PaletteFactory.PaletteFactory('',dictionary)
        palette = paletteClass.makePalette()

    elif len(sys.argv) == 2:  # filename, default palette
        constructor = FractalParser.FractalParser(sys.argv[1])
        dictionary = constructor.parser()
        fracConstruct = FractalFactory.FractalFactory(dictionary)
        fractal = fracConstruct.factory()

        paletteClass = PaletteFactory.PaletteFactory('', dictionary)
        palette = paletteClass.makePalette()

    else:  # no defaults
        constructor = FractalParser.FractalParser(sys.argv[1])
        dictionary = constructor.parser()
        fracConstruct = FractalFactory.FractalFactory(dictionary)
        fractal = fracConstruct.factory()

        paletteClass = PaletteFactory.PaletteFactory(sys.argv[2], dictionary)
        palette = paletteClass.makePalette()

    image = ImagePainter.ImagePainter(fractal, palette)
    image.picture()


main()
