# format_string

# source: https://stackoverflow.com/questions/53908134/what-is-20-format-string-meaning-in-python

popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987], 
          ["Java", 1, 2, 1, 1, 15, 0, 0],
          ["C", 2, 1, 2, 2, 1, 1, 1],
          ["C++", 3, 3, 3, 3, 2, 2, 5],
          ["C#", 4, 4, 7, 13, 0, 0, 0],
          ["Python", 5, 7, 6, 11, 27, 0, 0],
          ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
          ["PHP", 7, 6, 4, 5, 0, 0, 0],
          ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
          ["Perl", 9, 8, 5, 4, 4, 10, 0]]

format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"

for l in popularity: print(format_string.format(*l))