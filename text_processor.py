import io

path = 'C:\ProgStaff\DemonSlave\day_log.txt'


def split_dl_line(dl_line):
    dl_line = dl_line.replace('\n', '')
    while dl_line.find('  ') != -1:
        dl_line = dl_line.replace('  ', ' ')
    while dl_line.find('\t\t') != -1:
        dl_line = dl_line.replace('\t\t', '\t')
    dl_line = dl_line.split('\t')
    dl_line = dl_line[1:] if dl_line[0] == "" else dl_line
    dl_line.insert(0, dl_line[0].split(')')[0])
    dl_line[1] = dl_line[1][dl_line[1].find(')')+2:]
    dl_line.insert(2, dl_line[2].split(' ') if dl_line[2].find(' ') != -1 else [dl_line[2]])
    dl_line = dl_line[:-1]
    return dl_line


def action_alert1(f_line):
    return str('action_alert1' + f_line)


def action_alert2(f_line):
    print(split_dl_line(f_line))
    return str('action_alert2' + f_line)


def action_deadline(f_line):
    return str('action_deadline' + f_line)


def action_evaluate_proc(f_line):
    print(split_dl_line(f_line))
    return str('action_evaluate_proc' + f_line)


def action_alert_today(f_line):
    return str('action_alert_today' + f_line)


def action_done(f_line):
    return str('action_done' + f_line)


def action_repost(f_line):
    return f_line


key_words = {
    "СДЕЛАТЬ_СДЕЛАТЬ_СДЕЛАТЬ": action_alert2,
    "СДЕЛАТЬ_СЕГОДНЯ": action_alert_today,
    "СДЕЛАТЬ": action_alert1,
    "DEADLINE": action_deadline,
    "<<<DONE>>>": action_done,
    "%": action_evaluate_proc,
    "": action_repost,
}


def line_process(line_proc):
    for key in key_words:
        if line_proc.find(key) != -1:
            return key_words[key](line_proc)


with io.open(path, encoding='utf-8') as file:
    line_buffer = [line_process(line) for line in file.readlines()]
    outfile = open('day_log_updated.txt', 'w', encoding='utf-8')
    for out_line in line_buffer:
        outfile.write(out_line+'\n')
    outfile.close()
    file.close()
