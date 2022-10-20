

"""Create schedule from the given file."""
import re
from datetime import datetime


def number_convert_time(number: int) -> str:
    """Nice."""
    result = '{:02d}:{:02d}'.format(*divmod(number, 60))
    return result


def convert_to_pm_am(number: int) -> str:
    """Nice."""
    a = number_convert_time(number)
    d = datetime.strptime(a, "%H:%M")
    if d.strftime("%I:%M %p")[0] == "0":
        return d.strftime("%I:%M %p")[1:]
    else:
        return d.strftime("%I:%M %p")


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    together = {}
    if re.search(r"(\s+)(\d\d[^0-9]\d\d|\d\d[^0-9]\d|\d[^0-9]\d\d|\d[^0-9]\d)\s+([a-zA-Z]+)", input_string) is not None:
        for match in re.finditer(r"(\s+)(\d\d[^0-9]\d\d|\d\d[^0-9]\d|\d[^0-9]\d\d|\d[^0-9]\d)\s+([a-zA-Z]+)", input_string):
            # Lower words.
            lower_words = match.group(3).lower()
            # Split by non number symbol.
            result = re.split(r"\D+", str(match.group(2)))
            # Adding 0.
            result[0] = result[0].zfill(2)
            result[1] = result[1].zfill(2)
            # Join by :.
            result_with_comas = ":".join(result)
            # Transform time to minutes.
            if int(result_with_comas[:2]) <= 23 and int(result_with_comas[3:]) <= 59:
                result_in_minutes = int(result_with_comas[:2]) * 60 + int(result_with_comas[3:])
                if result_in_minutes not in together:
                    together[result_in_minutes] = list()
                together[result_in_minutes].append(lower_words)
        for key, value in together.items():
            together[key] = list(dict.fromkeys(value))
        for key, value in together.items():
            together[key] = ", ".join(value)
        # Sort dict by key.
        d_sorted = {key: value for key, value in sorted(together.items(), key=lambda item: int(item[0]))}
        list_of_times = []
        list_of_action = []
        for i in d_sorted:
            if d_sorted[i] not in list_of_action:
                list_of_action.append(d_sorted[i])
            if convert_to_pm_am(i) not in list_of_times:
                list_of_times.append(convert_to_pm_am(i))
        x = len(max(list_of_action, key=len))
        y = len(max(list_of_times, key=len))
        table = ""
        if x >= 7:
            z = ("-" * (x + y + 7))
            table += f"{z}\n"
            table += f"| {'time':>{y}} | {'entries':<{x}} |\n"
            z = ("-" * (x + y + 7))
            table += f"{z}\n"
            for row in d_sorted:
                table += f"| {convert_to_pm_am(row):>{y}} | {d_sorted[row]:<{x}} |\n"
            table += f"{z}\n"
        if x < 7:
            z = ("-" * (y + 14))
            table += f"{z}\n"
            table += f"| {'time':>{y}} | {'entries':<{7}} |\n"
            z = ("-" * (y + 14))
            table += f"{z}\n"
            for row in d_sorted:
                table += f"| {convert_to_pm_am(row):>{y}} | {d_sorted[row]:<{7}} |\n"
                z = ("-" * (y + 14))
            table += f"{z}\n"
        return table
    else:
        table = ""
        z = ("-" * 20)
        table += f"{z}\n"
        table += f"| {'time':>{5}} | {'entries':<{8}} |\n"
        table += f"{z}\n"
        table += f"| {'No entries found'} |\n"
        table += f"{z}\n"
        return table


if __name__ == '__main__':
    print(create_schedule_string("start gcyxiykxxe 9.43  jTPuRmLxl hfyzob usbujs vqpbktwcs 5!23    mUgrJ ixgnvpnen ojxntmni myxdhehua nmzqf ynhrc vhseuev 16?45  XuAvFtH zoyovl ydqsiaski zbyhfj nnhkjse bmvzmz qfwiqnpk txosqqjd rjjnpxtifk aovwceqdou 25B53 CWiKWOmfnU yljxmlvncs ffnlrxv -1a01 GdoYfZ 5=42   JtPURMlxl sblidhbvk cceadeqkj qbffnz hbizwq mwgwven iutye fyfgnfqcr jzrwbck 05?40  jtpurMlxL vctot rtiofiub xhchumswce qnhzbmb feujymfhhs zgmhkgypeq 5=60 MuGRj 25=23  URskxLk tttjlz ftlhexg olzgxwgmhi khxkvptqn tujabet xzrxr 17=58 mgldBET cejrj jehfbxmbel yzxqsfmte qsqfj upzfufzxxa nfseaatk wtawar ogkqqyvrmx 02.13  ifzGqA hrwqkatqtp nwzaoveu iicdf yybeoyydr mrnbg cejmgj 6b51    urskxLk ilutk jwvvwn xjqovo gcvomwidf bwyyn wseiqqkb jkiraqu zvprtndokj 10b49 xoVtxOVpee uqutinc ruyavklym bhcww coyunhblpv uzmvuhvvpo fymyrwupa fnzbtsl zpwgpdho 22?02   MugrJ lvwrbqtnd owdgjg 17A25 JFQYwj xwfkxnx owyybkp afhlwmy gppugpc axksvozkzm"))
