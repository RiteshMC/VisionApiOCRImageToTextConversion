import re


# get_block() is a function
# group the broken words received by Cloud Vision API text cordinates and them turns them into a single word
# But its not always correct, We are only trying to group them as much as possible.
def get_block(all_data, item):
    strip_i = re.sub(r"\s", "", item)
    col = ""
    col_array = []
    for jidx, j in enumerate(all_data):
        if col == strip_i:
            all_data[0:jidx] = []
            break
        if j["description"] in item:
            col += j["description"]
            col_array.append(j)
    return col_array


# get_xy_high_word() is a function
# It compares the (x,y) coordinate of the words and gets the Highest and lowest height of the word
# Along with it it also provides the x axis start value of the word
#     hh
#    -----
#    | A |
# wl -----
#     hl
# return format
# {
#         "word": word,
#         "height_high": hh,
#         "height_low": hl,
#         "weight_left": wl,
#         "item": item,
#
#     }
# Proper display format for coordinate visualisation
# print(it["boundingPoly"]["vertices"][3], it["boundingPoly"]["vertices"][2])
# print(it["boundingPoly"]["vertices"][0], it["boundingPoly"]["vertices"][1])
def get_xy_high_word(item):
    word = ""
    hh, hl, wl = 0, 0, 0
    for it in item:
        h_high = it["boundingPoly"]["vertices"][2]['y']
        if it["boundingPoly"]["vertices"][3]['y'] > it["boundingPoly"]["vertices"][2]['y']:
            h_high = it["boundingPoly"]["vertices"][3]['y']

        if h_high > hh:
            hh = h_high

        h_low = it["boundingPoly"]["vertices"][1]['y']
        if it["boundingPoly"]["vertices"][0]['y'] > it["boundingPoly"]["vertices"][1]['y']:
            h_low = it["boundingPoly"]["vertices"][0]['y']

        if h_low > hl:
            hl = h_low

        w_left = it["boundingPoly"]["vertices"][0]['x']
        if it["boundingPoly"]["vertices"][3]['x'] > it["boundingPoly"]["vertices"][0]['x']:
            w_left = it["boundingPoly"]["vertices"][3]['x']

        if w_left < wl or wl == 0:
            wl = w_left

        word += it["description"]

    ret = {
        "word": word,
        "height_high": hh,
        "height_low": hl,
        "weight_left": wl,
        "item": item,

    }

    return ret
