# ou can also use the caret symbol ( ^ ) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ( $ ) at the end of the regex to indicate the string must end
# with this regex pattern.


import re

regex = re.compile('^\d+\w+\s$')
match = regex.findall('2632jdsajdlasdasd ')
print(match)

import re
regex = re.compile(r'^\W+\w+\d$')
match = regex.findall('$jjsga42312')
print(match)




