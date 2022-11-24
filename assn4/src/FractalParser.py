import sys

class FractalParser:
    def __init__(self, filename):
        self.filename = filename

    def parser(self):
        """
        validify file/open file
        clean up data
        error checks
        make dictionary and return
        """
        # establish a default set of values
        if self.filename == '':
            dictionary = {'type': 'mandelbrot',
                          'pixels': 350,
                          'axisLength': 4.0,
                          'iterations': 50,
                          'min': {'x': -2.0, 'y': -2.0},
                          'max': {'x': 2.0, 'y': 2.0},
                          'pixelsize': 0.01142857}
            return dictionary
        else:
            rec = 0
            dictionary = {}
            file = open(self.filename)
            for line in file:
                if '#' in line:  # skip line if comment
                    pass
                else:
                    line = line.strip()  # strip whitespace
                    line = line.lower()  # make lowercase

                    if 'type' in line:  # check for required info and types
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), str):
                            dictionary['type'] = line[1].strip()
                        else:
                            print("invalid type value type")
                            sys.exit(1)
                    elif 'centerx' in line:  # check for required info and types
                        line = line.split(":")

                        rec += 1
                        if self.isTypeConvertible(line[1].strip(), float):
                            centerX = float(line[1].strip())
                        else:
                            print("invalid centerx value type")
                            sys.exit(1)

                    elif 'centery' in line:  # check for required info and types
                        line = line.split(":")
                        rec += 1
                        if self.isTypeConvertible(line[1].strip(), float):
                            centerY = float(line[1].strip())
                        else:
                            print("invalid centery value type")
                            sys.exit(1)

                    elif 'axislength' in line:  # check for required info and types
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), float):
                            axisLength = float(line[1])
                            dictionary['axisLength'] = float(line[1].strip())
                        else:
                            print("invalid axislength value type")
                            sys.exit(1)

                    elif 'pixels' in line:  # check for required info and types
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), int):
                            pixels = int(line[1])
                            dictionary['pixels'] = int(line[1].strip())
                        else:
                            print("invalid pixels value type")
                            sys.exit(1)

                    elif 'iterations' in line:  # check for required info and types
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), int):
                            dictionary['iterations'] = int(line[1].strip())
                        else:
                            print("invalid iterations value type")
                            sys.exit(1)
                    elif 'creal' in line:
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), float):
                            dictionary['creal'] = float(line[1].strip())
                        else:
                            print("invalid creal value type")
                            sys.exit(1)

                    elif 'cimag' in line:
                        line = line.split(":")
                        if self.isTypeConvertible(line[1].strip(), float):
                            dictionary['cimag'] = float(line[1].strip())
                        else:
                            print("invalid cimag value type")
                            sys.exit(1)

        if rec == 2:
            minX = centerX - (axisLength / 2.0)
            minY = centerY - (axisLength / 2.0)
            dictionary['min'] = {'x': minX, 'y': minY}
            maxX = centerX + (axisLength / 2.0)
            maxY = centerY + (axisLength / 2.0)
            dictionary['max'] = {'x': maxX, 'y': maxY}

            pixelsize = float(axisLength / pixels)
            dictionary['pixelsize'] = pixelsize
        else:
            print("missing valid centerx or centery values")
            sys.exit(1)

        # check all required data is present
        if dictionary['type'] == 'julia' or dictionary['type'] == 'burningshipjulia':
            if 'creal' not in dictionary or 'cimag' not in dictionary:
                print("missing required creal or cimag values")
                sys.exit(1)

        if 'type' not in dictionary or 'pixels' not in dictionary or \
                'axisLength' not in dictionary or 'iterations' not in dictionary or \
                'min' not in dictionary or 'max' not in dictionary or\
                'pixelsize' not in dictionary:
            print("missing required fractal values")
            sys.exit(1)

        file.close()
        return dictionary

    def isTypeConvertible(self, value, ofType):
        try:
            ofType(value)
            return True
        except ValueError:
            return False
