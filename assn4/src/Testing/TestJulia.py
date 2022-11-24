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

import unittest
import FractalParser
import PaletteFactory
import colour

# autocmd BufWritePost <buffer> !python3 runTests.py  	         	  


class TestJulia(unittest.TestCase):
    def test_values_present(self):
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        self.assertEqual(dictionary['type'], 'mandelbrot')
        self.assertEqual(int(dictionary['pixels']), 350)
        self.assertEqual(dictionary['axisLength'], 4.0)
        self.assertEqual(int(dictionary['iterations']), 50)

    def test_parser(self):
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        self.assertEqual(type(dictionary), dict)

    def test_dictionaryLength(self):
        keyCount = 0
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        for key in dictionary.keys():
            keyCount += 1
        self.assertEqual(7, keyCount)

    def test_palette_object(self):
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        paletteClass = PaletteFactory.PaletteFactory('palette1', dictionary)
        palette = paletteClass.makePalette()
        self.assertEqual(type(palette.getColor(5)), colour.Color)

    def test_palette_list(self):
        constructor = FractalParser.FractalParser('')
        dictionary = constructor.parser()
        paletteClass = PaletteFactory.PaletteFactory('palette1', dictionary)
        palette = paletteClass.makePalette()
        self.assertEqual(type(palette.colors), list)
        self.assertEqual(type(palette.colors[5]), str)


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
