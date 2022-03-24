import io

path = 'C:\ProgStaff\DemonSlave\day_log.txt'
task_buffer = []
state = {
    "Theme": "",
}


def split_dl_line(dl_line, f_state):
    dl_line = dl_line.replace('\n', '')
    while dl_line.find('  ') != -1:
        dl_line = dl_line.replace('  ', ' ')
    while dl_line.find('\t\t') != -1:
        dl_line = dl_line.replace('\t\t', '\t')
    dl_line = dl_line.split('\t')
    dl_line = dl_line[1:] if dl_line[0] == "" else dl_line
    dl_line.insert(0, dl_line[0].split(')')[0])
    dl_line[1] = dl_line[1][dl_line[1].find(')')+2:]

    if len(dl_line) > 2:
        dl_line.insert(2, dl_line[2].split(' ') if dl_line[2].find(' ') != -1 else [dl_line[2]])
        dl_line = dl_line[:-1]
    else:
        dl_line.insert(2, [])

    dl_line.insert(0, f_state["Theme"])
    return dl_line


def action_alert1(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_alert2(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_deadline(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_evaluate_proc(f_line, f_state):
    task = split_dl_line(f_line, f_state)
    tagline = task[3]
    percent = 0
    for i in range(0, len(tagline)):
        if task[3][i].find("/") != -1:
            percent = float(task[3][i].split("/")[0])/float(task[3][i].split("/")[1])
        if (task[3][i].find("%") != -1) and (percent != 0):
            task[3][i] = percent
    return task


def action_alert_today(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_done(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_repost(f_line, f_state):
    return split_dl_line(f_line, f_state)


def action_theme(f_line, f_state):
    f_line = f_line[:-1]
    if f_line.find("ПРЕДМЕТ") != -1:
        f_line = f_line.split(" ", 1)[1]
        f_state["Theme"] = f_line
        return f_line
    f_state["Theme"] = f_line
    return f_line


def action_ignore(f_line, f_state):
    return None


key_words = {
    "//////////////////////////////////////////////////////////": action_ignore,
    "--": action_ignore,
    "ПРЕДМЕТ": action_theme,
    "КВЕСТЫ": action_theme,
    "КНИГИ": action_theme,
    "СДЕЛАТЬ_СДЕЛАТЬ_СДЕЛАТЬ": action_alert2,
    "СДЕЛАТЬ_СЕГОДНЯ": action_alert_today,
    "СДЕЛАТЬ": action_alert1,
    "DEADLINE": action_deadline,
    "<<<DONE>>>": action_done,
    "%": action_evaluate_proc,
    ")": action_repost,
    "": action_ignore,
}


def line_process(line_proc, f_state):
    for key in key_words:
        if line_proc.find(key) != -1:
            return key_words[key](line_proc, f_state)


def make_task_board(f_task_buffer):
    base_task_list = [task for task in f_task_buffer if (task[1].find(".") == -1) and (task[1].isdigit())]
    res_list = []
    return res_list


with io.open(path, encoding='utf-8') as file:
    line_buffer = [line_process(line, state) for line in file.readlines()]
    line_buffer = [line for line in line_buffer if line]
    outfile = open('day_log_updated.txt', 'w', encoding='utf-8')
    task_board = make_task_board(line_buffer)
    for out_line in line_buffer:
        outfile.write(out_line)
    outfile.close()
    file.close()
