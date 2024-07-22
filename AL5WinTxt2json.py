import json

# text_pattern = re.pattern("#1-TEXT\n\[(\s)\]")


def read_txt(f_path):
    sentences = []

    with open(f_path, 'r', encoding='cp932') as f:
        txt_content = f.readlines()
    for i in range(len(txt_content)-2):
        line = txt_content[i]
        words = txt_content[i+2]
        if "TEXT" in line and "SYSTEM" not in line:
            sentences.append(words)

    return sentences


def convert2json(raw_list):
    json_ls = []
    for i in range(len(raw_list)):
        c_elem=raw_list[i]
        temp_dict = {"message": c_elem}
        json_ls.append(temp_dict)
    
    res = json.dumps(json_ls, ensure_ascii=False)

    return res 


def saveRes(json_string:str, f_path):
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(json_string)


if __name__ == "__main__":
    test_f = "./test/AA_H1.txt"
    out_file = "./test/AA_H1.json"

    result = read_txt(test_f)
    print(result)
    json_result = convert2json(result)
    # print(json_result)
    saveRes(json_result, out_file)

    pass


