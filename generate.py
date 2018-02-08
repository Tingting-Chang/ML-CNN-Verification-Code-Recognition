import random   
from PIL import Image, ImageDraw, ImageFont, ImageFilter   

try:
    import StringIO 
except ImportError:
    from io import StringIO, BytesIO      


class GenerateVerifiCode():
    def __init__(self):
        self.size = (120, 30)    # size:  Picture size ， format （ wide ， high ）， By default (120, 30)    
        self.length = 6          # length:  Number of verification code characters 

        self.chars = self.get_chars()      # chars:  Allowed character set ， Format string 
        self.font_type = self.get_font('') # Verification code font ， By default  arial.ttf
        self.font_size = 18                # Verification code font size 

        self.bg_color = (255, 255, 255)    # background color ， Default is white 
        self.fg_color = (0, 0, 255)        # Front view ， Verification code character color ， Default is blue #0000FF

        self.n_line = (1, 2)               # Range of the number of interference lines ， Format tuple ， By default (1, 2)，
        self.point_chance = 2              # Probability of interference point ， Size range [0, 100]

        self.image_type = 'JPEG'           # Picture save format ， By default GIF， Optional for GIF，JPEG，TIFF，PNG
        self.img = Image.new("RGB", self.size, self.bg_color)  #  Create graphics 
        self.draw = ImageDraw.Draw(self.img)  # Create brush



    def get_font(self, font_name):
        default_font = "/Library/Fonts/arial.ttf"  #  Verification code font 
        if font_name == '':
            return default_font    
        else:
            return "/Library/Fonts/" + font_name + ".ttf"
    
    def get_chars(self):
        _lower_cases = "abcdefghjkmnpqrstuvwxy"            #  Lowercase letters 
        _upper_cases = "ABCDEFGHJKLMNPQRSTUVWXY"           #  Capital 
        _numbers = "1234567890"                            #  number 
        init_chars = ''.join((_lower_cases, _upper_cases, _numbers))  #  Generating a set of allowed characters 
        return init_chars

    def get_rand_strs(self, length):
        """ Return random string by given length """
        if len(self.chars) == 0: raise Exception('The vocab used to generate random string is empty!!!') 
        return "".join(random.sample(self.chars, length))


    def create_strs(self):
        """ Draw verification code character """
        c_chars = self.get_rand_strs(self.length)
        strs = ' %s ' % ' '.join(c_chars)
        font = ImageFont.truetype(self.font_type, self.font_size)
        font_width, font_height = font.getsize(strs)       
        width, height = self.size
        
        self.draw.text(((width - font_width) / 3, (height - font_height) / 3), 
                strs, font=font, fill=self.fg_color)

        return strs

    def draw_lines(self):
        """ Draw interference line """
        line_num = random.randint(*self.n_line)

        for i in range(line_num):
            # Starting point
            begin = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            # End point
            end = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            self.draw.line([begin, end], fill=(0, 0, 0))

    def draw_points(self):
        """ Draw the interference point """
        width, height = self.size
        chance = min(100, max(0, int(self.point_chance)))  #  Size limit in [0, 100]

        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    self.draw.point((w, h), fill = (0, 0, 0))
        
    def draw_save(self):
        strs = self.create_strs()

        #  Graphic distortion parameter 
        params = [1 - float(random.randint(1, 2)) / 100,
            0,
            0,
            0,
            1 - float(random.randint(1, 10)) / 100,
            float(random.randint(1, 2)) / 500,
            0.001,
            float(random.randint(1, 2)) / 500
            ]
        img = self.img.transform(self.size, Image.PERSPECTIVE, params)  #  Create distortion
        img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)  #  Filter ， Boundary strengthening （ Greater threshold ）

        self.draw_lines()
        self.draw_points()

        mstream = BytesIO()
        img.save(mstream, self.image_type)
        img.save('validate.jpg', self.image_type)
    
        return mstream, strs       


if __name__ == '__main__':
    generate = GenerateVerifiCode()
    mstream, strs = generate.draw_save()
    print(f"[=] Random string {strs}")

