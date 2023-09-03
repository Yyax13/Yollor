class c:
    @staticmethod
    def black(text):
        return f"\033[0;30m{text}\033[0m"
    
    @staticmethod
    def red(text):
        return f"\033[0;31m{text}\033[0m"
    
    @staticmethod
    def green(text):
        return f"\033[0;32m{text}\033[0m"
    
    @staticmethod
    def brown(text):
        return f"\033[0;33m{text}\033[0m"
    
    @staticmethod
    def blue(text):
        return f"\033[0;34m{text}\033[0m"
    
    @staticmethod
    def purple(text):
        return f"\033[0;35m{text}\033[0m"
    
    @staticmethod
    def cyan(text):
        return f"\033[0;36m{text}\033[0m"
    
    @staticmethod
    def gray(text):
        return f"\033[1;30m{text}\033[0m"
    
    @staticmethod
    def yellow(text):
        return f"\033[1;33m{text}\033[0m"

class t:    
    #yellow tags
    tagn1_yellow = f"{c.cyan('[')}{c.yellow('1')}{c.cyan(']')}"
    tagn2_yellow = f"{c.cyan('[')}{c.yellow('2')}{c.cyan(']')}"
    tagn3_yellow = f"{c.cyan('[')}{c.yellow('3')}{c.cyan(']')}"
    tagn4_yellow = f"{c.cyan('[')}{c.yellow('4')}{c.cyan(']')}"
    tagn5_yellow = f"{c.cyan('[')}{c.yellow('5')}{c.cyan(']')}"
    tagn6_yellow = f"{c.cyan('[')}{c.yellow('6')}{c.cyan(']')}"
    tagn7_yellow = f"{c.cyan('[')}{c.yellow('7')}{c.cyan(']')}"
    tagn8_yellow = f"{c.cyan('[')}{c.yellow('8')}{c.cyan(']')}"
    tagn9_yellow = f"{c.cyan('[')}{c.yellow('9')}{c.cyan(']')}"
    tagn10_yellow = f"{c.cyan('[')}{c.yellow('10')}{c.cyan(']')}"
    hashtag_yellow = rf"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
    more_yellow = rf"{c.cyan('[')}{c.yellow('+')}{c.cyan(']')}"
    quest_yellow = rf"{c.cyan('[')}{c.yellow('?')}{c.cyan(']')}"
    minus_yellow= rf"{c.cyan('[')}{c.yellow('-')}{c.cyan(']')}"

    #black tags
    tagn1_black = f"{c.cyan('[')}{c.black('1')}{c.cyan(']')}"
    tagn2_black = f"{c.cyan('[')}{c.black('2')}{c.cyan(']')}"
    tagn3_black = f"{c.cyan('[')}{c.black('3')}{c.cyan(']')}"
    tagn4_black = f"{c.cyan('[')}{c.black('4')}{c.cyan(']')}"
    tagn5_black = f"{c.cyan('[')}{c.black('5')}{c.cyan(']')}"
    tagn6_black = f"{c.cyan('[')}{c.black('6')}{c.cyan(']')}"
    tagn7_black = f"{c.cyan('[')}{c.black('7')}{c.cyan(']')}"
    tagn8_black = f"{c.cyan('[')}{c.black('8')}{c.cyan(']')}"
    tagn9_black = f"{c.cyan('[')}{c.black('9')}{c.cyan(']')}"
    tagn10_black = f"{c.cyan('[')}{c.black('10')}{c.cyan(']')}"
    hashtag_black = rf"{c.cyan('[')}{c.black('#')}{c.cyan(']')}"
    more_black = rf"{c.cyan('[')}{c.black('+')}{c.cyan(']')}"
    quest_black = rf"{c.cyan('[')}{c.black('?')}{c.cyan(']')}"
    minus_black= rf"{c.cyan('[')}{c.black('-')}{c.cyan(']')}"

    #red tags
    tagn1_red = f"{c.cyan('[')}{c.red('1')}{c.cyan(']')}"
    tagn2_red = f"{c.cyan('[')}{c.red('2')}{c.cyan(']')}"
    tagn3_red = f"{c.cyan('[')}{c.red('3')}{c.cyan(']')}"
    tagn4_red = f"{c.cyan('[')}{c.red('4')}{c.cyan(']')}"
    tagn5_red = f"{c.cyan('[')}{c.red('5')}{c.cyan(']')}"
    tagn6_red = f"{c.cyan('[')}{c.red('6')}{c.cyan(']')}"
    tagn7_red = f"{c.cyan('[')}{c.red('7')}{c.cyan(']')}"
    tagn8_red = f"{c.cyan('[')}{c.red('8')}{c.cyan(']')}"
    tagn9_red = f"{c.cyan('[')}{c.red('9')}{c.cyan(']')}"
    tagn10_red = f"{c.cyan('[')}{c.red('10')}{c.cyan(']')}"
    hashtag_red = rf"{c.cyan('[')}{c.red('#')}{c.cyan(']')}"
    more_red = rf"{c.cyan('[')}{c.red('+')}{c.cyan(']')}"
    quest_red = rf"{c.cyan('[')}{c.red('?')}{c.cyan(']')}"
    minus_red= rf"{c.cyan('[')}{c.red('-')}{c.cyan(']')}"

    #green tags
    tagn1_green = f"{c.cyan('[')}{c.green('1')}{c.cyan(']')}"
    tagn2_green = f"{c.cyan('[')}{c.green('2')}{c.cyan(']')}"
    tagn3_green = f"{c.cyan('[')}{c.green('3')}{c.cyan(']')}"
    tagn4_green = f"{c.cyan('[')}{c.green('4')}{c.cyan(']')}"
    tagn5_green = f"{c.cyan('[')}{c.green('5')}{c.cyan(']')}"
    tagn6_green = f"{c.cyan('[')}{c.green('6')}{c.cyan(']')}"
    tagn7_green = f"{c.cyan('[')}{c.green('7')}{c.cyan(']')}"
    tagn8_green = f"{c.cyan('[')}{c.green('8')}{c.cyan(']')}"
    tagn9_green = f"{c.cyan('[')}{c.green('9')}{c.cyan(']')}"
    tagn10_green = f"{c.cyan('[')}{c.green('10')}{c.cyan(']')}"
    hashtag_green = rf"{c.cyan('[')}{c.green('#')}{c.cyan(']')}"
    more_green = rf"{c.cyan('[')}{c.green('+')}{c.cyan(']')}"
    quest_green = rf"{c.cyan('[')}{c.green('?')}{c.cyan(']')}"
    minus_green= rf"{c.cyan('[')}{c.green('-')}{c.cyan(']')}"

    #brown tags
    tagn1_brown = f"{c.cyan('[')}{c.brown('1')}{c.cyan(']')}"
    tagn2_brown = f"{c.cyan('[')}{c.brown('2')}{c.cyan(']')}"
    tagn3_brown = f"{c.cyan('[')}{c.brown('3')}{c.cyan(']')}"
    tagn4_brown = f"{c.cyan('[')}{c.brown('4')}{c.cyan(']')}"
    tagn5_brown = f"{c.cyan('[')}{c.brown('5')}{c.cyan(']')}"
    tagn6_brown = f"{c.cyan('[')}{c.brown('6')}{c.cyan(']')}"
    tagn7_brown = f"{c.cyan('[')}{c.brown('7')}{c.cyan(']')}"
    tagn8_brown = f"{c.cyan('[')}{c.brown('8')}{c.cyan(']')}"
    tagn9_brown = f"{c.cyan('[')}{c.brown('9')}{c.cyan(']')}"
    tagn10_brown = f"{c.cyan('[')}{c.brown('10')}{c.cyan(']')}"
    hashtag_brown = rf"{c.cyan('[')}{c.brown('#')}{c.cyan(']')}"
    more_brown = rf"{c.cyan('[')}{c.brown('+')}{c.cyan(']')}"
    quest_brown = rf"{c.cyan('[')}{c.brown('?')}{c.cyan(']')}"
    minus_brown= rf"{c.cyan('[')}{c.brown('-')}{c.cyan(']')}"

    #blue tags
    tagn1_blue = f"{c.cyan('[')}{c.blue('1')}{c.cyan(']')}"
    tagn2_blue = f"{c.cyan('[')}{c.blue('2')}{c.cyan(']')}"
    tagn3_blue = f"{c.cyan('[')}{c.blue('3')}{c.cyan(']')}"
    tagn4_blue = f"{c.cyan('[')}{c.blue('4')}{c.cyan(']')}"
    tagn5_blue = f"{c.cyan('[')}{c.blue('5')}{c.cyan(']')}"
    tagn6_blue = f"{c.cyan('[')}{c.blue('6')}{c.cyan(']')}"
    tagn7_blue = f"{c.cyan('[')}{c.blue('7')}{c.cyan(']')}"
    tagn8_blue = f"{c.cyan('[')}{c.blue('8')}{c.cyan(']')}"
    tagn9_blue = f"{c.cyan('[')}{c.blue('9')}{c.cyan(']')}"
    tagn10_blue = f"{c.cyan('[')}{c.blue('10')}{c.cyan(']')}"
    hashtag_blue = rf"{c.cyan('[')}{c.blue('#')}{c.cyan(']')}"
    more_blue = rf"{c.cyan('[')}{c.blue('+')}{c.cyan(']')}"
    quest_blue = rf"{c.cyan('[')}{c.blue('?')}{c.cyan(']')}"
    minus_blue= rf"{c.cyan('[')}{c.blue('-')}{c.cyan(']')}"

    #purple tags
    tagn1_purple = f"{c.cyan('[')}{c.purple('1')}{c.cyan(']')}"
    tagn2_purple = f"{c.cyan('[')}{c.purple('2')}{c.cyan(']')}"
    tagn3_purple = f"{c.cyan('[')}{c.purple('3')}{c.cyan(']')}"
    tagn4_purple = f"{c.cyan('[')}{c.purple('4')}{c.cyan(']')}"
    tagn5_purple = f"{c.cyan('[')}{c.purple('5')}{c.cyan(']')}"
    tagn6_purple = f"{c.cyan('[')}{c.purple('6')}{c.cyan(']')}"
    tagn7_purple = f"{c.cyan('[')}{c.purple('7')}{c.cyan(']')}"
    tagn8_purple = f"{c.cyan('[')}{c.purple('8')}{c.cyan(']')}"
    tagn9_purple = f"{c.cyan('[')}{c.purple('9')}{c.cyan(']')}"
    tagn10_purple = f"{c.cyan('[')}{c.purple('10')}{c.cyan(']')}"
    hashtag_purple = rf"{c.cyan('[')}{c.purple('#')}{c.cyan(']')}"
    more_purple = rf"{c.cyan('[')}{c.purple('+')}{c.cyan(']')}"
    quest_purple = rf"{c.cyan('[')}{c.purple('?')}{c.cyan(']')}"
    minus_purple= rf"{c.cyan('[')}{c.purple('-')}{c.cyan(']')}"

    #cyan tags
    tagn1_cyan = f"{c.cyan('[')}{c.cyan('1')}{c.cyan(']')}"
    tagn2_cyan = f"{c.cyan('[')}{c.cyan('2')}{c.cyan(']')}"
    tagn3_cyan = f"{c.cyan('[')}{c.cyan('3')}{c.cyan(']')}"
    tagn4_cyan = f"{c.cyan('[')}{c.cyan('4')}{c.cyan(']')}"
    tagn5_cyan = f"{c.cyan('[')}{c.cyan('5')}{c.cyan(']')}"
    tagn6_cyan = f"{c.cyan('[')}{c.cyan('6')}{c.cyan(']')}"
    tagn7_cyan = f"{c.cyan('[')}{c.cyan('7')}{c.cyan(']')}"
    tagn8_cyan = f"{c.cyan('[')}{c.cyan('8')}{c.cyan(']')}"
    tagn9_cyan = f"{c.cyan('[')}{c.cyan('9')}{c.cyan(']')}"
    tagn10_cyan = f"{c.cyan('[')}{c.cyan('10')}{c.cyan(']')}"
    hashtag_cyan = rf"{c.cyan('[')}{c.cyan('#')}{c.cyan(']')}"
    more_cyan = rf"{c.cyan('[')}{c.cyan('+')}{c.cyan(']')}"
    quest_cyan = rf"{c.cyan('[')}{c.cyan('?')}{c.cyan(']')}"
    minus_cyan= rf"{c.cyan('[')}{c.cyan('-')}{c.cyan(']')}"

    #gray tags
    tagn1_gray = f"{c.cyan('[')}{c.gray('1')}{c.cyan(']')}"
    tagn2_gray = f"{c.cyan('[')}{c.gray('2')}{c.cyan(']')}"
    tagn3_gray = f"{c.cyan('[')}{c.gray('3')}{c.cyan(']')}"
    tagn4_gray = f"{c.cyan('[')}{c.gray('4')}{c.cyan(']')}"
    tagn5_gray = f"{c.cyan('[')}{c.gray('5')}{c.cyan(']')}"
    tagn6_gray = f"{c.cyan('[')}{c.gray('6')}{c.cyan(']')}"
    tagn7_gray = f"{c.cyan('[')}{c.gray('7')}{c.cyan(']')}"
    tagn8_gray = f"{c.cyan('[')}{c.gray('8')}{c.cyan(']')}"
    tagn9_gray = f"{c.cyan('[')}{c.gray('9')}{c.cyan(']')}"
    tagn10_gray = f"{c.cyan('[')}{c.gray('10')}{c.cyan(']')}"
    hashtag_gray = rf"{c.cyan('[')}{c.gray('#')}{c.cyan(']')}"
    more_gray = rf"{c.cyan('[')}{c.gray('+')}{c.cyan(']')}"
    quest_gray = rf"{c.cyan('[')}{c.gray('?')}{c.cyan(']')}"
    minus_gray= rf"{c.cyan('[')}{c.gray('-')}{c.cyan(']')}"
