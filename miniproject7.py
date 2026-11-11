# D15
def parse_line(raw_line):
    """converts raw string in the format: hostname, used, total into a dict with labels and their values"""
    hostname_part, rest = raw_line.strip().split(",", 1)
    final_dict = {}
    final_dict["hostname"] = hostname_part.strip().lower()

    for part in rest.split(","):
        key, value = part.split("=")
        final_dict[key.strip()] = float(value.strip())

    return final_dict

def status_of(percent):
    """takes a percent value and returns a string status based on its value"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent > 90:
        return "WARNING"
    else:
        return "OK"


raw_records = ["  Srv-01 , used=87 , total=100 ",
"SRV-02,used=120,total=100",
"  srv-03,used=45 ,total=100",
"Srv-04 , used = 93 , total=100",
" SrV-05   , used=  67, total    = 100"]

with open("records.txt", "w") as f:
    for record in raw_records:
        f.write(record + "\n")

lim_count = 0
rec_count = 0
with open("records.txt") as f:
    for line in f:
        hostname, used, total = parse_line(line).items()
        percent = (used[1]/total[1])*100
        status = status_of(percent)
        print(parse_line(line), f"status:{status}")
        lim_count += 1 if status == "OVER LIMIT" else 0
        rec_count += 1
    print(f"OVERLIMIT:{lim_count} | TOTAL_RECORDS:{rec_count}")

