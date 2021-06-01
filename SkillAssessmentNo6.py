# import libraries
import re
import os

# Change working directory to this folder
address = os.getcwd ()
os.chdir(address)

# defining a class with two function
class file_name:
    # Define a function to extract any digits
    def __init__ (self, filename):
        self.filename = filename

    # Because we have tow pattern, we must define tow function.
    
    def number_extrction_pattern_non_digits_first (filename):
        pattern = (r'(\D+)(\d+)(\.jpg)')
        digits_pattern_non_digits_first = re.search(pattern, filename, re.IGNORECASE).group (2) 
        non_digits_pattern_non_digits_first = re.search(pattern, filename, re.IGNORECASE).group (1)
        return digits_pattern_non_digits_first, non_digits_pattern_non_digits_first

    # Second function for pattern as : 1993schrodinger.pdf
    def number_extrction_pattern_digits_first (filename):

        pattern = (r'(\d+)(\D+)(\.jpg)')
        digits_pattern_digits_first = re.search(pattern, filename, re.IGNORECASE).group (1) 
        non_digits_pattern_digits_first = re.search(pattern, filename, re.IGNORECASE).group (2)

        return digits_pattern_digits_first, non_digits_pattern_digits_first



if __name__ == '__main__':

    # Define a pattern to check filename pattern
    pattern_check1 = (r'(\D+)(\d+)(\.jpg)')

    # Declare each file address.
    for filename in os.listdir("F:\paul's folder"):

        if filename.endswith('.jpg'):
            if re.search(pattern_check1, filename, re.IGNORECASE):

                digits = file_name.number_extrction_pattern_non_digits_first (filename)[0]
                non_digits = file_name.number_extrction_pattern_non_digits_first (filename)[1]
                #os.rename(filename, digits + non_digits + '.jpg')
                ext = ".jpg"
                kwikpic_selfies = os.path.join(digits, ext)
                print(digits)
                #print(kwikpic_selfies.replace('/', ''))
                print(kwikpic_selfies.replace('\\', ''))   
            else :
                 print("Something error!, please check and try again")
