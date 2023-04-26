# define a pattern searching function 
def pattern_search(text, pattern, replacement,  case_sensitive=True):

    fixed_text = ""
    num_skips = 0

    for text_index in range(len(text)):
        match_count = 0

        if num_skips > 0:
            num_skips -= 1
            continue

        for pattern_index in range(len(pattern)):

            if case_sensitive and text[text_index + pattern_index] == pattern[pattern_index]:
                match_count += 1 
            elif not case_sensitive and text[text_index + pattern_index].lower() == pattern[pattern_index].lower():
                match_count += 1
            else:
                break

            if match_count == len(pattern):
                fixed_text += replacement
                num_skips += len(pattern) - 1
            else:
                fixed_text += text[text_index]


# # test parms 
# text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
# pattern = "NEEDLE"

# # test fucntion 
# pattern_search(text, pattern)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)
