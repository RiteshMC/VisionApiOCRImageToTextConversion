from parse_tool import get_block, get_xy_high_word
from request_tool import get_processed_data

# Please be sure to replace this with your ApiKey
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Please insert the image url you want to parse
image_url = "https://raw.githubusercontent.com/RiteshMC/VisionApiOCRImageToTextConversion/develop/resources/test-invoice.jpg"

# getting the dat and converting it into json format
response = get_processed_data(api_key, image_url)
jd = eval(response.text)
data = jd["responses"][0]

# Uncomment the code just incase you want to save the json response to file and read it.
# import json
# with open('data.json', 'w') as f:
#     json.dump(data, f)

all_data = data["textAnnotations"]
# here we are taking all the text detected by OCR and breaking them into an array.
# Note : the text received are not as expected in a proper format
all_data_str_arr = all_data[0]["description"].strip().split("\n")
# the first text received is the one that has all the text from the image so we are removing it after we put it in [all_data_str_arr] variable
all_data.pop(0)
# this is a extra piece of code required to get perfect value due to iteration issue
all_data.append(all_data[0])

# As the response from the Google Vision Api are all scrambled,
# Thus, using the (x,y) coordinate of the scrambled letters we are trying to group random letters into proper words.
# And also trying to find the highest y point and lowest y point of the word
# Along with trying to find the left most x point of the words so that we can compare them and turn them into block sentences.
word_blocks = []
for i in all_data_str_arr:
    block = get_block(all_data, i)
    word_blocks.append(get_xy_high_word(block))

# As, we have the words along with highest y point, lowest y point and left most x point of the words
# We are now going to turn them into sentences using height coordinates
sentence_blocks = []
used_sentence_blocks = []
# Offset incase of irregular handwriting
offset = 3

print("Total Sentences = ", len(word_blocks))
print("========================\n")
for x in range(len(word_blocks)):
    if len(word_blocks) <= 0:
        break
    if word_blocks[0] in used_sentence_blocks:
        word_blocks.pop(0)
        continue
    cur = word_blocks[0]
    cur_height_offset = cur["height_high"] - cur["height_low"]
    tmp = [word_blocks[0]]
    tmp_idx = []
    used_sentence_blocks.append(word_blocks[0])
    word_blocks.pop(0)

    for wb in word_blocks:
        if wb in used_sentence_blocks:
            continue

        if (cur["height_high"] >= wb["height_high"] - offset >= cur["height_low"]) \
                or (cur["height_high"] >= wb["height_low"] + offset >= cur["height_low"]):
            # also need to check ratio here
            used_sentence_blocks.append(wb)
            tmp.append(wb)

            # word_blocks.remove(wb)

    if len(tmp) > 0:
        tmp.sort(key=lambda wd: wd["weight_left"])
        sentence_blocks.append(tmp)

out = ""
for sb in sentence_blocks:
    out += ', '.join(["\"" + str(x["word"] + "\"") for x in sb]) + "\n"

# Uncomment the code just incase you want to save the output and read them in a file
# output_file_path = r'./output.txt'
# f = open(output_file_path, "a")
# f.write(out)
# f.close()

print(out)
print("successful\n\n")
