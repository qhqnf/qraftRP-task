def line_parser(str):
    result = []
    if '"' in str:
        temp = str.split('"')
        for index, value in enumerate(temp):
            if index % 2 == 0:
                result += value.strip(",").split(",")
            else:
                result.append(value)
    else:
        result = str.split(",")

    return result


if __name__ == "__main__":
    line = '2017,Level 1,99999,All industries,Dollars (millions),H04,"Sales, government funding, grants and subsidies",Financial performance,566951,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"'
    result = line_parser(line)
    print(result)
